# Baton: Captain Tommy Website Publish Recovery and V4 Follow-ups

Date: 2026-04-20
Project: `captain-tommy-website-publish`
Status: Published to `main`, substantially recovered, good enough for night stop, but not fully clean in Travel Trail v4 behavior or restored writing quality

## What happened today

Today turned into a double-work recovery day.

A clean publish repo had been assembled to create a push-safe public branch, but in the process some of the actual 2026-04-20 work was missing or partially flattened. That caused two overlapping problems:

1. the homepage and Travel Trail were liveable but had behavior regressions
2. four real content entries and improved character-bible guidance from earlier in the day had been lost from the clean publish snapshot and had to be reconstructed

We recovered enough to publish tonight, but future work should treat this as a recovered state, not a final polished one.

## Key publish outcome tonight

Pushed to production from local branch `clean-publish` to remote `main`.

Latest pushed commit at end of session:
- `c872b41` `Tweak place lane default filter labels`

Push result already succeeded.

## Important publish commit chain from tonight

The meaningful late-session publish commits were:
- `b260210` Restore Great Lakes homepage featured card
- `6808629` Restore 4/20 Tommy voice content and character bible updates
- `d256075` Move travel trail written content into contextual modals
- `23da3ce` Route homepage and archive links into correct travel trail contexts
- `7b635d1` Fix trail lane targeting and archive modal routing
- `9535af2` Open trail entries behind modal in matching lane context
- `530df6a` Force corridor pills to stay in corridor lane
- `ca2040e` Remove homepage what matters section
- `faac921` Reorder adventure structure cards
- `c872b41` Tweak place lane default filter labels

There were also dead-end/reverted attempts during the day. Do not assume every earlier commit on the branch reflects the final intended direction without checking this chain.

## What is now true on the live site

### Homepage
- Great Lakes card is back on homepage.
- The "What matters here" section was removed because it still read like site scaffolding instead of payoff.
- "Adventure Structure" cards were reordered to:
  1. Boat life
  2. Places worth returning to
  3. Deliveries

### Travel Trail v4
- Written content opens in modal form instead of dumping long growing inline lists into the page.
- Homepage pills and archive entry links now attempt to route into a matching lane/context before opening the modal.
- Place lane defaults to `All regions` instead of `Hudson River NYC`.
- Region label rendering now preserves `NYC` and `ICW` capitalization.

### Content recovery
- The four real written inputs from 2026-04-20 were restored into the publish repo and the content indices were regenerated.
- Character bible updates based on Tommy's raw writing were restored.

## The four recovered content pieces

These are the important restored raw-content-derived entries from earlier on 2026-04-20:
- log: New York Harbor arrival in June 2024 on Lady Victory, learning the boat after sudden command handoff, radar/plotter repaired, dense harbor traffic under Verrazzano
- story: Staniel Cay Bahamas sewage / pump / Y-valve disaster on Lady B during boss's birthday trip, emergency pump flown in and installed
- note: always check the whole interior before departure, because the red wine / crystal gift disaster in the V-berth of the tender proved that point
- memory fragment: the color change of the Gulf Stream crossing into the Bahamas, including the emotional shift and occasional dolphins

## Important unresolved issues

### 1. Travel Trail v4 lane routing is improved but still not correct
Tommy's final judgment tonight:
- modal behavior is much better
- some contextual pills still route into the Chapter lane when they should not
- not worth chasing further tonight

Interpretation:
- the contextual-modal architecture is now in the right neighborhood
- hash/state/lane precedence is still not fully correct
- future fixes should be surgical, not another large speculative rewrite

### 2. The recovered four entries are present, but the prose quality is below the stronger earlier pass
Tommy explicitly said the restored entries are weaker than the better edits that existed earlier and were lost.

That means tomorrow's work is not "write from scratch," but:
- restore those four entries to the earlier higher-quality expanded state
- preserve Tommy's real voice from the raw inputs
- avoid turning them into generic polished travel writing

### 3. The day contained duplicated work and contradictory repo states
Be careful on re-entry.

There were at least three overlapping realities today:
- the main working repo with broader local curation work
- the clean publish repo intended to be public-safe
- partially stale/reconstructed publish content that looked modern in shell but was missing the actual 4/20 content layer

Do not trust appearances. Verify repo, branch, and actual content counts before editing.

## Key repo distinctions

### Main working repo
Path:
- `/home/tm/.openclaw/workspace/captain-tommy-website`

Role:
- broader working/canonical build space
- contains larger local asset and curation state
- not the same thing as the clean public push repo

### Publish repo
Path:
- `/home/tm/.openclaw/workspace/captain-tommy-website-publish`

Branch used for publish work tonight:
- `clean-publish`

Remote push target used tonight:
- `clean-publish:main`

This repo is the one that matters first for tomorrow's live-site cleanup unless a deliberate resync from main working repo is chosen.

## Recommended re-entry order tomorrow

1. open `captain-tommy-website-publish`
2. verify branch and latest commits match tonight's chain
3. inspect the four restored content files and generated indices
4. improve those four entries back toward the stronger earlier quality
5. then resume Travel Trail v4 routing cleanup from the currently improved modal/context version, not from older theories
6. only after that consider whether the clean publish repo should be refreshed again from the main working repo or left as the live canonical surface

## Guardrails for tomorrow

- Do not redo the whole routing system from scratch.
- Do not assume the main repo and publish repo are in sync.
- Do not let another clean-up pass accidentally drop content or voice updates again.
- Treat Tommy's raw fragments as both source content and voice evidence.
- Before rewriting the four entries, read `CHARACTER_BIBLE.md` first.

## Quick sanity facts worth remembering

- live site tonight is acceptable and substantially better than the broken/stale state
- modal behavior is the biggest functional improvement that stuck
- Great Lakes card is back
- the fake-scaffolding homepage section is gone
- Places lane default is all regions
- `NYC` and `ICW` capitalization fix landed
- deeper v4 lane correctness still needs another pass
- restored content exists, but needs better prose restoration tomorrow
