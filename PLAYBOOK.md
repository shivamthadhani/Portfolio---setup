# AI-Powered SEO Content Production — Playbook / SOP

**Audience:** an in-house growth or content marketer at a startup (roughly 10–200 employees), running AI-assisted SEO content production on a lean budget with no dedicated AI-visibility analyst, enterprise tooling, or agency retainer.

**Methodology:** every recommendation below is sourced from `/research` in this repository — 10 practitioners' LinkedIn posts and YouTube transcripts collected May–June 2026 (see `/research/sources.md`). Where an expert's original recommendation assumed enterprise resources, I've adapted it for a lean team and labeled that adaptation explicitly as **[MY ADAPTATION]** — that framing is my interpretation, not the expert's stated recommendation. Sections asked for by the brief (disagreements, rejected ideas, original idea, weaknesses, who not to follow) are my own reasoning, clearly marked as such throughout.

---

## Executive Summary

**What this is:** a practical, source-backed playbook for AI-assisted SEO content production. Every recommendation traces back to a specific practitioner post or talk in this repository's `/research` folder — nothing here is invented.

**Who it's for:** an in-house growth or content marketer at a startup (roughly 10–200 employees) scaling content with AI, with no dedicated AI-visibility analyst, enterprise tool, or agency retainer.

**Five most important takeaways:**

1. Traffic is declining, but purchase intent isn't — track mentions, citations, and conversions, not just clicks (Core Principle 1).
2. Original expertise and real data beat generic AI content, every time a model chooses what to cite (Core Principle 2).
3. YouTube presence and off-site citations (Reddit, G2, third-party "best of" lists) matter as much as your own website (Core Principles 3–4).
4. Never publish AI output without human review, and never let AI claim experience it doesn't have (Core Principle 6, Section B).
5. Where experts genuinely disagree, this playbook picks a side and explains why (see *Where Experts Disagree*).

**How to use this document:** read the Playbook (Sections A–F) in order the first time, then use the checklists as your week-to-week reference. The sections after it — disagreements, rejections, original ideas, weaknesses, who not to follow — are judgment calls, included so you can see and challenge the reasoning behind the recommendations above them.

---

## Table of Contents

