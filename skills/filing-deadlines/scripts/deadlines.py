#!/usr/bin/env python3
"""UK private limited company deadline calculator.

Usage:
  python3 deadlines.py --incorporated 2025-03-14 [--ard 2026-03-31] [--years 3]
                       [--trading-start 2025-04-01] [--last-cs 2026-03-14] [--json]

--ard            The accounting reference date (period end) of the FIRST accounts if it
                 has been changed with AA01. Default: last day of the month of the first
                 anniversary of incorporation. Subsequent periods run for 12 months.
--trading-start  Date the company started to do business (for CT registration / CT periods).
                 Default: incorporation date.
--last-cs        Last confirmation date, if a confirmation statement was filed early.

Rules: Companies Act 2006 ss391, 442, 443, 853A; CTA 2009 s10; FA 1998 Sch 18.
Outputs are calculations — always double-check against the Companies House register
(https://find-and-update.company-information.service.gov.uk/) and HMRC online account.
"""
import argparse
import calendar
import json
from datetime import date, timedelta


def last_day(y, m):
    return calendar.monthrange(y, m)[1]


def is_month_end(d):
    return d.day == last_day(d.year, d.month)


def add_months(d, months, month_end_rule=True):
    """Add months using the CA 2006 s443 corresponding-date rule."""
    y, m = divmod(d.month - 1 + months, 12)
    y += d.year
    m += 1
    if month_end_rule and is_month_end(d):
        return date(y, m, last_day(y, m))
    return date(y, m, min(d.day, last_day(y, m)))


def anniversary(d, years):
    try:
        return d.replace(year=d.year + years)
    except ValueError:  # 29 Feb
        return date(d.year + years, 2, 28)


def default_first_ard(inc):
    a = anniversary(inc, 1)
    return date(a.year, a.month, last_day(a.year, a.month))


def ct_periods(start, end):
    """Split a period of account into CT accounting periods of max 12 months."""
    out = []
    s = start
    while s <= end:
        cap = add_months(s - timedelta(days=1), 12)  # last day of 12 months starting s
        e = min(cap, end)
        out.append((s, e))
        s = e + timedelta(days=1)
    return out


def fmt(d):
    return d.strftime("%a %d %b %Y")


def build(inc, ard=None, years=3, trading_start=None, last_cs=None):
    first_ard = ard or default_first_ard(inc)
    trading_start = trading_start or inc
    rows = {"company": {"incorporated": inc.isoformat(), "first_ard": first_ard.isoformat()},
            "periods": [], "confirmation_statements": [], "one_off": []}

    rows["one_off"].append({
        "item": "Register for Corporation Tax (within 3 months of starting to do business)",
        "due": add_months(trading_start, 3, month_end_rule=False).isoformat()})

    start = inc
    end = first_ard
    for i in range(years):
        months_long = (end - start).days
        first = i == 0
        over_12 = end > add_months(start - timedelta(days=1), 12)
        if first and over_12:
            acc_due = max(add_months(anniversary(inc, 1), 9), add_months(end, 3))
            rule = "first accounts >12 months: later of 9 months from first anniversary of incorporation (≈21 months) and 3 months after period end"
        else:
            acc_due = add_months(end, 9)
            rule = "9 months after period end"
        ct_start = max(start, trading_start)
        cts = []
        if ct_start <= end:
            for s, e in ct_periods(ct_start, end):
                cts.append({
                    "ct_period": f"{s.isoformat()} to {e.isoformat()}",
                    "pay_ct_by": (add_months(e, 9) + timedelta(days=1)).isoformat(),
                    "s455_repay_by": (add_months(e, 9) + timedelta(days=1)).isoformat(),
                    "file_ct600_by": add_months(end, 12).isoformat(),
                })
        rows["periods"].append({
            "period_of_account": f"{start.isoformat()} to {end.isoformat()}",
            "days": months_long + 1,
            "companies_house_accounts_due": acc_due.isoformat(),
            "accounts_rule": rule,
            "hmrc_ct_periods": cts,
            "rd_claim_notification_by_if_first_claim": add_months(end, 6).isoformat(),
        })
        start = end + timedelta(days=1)
        end = add_months(end, 12)

    base = last_cs or inc
    for n in range(1, years + 1):
        review_end = anniversary(base, n)
        rows["confirmation_statements"].append({
            "review_period_ends": review_end.isoformat(),
            "file_by": (review_end + timedelta(days=14)).isoformat()})
    return rows


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--incorporated", required=True)
    p.add_argument("--ard")
    p.add_argument("--years", type=int, default=3)
    p.add_argument("--trading-start")
    p.add_argument("--last-cs")
    p.add_argument("--json", action="store_true")
    a = p.parse_args()
    d = lambda s: date.fromisoformat(s) if s else None
    r = build(d(a.incorporated), d(a.ard), a.years, d(a.trading_start), d(a.last_cs))
    if a.json:
        print(json.dumps(r, indent=2))
        return
    print(f"Incorporated {fmt(d(a.incorporated))}; first accounting reference date {fmt(date.fromisoformat(r['company']['first_ard']))}\n")
    for o in r["one_off"]:
        print(f"* {o['item']}: {fmt(date.fromisoformat(o['due']))}")
    for per in r["periods"]:
        print(f"\nPeriod of account {per['period_of_account']} ({per['days']} days)")
        print(f"  Companies House accounts due: {fmt(date.fromisoformat(per['companies_house_accounts_due']))}  [{per['accounts_rule']}]")
        for c in per["hmrc_ct_periods"]:
            print(f"  CT period {c['ct_period']}: pay CT by {fmt(date.fromisoformat(c['pay_ct_by']))}; "
                  f"file CT600 by {fmt(date.fromisoformat(c['file_ct600_by']))}")
        if len(per["hmrc_ct_periods"]) > 1:
            print("  NOTE: period exceeds 12 months -> two CT600 returns are required.")
    print("\nConfirmation statements (assuming none filed early):")
    for c in r["confirmation_statements"]:
        print(f"  Review period ends {fmt(date.fromisoformat(c['review_period_ends']))} -> file by {fmt(date.fromisoformat(c['file_by']))}")
    print("\nAlso: identity verification personal codes needed for all directors at the next confirmation"
          " statement (12-month transition ends 18 Nov 2026). Verify every date on the Companies House register.")


if __name__ == "__main__":
    main()
