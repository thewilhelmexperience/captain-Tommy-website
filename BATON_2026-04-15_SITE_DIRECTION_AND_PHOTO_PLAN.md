# Baton: Captain Tommy Website, Site Direction and Photo Plan

Date: 2026-04-15
Project: `captain-tommy-website`
Status: Active, first real image pass landed, homepage voice pass underway, interactive route-map prototype in parallel

## Current state

The project has moved well beyond the original placeholder site and now has a credible first-pass visual identity.

Current homepage direction is intentionally focused on:
- Captain Tommy as a person and living brand
- story / voyage / adventure energy
- long-term expandability
- recruiter path moved away from dominating the homepage
- real imagery and real voice replacing scaffold text

The recruiter/CV side still exists and remains accessible via:
- `cv.html`
- QR code
- downloadable PDF files

## Current homepage features already in place

Implemented in `index.html`:
- adventure-first hero
- personal-brand framing instead of CV-first framing
- story/about section
- voyages/waters section
- route-map style framework (still slated for real interactive replacement)
- cinematic/photo-ready sections
- polaroid-style story framework
- Captain’s Log framework
- future journal/content-lane scaffolding
- contact section with CV side-door access

## What changed on 2026-04-16

Major progress landed during the iCloud photo and copy-shaping pass:
- first real homepage imagery was selected, optimized, and pushed
- homepage now uses lightweight `assets/site-photos-web/*.webp` assets instead of placeholders
- repo was cleaned so full originals and review material stay local-only (`photo-ingest/`, `photo-review/`, `assets/site-photos/` ignored)
- local branch history was rewritten before push so giant image payloads never reached GitHub
- current remote commit after image push is `4792465` (`Add first-pass Captain Tommy homepage imagery`)
- an additional local-only copy pass is in progress after that push, shaping the homepage into Tommy’s real voice before the next publish
- a `CHARACTER_BIBLE.md` has now been created and should be treated as a primary tone reference for future additions

## Current key commits

Recent useful commits in project repo:
- `4348b56` Build premium first-pass Captain Tommy website
- `a86830a` Polish Captain Tommy homepage presentation
- `c955ee8` Refocus homepage on Captain Tommy adventure brand
- `8cc916a` Add cinematic content lanes to homepage
- `fa1e41c` Start interactive travel narrative framework

## Remote

Git remote was updated to the new canonical path:
- `git@github.com:thewilhelmexperience/captain-Tommy-website.git`

Pushes are succeeding.

## Critical strategic decision

The homepage is **not** supposed to be a recruiter-first page.
That was explicitly corrected.

The intended split is:
- `index.html` = Captain Tommy vibe, adventures, stories, travel, personal brand
- `cv.html` = recruiter/employer landing page

## Important user vibe notes

Tommy’s self-description and framing are essential and should guide future copy:
- People tell him he is lucky.
- His view is that he often ends up in places where luck is necessary to move forward.
- He tends to walk through doors that open rather than obsessing over what lies beyond them.
- That does not mean random drifting or "wherever the tide decides." The right framing is calculated openness, intentional movement, and stepping beyond the comfort zone without abandoning judgment.
- He does not see himself as superior or trying to sell a fantasy.
- He is simply living a less-standard life and exposing the trail rather than pushing a story.
- He is calm, funny, and unflappable under pressure.
- He has a sharp sense of humor, but the site should not become jokey or cute.
- He is fascinated by the different human character of ports, islands, cities, and boating communities.
- He feels most at home in island and South Florida rhythms, but adapts well in new places.
- Driving the boat is the easy part; the real work is responsibility, preparation, safety, systems, and making someone else’s experience come together cleanly.
- He needs to know what a vessel truly has to give before he can trust her.

This should guide homepage voice.

## High-priority next phase

When the external drive is connected and available:
1. locate the photo source on the drive
2. inventory images
3. identify the strongest images for:
   - homepage hero
   - voyages/waters cards
   - polaroid stack
   - route-map/story moments
   - potential featured vessel/life images
4. inspect EXIF metadata, especially:
   - GPS/location
   - timestamps
   - device/source consistency
5. group photos by:
   - place
   - era/season
   - boat/chapter
   - aesthetic strength
6. create a curated narrative subset instead of using the full pile indiscriminately

## Photo selection principles

Pick images that feel:
- real
- atmospheric
- earned
- visually strong
- story-rich
- capable + adventurous

Be careful with anything that makes Tommy look:
- reckless
- showboaty
- irresponsible
- try-hard

If a photo is visually cool but weakens credibility, do not prioritize it.

## Strong likely image buckets

Look for:
- helm / underway portraits
- Bahamas water / cuts / anchorages
- golden-hour East Coast / ICW / offshore atmosphere
- Fort Lauderdale / home-waters visual anchors
- Great Lakes horizon / delivery energy
- boat-life detail shots that feel lived-in

## EXIF / route-map ambition

If usable EXIF location data survives, build toward:
- a travel trail / route-map experience
- stop-based stories
- clustered photos by region or chapter
- narrative geography instead of random gallery dumping

If EXIF is partial or poor, fake nothing. Use human curation and labeled story groupings instead.

## Content collaboration plan with Tommy

Tommy said he will be happy to write and/or guide log entries.
Use lightweight prompts instead of requesting polished prose.

Best prompts:
- Where were you going?
- What made the trip memorable?
- What boat was it?
- What was the feel of that chapter?
- Was there a moment, anchorage, stop, or weather decision that stuck with you?
- What would a stranger find interesting or unexpectedly human about that trip?

## Guardrails

Never drift into:
- generic luxury-yacht marketing vibe
- fake philosopher captain voice
- social-media influencer energy
- bragging
- glamorized recklessness

Always preserve:
- competence
- humanity
- wryness
- grounded adventure
- calculated risk, not chaos
- credibility first

## Practical next actions on resume

When resuming work, first do these in order:
1. inspect external drive mount state and locate photo payload
2. inventory candidate images and metadata
3. create a working shortlist folder or manifest
4. update homepage with first real image placements
5. document selected narrative/story clusters
6. commit and push incrementally

## Immediate next priorities

1. finish humanizing the remaining homepage sections top-to-bottom
2. review whether the meta "what this site is really trying to show" section should stay, be merged, or be replaced with more lived content
3. build and review a real interactive route-map prototype with clickable stops/cards
4. later integrate the chosen route-map direction into the homepage
5. continue refining image selections where captions/regions still mismatch
6. push the next copy pass only after review

## Files worth reading first next session

- `MISSION_DIRECTIVE_2026-04-15.md`
- `BATON_2026-04-15_SITE_DIRECTION_AND_PHOTO_PLAN.md`
- `CHARACTER_BIBLE.md`
- `index.html`
- `cv.html`
- any generated photo inventory/manifests once created
