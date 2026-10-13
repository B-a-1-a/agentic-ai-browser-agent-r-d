# Customer needs synthesis: what non-developer AI subscribers need and want from browser agents

This study looks at people who pay for an AI subscription but are not developers, and who want to automate tasks they do in a web browser. This file brings the evidence together using the customer-research skill's method:

- tag each piece of evidence as a job to be done, a pain, a trigger, an outcome, an alternative, or customer language
- group the evidence into themes
- score each theme by how often it appears (frequency) and how strongly people feel about it (intensity)
- give each insight a confidence label

The raw evidence is in [`sources/`](sources/) and [`data/`](data/). Quotes are copied exactly; the full set is in [`voc-quote-bank.md`](voc-quote-bank.md).

## Evidence base

| Stream | What it covers | Size | Main bias |
|---|---|---|---|
| S1 [AI browsers and first-party agents](sources/01-ai-browsers-and-first-party-agents.md) | Hands-on reviews, product changes, benchmarks | about 20 products | Reviewers are journalists and technical bloggers |
| S2 [Automation tools, orchestrators, using an existing AI subscription](sources/02-automation-tools-orchestrators-and-byo-subscription.md) | Competitors, pricing, policies, Trustpilot and Hacker News quotes | about 45 products | Trustpilot skews toward billing disputes |
| S3 [Community voice of customer](sources/03-community-voice-of-customer.md) | 70 exact quotes from Hacker News, the OpenAI, Make and n8n forums, Chrome Web Store, Lemmy and Bluesky | 70 entries (about 125 items for task counts) | 51 of the 70 are from Hacker News, so the sample skews technical. **Reddit and X could not be accessed.** |
| S4 [Review sites and stores](sources/04-review-sites-and-stores.md) | Chrome Web Store, App Store, Trustpilot, AppSumo and Product Hunt reviews | about 2,700 reviews read. 3,215 store reviews are saved in [`data/store-reviews.csv`](data/store-reviews.csv). | Extension reviewers skew toward developers. 1-star reviews are inflated by install failures. G2 and Capterra blocked access. |
| S5 [Adoption, trust and security](sources/05-adoption-trust-security.md) | Surveys from Menlo, Accenture, Pew, Gartner, AARP and others, plus security research | about 30 reports | Wording differs between surveys. Some numbers come from a single source. |

**Our own check.** We ran a keyword count over the 2,207 store reviews dated 2025-10 to 2026-10 ([`data/theme_counts.py`](data/theme_counts.py)). Among the 1,008 reviews rated 1 to 3 stars:

| Complaint | Share of 1–3 star reviews |
|---|---|
| Cost, credits or usage limits | 26% |
| Connection or setup failures | 25% |
| Lost work, history or sessions | 9% |
| Security or trust | 4% |
| Permission prompts or having to babysit the agent | 4% |
| Isolation or parallel work | 1% (rare, but very strongly felt) |

**Confidence labels:**
- **HIGH:** 3 or more independent streams agree.
- **MEDIUM:** 2 streams agree, or the evidence only comes from one segment.
- **LOW:** a single source, or an inference.

---

## Part 1: The greatest unanswered needs

These are ranked by frequency × intensity. Each need is a problem that current products leave unsolved or make worse.

### N1. "Don't surprise me with the bill." Predictable cost that uses what I already pay for. HIGH

- **Evidence:**
  - Cost, credits and limits are the most common complaint: 26% of 1–3 star reviews, 45% of negative Manus iOS reviews, and 58% of negative Genspark iOS reviews.
  - Trustpilot ratings are low for credit-based agents: Manus 1.2, Lindy 1.7, Zapier 1.3.
  - Perplexity moved browser control behind credits during people's prepaid plans, and users reacted angrily.
  - ChatGPT Plus users hit a 5-hour usage cap, and Claude Pro users burn through their tokens.
  - In the community sample (S3), 7 of 70 entries are about cost.
- **What hurts:**
  - Paying for failed runs: "I lost 15,000 credits even though the output was incorrect".
  - Credits that expire.
  - Not knowing what a task will cost: "There is no predictable cost per task".
  - Paying on top of a subscription they already have.
- **The opportunity:** "Love it, and it works seamlessly with my existing ChatGPT subscription." / "This $20 Claude subscription and extension made real profit."
- **Implication:** Before each run, show what it will cost against the user's plan. Let users cap spending per agent. Never charge for a failed run. Our own pricing must not feel like credits stacked on top of their subscription.

