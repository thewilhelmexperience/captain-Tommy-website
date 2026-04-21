# Captain Tommy Website Mission Addendum: Publish Recovery

Date: 2026-04-20
Project: `captain-tommy-website-publish`
Purpose: Prevent future sessions from repeating today's recovery mistakes while finishing the site in the right order.

## What this addendum is for

This is not a replacement for the original mission directive.
It is an operational correction after a day where publish-safe cleanup accidentally stripped out real content/context and forced partial reconstruction.

Use this addendum together with:
- `MISSION_DIRECTIVE_2026-04-15.md`
- `CHARACTER_BIBLE.md`
- `BATON_2026-04-20_PUBLISH_RECOVERY_AND_V4_FOLLOWUPS.md`

## Mission correction

The publish repo should stay:
- public-safe
- runtime-complete
- voice-true
- behaviorally coherent

It should **not** become:
- an over-trimmed shell that looks clean but has lost real content
- a stale mirror missing same-day writing and tone updates
- a technically tidy repo with broken page behavior

If there is tension between "clean" and "complete enough to be true to the site," choose complete.
If there is tension between "minimal" and "actually carrying the current work," choose actually carrying the current work.

## Current priority order

For the next work session, prioritize in this order:

1. restore the four recovered 2026-04-20 entries to their stronger earlier quality
2. finish Travel Trail v4 lane/context correctness without breaking the new modal behavior
3. only then consider broader structural cleanup or repo resync work

Do not invert this order unless Tommy explicitly changes priorities.

## Rules for content recovery work

When a content layer has been reconstructed from chat history or raw fragments:
- treat the restored version as provisional
- compare it against the known stronger intent from the same day
- improve it toward specificity, operational detail, and Tommy's real voice
- do not replace grounded details with generic smooth prose

The target is not "pretty writing."
The target is writing that feels like Tommy and carries more of what the earlier, better pass had.

## Rules for Travel Trail v4 work

Travel Trail is currently in a fragile improved state.

Meaning:
- modal behavior is a real win and should be preserved
- contextual routing is partly improved but still imperfect
- future fixes should be narrow, testable, and reversible

Do not do another big blind rewrite of route state, lane selection, or archive behavior.
Instead:
- identify exact failing clicks
- trace the resulting hash/state/lane selection
- patch precedence or context rules surgically
- re-test the exact reported case

## Repo-truth rule

Before doing new work, verify which repo is the actual target.

Main working repo:
- `/home/tm/.openclaw/workspace/captain-tommy-website`

Publish repo:
- `/home/tm/.openclaw/workspace/captain-tommy-website-publish`

Do not assume they are in sync.
Do not assume the more modern-looking file is the truer one.
Check the actual branch, commit chain, and content counts.

## Anti-repeat rule

Today's waste came partly from having to do meaningful work twice.
Future sessions should explicitly avoid repeating that pattern.

Before any cleanup or reduction pass, ask:
- will this remove real runtime assets?
- will this drop actual writing/content work?
- will this separate voice/content improvements from the publish surface?
- am I cleaning appearances instead of preserving the real site?

If the answer might be yes, stop and verify first.

## Voice rule remains active

Tommy's raw fragments, notes, and story stubs are both:
- content source material
- evidence of voice

Whenever new raw writing appears:
- consult `CHARACTER_BIBLE.md`
- preserve blunt operational phrasing and dry understatement
- update the bible if a repeatable voice pattern becomes clearer

## Success condition for the next session

The next session is successful if:
- the four recovered entries are restored to stronger quality
- Travel Trail v4 behaves correctly for the specific contextual-link cases Tommy cares about
- no content or context is lost in the process

That is more important than any additional polishing flourish.
