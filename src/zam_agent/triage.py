"""Detecting support tickets and technical issues posted in the channel.

#zam-ask-here is for questions about ZAM and Theme Market. Technical issues,
merchant incidents and ticket links belong in HubSpot, where they can be
tracked and answered by the people who own them.

Link detection is deliberately **not** a model call: a HubSpot or Jira URL is a
string, and recognising one should be instant, free and impossible to talk out
of. The model is only consulted for an unlinked description of a technical
problem, which does need judgement.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Literal

TicketKind = Literal["hubspot", "jira", "none"]

# Slack wraps URLs as <https://…|label>, so match the bare host anywhere.
_HUBSPOT_HOSTS = (
    "hubspot.com",
    "hs-sites.com",
    "hsforms.com",
    "hubspotlinks.com",
    "hubspotusercontent",
)
_JIRA_HOSTS = ("atlassian.net", "atlassian.com", "jira.")

_URL = re.compile(r"https?://[^\s<>|)\]]+", re.IGNORECASE)
# A Jira issue key: ZAMCASE-123, ZAM-45. Needs a boundary so "COVID-19" and
# ordinary hyphenated words do not match.
_JIRA_KEY = re.compile(r"(?<![A-Za-z0-9/_-])([A-Z][A-Z0-9]{1,11})-(\d{1,6})(?![A-Za-z0-9-])")
_JIRA_PATH = re.compile(r"/(?:browse|issues)/[A-Z][A-Z0-9]{1,11}-\d{1,6}", re.IGNORECASE)

# Words that are a Jira-key false positive far more often than a real key.
_JIRA_KEY_DENYLIST = frozenset({"COVID", "ISO", "UTF", "SHA", "RFC", "GMT", "UTC", "IPV", "SAR", "VAT"})


@dataclass(frozen=True)
class TicketSignal:
    """What was found in a message, and therefore where it belongs."""

    kind: TicketKind = "none"
    matched: tuple[str, ...] = ()

    @property
    def found(self) -> bool:
        return self.kind != "none"

    @property
    def already_in_hubspot(self) -> bool:
        """They have a HubSpot ticket already -- the nudge is 'follow up there'."""

        return self.kind == "hubspot"


def detect_ticket_links(text: str) -> TicketSignal:
    """Find a HubSpot or Jira reference. HubSpot wins when both appear."""

    if not text:
        return TicketSignal()

    urls = _URL.findall(text)
    lowered = text.lower()

    hubspot = [url for url in urls if any(host in url.lower() for host in _HUBSPOT_HOSTS)]
    if not hubspot and any(host in lowered for host in _HUBSPOT_HOSTS):
        hubspot = [host for host in _HUBSPOT_HOSTS if host in lowered]
    if hubspot:
        return TicketSignal(kind="hubspot", matched=tuple(dict.fromkeys(hubspot))[:3])

    jira: list[str] = [url for url in urls if any(host in url.lower() for host in _JIRA_HOSTS)]
    jira.extend(match.group(0) for match in _JIRA_PATH.finditer(text))
    for match in _JIRA_KEY.finditer(text):
        if match.group(1).upper() not in _JIRA_KEY_DENYLIST:
            jira.append(match.group(0))
    if jira:
        return TicketSignal(kind="jira", matched=tuple(dict.fromkeys(jira))[:3])

    return TicketSignal()
