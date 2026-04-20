# Content Architecture Sketch

A clean content system for Captain Tommy that keeps authorship simple, relationships explicit, and front-end navigation flexible.

## Recommendation

Use a filesystem-first content model:

- author content as Markdown files
- store structured metadata in frontmatter
- generate JSON datasets for the site at build time
- keep relationships explicit across places, corridors, chapters, years, and content types

Avoid XML. Avoid a runtime database unless the project later grows into multi-user editing, search-heavy tooling, or private workflow state that plain files can no longer carry comfortably.

## Core principles

1. Canonical content lives in files, not in the browser data output.
2. The site consumes generated JSON, not raw Markdown.
3. One content item can relate to many places, corridors, chapters, and years without duplication.
4. Index-page excerpts and Travel Trail archive views should come from the same underlying content records.
5. Photos, logs, notes, and stories should be connected but not forced into the same visual treatment.

## Content types

### Logs

Best for chronological entries, passages, work runs, repositionings, deliveries, crossings, and dated moments.

Examples:
- Fort Lauderdale to Chub Cay run
- Palm Beach weather window note
- East Coast reposition southbound

Behavior:
- newest entries appear on `index.html`
- full archive appears in Travel Trail
- should sort naturally by date

### Stories

Best for fuller narrative pieces, memories, reflections, standout trips, major experiences, and editorial longform.

Examples:
- first crossing memory
- learning the islands
- what New York harbor really feels like after dark

Behavior:
- can be tied to one date or a broader span
- should appear in Travel Trail as a richer narrative layer
- may deserve featured treatment in some sections

### Notes

Best for short observations, context fragments, boat-specific notes, local knowledge, and details that matter but do not need full story treatment.

Examples:
- bridge timing note
- anchorage impression
- marina/work/owner context
- weather or route lesson

Behavior:
- lighter-weight than logs or stories
- useful as supporting material beneath places and chapters

### Optional later types

These do not need to exist on day one, but the model should allow them:
- routes
- boats
- people/crew
- galleries
- documents
- audio clips

## Proposed folder structure

```text
content/
  logs/
    2025/
      2025-05-14-boca-to-nyc-run.md
      2025-03-03-crossing-to-chub-cay.md
  stories/
    home-waters/
      thirteen-foot-whaler.md
    bahamas/
      learning-the-exumas.md
  notes/
    places/
      fort-lauderdale-yard-rhythm.md
      normans-cay-first-impression.md
    routes/
      gulf-stream-window-rule.md
```

Generated outputs:

```text
assets/data/
  content-index.json
  logs-recent.json
  logs-archive.json
  stories-index.json
  notes-index.json
  content-by-place.json
  content-by-corridor.json
  content-by-chapter.json
  content-by-year.json
```

If preferred, these generated files can live under `assets/content/` instead of `assets/data/`. The important part is that they are generated, not manually maintained.

## Recommended frontmatter schema

Use YAML frontmatter in Markdown files.

Example log:

```md
---
id: log-2025-03-03-crossing-to-chub-cay
type: log
title: Crossing to Chub Cay
date: 2025-03-03
summary: Left South Florida on a clean weather window and settled into the long pull east.
status: published
featured: false
corridors:
  - south-florida
  - bahamas
places:
  - fort-lauderdale
  - crossing
  - chub-cay
chapters:
  - exploration-years
years:
  - 2025
tags:
  - crossing
  - weather-window
  - bahamas
boats: []
people: []
images:
  - assets/images/bahamas/chub-cay/2025/large/example.jpg
related:
  stories: []
  notes: []
---

Body copy goes here.
```

Example story:

```md
---
id: story-thirteen-foot-whaler
type: story
title: The Thirteen-Foot Whaler Years
date: 1993-06-01
dateEnd: 1995-08-31
summary: When a tiny Whaler was not a toy but transportation, freedom, and the start of everything.
status: published
featured: true
corridors:
  - south-florida
places:
  - fort-lauderdale
  - boca-raton-delray
chapters:
  - home-waters-runs
years:
  - 1993
  - 1994
  - 1995
tags:
  - childhood
  - whaler
  - home-waters
images: []
related:
  logs: []
  notes: []
---

Story body goes here.
```

Example note:

```md
---
id: note-gulf-stream-window-rule
type: note
title: Gulf Stream Window Rule
date: 2025-03-01
summary: A short note about what actually makes a crossing day feel right.
status: published
corridors:
  - bahamas
  - south-florida
places:
  - crossing
chapters:
  - exploration-years
years:
  - 2025
tags:
  - crossing
  - seamanship
  - weather
images: []
related:
  logs:
    - log-2025-03-03-crossing-to-chub-cay
  stories: []
---

Short note body goes here.
```

## Shared metadata fields

Suggested common fields across logs, stories, and notes:

- `id`
- `type` (`log`, `story`, `note`)
- `title`
- `date`
- `dateEnd` (optional)
- `summary`
- `status` (`draft`, `published`)
- `featured` (optional)
- `corridors` (array)
- `places` (array)
- `chapters` (array)
- `years` (array)
- `tags` (array)
- `boats` (optional array)
- `people` (optional array)
- `images` (optional array)
- `related` (optional object)

