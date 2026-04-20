# Content Schema and Index Plan

A scale-ready content model for logs, stories, notes, image-backed memories, and future archive growth.

## Recommendation

Use a hybrid system:

- Markdown + YAML frontmatter for authoring and canonical editorial source
- generated JSON for site rendering
- SQLite as the indexing, search, and relationship layer

This keeps content human-writable while giving the archive room to grow without turning into an unsearchable pile.

## Goals

The system should support:

- rapid entry of remembered moments during passage or downtime
- longform stories written later from those remembered fragments
- logs shown both on the homepage and in the full Travel Trail archive
- notes attached to places, passages, or images
- relationships to gallery photos that help support the story
- cross-navigation by place, corridor, chapter, date, year, tags, boats, people, and image ids
- enough scale to keep working as content grows heavily over time

## Architecture layers

## 1. Authoring layer

Canonical source lives as Markdown files with frontmatter.

```text
content/
  logs/
  stories/
  notes/
```

These files are the editorial truth.

## 2. Build layer

A build script parses content, validates links, resolves image references, and generates:

- site JSON feeds
- a local SQLite index database

## 3. Delivery layer

The site consumes generated JSON files for rendering.

SQLite is for indexing, validation, search, and future intake/admin helpers, not for serving the static site directly.

## Canonical content folders

```text
content/
  logs/
    2025/
      2025-03-03-crossing-to-chub-cay.md
      2025-05-14-boca-to-nyc-run.md
  stories/
    home-waters/
      thirteen-foot-whaler-years.md
    bahamas/
      learning-the-exumas.md
    nyc/
      city-water-after-dark.md
  notes/
    passage/
      gulf-stream-window-rule.md
    places/
      fort-lauderdale-yard-rhythm.md
      normans-cay-first-impression.md
    boats/
      first-boss-new-boat-adjustment.md
```

## Canonical identity model

Every content item gets:

- a stable `id`
- a `type`
- one authoring file path
- explicit relationships

Example ids:
- `log-2025-03-03-crossing-to-chub-cay`
- `story-thirteen-foot-whaler-years`
- `note-gulf-stream-window-rule`

These ids are what other records refer to.

## Frontmatter schema

All content types share a core schema.

## Shared fields

```yaml
id: log-2025-03-03-crossing-to-chub-cay
type: log
title: Crossing to Chub Cay
slug: crossing-to-chub-cay
date: 2025-03-03
dateEnd:
summary: Left South Florida on a clean weather window and settled into the long pull east.
status: published
featured: false
visibility: public
sourcePriority: 50
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
seasonYears:
  - 2025-spring
tags:
  - crossing
  - bahamas
  - weather-window
boats: []
people: []
imageIds: []
coverImageId:
relatedContent: []
sourceLinks: []
draftNotes:
intake:
  source: manual
  capturedAt: 2026-04-19T09:00:00-04:00
---
```

## Field notes

### `id`
Stable internal identifier. Never change casually.

### `type`
One of:
- `log`
- `story`
- `note`

### `slug`
Display or URL helper.

### `date` / `dateEnd`
For a point in time or a span.

### `status`
Suggested values:
- `draft`
- `published`
- `hidden`

### `sourcePriority`
Optional future helper if multiple related items compete for display prominence.

### `corridors`, `places`, `chapters`
Explicit relationship arrays.

### `years`, `seasonYears`
Useful for filtering and grouping.

### `imageIds`
Important: use stable image ids, not raw file paths.

### `coverImageId`
Optional lead image for cards or feature views.

### `relatedContent`
Optional manual related-content override using content ids.

### `sourceLinks`
For optional external/internal references later.

### `draftNotes`
Optional private or build-excluded editorial notes.

### `intake`
Tracks how the item entered the system.

## Type-specific guidance

## Logs

Logs should usually have:
- precise date
- clear place/corridor links
- optional image ids
- concise but real narrative body

