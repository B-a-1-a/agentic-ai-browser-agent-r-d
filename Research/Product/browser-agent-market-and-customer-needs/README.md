# Browser agent market and customer needs

## Purpose

The team plans a standalone desktop app that runs and manages several browser agents at once, similar to how Conductor runs coding agents. The target customer:

- already pays for an AI subscription (ChatGPT, Claude, Gemini, Perplexity)
- is not necessarily a developer
- wants to automate tasks they do in the browser or in web apps

This study answers three questions:

1. What does the current market for this product look like?
2. What are the customers' greatest unanswered needs?
3. What do customers want most?

## Approach

We used the [`customer-research`](https://github.com/coreyhaines31/marketingskills) skill. It is installed at `.agents/skills/customer-research/`. The skill describes three modes of research. We used two of them:

- **Mode 2 (mine existing online sources).** Five research streams ran in parallel on 2026-10-12. They collected evidence from the last 12 months:
  1. AI browsers and the browser agents the big AI companies build ([notes](sources/01-ai-browsers-and-first-party-agents.md))
  2. No-code automation tools, agent orchestrators, and whether an app can run on the customer's existing AI subscription ("bring your own subscription") ([notes](sources/02-automation-tools-orchestrators-and-byo-subscription.md))
  3. What people say in online communities ([notes](sources/03-community-voice-of-customer.md))
  4. Reviews on review sites, app stores, and extension stores ([notes](sources/04-review-sites-and-stores.md))
  5. Adoption, trust, security, and pushback from websites ([notes](sources/05-adoption-trust-security.md))
- **Mode 1 (analyze the evidence).** We tagged evidence as a job to be done, a pain, a trigger, an outcome, an alternative, or customer language. We grouped the evidence into themes and scored each theme by how often it appeared and how strongly people felt about it. We gave every insight a confidence label: HIGH means 3 or more independent sources; MEDIUM means 2 sources, or evidence from only one customer segment; LOW means a single source.
- **Mode 3 (interviews and surveys)** has not been done yet. A plan is ready in [research-gaps-and-next-steps.md](research-gaps-and-next-steps.md).

## Status

**Desk research is complete. The findings are directional and should be confirmed with interviews before we commit to a direction.**

## Key findings

### The market (October 2026)

Details are in [market-landscape.md](market-landscape.md).

- **There is real demand among people who already pay for AI.**
  - ChatGPT has about 50 million paying subscribers.
  - 65% of people who pay for AI have used an agent, compared with 13% of people who don't pay.
- **General-purpose browser agents have not kept their users.**
  - ChatGPT Agent reportedly lost about 75% of its weekly users because people "couldn't figure out what to do with it".
  - OpenAI shut down its Atlas browser after 292 days. Google shut down Project Mariner. Microsoft retired Edge Copilot Mode.
- **The big AI companies now offer background, scheduled, and parallel agents inside their own apps,** but each one works only with that company's AI. Examples: ChatGPT Work and Dots, Claude Cowork and Claude in Chrome, Gemini Spark, and Comet Background Assistants.
- **No product combines all four parts of our concept:**
  1. easy for non-developers to use
  2. several browser agents running in parallel, with a way to monitor them
  3. runs on the customer's existing AI subscription
  4. uses the customer's own logged-in browser

  The closest product, Browser Use Desktop, appears to have stalled at version 0.0.31.
- **Running on the customer's existing subscription is only partly possible, and the rules keep changing.**
  - OpenAI has an official "Sign in with ChatGPT" program, but commercial apps must apply and be approved. Conductor is one of the launch partners.
  - Anthropic forbids third-party apps from offering a Claude.ai login. It does allow an app to wrap the unmodified Claude Code program, with the user signing in themselves.
  - Google bans apps that reuse Gemini CLI's login, but appears to allow wrapping its official command-line tool.
- **The main risks:**
  - The big AI companies may add multi-agent management themselves. Cowork is the closest competitor.
  - Prompt injection, where hidden text on a web page takes over the agent, is still unsolved. Gartner advises companies to block AI browsers.
  - Websites increasingly detect and block agents. Amazon and eBay forbid them in their terms of service, and Cloudflare blocks unidentified agents.
  - Customers may not pay on top of a subscription they already have.

### The greatest unanswered needs, ranked

Details are in [customer-needs-synthesis.md](customer-needs-synthesis.md).

1. **"Don't surprise me with the bill."** People want a predictable cost that uses what they already pay for. Cost, credits, and usage limits come up in 26% of 1–3★ reviews. *(HIGH)*
2. **"Tell me it actually worked."** People want evidence that a task was completed, plus a history they can replay and resume. Today agents claim tasks are "complete" when they are not, and sessions get lost. *(HIGH)*
3. **"Make it obvious what it's for and how to start."** People want to start from a result, not a blank prompt box. ChatGPT Agent lost users who "couldn't figure out what to do with it". *(HIGH)*
4. **"It has to just connect and keep working."** Connection and setup failures appear in 25% of 1–3★ reviews. They are the main reason the top extensions are rated 2.9★ (Claude in Chrome) and 2.75★ (ChatGPT). *(HIGH)*
5. **"Ask me at the right moments, not on every click."** People want to approve the overall plan, set permissions by type of action, and always be asked before a payment. Only 9–12% of consumers accept AI paying on its own. *(HIGH)*
6. **"Run it without me, and don't take over my browser."** People want agents that run in the background, each in its own separate browser that stays logged in. Few people mention this, but those who do feel strongly about it. *(HIGH as a need; MEDIUM on how common it is among non-developers)*
7. **"Get me past the login, two-factor code, CAPTCHA, or bot block."** *(HIGH)*
8. **"Keep me safe without making me a security expert."** Safe settings must be built in by default. *(HIGH as a reason people don't adopt)*
9. **"Don't take my workflows away."** Atlas, Agent Mode, Dia Pro, and Comet's browser control were all removed or locked behind credits in 2026. *(MEDIUM-HIGH)*
10. **"Teach it once, then let me reuse it, without building a workflow."** *(MEDIUM)*
11. **One control panel across AI companies.** This is a clear gap in the market, but few customers ask for it directly. Test it before making it the headline feature. *(LOW as a stated need)*

### What customers want most, in their own words

1. Hand off the boring, multi-step work on websites: "I know exactly what to do, it's just very tedious to actually do it."
2. Watch websites for them and report changes: "check once a day for the next week and notify me of any price changes."
3. Work in its own tabs while they keep working: "while i can do my work in other tabs with out getting interlinked or disturbed."
4. Use the subscription they already have: "works seamlessly with my existing ChatGPT subscription."
5. Give an input, get a finished result: "choose a tool → provide the input → receive the completed result."
6. Only ask before spending money: "research is fine, but I don't want the AI to go on a shopping spree."

**Top tasks they want automated:**

1. Filling in forms on portals (licensing, tax, government, job applications)
2. Monitoring websites and sending alerts
3. Travel and appointment booking
4. Shopping research
5. Admin work inside web apps that have no API (a way for software to connect to them)
6. Research gathered into a spreadsheet

### The biggest challenge to our assumptions

"An orchestrator like Conductor" is a developer's way of thinking about the product. Non-developers describe the result they want ("my tax declaration", "watch these listings"). They don't talk about agents. Running agents in parallel is a means to an end. People experience its value as recurring jobs that happen in the background.

**Hypothesis:** lead with jobs and results. Build the orchestration (separate browser profiles, an inbox for approvals, run evidence, and scheduling) as the foundation, and keep it mostly invisible to the user. See Part 5 of the synthesis.

## Files

| File | Contents |
|---|---|
| [market-landscape.md](market-landscape.md) | Map of competitors, forces shaping the market, whether the customer's subscription can be used, gaps in the market, who could take this opportunity first |
| [customer-needs-synthesis.md](customer-needs-synthesis.md) | Ranked unanswered needs, top wants, top tasks, jobs-to-be-done map, provisional segments, contradictions, product implications |
| [voc-quote-bank.md](voc-quote-bank.md) | Exact customer quotes grouped by theme, plus customer vocabulary to use in copy |
| [research-gaps-and-next-steps.md](research-gaps-and-next-steps.md) | Gaps, beliefs to test, a Sales Safari plan (reading what customers say online), an interview guide, a survey, proposed experiments |
| [sources/](sources/) | Raw notes from each of the five research streams, with source URLs and dates |
| [data/store-reviews.csv](data/store-reviews.csv) | 3,215 Chrome Web Store and App Store reviews collected on 2026-10-12 |
| [data/theme_counts.py](data/theme_counts.py) | Script that counts review themes by keyword. Run `python3 data/theme_counts.py` from this directory. |

## Limitations

- **Reddit and X could not be accessed.** Our research tools blocked Reddit, and X returned a payment-required error. These are where most non-developers discuss this topic, so our evidence about non-developers is thinner than we want. Much of it comes from store reviews, surveys, and people describing others.
- **The community sample leans toward developers.** 51 of the 70 community entries come from Hacker News.
- **Some review sites were blocked.** G2, Capterra, GetApp, and TrustRadius refused access.
- **Some quotes may not be exact.** Trustpilot and forum quotes went through a tool that may summarize pages. Check them before quoting them publicly.
- **Some market figures rest on one source or conflict between sources.** Examples are ChatGPT Agent's user drop, Comet's monthly users, and ChatGPT Work's user count. They are marked in the source notes. Check them before using them outside the team.
- **The landscape changes monthly,** and in 2026 the rules on using a customer's existing subscription changed several times. Re-check the market landscape before making decisions.

## Related

- Proposed follow-up experiments are listed in [research-gaps-and-next-steps.md](research-gaps-and-next-steps.md#6-experiments-to-run-next). Each experiment needs its own directory under `Experiments/`.