- [Core Principles](#core-principles)
- [The Playbook](#the-playbook)
  - [A. Topic & Prompt Research](#a-topic--prompt-research)
  - [B. Briefing & Drafting Workflow](#b-briefing--drafting-workflow)
  - [C. Structuring Content for AI Retrieval](#c-structuring-content-for-ai-retrieval)
  - [D. Off-Site Citation Building](#d-off-site-citation-building)
  - [E. Measurement & Tracking](#e-measurement--tracking)
  - [F. Refresh & Maintenance](#f-refresh--maintenance)
- [Where Experts Disagree](#where-experts-disagree)
- [What I Rejected and Why](#what-i-rejected-and-why)
- [My Original Ideas](#my-original-ideas)
- [Weaknesses of This Playbook](#weaknesses-of-this-playbook)
- [Who I Would NOT Recommend Following, and Why](#who-i-would-not-recommend-following-and-why)
- [Conclusion](#conclusion)
- [Source Verification Notes](#source-verification-notes)

---

## Core Principles

1. **Clicks are declining; purchase intent isn't.** Measure mentions, citations, and conversions — not just traffic.

   One Kevin Indig client lost ~50% of EU organic traffic but gained 20% YoY conversions (source: Kevin Indig, LinkedIn, "Visibility beats clicks," https://www.linkedin.com/posts/kevinindig_visibility-beats-clicks-ugcPost-7471580351279108096-gaoA, 14.06.2026).

   AI Overviews cut clicks to the #1 organic result by 58%, per Ahrefs' own study (source: Tim Soulo, LinkedIn, https://www.linkedin.com/posts/timsoulo_in-the-last-6-months-at-ahrefs-we-analyzed-share-7467561526015463424-9suJ, 08.06.2026).

2. **Original expertise beats generic AI content.** Content needs "Information Gain" — genuinely new entities, data, or insight — or it won't surface in AI answers (source: Bernard Huang, "Future of Search and AI," https://www.youtube.com/watch?v=TpXnYqLeu2g, 28.07.2023).

   Mass AI-scaled content without original insight "almost always crashes and burns" (source: Lily Ray, "AI Search 2025 Recap and 2026 Game Plan," https://www.youtube.com/watch?v=2vtFN9lDciM, 18.12.2025).

3. **YouTube presence correlates unusually strongly with AI visibility.** Ahrefs found YouTube mentions have the highest correlation (0.737) with AI brand visibility of any factor studied (source: Tim Soulo, LinkedIn, 08.06.2026, cited above).

   Video is also named the second most-cited source type across AI platforms generally (source: Mike King, "Query Fan-Out: What It Is and What You Should Do," https://www.youtube.com/watch?v=hDYQ3AqMOOs, 16.01.2026).

4. **Off-site citations now matter as much as owned content.** AI trusts different sources per topic and doesn't have a fixed list — off-property authority has to be built topic by topic (source: Kevin Indig, LinkedIn, "AI trusts a different set of sources for every topic," https://www.linkedin.com/posts/kevinindig_ai-trusts-a-different-set-of-sources-for-share-7472249743503503360-3b4H, 15.06.2026).

5. **Measure AI visibility with repeated sampling, not one-off checks.** Running an identical ChatGPT prompt 3x yielded only 2.2% citation consistency across 815,000 prompt-page pairs studied — a single-run tracker measures volatility, not visibility (source: Kevin Indig, LinkedIn, "A prompt tracker that runs each prompt once," https://www.linkedin.com/posts/kevinindig_a-prompt-tracker-that-runs-each-prompt-once-share-7469012961387511808-14kf, 12.06.2026).

6. **Human review is non-negotiable.** Ahrefs' own AI-assisted writing workflow explicitly front-loads human direction (brief → outline → draft) and never lets AI claim first-hand experience it doesn't have (source: Tim Soulo / Ryan Law, "AI Writing at Scale: Ahrefs' Step-by-Step Workflow," https://www.youtube.com/watch?v=D7LBx8RFOcQ, 05.08.2025).

---

## The Playbook

### A. Topic & Prompt Research

Build a prompt library from queries that actually trigger AI Overviews — found via keyword tools with SERP-feature filters (e.g., Semrush Keyword Magic Tool) — rather than relying on raw keyword volume, which AI search doesn't map to cleanly (source: Aleyda Solis, LinkedIn, "A useful and often underused input," https://www.linkedin.com/posts/aleyda_a-useful-and-often-underused-input-for-share-7471063307890749440--k7e, 12.06.2026).

Mine real customer language instead of starting from keyword-research tools: pull a batch of sales-call transcripts or support tickets through an AI summarizer to surface actual phrasing and objections (source: Kevin Indig, "Google Will Kill Your Traffic — Here's How You Adapt," https://www.youtube.com/watch?v=jQXvbeYF5go, 26.08.2025 — describes doing this at Ramp with the Humata tool across ~50 calls).

Run a content-gap pass: export your existing article titles and ask an AI model to find topics that are "almost but never written" via semantic-distance comparison against your library (source: Andy Crestodina, "Andy Crestodina on SEO Content Gaps and Using AI," https://www.youtube.com/watch?v=nMxIprRHjuU, 30.07.2025).

**[MY ADAPTATION]** Kevin Indig's enterprise prompt-tracking design uses ~40 seed prompts (12 brand, 12 category, 16 problem-focused), sampled 5x per platform, weekly, across ChatGPT/Perplexity/Gemini/Google AI Overviews, segmented by buyer persona (source: Kevin Indig, LinkedIn, "Good prompt tracking starts with sample design," https://www.linkedin.com/posts/kevinindig_good-prompt-tracking-starts-with-sample-design-share-7470197034172710912-SIrr, 10.06.2026).

That's a full-time job at enterprise scale. For a lean team, I'd scale it down to **10–15 prompts (roughly 5 brand, 5 category, 5 problem), sampled 3x, in ChatGPT and Google AI Overview only, once a month** — same sampling logic, a fraction of the effort. This scaled-down cadence is my own suggestion, not Indig's.

#### ✅ Before Researching
- [ ] Prompt queries pulled via SERP-feature-filtered keyword tools, not just volume
- [ ] Real customer language mined from sales calls or support tickets
- [ ] Content-gap pass run against existing article titles
- [ ] Lean prompt list built/updated (~10–15: brand / category / problem)

### B. Briefing & Drafting Workflow

Front-load direction before generation: brief → outline → draft. Polishing a bad finished draft has a low ceiling compared to giving the model a strong brief upfront (source: Tim Soulo / Ryan Law, "AI Writing at Scale," 05.08.2025).

The content brief should include: target keyword, working title, the writer's own must-include points and experience, a topical-coverage gap analysis versus top-ranking competitor pages, and specific product or feature mentions required (source: same, 05.08.2025).

Only draft AI-assisted content on topics you already have genuine expertise in — specifically so you can judge whether the output is actually good (source: same, 05.08.2025). Don't let a prompt invent false first-hand experience. Use "write as someone in the trenches" prompting only to flag *where* a human should insert a real anecdote, never to fabricate one (source: same, 05.08.2025).

Structure outlines with MECE (mutually exclusive, collectively exhaustive) sections, Barbara Minto's Pyramid Principle (one idea per section, evidence then elaboration), and "bottom-line-up-front" per section (source: same, 05.08.2025).

**[MY ADAPTATION]** Ahrefs' workflow runs a dedicated ChatGPT "project" pre-loaded with 7 separate SOP documents (outline rules, style guide, product-mention rules, CMS shortcodes, line-edit checklist) (source: same, 05.08.2025). A lean team doesn't need 7 documents or a "project" feature — **one reusable prompt file** (a single doc combining your voice guide, structure rules, and a short "never do this" list, pasted at the top of every drafting session) captures the same idea with far less setup. This one-file simplification is my own suggestion.

#### ✅ Before Drafting
- [ ] Writer has genuine first-hand expertise in this topic
- [ ] Brief complete: keyword, title, must-include points, gap analysis, product mentions
- [ ] Reusable prompt file (voice + structure + "never do this") ready to paste in
- [ ] Outline follows MECE + Pyramid Principle + bottom-line-up-front

Do not trust AI-suggested internal links by default. In Ahrefs' own workflow, roughly half the links an AI model suggested were hallucinated or broken, and one shipped to their live blog (source: same, 05.08.2025). Constrain link suggestions to a real, supplied URL list, or handle internal linking as a separate, tool-driven post-publish step.

Have a human line-edit pass before anything publishes: open each section with its core idea, address obvious objections, cut vague words for precise ones, define jargon, vary sentence rhythm, and strip AI-flavored phrasing (e.g. "This isn't X, it's Y") (source: same, 05.08.2025).

### C. Structuring Content for AI Retrieval

Write clear, self-contained, "atomic" answers per section — this is the actionable version of "chunking" advice that's stable enough to act on, since the underlying technical chunking mechanics change per model and aren't something you can directly control (source: Lily Ray, "GEO, AEO, LLMO: Separating Fact from Fiction," https://www.youtube.com/watch?v=2nJkT8zOzcM, 10.11.2025). *(Mike King disagrees with this framing — see Disagreements, #2.)*

Use specific, data-backed claims (semantic triples: subject–predicate–object) instead of vague, bundled sentences — e.g. "our analysis of 200 lakefront properties showed 18% appreciation" beats a general claim (source: Mike King, "Query Fan-Out," 16.01.2026).

Cover multiple sub-intents per page, not just one target keyword. AI systems generate synthetic "fan-out" subqueries that don't always match what a human would search, so single-intent pages leave coverage gaps (source: same, 16.01.2026; also Aleyda Solis, "Google AI Mode vs Traditional Search," https://www.youtube.com/watch?v=LGvbEHyX5oE, 01.07.2025).

Treat schema markup as baseline technical hygiene, not a growth lever for AI citations. Ahrefs' own study across ~1B data points found schema had zero meaningful impact on AI citation likelihood (source: Tim Soulo, LinkedIn, 08.06.2026, cited above). *(Mike King disagrees — see Disagreements, #1.)*

#### ✅ Before Publishing
- [ ] Every AI-suggested internal link verified as real
- [ ] Line-edit pass done: precise words, objections addressed, jargon defined, AI phrasing removed
- [ ] No AI-claimed experience that isn't genuinely the writer's own
- [ ] Content covers multiple sub-intents, not one keyword
- [ ] Schema added as baseline hygiene, not a growth lever

### D. Off-Site Citation Building

Prioritize getting listed on other people's "best X" or comparison pages over publishing your own. Ahrefs deliberately keeps self-published listicles under 1% of its own content and rarely ranks itself #1 in them (source: Glen Allsopp, "Tim Soulo vs Glen Allsopp: Ahrefs Use Case Showdown," https://www.youtube.com/watch?v=EbT3LE-Y2gk, 26.02.2026).

Match your off-site push to where your buyers and AI models actually look: G2, Capterra, and Gartner for B2B software; Reddit and niche forums for consumer categories (source: Kevin Indig, "SEO in the Age of AI: Google Overviews, E-Commerce & the Future of Search," https://www.youtube.com/watch?v=qujABKOAThA, 15.09.2025).

Publish to YouTube, or at minimum ensure any hosted video has a real transcript available. Lily Ray's own test found LLMs pick up only what's in the audio transcript plus title and description, never what's shown only visually (source: Lily Ray, "AI Search 2025 Recap and 2026 Game Plan," 18.12.2025 — she flags this test as informal, not rigorous).

**[MY ADAPTATION]** Enterprise teams run dedicated digital-PR functions to build third-party mentions across many sites at once. A lean team can't do that in parallel. My recommendation: **pick one off-site channel that matches your actual buyer (e.g., G2 for B2B SaaS, a specific subreddit for consumer) and commit to consistent, non-promotional presence there for a full quarter before adding a second channel.** This single-channel-first sequencing is my own prioritization call, not something any source in this repo specifically recommended.

### E. Measurement & Tracking

Track revenue and conversions as the top KPI, not rankings or raw traffic. Pair it with a secondary brand-salience metric — e.g. branded search volume over time, or a periodic sales-team question: "how did you hear about us, and if it was ChatGPT, can you paste the transcript?" (source: Lily Ray, "AI Search 2025 Recap and 2026 Game Plan," 18.12.2025).

Segment GA4 to separate AI-referral traffic from generic direct/organic — this isn't broken out by default (source: Lily Ray, "GEO, AEO, LLMO," 10.11.2025, citing Dana DiTomaso's GA4 segment method).

**[MY ADAPTATION]** For actual prompt sampling: given the Section A scale-down (10–15 prompts, 3x, monthly, in ChatGPT + Google AI Overview), log results in a plain spreadsheet — prompt, platform, date, whether you were mentioned, which source(s) got cited instead of or alongside you. This replaces Kevin Indig's enterprise system (AirOps-style tooling, weekly, 4 platforms) with a manual version scaled to what one person can sustain (source basis: Kevin Indig, LinkedIn, 12.06.2026 and 10.06.2026, both cited above — cadence and platform count are my scale-down, not Indig's).

#### ✅ Monthly Review
- [ ] ~10–15 prompt sample (3x each) run through ChatGPT + Google AI Overview
- [ ] Results logged: prompt, platform, mentioned or not, who was cited instead
- [ ] Revenue/conversion trend checked, not just rankings or traffic
- [ ] GA4 AI-referral segment reviewed

### F. Refresh & Maintenance

Prioritize refreshing pages AI is *already* citing over creating new content from scratch. Those pages are already shaping answers, so updates compound faster than new content builds authority from zero (source: Bernard Huang, "AI-driven SEO revolution: future of discoverability," https://www.youtube.com/watch?v=f84ovVChEh4, saas.unbound podcast — exact episode date not publicly confirmed, see Weaknesses).

Set a quarterly refresh cadence as a default starting point for content in categories where competitors' "last updated" dates move quickly (source: Ross Hudgens, "AI Visibility, Data Journalism, and the Future of SEO," https://www.youtube.com/watch?v=8-PS7gR2G0I, 11.12.2025).

Avoid cosmetic-only refreshes — updating a timestamp without real new substance. Google demotes this, and it can hurt both search and AI visibility rather than help (source: Lily Ray, "GEO, AEO, LLMO," 10.11.2025).

#### ✅ Quarterly Refresh
- [ ] Pages AI already cites identified and prioritized first
- [ ] Competitor "last updated" dates checked in your category
- [ ] Refreshes confirmed to add real substance, not just a timestamp change

---

## Where Experts Disagree

**1. Does schema markup matter for AI citations?**

- **Tim Soulo / Ahrefs:** their study across ~1B data points found schema markup had zero meaningful impact on AI citation likelihood (source: Tim Soulo, LinkedIn, 08.06.2026, cited above).
- **Mike King:** directly disputes the "structured data doesn't matter" position, calling it unproductive, and states iPullRank sees measurable value from underused schema.org vocabularies (source: Mike King, "Query Fan-Out," 16.01.2026).
- **My take:** I side with Soulo — it's the only side backed by a published, numbered study; King's claim is asserted without figures. Keep schema for baseline hygiene, but don't spend limited hours chasing AI-citation gains from it.

**2. Is "chunking" an actionable SEO tactic?**

- **Lily Ray:** argues chunking isn't a real lever you can control — it's an internal AI-engineering detail that varies by model and changes constantly. The only durable takeaway is "write atomic, self-contained answers" (source: Lily Ray, "GEO, AEO, LLMO," 10.11.2025).
- **Mike King:** treats chunking as concrete and prescriptive — target roughly 500-token passages, use headings as chunk boundaries — and explicitly rebuts Danny Sullivan's public skepticism on this as "misinformation" (source: Mike King, "Query Fan-Out," 16.01.2026).
- **My take:** I side with Ray, not because King is wrong, but because targeting a precise token-count chunk size needs ongoing technical iteration a lean team doesn't have bandwidth for. "Write clear, atomic answers" captures the same idea without a developer.

**3. Should you block AI crawlers?**

- **Aleyda Solis (sharing a third-party proposal):** argues publishers should build aggressive bot defenses and consider blocking even Googlebot if referral traffic keeps collapsing (source: Aleyda Solis, LinkedIn, "The LLMs have caused enough damage to Publishers," https://www.linkedin.com/posts/aleyda_the-llms-have-caused-enough-damage-to-publishers-share-7470746981372698624-QBkV, 11.06.2026).
- **Kevin Indig:** recommends a cost-benefit analysis before blocking anything, citing reported 700%+ year-over-year ChatGPT referral-traffic growth as a reason not to block prematurely, and notes no one is actually getting paid yet under pay-per-crawl models (source: Kevin Indig, "SEO in the Age of AI," 15.09.2025).
- **My take:** I side with Indig. A startup has no negotiating leverage with LLM vendors the way a major publisher might, and blocking crawlers pre-emptively cuts off free distribution with no compensating benefit. This debate matters far more to large publishers than to a startup marketer.

**4. How much should you prioritize ChatGPT specifically?**

- **Bernard Huang:** his own sampling found ChatGPT performs live search only ~45% of the time (mostly for "fresh"/research-intent queries), concluding ChatGPT-specific optimization is "currently low-value" and Gemini should be the priority (source: Bernard Huang, "How To Do AEO: Live Session," https://www.youtube.com/watch?v=RMg2eTZL7Jk, 13.02.2026).
- **Kevin Indig:** states ChatGPT drives roughly 80% of the LLM-referral value his clients see (source: Kevin Indig, "Google Will Kill Your Traffic," 26.08.2025).
- **My take:** this needs reasoning, not a side — the numbers aren't necessarily contradictory. Huang measured how often ChatGPT does a live retrieval; Indig measured share of referral traffic. Track both platforms in the Section E sampling, then let your own GA4 data — not either expert's client base — decide where to lean budget.

**5. How much should AI actually write?**

- **Bernard Huang:** says yes to AI-generated content at scale, arguing brands not scaling with AI "will be left behind" (source: Bernard Huang, "AI-driven SEO revolution," saas.unbound, date not confirmed — see Weaknesses).
- **Andy Crestodina:** writes everything by hand and challenges anyone to find an Orbit Media article AI could have produced, arguing AI is good for none of the qualities — visual, collaborative, expert-quoted, opinionated — that make content actually work (source: Andy Crestodina, "SEO Isn't Dead — You're Just Doing It Wrong," https://www.youtube.com/watch?v=1hcv93CwulE, 08.08.2025 — video ID match for this exact upload could not be independently confirmed; see Weaknesses).
- **Lily Ray:** takes a middle position — AI-assisted daily, but she neither generates final content with AI nor recommends clients do so, citing her own observation that lightly-edited AI content sees shrinking short-term gains as Google gets better at detecting it (source: Lily Ray, "How SEO is Evolving in 2025," https://www.youtube.com/watch?v=mgI1U7XPsUA, 11.04.2025).
- **My take:** I side with Ray's middle position. Crestodina's "write everything by hand" assumes Orbit Media's decades of manual practice and team depth a lean startup usually lacks at the volume needed to compete. Huang's "scale it fully" ignores the same data Ray cites — thin AI content underperforms increasingly as detection improves. AI-assisted, human-directed, human-edited is the workable middle.

**6. Should you publish more scaled "best X" content?**

- **Ross Hudgens:** his data pushes toward building more comparison/TOFU content, citing HubSpot hitting 83% brand visibility on "what is CRM" (source: Ross Hudgens, LinkedIn, "Big news: TOFU content is back," https://www.linkedin.com/posts/rosshudgens_big-news-tofu-content-is-back-if-you-search-share-7468388280732971008-xwQT, 08.06.2026).
- **Lily Ray:** warns self-published "best X" listicles are a "loophole" she expects Google to crack down on in 2026 (source: Lily Ray, "AI Search 2025 Recap and 2026 Game Plan," 18.12.2025).
- **Glen Allsopp:** takes the opposite approach of both — get listed on other people's best-of pages rather than publish your own (source: Glen Allsopp, "Tim Soulo vs Glen Allsopp," 26.02.2026, cited above).
- **My take:** I side with Allsopp for a startup. A brand-new domain has essentially no authority to win a self-published "best X" fight against Wikipedia, G2, or Reddit — Ahrefs' data shows only 32.3% of ChatGPT's top citations are even influenceable, dominated by sources like Wikipedia and homepages (source: Tim Soulo, LinkedIn, 08.06.2026, cited above). The highest-leverage move with no domain authority is third-party placement, not more of your own listicles.

---

## What I Rejected and Why

**1. Kevin Indig's full enterprise prompt-tracking system, adopted wholesale.**

His design — 40 seed prompts, 5x runs, 4 platforms, weekly, persona-segmented, with confidence intervals (source: Kevin Indig, LinkedIn, 10.06.2026, cited above) — is sound methodology. But recreating it manually is close to a full-time job, and the tooling that automates it (AirOps-style platforms) is priced for enterprise budgets. I rejected adopting it as-is and instead adapted it down in Sections A and E — a scaled version, not the full system.

**2. Mike King's custom fan-out simulation tooling.**

King describes building an "AIO simulator," extracting Gemini's fan-out queries via the API, and using tools like Ollama and CrewAI to build custom agents (source: Mike King, "Relevance Engineering, AI Search & Query Fan-Out," https://www.youtube.com/watch?v=pQLivtcqCZs, 27.05.2025). I rejected this entirely — it requires in-house engineering and data-science capability a 10–200 person startup's marketing function essentially never has. No lean adaptation exists; it's simply out of scope, so it doesn't appear in the Playbook above.

**3. Bernard Huang's description of Reddit "karma farming" and coordinated multi-account brand plugging.**

Huang describes these tactics as things he's observed working in the market, including closing comments to block rebuttals (source: Bernard Huang, "AI-driven SEO revolution," saas.unbound, date not confirmed). I'm rejecting this outright, not adapting it. Huang himself frames it as an unresolved cat-and-mouse dynamic, not an endorsement, and Lily Ray separately reports the same category of tactic — self-promotional listicles, Reddit astroturfing — as exactly what mainstream media is now covering and what she expects Google to crack down on (source: Lily Ray, LinkedIn, "The media is finally catching onto the popular SEO/GEO tactics," https://www.linkedin.com/posts/lily-ray-44755615_the-media-is-finally-catching-onto-the-popular-ugcPost-7470498942439378945-zrp_, 11.06.2026). A startup has far less legal and PR capacity to absorb a manipulation-related penalty than the brands in these examples.

---

## My Original Ideas

**The "Citation Debt Log."**

None of the 10 sources in this repo proposed this specific mechanism — it's my own synthesis of two ideas that exist separately in the research: Kevin Indig's "map which domains AI already cites per topic, then earn your way into that set" (source: Kevin Indig, LinkedIn, 15.06.2026, cited above), and the Section E manual prompt-sampling workflow.

Instead of treating citation-source mapping as a one-time research exercise, run it as a standing operational log. Every time your monthly prompt sample (Section E) turns up a citation — yours or a competitor's — log it in one spreadsheet row: the prompt, the platform, the exact source cited (a specific competitor page, a Reddit thread, a G2 listing, a comparison site), and a status column: *not pursued / outreach attempted / citation earned*. Over a few monthly cycles, this becomes a running action queue rather than a static report.

**Why it could work:** it piggybacks entirely on work the team already does — the monthly sampling from Section E — so it adds almost no overhead. It also converts a vague goal ("build AI-source authority") into the same concrete, assignable task format lean teams already use for other channels, like a link-building tracker, rather than a one-off analysis that gets read once and forgotten.

It's untested — I have no source or data confirming it works, which is why it's flagged as original and belongs here, not in the Playbook proper.

---

## Weaknesses of This Playbook

- **The source panel skews toward large agencies and platforms** (Ahrefs, Siege Media, Clearscope, Amsive, iPullRank). Every "[MY ADAPTATION]" tag in this document is my own untested scaled-down interpretation of an enterprise workflow — none of the 10 experts actually validated these smaller versions at startup scale. Treat the adaptations as reasonable starting points, not proven tactics.

- **Two YouTube sources have unconfirmed publish dates** despite a direct lookup: Bernard Huang's "AI-driven SEO revolution" (saas.unbound podcast) and Andy Crestodina's "The AI Impact on SEO" (Marketing Companion, Episode 309). A third source's video ID (Andy Crestodina, "SEO Isn't Dead — You're Just Doing It Wrong," 1hcv93CwulE) could not be independently re-confirmed against public search results under that exact ID, though the transcript content and title match what's in the repo. I've cited the closest available match with this caveat attached rather than silently presenting it as fully verified.

- **Sources span a wide, uneven date range** — one Bernard Huang video traces to July 2023, well before AI Overviews existed in their current form, alongside material from as recent as early 2026. I've cited each with its real date so you can weigh recency yourself, but the playbook doesn't otherwise flag which specific claims might be stale.

- **Several headline statistics come from a single vendor's proprietary dataset** (Ahrefs, Amsive, AirOps), each with a commercial incentive to publish results flattering to the tools they sell. None of these numbers were independently cross-checked against a second source in this repo.

- **Section D (off-site citation building) is the least concretely actionable part of this playbook.** Every expert agrees it matters; none gave a process sized for a one-person lean team. My Citation Debt Log idea (above) is a genuine attempt to close that gap, but it's unverified.

- **No source in this repo speaks from a B2C/e-commerce startup perspective.** Most of the transactional and funnel-stage data comes from B2B SaaS-oriented practitioners (Hudgens, Schwartz, Indig), so an e-commerce startup applying this playbook should expect some sections — especially TOFU/BOFU framing in Section A — to need further adjustment beyond what's covered here.

- **One planned source is entirely unusable:** Glen Allsopp's "SEO Blueprint 3" video transcript failed to fetch (subtitles disabled) and contains no content, reducing his effective source count in this repo to one YouTube talk plus four substantive LinkedIn posts.

---

## Who I Would NOT Recommend Following, and Why

**Bernard Huang.**

Not a claim that his ideas are worthless — his three-layer AI model (training data / validation search / memory-context) and "Information Gain" framing are genuinely useful and cited in the Core Principles above. The concern is relying on him as a primary, ongoing source, for three reasons grounded in this repo's own material:

1. **His LinkedIn presence has zero substantive content on the stated topic in the window sampled.** All five posts cover an AI trading experiment, a video game he built, and navigating London's bus system — nothing about SEO or content production (source: Bernard Huang, LinkedIn posts 1–5, https://www.linkedin.com/posts/bernardjhuang_i-think-i-finally-understand-what-all-this-share-7471124722148118528-utAZ and related, June 2026). A marketer wanting a practitioner to follow day-to-day, the way you might follow Indig or Hudgens, won't get that from his feed.

2. **Several confident claims in his YouTube talks aren't accompanied by published data**, unlike Soulo, Indig, or Hudgens, who consistently cite sample sizes and methodology. His statement that Google restricted scraping to the top 10–20 results, "forcing" LLMs to lean on Google's trust signals, is presented as fact with no source given (source: Bernard Huang, "AI-driven SEO revolution," saas.unbound, date not confirmed).

3. **He describes manipulative tactics — Reddit karma farming, coordinated multi-account posting, closing comments to block rebuttals — with limited caveating**, framing them as "it currently works" rather than warning practitioners away. A real risk for a startup with limited capacity to absorb a platform penalty (source: same).

**Net recommendation:** watch his talks and webinars — they contain real frameworks — but don't treat his day-to-day public writing as a reliable source the way you reasonably could with others in this set.

---

## Conclusion

Every disagreement, rejection, and adaptation in this playbook comes back to the same bet: AI is a production accelerant, not a substitute for judgment. The experts disagree on schema markup, chunking, crawler blocking, and how much AI should write — but none, even the most bullish on automation, argue that AI-generated content wins on its own. It wins when fed real expertise, original data, and a human editor willing to cut what doesn't hold up.

That's the philosophy behind every adaptation here. A lean team can't out-resource an enterprise content operation, but it can out-judge one — by being more selective about what gets published, more honest about what's untested, and more disciplined about checking AI output against what a real practitioner would know. The checklists exist to enforce that discipline when there's no second reviewer to catch a mistake.

If one instruction matters more than the rest, it's the one repeated in Core Principle 6 and the Before Drafting checklist: never let AI claim expertise it doesn't have. Everything else here is tactics; that's the guardrail they depend on.

The objective of this playbook was never to produce more AI content — it's to produce content AI systems repeatedly choose to trust and cite.

---

## Source Verification Notes

All YouTube publish dates above were independently looked up (not present in the original transcript files, which only include title, video ID, and URL). Where a date could not be confirmed after a direct search, that's stated inline rather than estimated. Full source list with LinkedIn post dates (already present in the repo) is at `/research/sources.md` and `/research/linkedin-posts/`; transcripts are at `/research/youtube-transcripts/`.