Good for:
- runs
- deliveries
- crossings
- workdays with meaningful motion
- moments worth timeline placement

## Stories

Stories may have:
- broader time span
- stronger narrative body
- more images
- featured treatment
- more chapter emphasis

Good for:
- memories
- major phases
- turning points
- historical reflections

## Notes

Notes should be lighter and faster.

Good for:
- remembered details
- local knowledge
- quick observations
- route truths
- fragments that may later feed logs/stories

This matters because during passage you may send many notes that later become richer logs or stories.

## Image-link model

This is the crucial part for scale.

Content should not depend on raw derivative file paths.

Instead, every content item should reference stable image ids from the gallery/catalog system.

Example:

```yaml
imageIds:
  - south-florida-fort-lauderdale-2025-0012
  - bahamas-crossing-2025-0004
  - bahamas-chub-cay-2025-0007
coverImageId: bahamas-crossing-2025-0004
```

## Why image ids matter

If gallery assets are rebuilt, moved, or regenerated:
- file paths may change
- derivatives may change
- manifests may change

But if image ids remain stable, content relationships survive.

## Required image-side support

Image manifests/catalog records should expose stable ids and enough metadata to resolve them.

Suggested image catalog fields:
- `id`
- `region`
- `place`
- `year`
- `seasonYear`
- `source`
- `thumb`
- `large`
- `captureDate`
- `lat`
- `lon`
- `tags`

## SQLite index purpose

SQLite is not the editorial source.
It is the fast relationship/search/index layer.

Use it for:
- validation
- browsing
- searching
- reverse lookups
- future intake tools
- future admin/reporting helpers

## Suggested SQLite tables

## `content_items`

One row per log/story/note.

Fields:
- `id` TEXT PRIMARY KEY
- `type` TEXT
- `title` TEXT
- `slug` TEXT
- `date` TEXT
- `date_end` TEXT
- `summary` TEXT
- `status` TEXT
- `featured` INTEGER
- `visibility` TEXT
- `source_priority` INTEGER
- `cover_image_id` TEXT
- `body_markdown` TEXT
- `body_html` TEXT
- `source_path` TEXT
- `created_at` TEXT
- `updated_at` TEXT

## `content_places`

Many-to-many join.

Fields:
- `content_id` TEXT
- `place_id` TEXT

## `content_corridors`

Fields:
- `content_id` TEXT
- `corridor_id` TEXT

## `content_chapters`

Fields:
- `content_id` TEXT
- `chapter_id` TEXT

## `content_years`

Fields:
- `content_id` TEXT
- `year` INTEGER

## `content_season_years`

Fields:
- `content_id` TEXT
- `season_year` TEXT

## `content_tags`

Fields:
- `content_id` TEXT
- `tag` TEXT

## `content_people`

Fields:
- `content_id` TEXT
- `person_id` TEXT

## `content_boats`

Fields:
- `content_id` TEXT
- `boat_id` TEXT

## `content_images`

Fields:
- `content_id` TEXT
- `image_id` TEXT
- `sort_order` INTEGER
- `is_cover` INTEGER
- `caption_override` TEXT

## `content_related`

Manual content-to-content links.

Fields:
- `content_id` TEXT
- `related_content_id` TEXT
- `relation_type` TEXT

## `images`

Mirror useful fields from image manifest/catalog for lookup.

Fields:
- `id` TEXT PRIMARY KEY
- `region_id` TEXT
- `place_id` TEXT
- `year` INTEGER
- `season_year` TEXT
- `capture_date` TEXT
- `thumb_path` TEXT
- `large_path` TEXT
- `source_path` TEXT

## `places`

Fields:
- `id` TEXT PRIMARY KEY
- `region_id` TEXT
- `name` TEXT
- `sub` TEXT

## `corridors`

Fields:
- `id` TEXT PRIMARY KEY
- `name` TEXT

## `chapters`

