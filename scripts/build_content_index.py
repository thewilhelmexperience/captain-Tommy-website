#!/usr/bin/env python3
"""Build starter content JSON indexes and a SQLite relationship index.

This is an initial scaffold, not the finished production builder.
It establishes the folder conventions, metadata expectations, and output targets
for logs, stories, notes, memories, and intake-backed promotion later.
"""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = ROOT / 'content'
OUTPUT_DIR = ROOT / 'assets' / 'data'
DB_PATH = ROOT / 'data' / 'content-index.sqlite3'

VALID_TYPES = {'log', 'story', 'note', 'memory'}

FOLDER_TYPE_MAP = {
    'logs': 'log',
    'stories': 'story',
    'notes': 'note',
    'memories': 'memory',
}


@dataclass
class ContentRecord:
    id: str
    type: str
    title: str
    slug: str
    date: str | None
    dateEnd: str | None
    summary: str
    status: str
    featured: bool
    visibility: str
    corridors: list[str]
    places: list[str]
    chapters: list[str]
    years: list[int]
    seasonYears: list[str]
    tags: list[str]
    boats: list[str]
    people: list[str]
    imageIds: list[str]
    coverImageId: str | None
    relatedContent: list[str]
    sourcePath: str
    body: str


def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith('---\n'):
        return {}, text
    parts = text.split('\n---\n', 1)
    if len(parts) != 2:
        return {}, text
    raw = parts[0][4:]
    body = parts[1]
    data: dict[str, Any] = {}
    current_key: str | None = None
    for line in raw.splitlines():
        if not line.strip():
            continue
        if line.startswith('  - ') and current_key:
            existing = data.get(current_key)
            if existing is None:
                data[current_key] = []
            elif not isinstance(existing, list):
                data[current_key] = [existing]
            data[current_key].append(line[4:].strip())
            continue
        if ': ' in line:
            key, value = line.split(': ', 1)
            current_key = key.strip()
            value = value.strip()
            if value == '[]':
                data[current_key] = []
            elif value.lower() == 'true':
                data[current_key] = True
            elif value.lower() == 'false':
                data[current_key] = False
            elif value == '':
                data[current_key] = None
            else:
                data[current_key] = value
        elif line.endswith(':'):
            current_key = line[:-1].strip()
            data[current_key] = None
    return data, body.strip()


def normalize_record(path: Path) -> ContentRecord:
    meta, body = parse_frontmatter(path.read_text())
    parent_dir = path.parent.parts[0] if path.is_relative_to(CONTENT_DIR) else path.parts[-3]
    record_type = meta.get('type') or FOLDER_TYPE_MAP.get(parent_dir, parent_dir.rstrip('s'))
    if record_type not in VALID_TYPES:
        raise ValueError(f'{path}: invalid type {record_type!r}')
    title = meta.get('title') or path.stem.replace('-', ' ').title()
    slug = meta.get('slug') or path.stem
    return ContentRecord(
        id=meta.get('id') or f'{record_type}-{slug}',
        type=record_type,
        title=title,
        slug=slug,
        date=meta.get('date'),
        dateEnd=meta.get('dateEnd'),
        summary=meta.get('summary') or '',
        status=meta.get('status') or 'draft',
        featured=bool(meta.get('featured', False)),
        visibility=meta.get('visibility') or 'public',
        corridors=list(meta.get('corridors') or []),
        places=list(meta.get('places') or []),
        chapters=list(meta.get('chapters') or []),
        years=[int(y) for y in (meta.get('years') or [])],
        seasonYears=list(meta.get('seasonYears') or []),
        tags=list(meta.get('tags') or []),
        boats=list(meta.get('boats') or []),
        people=list(meta.get('people') or []),
        imageIds=list(meta.get('imageIds') or []),
        coverImageId=meta.get('coverImageId'),
        relatedContent=list(meta.get('relatedContent') or []),
        sourcePath=str(path.relative_to(ROOT)),
        body=body,
    )


