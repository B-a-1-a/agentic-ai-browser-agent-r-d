# Market landscape: browser agents for non-developers who already pay for AI (October 2026)

This file summarizes the competitive landscape. The detailed evidence is in [`sources/01`](sources/01-ai-browsers-and-first-party-agents.md), [`sources/02`](sources/02-automation-tools-orchestrators-and-byo-subscription.md), and [`sources/05`](sources/05-adoption-trust-security.md). Confidence labels follow the customer-research skill:

- **[HIGH]**: 3 or more independent sources.
- **[MEDIUM]**: 2 sources.
- **[LOW]**: 1 source.

## The short version

1. **Demand is real, and it comes from people who already pay for AI.**
   - ChatGPT alone has 50M paying subscribers.
   - 65% of people who pay for AI have used an agent, compared with 13% of people who don't pay. [MEDIUM]
2. **General-purpose browser agents have not kept their users.**
   - ChatGPT Agent lost about 75% of its weekly users within months, because people "couldn't figure out what to do with it". [LOW: one source]
   - OpenAI shut down its Atlas browser after 292 days. [HIGH]
   - Google shut down Project Mariner. [HIGH]
3. **The big AI labs are building browser agents into their own apps, not separate browsers.** Each lab now has background, scheduled, and parallel agents. Each one only works with that lab's own model, inside that lab's own app. [HIGH]
4. **Nobody offers what we are proposing.** No product combines all of these:
   - an app non-developers can use
   - several agents running in parallel, with monitoring
   - the AI subscription the user already pays for
   - the user's own logged-in browser sessions

   The closest product, Browser Use Desktop, appears to have stalled at version v0.0.31. [MEDIUM]
5. **Using the customer's existing subscription is possible, but only through narrow, changing routes.** OpenAI has an official, invite-only route. Anthropic and Google only allow wrapping their official command-line tools. [MEDIUM: these policies changed at least 5 times in 2026]
6. **The main risks are:**
   - the big labs adding multi-agent management themselves
   - providers changing what subscription use they allow
   - prompt-injection security (hidden instructions on a web page that hijack the agent)
   - websites blocking agents
   - users who won't pay on top of the subscription they already have. Vibe Kanban, a free agent orchestrator, shut down for this reason.

## 1. Market map

| Segment | Examples (status Oct 2026) | What they do well | Where they leave our customer underserved |
|---|---|---|---|
| **AI labs' own assistants with built-in browser agents** | ChatGPT Work, plus a Chrome extension and the "Dots" always-on agents · Claude in Chrome (generally available 2026-08-26) and Claude Cowork with a built-in browser · Gemini Spark and Chrome auto browse · Perplexity Comet and Computer · Edge "Browse with Copilot" | Huge reach and bundled pricing. They now run tasks in the background, on schedules, and in parallel. Cowork reports that over 90% of its usage is non-developer work. | Each works only with its own lab. Parallel cloud browsers fail at logins and CAPTCHAs. The local extensions break easily: Claude in Chrome is rated 2.9★ and ChatGPT's extension 2.75★, and about 25% of negative reviews are about setup or connection failures. Usage caps apply (for example, a 5-hour limit on Plus). Regional limits (US only, no EU). Labs keep cancelling products. |
| **AI-native browsers** | Comet · Opera Neon (free host for your own agent since 2026-08-14) · Dia (consumer Pro plan dropped, now enterprise) · Genspark · Fellou · Sigma · Brave Leo (opt-in) · BrowserOS (open source) | Agent built into the browser. Neon and BrowserOS let you bring your own agent. | Asks users to switch browsers. All AI-first browsers together have no more than 2.66% of browser sessions. Users lost bookmarks and history when Atlas shut down. |
| **General agents paid with credits** | Manus · Genspark Super Agent · Perplexity Computer · Lindy · Twin · Simular | Can do almost anything. Real revenue: Manus about $125M a year, Genspark about $250M a year [LOW]. | Credits are the #1 complaint (Trustpilot ratings of 1.2 to 1.7). Users can't see what they're doing ("no window in"). They claim tasks are "complete" when they are not. |
| **No-code automation and RPA** (RPA is software that repeats recorded clicks and keystrokes) | Zapier · Make · n8n · Bardeen · Axiom · Browse AI · UiPath · Power Automate · Relay.app (shut down 2026-09) | Predictable once set up. Large libraries of integrations. | Most connect through APIs and can't log in to websites ("A make agent essentially can only make API calls"). You must build a workflow before anything runs. Pricing per task or credit runs out fast. |
| **Browser-agent tools for developers and power users** | Browser Use (open source, cloud, and **Desktop app**) · Browserbase/Director · Skyvern · Nanobrowser · rtrvr.ai · Do Browser · Ego lite · Yurei · Steel | Can use your own key or subscription. Can use your local logged-in profile. Ego and Browser Use run agents in parallel, each in its own "Space". | Built for developers. Setup needs an MCP connection (Model Context Protocol, a standard way to plug tools into AI apps), an API key, or a command line. Many are early or stalled. |
| **Agent orchestrators (coding)** | Conductor · Codex app · Cursor Agents Window · Sculptor · Pizza Bot · Vibe Kanban (company shut down 2026-04) | The interface patterns we want: an isolated workspace per task, starting tasks in batches, review screens, inboxes, routines, mobile approval. | Code only. No equivalent of a code diff for browser work. Vibe Kanban: "the vast majority are free users and we couldn't find a business model." |