### N2. "Tell me it actually worked." Proof that the job is done, plus a history of what happened. HIGH

- **Evidence:**
  - Agents report success when they have not finished: "It gave the impression that it paginated through all the listings, but I don't think it actually did" (S3 #7). Manus "confidently announcing that a task is complete" (S4).
  - Work is lost: 9% of 1–3 star reviews mention lost work or history. Claude in Chrome loses the session when you switch tabs, and there is "no history or log to recover what was in progress".
  - On the OSWorld 2.0 benchmark, the most common failure is that agents "skip verification".
  - Perplexity Computer ran "$200 in compute credits" in a silent loop with "no window in".
- **In customers' words:** "Users need reliability, persistence, auditability, and the ability to review previous actions. Without these basics, it is difficult to trust the extension with any serious task."
- **Implication:** Every run should produce evidence:
  - counts compared against the source ("checked 70 of 70 listings")
  - screenshots of the final state
  - a list of what was entered and submitted
  - an honest "couldn't do X" instead of a made-up result
  - a run history the user can replay and resume

  Coding agents have a code diff to review. Browser agents need an equivalent, and no consumer product offers one today.

### N3. "Make it obvious what it's for and how to start." Starting from the outcome, not from a blank prompt box. HIGH

- **Evidence:**
  - ChatGPT Agent lost about 75% of its weekly users because people "couldn't figure out what to do with it or didn't know it existed" (S5).
  - A Comet user wrote: "After three months of using this as my main browser, I still don't understand the purpose of it."
  - A retail manager went back to plain chat after seeing ChatGPT Work's settings: "The capability was useful to him. The interface created the barrier."
  - Simon Willison called ChatGPT Work "an extraordinarily confusing and very powerful product."
  - Other setup complaints: Bardeen has "The most complicated UI I have ever seen", and Automa "does require coding experience".
- **The tension:** people want results without building workflows: "can this fill forms for me without me needing to setup an entire workflow?"
- **Implication:**
  - Lead with named jobs ("Fill this application", "Watch these listings", "Put this research into a sheet"), not with "create an agent".
  - Hide the names of AI models and modes.
  - Make the first success happen within minutes.

### N4. "It has to just connect and keep working." No fragile chain of extension, app and command-line tool. HIGH

- **Evidence:**
  - 25% of 1–3 star reviews mention connection or setup failures.
  - The ChatGPT extension shows an "Install the app to use ChatGPT in Chrome" loop (49 reviews), plus Codex errors.
  - Claude in Chrome often "can't reach" the desktop app or Claude Code.
  - Browser MCP "Disconnects all the time".
  - ChatGPT Work's cloud browser froze when the user tried to take over.
- **Implication:** A standalone app that runs its own browser avoids the extension-to-desktop handshake that drags down the incumbents' ratings (2.9 and 2.75 stars). Add health checks and self-repair, and explain failures in plain English.

### N5. "Ask me at the right moments, not every click." Approvals that match how people actually delegate. HIGH

- **Evidence:**
  - Users are tired of approving every action: "I have to approve every single javascript… How am I supposed to read and understand those???" and "babysitting this stupid thing all f ing day long".
  - Hacker News commenters: "Approval fatigue will kick in", and "gating on the class of action rather than each call" works better.
  - Surveys draw the line at payment: 32–43% will delegate if they give final approval, but only 9–12% accept fully autonomous payment (S5).
  - Agents also confirm too much: one "completes the booking form then comes back and asks me if it should book it...so annoying".
- **Implication:**
  - Let users approve the plan in plain English.
  - Set permissions by type of action: reading is free, writing asks once per site or task, paying, sending or deleting always stops for approval.
  - Let trust grow task by task ("white list tasks one at a time as I gained trust").
  - Let users approve in batches from one inbox.
  - Spending caps work like a "corporate credit card with limits".

### N6. "Run it without me, and don't take over my browser." Background agents, kept separate, using my logins. HIGH as a need, MEDIUM on how common it is among non-developers

- **Evidence:**
  - Users want isolation: "step one has got to be isolation… the agent can do work while I work on something else. If I have to wait for the agent to use the browser how does that make sense to anyone?"
  - Current tools interfere: "Every time I open the panel or leave a tab, it creates a new session and a new tab group" and "if I need different projects/tabs running at once it never knows which one to connect to."
  - The strongest praise: "cuts my time in half by automating the work in dedicated browser tabs, while i can do my work in other tabs."
  - On Hacker News, users say "I don't need to be in the loop for each step and I don't want to have to keep checking myself" and "while the agent clicks through these (oftentimes dog slow) UIs I can do other things."
  - Competitors face a trade-off. Cloud agents can run in parallel but fail at logins. Local agents keep your logins but take over your one browser (S1, S2).
- **Note:** fewer than 2% of reviews mention this directly, but those who do feel strongly, and it comes from heavier users. Non-developers say "in the background" or "while I do other things". They do not say "parallel" or "orchestrate".
- **Implication:**
  - Give each agent its own browser profile that keeps its logins.
  - Run agents in the background and never steal focus.
  - One failing agent must not break the others.
  - This is also the answer to "it's slow": slowness stops mattering when nobody is watching.

### N7. "Get me past the login, two-step code, CAPTCHA and bot wall." HIGH

- **Evidence:**
  - "Bot protections are obviously the biggest pain point."
  - "fully banned by Cloudflare. I tried cancelling a phone subscription."
  - Google refused to let one user log in because "the agent's browser wasn't trustworthy."
  - Another user noted that the agent "won't get" the two-step code from email "even tho it has access to your email."
  - "CAPTCHA pages were a complete blocker" (Fellou). MacStories said getting past login "is still too frustrating."
  - About 57.5% of web requests are now bots, and Cloudflare and Amazon actively block agents (S5).
- **Implication:**
  - Running locally in the user's real, already logged-in profile should cause fewer blocks than cloud browsers. This is an inference; we should test it.
  - When the agent gets stuck, it should notify the user and let them take over cleanly, then hand control back.

### N8. "Keep me safe without making me a security expert." Safe defaults. HIGH as a barrier to adoption, MEDIUM as something users ask for

- **Evidence:**
  - People who do not use AI cite privacy as their top reason (76%). 71% say AI makes data less secure (Pew). 51% of adults over 50 say AI is unsafe (AARP).
  - Gartner advises companies to block AI browsers. Prompt injection is still unsolved.
  - Users' own fears: "a highlight border noting that the agent is viewing it while I tried to pull my account number stuff which is scary", "security nightmare… only use this extension in a dedicated Profile", "I wouldn't open by internet banking inside this browser."
- **Contradiction to note:** technical users talk about sandboxes and read-only access. Non-technical adopters rarely mention security in reviews ("People don't care about privacy. They want something that just works.") and sometimes approve everything without reading. So safety has to be **built in by default, not configured by the user.**
- **Implication:**
  - Give each agent its own isolated profile.
  - Block banking and health sites unless the user opts in.
  - Let users choose which sites each agent may use.
  - Enforce spending caps and a kill switch in the app itself, not just in the model's instructions. The OpenClaw incident showed why: the agent forgot its "STOP" instruction.
  - Never store passwords centrally.

### N9. "Don't take my workflows away." Workflows that last and that the user owns. MEDIUM-HIGH

- **Evidence:**
  - OpenAI retired Atlas and Agent Mode: "A distinct capability was simply removed." / "We trusted OpenAI enough to make Atlas our main browser."
  - A Claude update deleted saved shortcuts: "That was hours of adjusting and instructions!"
  - Perplexity moved Comet's browser control behind credits.
  - Manus deleted user data. Dia Pro and Google's Mariner were discontinued.
- **Implication:** Save workflows in a portable format that works with any AI vendor. "Your automations survive vendor changes" is a credible promise because every major vendor has broken it this year.

### N10. "Teach it once, then reuse it, without building a workflow." MEDIUM

- **Evidence:**
  - "Some of us simply want to turn a repeated task into a reliable tool… choose a tool → provide the input → receive the completed result."
  - "For old and shitty healthcare websites it's easier to just show the workflow than explain it."
  - Praise for rtrvr: "first do recordings and teach the AI."
  - "it should update itself with that problem->solution-trick that way it only looses time and tokens the first round."
- **The tension:** people want reuse but dislike building workflows. Also, many life tasks are "one off (few off)".
- **Implication:**
  - Accept a plain-language request for one-off tasks.
  - After a run succeeds, offer to save it as a tool or put it on a schedule.
  - Let users record a demonstration on hard sites.
  - Cache what worked so repeat runs are faster and cheaper.

### N11. "One place for all my AI." A control panel that works across AI vendors. LOW as a stated need, HIGH as a gap in the market

- **Evidence:**
  - Competitor analysis shows that every parallel-agent product is tied to one vendor (S1, S2).
  - Some users already split work across vendors: "I use claude's chrome plugin all the time. As well Chatgpt's agent mode."
  - Users switch products when vendors change pricing.
  - However, **no customer in our sample explicitly asked for a dashboard that covers several vendors.**
- **Implication:** Treat this as a hypothesis, not a proven need. It may matter more as protection against vendor changes and usage limits ("route to whichever plan has headroom") than as a reason people buy. Test it in interviews before making it the headline.

---

## Part 2: What customers want most, in their own words

These are the outcomes and capabilities customers ask for, ranked by frequency × intensity across the five streams.

| Rank | What they want | How they say it | Linked needs | Confidence |
|---|---|---|---|---|
| 1 | **Hand off the boring, multi-step web chores**, especially on sites with no API | "I know exactly what to do, it's just very tedious to actually do it." · "this literally saved hours of doing this tedious work" · "automate tasks for apps that don't have connectors" | N3, N2 | HIGH (20 of 70 community entries, plus the strongest 5-star reviews) |
| 2 | **Watch websites for me and tell me when something changes** | "check once a day for the next week and notify me of any price changes" · "scrape some certain websites on a regular schedule… report the result to me" · "No tools seem to have a debounce feature" (debounce means only alerting when something actually changes) | N6, N10 | HIGH (8 of 70 entries, plus Claude reviews asking for scheduled tasks, plus ChatGPT Work, Cowork and Spark all shipping schedules) |
| 3 | **Work in its own tabs, in the background, while I keep working** | "while i can do my work in other tabs with out getting interlinked or disturbed" · "I don't want to have to keep checking myself" | N6 | HIGH |
| 4 | **Use the AI subscription I already pay for, at a cost I can predict** | "works seamlessly with my existing ChatGPT subscription" · "you get the same model you already use" · "a way to see how many credits you need for a specific task" | N1 | HIGH |
| 5 | **Give it an input, get a finished result** (a tool, not a platform) | "choose a tool → provide the input → receive the completed result" · "simply ask ai to do their daily task on web" · "No coding, no macros, no BS" | N3, N10 | MEDIUM-HIGH |
| 6 | **Only ask me before money, messages or anything I can't undo** | "research is fine, but I don't want the AI to go on a shopping spree" · "corporate credit card with limits" · "I want to review the choices made on my behalf" | N5, N8 | HIGH |
| 7 | **Show me what it did, and let me pick up where it left off** | "reliability, persistence, auditability, and the ability to review previous actions" · "a reliable method for exporting existing… work without restarting a task" | N2 | HIGH |
| 8 | **Let me show it once, and have it remember** | "easier to just show the workflow than explain it" · "only looses time and tokens the first round" | N10 | MEDIUM |
| 9 | **Don't make me switch browsers or lose my stuff** | "lost my browser's history and favorites, passwords" · "Atlas sucked… *bookmarks*" | N9, N4 | MEDIUM |
| 10 | **Faster** | "dog slow" · "very slow compared to my repetitive tapping" | N6 | MEDIUM. Users mind slowness less when they don't have to watch. |

### Top tasks to automate

This ranking combines the counts from the community sample (S3) with themes from the review data (S4) and the Menlo 2026 usage survey (S5).

| Rank | Task | Example evidence | Notes for the product |
|---|---|---|---|
| 1 | **Filling in forms on portals**: licensing and credentialing applications, tax, immigration and other government sites, job applications | credentialing applications · German tax declaration · electronic travel authorization · "apply for 10 jobs" | High stakes, done rarely, tedious. The agent needs to pull data from the user's local files (PDFs, passport scans). Needs field-by-field review before submitting. |
| 2 | **Watching sites and sending alerts**: prices, listings, items back in stock, rule or policy pages, daily digests | rental listings checked twice a day · concert ticket prices · German law pages · Zillow price drops | **This is the task most likely to become a habit.** Needs scheduling, alerts only when something changes, and a digest. |
| 3 | **Travel, reservations and appointments** | Airbnb with precise requirements · rental car discount codes · restaurant availability · dentist · tennis court | Stop before paying. Date pickers are a known failure point. |
| 4 | **Shopping research and comparing deals** (stop before checkout) | out-of-print DVDs on eBay · best new and used options · grocery coupons | 50% of shoppers who use AI use it to compare products (Menlo). Big retailers block agents. |
| 5 | **Admin work inside web apps that have no API**: invoices, VAT, quotes, receipts, applicant tracking systems, product data for online shops, old healthcare systems | Uber receipts for reimbursement · VAT spreadsheet · "legacy software with no API" | Strong fit for small businesses and independent professionals. Recurring. |
| 6 | **Research compiled into a spreadsheet, and lead lists** | Google Maps results into a Google Sheet · LinkedIn leads into a sheet | The output is a table, which is easy to check. |
| 7 | **Email and calendar briefings, and personal admin** | daily digest · family calendar events | Read-only access is the trusted starting point. |
| 8 | **Bills, subscriptions, insurance quotes, cancellations** | insurance quotes · medical bills · cancelling a phone plan | Sites use dark patterns to make cancelling hard, and Cloudflare blocks agents. Hard to deliver today. |

---

## Part 3: Jobs-to-be-done map

| Kind of job | The job |
|---|---|
| **Functional** | Finish repetitive, multi-step chores across websites (often sites with no API) correctly, without doing them by hand. Keep an eye on information that changes and act when it matters. Turn web research into a usable result (a sheet, a digest, a filled form). Get a one-off, high-stakes form exactly right. |
| **Emotional** | Relief from tedium ("loathe clicking through these sites"). Feel in control and safe, not "scary". Confidence that the job is really done. Feel they are getting their money's worth from the AI subscription ("made real profit"). Not be anxious about a surprise bill. |
| **Social** | Look responsive and competent to clients, a boss or family ("my 2nd staff", "secret weapon"). Avoid being the person whose account got banned. For the technically confident helper: be the person who "set it up" for friends, family or coworkers. |

---

## Part 4: Provisional segments

The skill's rule is that a persona needs at least 5 to 10 data points from one consistent segment. The segments below meet that rule only loosely, and much of the evidence is second-hand. **Treat them as hypotheses to confirm in interviews, not as final personas.** Fields with no supporting data are marked "unknown". We have not filled them in with guesses.

### Segment A: The admin-heavy independent professional (about 10 data points)
- **Who:** freelancers, licensed professionals (healthcare, therapy), consultants and solo founders. Pays $20 a month for Claude or ChatGPT.
- **Main job:** get the paperwork and portal admin around their real work done (credentialing, taxes and VAT, invoices, receipts, applicant tracking systems, Search Console, WordPress).
- **Triggers:** a deadline (license renewal, tax season, month-end reimbursement). A portal that has no API. Seeing a friend's agent do it.
- **Top pains:** "Inputting hundreds of information is so tedious". Connection failures. Running out of tokens. Lost sessions.
- **What success looks like:** "saved hours", "cuts my time in half", "made real profit".
- **Objections:** account bans ("termination letter citing 'fraudulent conduct'"). Giving passport or bank details to an AI company.
- **Alternatives:** doing it by hand, an accountant or virtual assistant, a Claude or ChatGPT extension.
- **Language:** "tedious", "credentialing applications", "tax declaration", "receipts".
- **Willingness to pay on top of their AI subscription:** unknown.

### Segment B: The small-business operator or operations staffer (about 8 data points)
- **Who:** online shop and retail managers, small-business owners who write quotations and work orders, sales and lead-generation staff, automation consultants serving clinics.
- **Main job:** move data between web apps that don't talk to each other, and produce standard documents.
- **Triggers:** a system with no API. Zapier or Make can't log in to the site. Repeated weekly work.
- **Top pains:** the interface asks them to learn a system first ("The interface created the barrier"). Workflows that "stop halfway". Credit costs.
- **What success looks like:** "turn a repeated task into a reliable tool".
- **Objections:** reliability, pricing confusion.
- **Alternatives:** Zapier or Make (API only), Bardeen or Axiom (complex to set up), a virtual assistant, doing it by hand.
- **Company size, number of seats, who decides to buy:** unknown.

### Segment C: The life-admin power consumer (about 11 data points; this segment skews technical in our sample)
- **Who:** people hunting for deals, renting a home, looking for a job, planning travel, managing a family's admin.
- **Main job:** search, compare and monitor across many sites, then act at the right moment.
- **Triggers:** an active search (apartment, job, trip). A price-sensitive purchase.
- **Top pains:** agents that fail quietly, slowness, getting blocked by sites, usage caps ("maxed out my 40 for this month in 3 days").
- **What success looks like:** a digest they can act on from their phone, an alert when a price drops.
- **Objections:** never let it check out on its own.
- **Alternatives:** doing it by hand, Comet, Claude in Chrome, ChatGPT Work, Muse.

### Segment D: The tech-savvy helper (about 5 data points). This is a channel, not the main buyer
- **Who:** the developer or power user who sets up agents for a partner, parents, friends or coworkers ("set up Cowork for several non-technical friends").
- **Why they matter:** they shape what non-technical people adopt. They also notice that non-technical people "struggle to get up and running" and end up "blind approving".
- **Implication:** consider letting a helper share templates or set up a family member's agents, possibly with a mode where the helper approves on their behalf.

### Later segments, not ready for personas
- **Older adults:** AARP found 80% of adults over 50 have used AI, but 42% call themselves beginners and 51% think AI is unsafe.
- **Blind and low-vision users:** current agents complete only 52.5% of tasks for them.

Both groups have real need but low trust and low success rates today. Build accessibility in from the start (screen-reader support, voice), but don't lead with these segments.

---

## Part 5: Contradictions and challenges to our assumptions

The skill asks us to try to prove our assumptions wrong. Here is where the evidence pushes back on the team's starting idea.

1. **"An orchestrator like Conductor" is a developer's frame.**
   - Conductor's ideas (workspaces, branches, diffs) are native to developers. Non-developers name the document or result they want ("quotation", "tax declaration"). They don't think in agents.
   - The parts of the orchestrator idea that carry over are: isolation, starting many jobs at once, a screen to review results, an approval inbox, schedules, and status at a glance.
   - **Hypothesis:** lead with jobs and results, and keep the orchestration mostly invisible. Show "your 4 jobs ran today, 1 needs you", not "manage 4 agents".
2. **Running agents in parallel is a means, not something most people ask for.**
   - Heavy users ask for parallel agents loudly. Non-developers ask for "in the background", "while I work" and "check it for me every day".
   - The value of running agents at the same time shows up as recurring and background jobs, not as people watching many agents at once.
3. **"Uses the subscription they already have" works only in part.**
   - It is officially possible with OpenAI, through a gated partner program.
   - With Anthropic and Google it requires installing and signing into their official command-line tool, which is a barrier for non-developers. Their usage limits are designed for "ordinary, individual usage", and running agents in parallel burns through those limits quickly.
   - Customers love the idea, but it cannot be the only path.
4. **Users want autonomy and also want control.** "I don't need to be in the loop for each step" sits alongside "I want to review the choices made on my behalf". These fit together if permissions depend on the type of action: free for reading, ask for actions that can't be undone.
5. **Users want reusable workflows but hate building them.** The way through is to save a workflow from a run that already succeeded.
6. **Security worries stop people from adopting, but adopters rarely ask for security.** Surveys show distrust is the main reason people don't use agents. Yet non-technical adopters approve everything without reading. So safety must be the default, and it should be marketed to people who haven't adopted yet.
7. **Benchmarks don't match what users experience.** Benchmark scores on live websites have reached 97–99%, but users still report frequent failures. Don't position the product on raw capability. Position it on verified results.
8. **Our evidence about non-technical users is thinner than we would like.** Reddit was blocked, and most of the non-developer signal comes from store reviews, second-hand reports and surveys. The ranking above is directional. Interviews are needed before committing to a direction (see [`research-gaps-and-next-steps.md`](research-gaps-and-next-steps.md)).

---

## Part 6: What this means for the product

**Build these first, in priority order:**

1. **Start from jobs, not from a blank prompt.** Offer templates for the top tasks: fill a form from my files, watch these pages and alert me on changes, research into a sheet, routine admin in a web app.
2. **One isolated, logged-in browser profile for each agent.** Run in the background and never steal focus. If one agent fails, the others keep running. Import logins one site at a time.
3. **Proof of completion.** Success checks, screenshots, counts, an honest "couldn't do this", and a run history that can be replayed and resumed.
4. **An approval inbox.** Approve the plan, not each click. Permissions by type of action (read / write / pay, send or delete). Approve in batches. Notifications on the phone. Spending caps enforced by the app.
5. **Clear costs.** An estimate before each run, the room left on each subscription, and a queue that waits for usage limits to reset.
6. **A good handoff for logins, two-step codes and CAPTCHAs.** Notify the user, let them take over, then let the agent continue.
7. **Save a successful run as a tool.** Then the user can schedule it. Record a demonstration on hard sites. Cache steps that worked.
8. **Safe defaults.** Banking and health sites blocked unless the user opts in. Site allowlists. A kill switch that stops the actual process. No central password storage.
9. **Portable workflows** that don't depend on one AI vendor.

**Avoid these:**

- A blank prompt box as the main interface.
- Asking users to switch browsers.
- Pricing in opaque credits, or charging for failed runs.
- Asking users to approve low-level steps they can't read.
- Making payments without the user's approval.
- Building the product on one provider's subscription loophole.
