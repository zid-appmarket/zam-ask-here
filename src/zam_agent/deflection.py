"""Redirecting technical issues and ticket links out of the channel.

The channel's own topic says to keep technical issues, merchant incidents and
escalations out of it. This posts a short, friendly nudge toward HubSpot
instead, in the sender's language.

Two cases, because they need different advice:

* They posted a **HubSpot** link -- the ticket exists, so the answer is "follow
  it up there, not here".
* They posted a **Jira** link or described a technical problem -- there is no
  ticket the support team can act on, so the answer is "please raise one".

The nudge never tags anyone, never states a policy, and never claims the issue
is invalid. It is routing, not judgement, which is why it does not wait for the
📣 approval that answers do.
"""

from __future__ import annotations

from typing import Literal

from .security import sanitize_outbound

Lang = Literal["ar", "en"]
Reason = Literal["hubspot_link", "jira_link", "technical_issue"]

_FOLLOW_UP_IN_HUBSPOT: dict[Lang, str] = {
    "en": (
        "Thanks — since this is already a HubSpot ticket, please follow it up there "
        "rather than in this channel, so the updates stay on the ticket and the right "
        "team sees them."
    ),
    "ar": (
        "شكرًا — بما إن فيه تكت على HubSpot، تابعها هناك بدل القناة، عشان التحديثات "
        "تبقى على التكت ويشوفها الفريق المختص."
    ),
}

_RAISE_IN_HUBSPOT: dict[Lang, str] = {
    "en": (
        "This looks like a technical issue, and this channel is for ZAM and Theme Market "
        "questions only. Please raise it as a HubSpot ticket so it gets tracked and picked "
        "up by the team that owns it."
    ),
    "ar": (
        "هذا يبدو موضوع تقني، والقناة مخصصة لاستفسارات ZAM وسوق القوالب فقط. "
        "الرجاء رفعه كتكت على HubSpot عشان يتابع ويوصل للفريق المسؤول."
    ),
}

_LINK_LABEL: dict[Lang, str] = {
    "en": "Raise a ticket",
    "ar": "ارفع تكت",
}

_STILL_HAPPY: dict[Lang, str] = {
    "en": "Happy to help here with anything about ZAM or Theme Market itself.",
    "ar": "وأنا حاضر هنا لأي استفسار عن ZAM أو سوق القوالب نفسها.",
}


def deflection_message(
    *,
    reason: Reason,
    language: Lang,
    hubspot_ticket_url: str | None = None,
) -> str:
    """The nudge to post in-thread. Returns plain Slack mrkdwn."""

    if reason == "hubspot_link":
        return sanitize_outbound(_FOLLOW_UP_IN_HUBSPOT[language])

    lines = [_RAISE_IN_HUBSPOT[language]]
    if hubspot_ticket_url:
        lines.append(f"<{hubspot_ticket_url}|{_LINK_LABEL[language]}>")
    lines.append(_STILL_HAPPY[language])
    return sanitize_outbound("\n".join(lines))