## 2. Six forces shaping the market

### 2.1 Browser agents are becoming a feature inside the AI apps people already use [HIGH]

- OpenAI on shutting down Atlas: "the browser is a feature, not the destination."
- Google shut down Project Mariner and moved it into Chrome and Gemini Spark.
- Microsoft retired Copilot Mode in Edge.
- Dia dropped its consumer Pro plan.
- Opera turned Neon into a free host for agents users bring themselves.
- a16z (March 2026): "No AI browser has seen accelerating growth."

**What this means for us:** don't build a browser people must switch to. Build a layer that sits on top of the subscriptions and browser people already have.

### 2.2 The industry is moving toward parallel, background agents, but each one only works inside its own lab [HIGH]

These all launched between October 2025 and September 2026:

- Comet Background Assistants, with a "mission control" screen (Max plan only, $200)
- Perplexity Computer ("run dozens in parallel")
- Claude Cowork: parallel tasks, scheduled runs, and Dispatch (start tasks from your phone)
- ChatGPT Work: helper agents, schedules, and triggers
- OpenAI Dots: always-on agents
- Gemini Spark: runs 24/7, in parallel

None of them lets a user who pays for both ChatGPT and Claude see all their agents in one place. A Hacker News thread asking "What should the GUI for AI agents look like?" got 139 points and 85 comments (2026-07-31).

### 2.3 Reliability is improving fast, but long tasks still need supervision [MEDIUM]

**Benchmarks:**
- OSWorld 2.0 measures long tasks that take a human about 1.6 hours. The best agent fully completed 20.6% of tasks in June 2026 and 44.3% in September 2026.
- Agents mostly fail because they "lose track of constraints, … guess rather than ask the user, and skip verification."
- Benchmark scores themselves are unreliable. A UC Berkeley team got near-perfect scores by exploiting flaws in the benchmarks, and 15.3% of "failed" verdicts were wrong.

**Hands-on tests in 2026:**
- **Works:** short tasks on a single site that end in a confirmation step. Examples: research, comparing options, filling a form, building a cart. Chrome auto browse completed 4 of 5 real tasks.
- **Still breaks:** logins and CAPTCHAs, date pickers, cancellation flows designed to trap users ("dark patterns"), and long chains of steps.

**What this means for us:** design for supervision that doesn't need the user watching. Run tasks unattended, check that they finished correctly, and hand off to the user for logins and CAPTCHAs.

