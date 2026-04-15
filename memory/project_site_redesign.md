---
name: captain-tommy-website redesign
description: Status and design decisions for the Captain Tommy Molenhouse personal yacht captain website
type: project
---

Full redesign of index.html completed April 2026. Site lives at captain-tommy.com on Cloudflare Pages.

**Why:** Brief called for the main site to feel like Tommy and his adventures, not a resume dump. CV should be a subpage only.

**Design decisions:**
- Color palette: dark navy (#05101e) + cyan accent (#4fc3f7) + seafoam (#7dd9a8) + gold (#c8a86b) for premium maritime feel
- Typography: Inter (body) + Playfair Display (headings, italic for hero)
- Hero: full-viewport CSS ocean gradient with animated shimmer — photo-ready (see <!-- PHOTO --> comments)
- Three new sections added: Cruising Grounds (4 region cards with CSS gradients), Vessels Commanded (4 spec cards), Captain's Log (narrative entries)
- Value prop uses 01/02/03 numbered cards, not a resume list
- Mobile nav: hamburger toggle, JS class-based

**Tech:** Plain static HTML/CSS — no build step, fast Cloudflare Pages deploy. CV stays at cv.html.

**Photo placeholders:** Comments in index.html mark exactly where hero photo, and each ground card photo should go. Suggested shots: aerial Bahamas turquoise / moody East Coast coastal / golden hour Fort Lauderdale / Lake Michigan open water.

**How to apply:** When photos arrive, add background-image to .hero-ocean and .ground-* classes per the <!-- PHOTO --> comments. Captain's Log entries can be updated as deliveries complete.