This keeps the system explicit and lets the front end answer questions like:
- show all content tied to Norman's Cay
- show all 2021 Bahamas content
- show stories connected to Home Waters Runs
- show latest published logs on the homepage

## Relationship model

This is the important part.

Do not make logs or stories “belong” to only one thing.

A single item may connect to:
- one or more places
- one or more corridors
- one or more chapters
- one or more years
- one or more images

That means:
- a log can appear in the homepage recent feed
- the same log can appear in the Travel Trail archive
- the same log can appear under a place card
- the same log can appear inside a chapter view

No duplicated files, no duplicated copy, no split source of truth.

## Build pipeline

Recommended build flow:

1. Read Markdown files in `content/`
2. Parse frontmatter + body
3. Validate referenced corridors, places, and chapters
4. Generate normalized JSON records
5. Generate derived indexes for UI use

Outputs should include:

### 1. Master content index

`assets/data/content-index.json`

Contains every published content record in one normalized list.

### 2. Recent logs feed

`assets/data/logs-recent.json`

Used by `index.html` to show most recent log entries.

### 3. Archive datasets

- `assets/data/logs-archive.json`
- `assets/data/stories-index.json`
- `assets/data/notes-index.json`

Used by Travel Trail.

### 4. Relationship maps

- `assets/data/content-by-place.json`
- `assets/data/content-by-corridor.json`
- `assets/data/content-by-chapter.json`
- `assets/data/content-by-year.json`

These make UI lookups fast and simple.

## How this should appear in the site

## Index page

Index should show:
- latest logs
- maybe one featured story
- optionally one or two recent notes if they are strong enough

Important rule:
- homepage shows only a curated slice of the same content system
- it should not be a separate manually maintained content track

## Travel Trail page

Travel Trail should become the full archive browser.

It already has:
- corridors
- places
- chapters
- archive/photos

Add content as another navigable layer that can be filtered by:
- type
- year
- place
- corridor
- chapter

Recommended presentation:

### Corridor view
Show:
- representative places
- related logs
- related stories
- related notes

### Place view
Show:
- gallery
- place note/summary
- related logs
- related stories
- related notes

This is likely the strongest everyday browsing surface.

### Chapter view
Show:
- chapter intro
- representative places/stops
- most important logs/stories/notes tied to that arc

### Archive/content tab
Could become a combined content browser with toggles:
- All
- Logs
- Stories
- Notes

This avoids burying the non-photo material.

## Navigation suggestions

Recommended UI controls:

- top-level content-type filter: `All / Logs / Stories / Notes`
- year filter
- corridor filter
- place filter
- chapter filter
- sort options: newest, oldest, featured

Each content card should show:
- type
- title
- date or year span
- short summary
- linked places/corridors
- thumbnail if present

When opened, an entry should link back into:
- related place
- related chapter
- related gallery/images

## Intake/update workflow

Keep intake dead simple.

### Phase 1: manual-authoring friendly
- create Markdown file
- write frontmatter
- write body
- run build script

### Phase 2: assisted templates
Later we can add scripts like:
- `new_log.py`
- `new_story.py`
- `new_note.py`

That would scaffold a new file with required metadata.

### Phase 3: import helpers
Later still, we can support:
- turning trip notes into draft logs
- turning selected photo groups into draft story seeds
- generating suggested place/corridor tags from linked images

But the core model should stay plain-file first.

## Why not XML

XML would mostly give structure without giving much practical upside here.

Downsides:
- harder to hand-edit comfortably
- uglier authoring experience
- weaker fit with Markdown-driven content workflow
- not naturally pleasant for Git-based editorial work

It is not wrong, just not the right tool for this job.

## Why not a runtime database yet

A lightweight database could work, but it adds complexity before the project needs it.

It becomes worthwhile only if you later need:
- private draft dashboards
- complex full-text search
- rich editorial workflow state
- multiple editors at once
- API-driven admin interface

For the current phase, repo files + generated JSON is the sweet spot.

## Recommended identifiers

To keep references stable, chapters should get explicit ids too.

Suggested chapter ids:
- `home-waters-runs`
- `exploration-years`
- `deeper-into-the-islands`
- `city-water-and-east-end-runs`

Content items should reference those ids, not display names.

## Near-term implementation plan

### Step 1
Define the schema and folder structure.

### Step 2
Add chapter ids and make sure places/corridors already have stable ids.

### Step 3
Create a small pilot content set:
- 3 logs
- 2 stories
- 3 notes

### Step 4
Write a build script that generates:
- master content index
- recent logs feed
- place/corridor/chapter/year relationship maps

### Step 5
Wire homepage recent logs to generated JSON.

### Step 6
Wire Travel Trail content browser to the same data.

## Recommendation in one sentence

Use Markdown + frontmatter as the source of truth, generate JSON for the site, and make logs, stories, and notes one connected relationship graph rather than separate disconnected features.