### 2.4 People will let agents do research, but they draw a line at paying [HIGH]

| How much control people will give an agent (Accenture, n=25,590) | Share |
|---|---|
| Work together with it | 85% |
| Let it do a specific task | 74% |
| Let it decide, if they approve the payment | 32% |
| Let it pay on its own | 9–12% |

Other surveys agree:
- Gartner: 11% would let AI make purchase decisions.
- Riskified: 55% won't let an agent buy anything, and 73.9% expect a biometric or one-time-code check on every agent transaction.
- When something goes wrong, 50.8% blame the AI platform.

### 2.5 Security is the main objection from businesses and experts [HIGH]

- OpenAI says prompt injection is "unlikely to ever be fully 'solved.'"
- Gartner (December 2025): "CISOs must block all AI browsers in the foreseeable future."
- A University of Washington study (June 2026) found ways to break the browser's same-origin protection (the rule that keeps one site from reading another site's data) in Atlas, Gemini in Chrome, Claude for Chrome, and Comet.
- Zenity's "PleaseFix" attack took over Comet through a calendar invite.
- Malicious injection content on the web grew 32% in Google's crawl (November 2025 to February 2026).
- The OpenClaw incident: an agent lost its "wait for approval" instruction during context compaction and deleted an inbox in bulk.

**What this means for us:** running many agents multiplies exposure. Safety defaults must be enforced by the app itself, not only by instructions to the model.

### 2.6 Websites are pushing back [HIGH]

- Bots now make 57.5% of HTML requests (Cloudflare, June 2026).
- Cloudflare wants agents to sign their requests (Web Bot Auth) and removed Perplexity from its list of verified bots.
- eBay bans "buy-for-me agents… without human review." Amazon blocked Meta's Muse agent (September 2026).
- **A legal win for agents that run on the user's device:** in August 2026 the Ninth Circuit lifted the injunction against Comet in Amazon's lawsuit. Because the agent runs on the user's device, the court treated the user as the one accessing Amazon. Claims based on terms of service remain open.

**What this means for us:** an agent that runs locally on the user's machine, in the user's own logged-in browser profile, is legally safer than a cloud agent. It will still hit blocks on major retailers. Never store users' passwords centrally.

## 3. Can we use the customer's existing AI subscription? (October 2026)

| Provider | What is allowed | Route for our app | Risk |
|---|---|---|---|
| **OpenAI (ChatGPT Plus/Pro)** | **Sign in with ChatGPT, with usage counted against the user's plan** (launched 2026-09-29). Users set a weekly limit per app. The app cannot read their chats. Conductor was a launch partner. | Apply for the commercial trial, which is limited to selected partners. Open-source apps can register on their own. The Codex App Server can be embedded in other apps. | Access is gated. Plus subscribers share one 5-hour limit across all apps. Technical restrictions such as `store:false`. |
| **Anthropic (Claude Pro/Max)** | **No Claude.ai login inside third-party apps.** Apps may not "collect, store, or intermediate Claude.ai credentials". Allowed: the user signs in to the **unmodified Claude Code program** with their own subscription, "including where a platform hosts Claude Code". | Wrap the unmodified Claude Code program, which the user installs and signs in to themselves. The Agent SDK docs say third-party apps may not offer claude.ai login or rate limits "unless previously approved". | The policy changed at least 5 times in 2026. Limits assume "ordinary, individual usage", which conflicts with running many agents in parallel. Installing Claude Code is a hurdle for non-developers. |
| **Google (AI Pro/Ultra)** | Reusing Gemini CLI's login inside third-party apps is detected, and Google **banned** some subscribers who did it (February 2026). Gemini CLI stopped serving consumer plans in June 2026 and was replaced by Antigravity CLI, which is closed source. A forum answer says running the official command-line tool locally for one user "is permitted". [LOW] | Wrap Antigravity CLI. | Least clear of the three. Not available in some regions. |
| **GitHub Copilot** | The Copilot SDK became generally available in June 2026 for all subscribers. Commercial use by third-party apps is unclear. | Copilot SDK | Gray area. |
| **Other routes** | Bring your own API key (always allowed, but hard for non-developers). Build an MCP server, a ChatGPT app, or a Claude plugin, so we run inside their apps and they pay for the AI, but we lose our own interface. Sell our own credits (users dislike this most). | — | — |