Fields:
- `id` TEXT PRIMARY KEY
- `name` TEXT
- `year_range` TEXT
- `sort_order` INTEGER

## Scale behavior

This design scales because:
- authoring stays simple even as content volume rises
- relationship lookups stay fast
- filters remain cheap
- reverse image-to-story and place-to-log queries become easy
- the site can keep consuming compact generated JSON instead of doing runtime heavy lifting

## Intake model for passage-time memories

This part matters a lot.

You said you will remember things during passage and send them in while underway or during downtime.

So the system should support two lanes:

## Lane 1: direct finished content
For when you send something already close to publishable.

Flow:
1. create Markdown record
2. attach metadata
3. optionally link images
4. publish

## Lane 2: quick memory capture
For when you send rough fragments that may become content later.

Suggested staging area:

```text
intake/
  memories/
    2026-05-14-2140-bahamas-crossing-note.md
    2026-05-15-0830-nyc-night-arrival-fragment.md
```

These can use a lighter schema:

```yaml
id: intake-2026-05-14-2140-bahamas-crossing-note
type: intake-memory
date: 2026-05-14T21:40:00-04:00
summary: Remember how the water changed right after the edge of the stream.
possiblePlaces:
  - crossing
possibleCorridors:
  - bahamas
possibleChapters:
  - exploration-years
possibleImageIds: []
status: unprocessed
---
Raw remembered fragment here.
```

Later, intake items can be promoted into:
- log
- story
- note

This keeps fast capture from cluttering published content.

## Generated site JSON outputs

Recommended outputs:

### `assets/data/content-index.json`
All published content, normalized.

### `assets/data/logs-recent.json`
Recent logs only, for homepage.

### `assets/data/logs-archive.json`
All published logs.

### `assets/data/stories-index.json`
All published stories.

### `assets/data/notes-index.json`
All published notes.

### `assets/data/content-by-place.json`
Map place -> content ids.

### `assets/data/content-by-corridor.json`
Map corridor -> content ids.

### `assets/data/content-by-chapter.json`
Map chapter -> content ids.

### `assets/data/content-by-year.json`
Map year -> content ids.

### `assets/data/content-by-image.json`
Map image id -> content ids.

This last one is especially useful for gallery-backed storytelling.

## UI/navigation implications

## Homepage

Homepage logs section should read from `logs-recent.json`.

Each item can link to:
- full log entry
- related place in Travel Trail
- related gallery images

## Travel Trail

Travel Trail should become the deep archive browser.

Add content filters:
- content type
- year
- corridor
- place
- chapter
- maybe tags later

Each place panel should be able to show:
- gallery images
- linked logs
- linked stories
- linked notes

Each chapter panel should be able to show:
- chapter intro
- related places
- related logs/stories/notes

Each image in a gallery could eventually show:
- related logs
- related stories
- related notes

That is where the system starts feeling truly connected.

## Suggested first schema additions needed now

To prepare the current site for this future:

### Add explicit chapter ids
Suggested ids:
- `home-waters-runs`
- `exploration-years`
- `deeper-into-the-islands`
- `city-water-and-east-end-runs`

### Keep place ids stable
Already mostly in place.

### Keep image ids stable
Very important. Do not let rebuilds randomly regenerate ids.

## Recommended next implementation steps

### Step 1
Add chapter ids into the front-end data model.

### Step 2
Create content folder skeleton:
- `content/logs/`
- `content/stories/`
- `content/notes/`
- `intake/memories/`

### Step 3
Create 2 to 3 real pilot entries of each type.

### Step 4
Write a parser/build script that:
- reads Markdown
- validates ids
- resolves image ids
- writes JSON
- populates SQLite

### Step 5
Wire homepage recent logs.

### Step 6
Wire Travel Trail content layer.

## Recommendation in one sentence

Use Markdown as the canonical editorial source, stable image ids as the media relationship key, generated JSON for the static site, and SQLite as the scalable index that keeps the whole archive searchable and connected.