def load_content() -> list[ContentRecord]:
    records: list[ContentRecord] = []
    for path in sorted(CONTENT_DIR.rglob('*.md')):
        if path.name == 'README.md':
            continue
        records.append(normalize_record(path))
    return records


def write_json(records: list[ContentRecord]) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    published = [r for r in records if r.status == 'published']
    (OUTPUT_DIR / 'content-index.json').write_text(json.dumps([asdict(r) for r in published], indent=2) + '\n')
    (OUTPUT_DIR / 'logs-recent.json').write_text(json.dumps([asdict(r) for r in published if r.type == 'log'], indent=2) + '\n')
    (OUTPUT_DIR / 'stories-index.json').write_text(json.dumps([asdict(r) for r in published if r.type == 'story'], indent=2) + '\n')
    (OUTPUT_DIR / 'notes-index.json').write_text(json.dumps([asdict(r) for r in published if r.type == 'note'], indent=2) + '\n')
    (OUTPUT_DIR / 'memories-index.json').write_text(json.dumps([asdict(r) for r in published if r.type == 'memory'], indent=2) + '\n')


def rebuild_sqlite(records: list[ContentRecord]) -> None:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.executescript(
        '''
        DROP TABLE IF EXISTS content_items;
        DROP TABLE IF EXISTS content_places;
        DROP TABLE IF EXISTS content_corridors;
        DROP TABLE IF EXISTS content_chapters;
        DROP TABLE IF EXISTS content_years;
        DROP TABLE IF EXISTS content_images;

        CREATE TABLE content_items (
          id TEXT PRIMARY KEY,
          type TEXT NOT NULL,
          title TEXT NOT NULL,
          slug TEXT NOT NULL,
          date TEXT,
          date_end TEXT,
          summary TEXT,
          status TEXT NOT NULL,
          featured INTEGER NOT NULL,
          visibility TEXT NOT NULL,
          cover_image_id TEXT,
          source_path TEXT NOT NULL,
          body_markdown TEXT NOT NULL
        );

        CREATE TABLE content_places (content_id TEXT NOT NULL, place_id TEXT NOT NULL);
        CREATE TABLE content_corridors (content_id TEXT NOT NULL, corridor_id TEXT NOT NULL);
        CREATE TABLE content_chapters (content_id TEXT NOT NULL, chapter_id TEXT NOT NULL);
        CREATE TABLE content_years (content_id TEXT NOT NULL, year INTEGER NOT NULL);
        CREATE TABLE content_images (content_id TEXT NOT NULL, image_id TEXT NOT NULL, sort_order INTEGER NOT NULL DEFAULT 0);
        '''
    )
    for record in records:
        cur.execute(
            '''INSERT INTO content_items
            (id, type, title, slug, date, date_end, summary, status, featured, visibility, cover_image_id, source_path, body_markdown)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (
                record.id, record.type, record.title, record.slug, record.date, record.dateEnd,
                record.summary, record.status, int(record.featured), record.visibility,
                record.coverImageId, record.sourcePath, record.body,
            ),
        )
        cur.executemany('INSERT INTO content_places (content_id, place_id) VALUES (?, ?)', [(record.id, v) for v in record.places])
        cur.executemany('INSERT INTO content_corridors (content_id, corridor_id) VALUES (?, ?)', [(record.id, v) for v in record.corridors])
        cur.executemany('INSERT INTO content_chapters (content_id, chapter_id) VALUES (?, ?)', [(record.id, v) for v in record.chapters])
        cur.executemany('INSERT INTO content_years (content_id, year) VALUES (?, ?)', [(record.id, v) for v in record.years])
        cur.executemany('INSERT INTO content_images (content_id, image_id, sort_order) VALUES (?, ?, ?)', [(record.id, v, i) for i, v in enumerate(record.imageIds)])
    conn.commit()
    conn.close()


def main() -> None:
    records = load_content()
    write_json(records)
    rebuild_sqlite(records)
    print(f'indexed_records {len(records)}')
    print(f'json_dir {OUTPUT_DIR}')
    print(f'sqlite_db {DB_PATH}')


if __name__ == '__main__':
    main()