**What this means for the business:**
- The value we can charge for is orchestration, reliability, safety, and saved workflows. The AI itself is paid for by the user's subscription.
- Pricing must not feel like "credits on top of credits".
- Treat "works with the plan you already pay for" as a **feature that depends on each provider's permission**, not as the foundation of the product.
- Keep a fallback: transparent hosted billing per task, with the cost shown before each run.

## 4. What competitors leave open

| # | Gap | Evidence | Confidence |
|---|---|---|---|
| 1 | **One place to run agents from different labs** using the subscriptions people already have | Every lab's parallel-agent product only works with that lab. The tools that work across labs (Neon, BrowserOS, Ego, Yurei) need MCP or a command line. | HIGH that the gap exists. **LOW evidence that customers ask for it directly.** See the needs synthesis. |
| 2 | **Isolated, logged-in, background browser profiles, one per agent** | Cloud parallel agents fail at logins. Local agents take over the one browser the user is working in. Users ask for "isolation" and "dedicated tabs". Only developer tools (BrowserOS neo, Ego, Browser Use Desktop) do this today. | HIGH |
| 3 | **A review screen and approval inbox for browser work**, the equivalent of a code diff | No consumer product has one. Comet's mission control requires the $200 plan. Perplexity Computer is "a black box". | HIGH |
| 4 | **Scheduling that knows each subscription's usage limits** | 5-hour caps, daily caps, credits. "Draconian 5-hour rolling cap… bricked my project." | MEDIUM |
| 5 | **Checking that a task really finished, plus guided handoffs to the user** | False "done" reports. OSWorld failures come from skipped verification. Agents can't handle date pickers, dark patterns, or CAPTCHAs. | HIGH |
| 6 | **Safety defaults a non-developer can understand** | Gartner and the University of Washington have scared buyers. Brave and Anthropic's isolated profiles show the direction. Per-site permissions exist mostly in enterprise products. | MEDIUM-HIGH |
| 7 | **Workflows that survive when a vendor changes or shuts down its product** | Atlas, Mariner, Copilot Mode, Dia Pro, ChatGPT Agent, and Comet browser control (moved behind credits) all changed or disappeared. Manus deleted user data. | HIGH |
| 8 | **Windows and markets outside the US** | Auto browse and Spark are US-first. Browse with Copilot is US-only. Claude in Chrome works only in Chrome. Dia on Windows has no agent features. | MEDIUM |

## 5. Who could absorb this opportunity

- **Anthropic (Cowork):** the closest competitor. It already has non-developer users, a built-in browser with separate profiles, parallel tasks, scheduling, and mobile Dispatch. What it lacks: support for other labs, a multi-agent dashboard, and a review inbox.
- **OpenAI (ChatGPT Work, Dots):** always-on cloud agents, triggers, and replay. It also owns the only official sign-in route for third-party apps. Its cloud browsers keep failing at logins.
- **Google (Chrome auto browse, Spark):** ships to about 3B Chrome users by default. Sean Kim called auto browse "useful enough that a non-developer keeps it on." The founder of Relay.app, a shut-down automation startup, joined the Chrome team to build "AI in Chrome".
- **Browser Use:** already ships the closest product concept (Desktop app, "a team of browser agents", Claude and ChatGPT subscription support), but appears stalled. It could restart quickly.

**Defensible position, if one exists:** be the neutral, local-first control room for browser work. It would:
1. run each agent in its own logged-in profile
2. let users review and approve what agents do
3. keep users' workflows when vendors change their products
4. work across whichever AI subscriptions the user already has
