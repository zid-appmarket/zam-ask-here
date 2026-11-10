---
# Synced from https://docs.zid.sa/changing-a-plan-2499430m0
# Do not hand-edit: scripts/sync_docs.py overwrites this file.
# Correct the upstream page instead, then re-run the sync.
id: pd-changing-a-plan
title: "Changing a plan"
product: zam
audience: all
status: verified
updated: 2026-11-10
source_url: https://docs.zid.sa/changing-a-plan-2499430m0
tags: [from-docs-site, partner-docs]
language: en
---

> Changing a plan - Zid Docs
# Changing a plan

When a merchant on one of your plans buys a different one, Zid has to decide what happens to the time they already paid for. This page explains that decision, so you can answer a merchant who thinks they were charged twice.

**This page applies to OAuth apps published in Zid App Market.**

Private apps are not sold through the market and have no subscriptions. Usage-based subscriptions work differently — they have no end date and nothing to carry over. See Usage-based plans .

## The one rule #

**Zid never prorates a plan change.** The merchant always pays the full listed price of the plan they are moving to. Nothing is discounted for the days they have left.

But the value of those remaining days is **never thrown away**. It goes one of two ways:

What happens to the unused value

**Credited** It is deducted from the new plan's invoice, so the merchant pays less at checkout

**Frozen** It is held, and the old plan comes back automatically after the new one ends

Which one you get depends on a single condition: **whether the plan the merchant is moving to has a live offer.**

## A merchant holds one subscription per app #

A merchant can only be on one of your plans at a time. So a plan change is always a replacement, never an addition. There is no way for a merchant to hold two of your plans at once, and no way to buy a top-up on top of an existing plan. See Plans and pricing .

## The four outcomes #

These are conditions, not steps. The merchant's situation selects exactly one.

Outcome When it applies The old subscription Its unused value Credit at checkout

**Credit note** The target plan has no live offer. This is the ordinary upgrade, and the default Replaced Becomes credit on the new invoice Deducted

**Freeze and start offer** A different plan, and that plan has a live offer this merchant has not used yet Set to `frozen` Held, then resumes after the new plan ends Nothing

**Extend existing** The merchant buys the same plan again, while an offer or a frozen plan is in play Kept as-is Stays on the same subscription; the end date moves out Nothing

**Upgrade mid-offer** The merchant is already mid-offer and moves up to a more expensive plan that has no offer of its own Replaced Becomes credit — **including** anything frozen, which is then dropped Deducted

### Why an offer freezes instead of crediting #

An offer already contains the discount. If Zid also credited the old subscription's remaining value, the same period would be discounted twice — once by the offer and once by the credit. Freezing keeps the merchant's paid time intact without discounting it twice, and keeps your revenue share correct on the offer purchase.

## Freeze and resume, step by step #

This is the outcome partners get asked about, because the merchant sees the full price with no deduction.

Say a merchant is on your annual plan with 294 days left, and you are running a "subscribe for a year, get a year free" offer on a higher plan.

1 .

The merchant buys the higher plan. They are charged its full price, with **no credit line**.

2 .

They are granted the plan's own period **plus** the offer's free period — so a one-year plan with a one-year offer gives them 730 days, not 365.

3 .

Their old subscription is set to `frozen`. Its remaining 294 days and its unused value are stored and stop counting down.

4 .

Automatic renewal is paused, so the frozen plan cannot be billed while it is paused.

5 .

When the new plan's 730 days end, Zid automatically creates a fresh subscription on the **old** plan for the remaining 294 days.

6 .

Automatic renewal is restored, using whatever setting the merchant originally had.

The merchant ends up with every day they paid for. Nothing is lost at any point.

### What the merchant sees #

Your app's plans page in the merchant's Zid dashboard shows the frozen plan next to the active one — its name, the days remaining, the price they paid, and the date it will resume.

Send a confused merchant here first. It usually answers the question without a support ticket.

## What your app receives #

You get two events, and they can be years apart.

Event When `plan_name` `old_plan_name`

`app.market.subscription.upgrade` At purchase The new plan the merchant bought The plan that is now frozen

`app.market.subscription.renew` When the frozen plan resumes The **old** plan The plan that just ended

**Your app must accept a `renew` that moves a merchant down a tier.**

When a frozen plan resumes, `renew` arrives carrying a cheaper plan with a shorter remaining period, long after the original purchase. This is not an error, a cancellation, or a downgrade request.

If your app assumes a plan change only ever moves upward, it will either ignore this event or keep the merchant on the higher plan. Your entitlements and Zid's billing records then disagree, and the merchant keeps access they are no longer paying for.

A subscription's `status` can be `frozen`. Treat it as "paused, not cancelled" — the merchant has no access on that plan right now, but they will get it back. See Subscription and app events .

## Plan changes that are blocked #

Not every plan change is allowed. These are rejected at checkout, before payment.

**A downgrade while an offer is in play.** If the merchant has a frozen plan behind their subscription, or their subscription came from an offer, they can only move to a plan that is both **longer or equal in duration** and **higher in price**. Moving sideways or down is refused, because it would replace the subscription and leave the frozen plan with nothing to return to.

**More than four years of committed time.** Zid adds up the days left on the active subscription, the days held in any frozen plan, and the days the new purchase would add. If the total is over 1,460 days, the purchase is refused. A merchant already holding a two-year offer plan plus a frozen year has limited room left, so a second "buy one, get one" purchase on your app will be blocked.

**An unpaid usage charge.** A merchant with an overdue or defaulted usage-based charge cannot change plans until it is settled.

## Refunds do not undo a plan change #

A refund is not a way to reverse an upgrade, and it is not a way to return the unused part of a subscription.

**There is no partial refund.** Zid cannot refund only the days a merchant has not used. A refund applies to a whole purchase.

**A refund removes your app.** It marks the subscription refunded, uninstalls your app from that store and revokes its tokens.

**A refund destroys frozen time permanently.** Anything held behind the subscription is discarded and will never resume.

**Offer purchases stop being refundable after 24 hours.**

If a merchant asks for the unused value back as money, the answer is no. Explain the freeze instead.

## Common questions #

### The merchant had 10 months left and was charged full price. Where did the money go? #

Nowhere. Check your app's plans page in their dashboard for a frozen plan. If it is listed with a resume date, the remaining time is being held and will come back automatically.

### Can I make the merchant pay only the difference? #

No. There is no top-up, balance adjustment or difference-only purchase. Every plan change is a full purchase of the target plan. A private plan does not help here either — it is still a plan, and for a merchant mid-offer it is only allowed if it costs **more** than the plan they are on. See Private plans .

### Can the unused value go to the merchant's Zid wallet? #

Only if they originally paid from the wallet. A card payment is refunded to the card. You cannot choose where a refund goes.

### Does a merchant keep frozen time if they uninstall my app? #

Yes. Uninstalling does not discard it. The frozen plan still resumes, so the entitlement is there if the merchant reinstalls. Only a refund destroys it.

### Can a merchant use the same offer twice? #

No. An offer can be redeemed once per store. If the merchant buys the same plan again later, it is treated as an ordinary renewal and the free period is not granted a second time.

### Will the merchant be billed again when the frozen plan resumes? #

If they had automatic renewal switched on, yes — at the end of the resumed period, at that plan's price then. Renewal is restored to the setting they originally had. Tell merchants this up front; it is the part that surprises them.

Modified at 2026-10-28 06:28:55

Previous

Subscription and app events

Next

Authorization
