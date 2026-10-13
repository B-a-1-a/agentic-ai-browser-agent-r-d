# Source notes 02: Automation tools, agent orchestrators, and "bring your own subscription"

These notes are raw findings from one research stream, collected on 2026-10-12. They cover four areas:

- tools that automate work without code ("no-code" automation)
- startups that build browser agents
- apps that run and manage many agents at once ("orchestrators")
- whether an app can use the AI subscription a customer already pays for ("bring your own subscription")

**How to read these notes:**

- The research hit its web-search limit partway through. After that, the rest was checked by fetching pages directly, through the GitHub API, and through the Hacker News API.
- **[2°]** means only one secondary source supports the item. **[unverified]** means it could not be checked.
- Hacker News quotes were copied word for word through the Hacker News API. Trustpilot quotes were collected with a tool that summarizes pages, so check them against the original before you publish them.

## Bottom line

**No product combines all four parts of our concept.** The four parts are:

1. it is easy to use for people who are not developers
2. it runs and watches many browser agents in parallel
3. it uses the AI subscription the customer already pays for
4. it uses the customer's own logged-in browser

**The closest product is the Browser Use Desktop App** ("Run a team of browser agents on your desktop"). But its last release was v0.0.31 on 2026-05-09, and no code has changed since 2026-05-26. It appears to be stalled.

**Using a customer's subscription is now possible, but only in narrow ways:**

- **OpenAI (ChatGPT):** OpenAI launched an official "Sign in with ChatGPT" program on 2026-09-29. Commercial apps must apply to join it.
- **Anthropic (Claude) and Google (Gemini):** The only allowed route is to run each company's official command-line agent, without changes. The customer signs in to that agent with their own account. The agents are Claude Code (Anthropic) and Antigravity CLI (Google).

**The market is consolidating.** Several products have shut down: Relay.app, the company behind Vibe Kanban, and ChatGPT Atlas. MultiOn and Magnitude changed direction. Anthropic bought Vercept, the company behind Vy.

## 1. Competitor tables

### A. No-code automation tools with AI agents

| Product | Category | Target user | Price (Oct 2026) | How it automates the browser | Strengths | Main complaints | Source |
|---|---|---|---|---|---|---|---|
| **Zapier** (Agents, Copilot) | Workflow automation with an agents add-on | Non-developers, small businesses | Pro plan from $19.99/month, paid yearly, with 750 tasks. Agents: free for 400 activities; Pro about $33.33/month for 1,500 activities. | Agents can browse websites in the cloud. There is also a Chrome extension. You pay per activity. | Connects to a very large number of apps. Copilot builds automations for you. | Task limits run out fast. Copilot struggles. Trustpilot rating: 1.3 out of 5 (322 reviews). | [pricing](https://zapier.com/pricing); [Trustpilot](https://www.trustpilot.com/review/zapier.com) |
| **Make** | Visual workflows. AI Agents added 2026-02-11. | Non-developers to technical users | Free plan with 1,000 credits. Core $12, Pro $21, Teams $38 per month **[2°]**. | No built-in browser agent found. | Cheap per credit. | Unused credits expire. Extra credits cost 25% more **[2°]**. | [Latenode](https://latenode.com/blog/make-ai-agents) |
| **n8n** | Workflow and agent builder. You can run it on your own server ("self-host"). | Technical users, operations teams | Starter €20/month, paid yearly (2,500 runs). Pro €50. Business €667. Free if you self-host. | No built-in browser agent found. | Charges per workflow run, not per step. You can use your own AI keys. You can self-host. | Aimed at technical users. | [pricing](https://n8n.io/pricing/) |
| **Lindy** | AI assistant and agent builder | Non-developers, small businesses | 7-day trial with $50 of credits. Team plan from $29.99/month (3,000 credits). Extra credits cost $10 per 1,000. | Uses a browser that runs in the cloud. Paid plans only. | You build agents by describing them in plain language. | You cannot see how credits are spent. Trustpilot: 1.7 out of 5. | [pricing](https://www.lindy.ai/pricing); [Trustpilot](https://www.trustpilot.com/review/lindy.ai) |
| **Gumloop** | Agent-first automation | Non-developers, operations teams | Pro $37/month (20,000 credits), plus an 8% fee **[2°]**. | **[unverified]** | Supports more than 35 AI models. | Fees stack up. Extra use costs 2.7 times the included rate. | [Jetadmin](https://www.jetadmin.io/blog/gumloop-review/) |
| **Relay.app** | AI workflows where a person reviews steps | Non-developers | **Shut down.** Announced 2026-07-16. Paid accounts deleted 2026-09-14. | n/a | n/a | Its CEO joined Google as a Vice President of Product for Chrome. | [TechCrunch 2026-08-17](https://techcrunch.com/2026/08/17/ai-automation-startup-relay-shuts-down-staff-joins-googles-chrome-team/) |
| **Bardeen** | Now focused on sales automation | Sales teams | $10–$50/month | Chrome extension | Collects and fills in sales lead data | Charges credits for every row of data. | [pricing](https://www.bardeen.ai/pricing) |
| **Axiom.ai** (Y Combinator) | Browser automation that records your steps | Non-developers, operations teams | $15–$250/month, based on hours of running time | Chrome extension plus bots in the cloud. Also connects to Claude through MCP (Model Context Protocol, a standard way to plug tools into AI assistants) and a Claude Code skill. | You pay for running time, not credits. Works with Claude. | — | [pricing](https://axiom.ai/pricing) |
| **Browse AI** | "Robots" that collect data from websites and watch them for changes | Non-developers | Free plan (50 credits). $19–$87/month **[2°]**. | You click through a site to record what the robot should do. | Quick to set up. | "glitchy". Little AI. Trustpilot: 2.7 out of 5. | [Trustpilot](https://www.trustpilot.com/review/browse.ai) |
| **Automa** | Open-source browser extension where you build tasks from blocks | Hobbyists | Free | Chrome extension | Free. 21.7k stars on GitHub. | No code changes since 2026-03-02. | [GitHub](https://github.com/AutomaApp/automa) |
| **UiPath** | Automation software for large companies, with agents | Large companies. A free Community plan is available. | Community plan free. Basic plan from $25/month. | ScreenPlay automates apps from plain-language instructions. | Strong controls and oversight for companies. | Not designed for individual consumers. | [pricing](https://www.uipath.com/pricing) |
| **Microsoft Power Automate / Copilot Studio** | Automation plus agents that operate a computer | Large companies, Windows | 5 Copilot Credits per step | The agent controls a Windows computer that you set up. | Saves login details securely. Lets you list which sites and apps the agent may use. Emails a person when supervision is needed. | Setup is complex, aimed at large companies. | [Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-copilot-studio/computer-use) |

### B. Browser-agent startups

| Product | Category | Target user | Price | How it automates the browser | Strengths | Main complaints | Source |
|---|---|---|---|---|---|---|---|
| **Browser Use** (open-source code, cloud service, **Desktop App**) | Toolkit for building agents, a cloud service, and a desktop app | Developers. The desktop app is for advanced non-developers. | Cloud: $0.02 per browser-hour, plus 20% on AI model costs. The desktop app is free. | The desktop app copies your browser cookies into a fresh browser, so your logins carry over. You start tasks with a keyboard shortcut or a WhatsApp message. It supports **"Claude Code Subscription or API Key"** and **"ChatGPT Subscription or API Key."** | **The closest match to our concept.** The open-source project has 117.7k stars on GitHub. | The desktop app has only 700 stars, is at version v0.0.31, and has had no code changes since 2026-05-26. | [desktop](https://github.com/browser-use/desktop); [pricing](https://browser-use.com/pricing) |
| **Browserbase Director / Stagehand** | Director lets non-developers create automations without code. Stagehand is a developer toolkit. | Director is aimed at "operators, analysts, marketers." Stagehand is for developers. | $0–$99/month | Runs only in Browserbase's cloud browsers. | Leading infrastructure provider. | Locked to Browserbase's cloud. | [Skyvern blog](https://www.skyvern.com/blog/director-reviews-pricing-alternatives/) |
| **Skyvern** (Y Combinator) | Browser automation that uses AI vision, open source plus a cloud service | Developers, operations teams | $0–$149/month | Cloud, or run it on your own servers | Works on websites it has never seen before. 23.2k stars on GitHub. | Charges credits for every action. | [pricing](https://www.skyvern.com/pricing) |
| **MultiOn** | **Changed direction.** It is now AGI, Inc. and makes an agent for Android phones. | Consumers | n/a | Left the browser-agent market. | n/a | n/a | [theagi.company](https://theagi.company/) |
| **HyperWrite** | Writing assistant with an agent mode | Consumers | $19.99–$44.99/month | Chrome extension | Cheap | Now focuses on writing, not agents. | [hyperwriteai.com](https://www.hyperwriteai.com/) |
| **Do Browser** | Chrome agent you control with plain-language instructions | Advanced business users | **Free if you connect your own ChatGPT or Claude subscription**, plus 10 messages on its own AI. Paid plans cost $25–$100/month. | Chrome extension | Free plan that uses your own subscription. | It does not explain how it connects to your subscription **[unverified]**. If it uses your Claude.ai login, that breaks Anthropic's rules. | [dobrowser.io](https://www.dobrowser.io/) |
| **Nanobrowser** | Open-source Chrome extension that uses several agents | Hobbyists | Free. You supply your own API key. | Extension | 14.1k stars on GitHub | You need an API key. | [GitHub](https://github.com/nanobrowser/nanobrowser) |
| **Magnitude** (Y Combinator) | **Changed direction** from browser agents to infrastructure for running AI models | Developers | Free | n/a | n/a | n/a | [Launch HN](https://news.ycombinator.com/item?id=49911995) |
| **Twin** | No-code agent builder | Small business teams | From €20/month plus credits | A cloud browser agent that "can log into any website" | Claims more than 5,000 app connections. | — | [twin.so](https://twin.so/learn/what-is-twin/) |
| **Simular (Sai)** | Desktop agent that operates your computer | Advanced non-developers, teams | $50–$500/month | Controls your own Mac, or a private computer in the cloud. Asks for approval before actions that cannot be undone. | Claims 73% on OSWorld 2.0, a test of how well agents operate computers. | Prices keep changing. | [simular.ai](https://www.simular.ai/simular-desktop) |
| **Manus** | General-purpose agent | Consumers, advanced non-developers | $20–$40/month **[2°]** | A cloud computer, or your own browser through an extension | Can do many kinds of tasks. | Uses up credits fast, and unused credits expire. Trustpilot: 1.2 out of 5. | [Trustpilot](https://www.trustpilot.com/review/manus.im) |
| **Genspark Super Agent** | All-in-one agent | Consumers | $0–$249.99/month **[2°]** | Cloud agent plus an extension | Produces many kinds of output. | Trustpilot rating hidden. Unlimited chat was replaced by a weekly limit. | [Trustpilot](https://www.trustpilot.com/review/genspark.ai) |
| **Kortix / Suna** | Open-source "AI Operating System" | Developers | Free / **[unverified]** | Browser that runs in an isolated cloud environment | 20.3k stars on GitHub | — | [GitHub](https://github.com/kortix-ai/suna) |
| **rtrvr.ai** | Extension, cloud browser, API, and MCP | Knowledge workers | Free plan shows sponsored content. You can use your own AI keys. | Extension or cloud browser | Works on sites where you are logged in. | Free plan depends on ads. | [rtrvr.ai](https://www.rtrvr.ai/) |
| **BrowserOS** | Open-source browser with a built-in agent | Advanced non-developers | Free | **Sign in with your ChatGPT Plus/Pro, GitHub Copilot, or Qwen Code account.** No API key needed. | Free, and no API key needed. | — | [blog](https://browseros.com/blog/bring-your-own-agent) |
| **Ego (lite)** | Browser that outside AI agents can control | Developers, advanced non-developers | Free (Mac only) | Claude Code, Codex, or Cursor control the browser. Each agent works in its own separate "Space." Imports your Chrome cookies so your logins carry over. | Many agents can run at once without getting in each other's way. | Mac only. | [lite.ego.app](https://lite.ego.app) |
| **Hark "Handoff"** | Consumer browser agent | Consumers | Waitlist | Uses its own AI model to take actions | Raised $700M. | Not launched yet. | [TechCrunch](https://techcrunch.com/2026/08/05/hark-previews-its-browser-use-agent-for-completing-tasks/) |
| **Vercept (Vy)** | App whose agent operates your computer | Consumers | **Anthropic bought the company on 2026-02-25.** Vy shut down. | n/a | n/a | n/a | [Hacker News](https://news.ycombinator.com/item?id=47168371) |

**Other 2026 launches to watch:**

- **Intuned:** browser automations written as code.
- **Screenpipe:** "Record how you work and turn that into agents."
- **Kampala:** works out how an app communicates behind the scenes and turns that into an API.
- **Steel.dev:** "fleets of browser sandboxes," meaning many isolated browsers that agents can use.

## 2. How orchestrators are designed

| Orchestrator | Status | Design patterns worth copying | For non-developers or browser tasks? |
|---|---|---|---|
| **Conductor** | Active. Free if you use your own subscriptions or keys. Pro $50/month. Teams $60/user. | "Each task gets its own workspace, branch, files, terminal, diff, and review path." A Dispatcher creates many tasks quickly. A diff view shows what changed. Checkpoints. Cloud workspaces that "keep working when you close the app." Several people can work together. Routines. An iOS app. **Sign in with ChatGPT** (2026-09-29). | For developers only. No browser agents. [docs](https://www.conductor.build/docs/), [changelog](https://www.conductor.build/changelog.md), [pricing](https://www.conductor.build/pricing) |
| **Codex app** (inside the ChatGPT desktop app since 2026-07-09) | Active | Each thread gets its own workspace. Shows what changed, with a panel for submitting changes. Automations. Can hand work off to the cloud. Has a built-in browser and can operate the computer. The **ChatGPT Work** mode handles tasks that are not coding. It can run once, on a schedule, in response to an event, or by watching continuously. It shows a plan for you to approve first. **Dots** are always-on agents with their own computer. | Work mode is aimed at non-developers. Users report confusion about which mode to use, and the modes share one 5-hour usage limit. |
| **Claude Cowork** | Active. Available on Pro, Max, Team, and Enterprise plans. | Shows its plan and waits for your approval. "You see what it's doing and can stop it at any step." Runs scheduled tasks without supervision. You can start tasks from your phone. Has a built-in browser panel with its own separate profile. | **Yes, for both non-developers and browser tasks.** But from the user's point of view, it mostly handles one task at a time. [product](https://claude.com/product/cowork) |
| **Cursor 3 "Agents Window"** | Active | One panel shows agents running locally, in the cloud, or on remote machines. Up to 8 agents in parallel **[2°]**. | For developers |
| **Vibe Kanban** | **The company shut down on 2026-04-10.** The open-source project continues. | A kanban board of agent tasks. You can comment on changes. Live preview. | It shut down because "the vast majority are free users and we couldn't find a business model." [blog](https://vibekanban.com/blog/shutdown) |
| **Crystal → Nimbalyst** | Crystal stopped in February 2026. | A kanban board of sessions. Each session works in its own separate copy of the code. iOS app. | For developers |
| **Sculptor** (Imbue) | Free test version | Each agent runs in its own isolated container. "Pairing Mode." You can use your own Claude subscription. | For developers |
| **Pizza Bot** (open source) | New | **Inbox model:** finished work goes to "Unread," and decisions you need to make go to "Action." Approvals carry over between sessions. Desktop notifications. | General-purpose agents |

**Design patterns that would work for browser tasks for non-developers:**

1. **One task, one separate workspace.** For browser work, give each agent its own browser profile (a "Space"), loaded with the user's cookies so the user's logins carry over. Ego lite and Browser Use Desktop already do this.
2. **Start many tasks at once.** For example, "do this for these 30 rows" becomes one action. Conductor's Dispatcher and Browser Use's keyboard shortcut do this.
3. **A screen to review the agent's work, so you don't have to watch it run.** Coding tools show a "diff" (a list of exactly what changed). Browser tools have nothing similar yet. Options include:
   - a preview of a form before the agent submits it
   - a table of the data the agent collected
   - screenshots of what changed
   - a log of actions that cannot be undone
4. **An inbox with a queue of items to approve.** This answers the complaint that "you can't realistically review everything they do."
5. **Status at a glance, notifications, and approval from your phone.**
6. **Checkpoints and replay.** Record each browser session so you can replay a failed run and fix it.
7. **Routines and schedules.**
8. **Keep running in the cloud** when the laptop goes to sleep.

**No current product combines patterns 1–4 for browser work.**

## 3. Can an app use the customer's existing subscription? (October 2026)

### Anthropic (Claude Pro/Max)

**Short answer:** an app cannot offer "log in with Claude." It can run the official Claude Code program, unchanged, and let the customer sign in to that.

Anthropic's main rule ([legal-and-compliance](https://code.claude.com/docs/en/legal-and-compliance)):

> "Anthropic does not permit third-party developers to offer Claude.ai login into their own applications, or to route requests through Free, Pro, or Max plan credentials on behalf of their users. Moreover, developers may not collect, store, or intermediate Claude.ai credentials or session tokens."

The same page also allows this:

> "Nor does it prevent an end user from signing in to the unmodified Claude Code binary with their own Claude subscription, including where a platform hosts Claude Code."

This exception has conditions:

- The app must not change the Claude Code program.
- The app must not remove its sign-in options.
- The app must not pay for, resell, or come between the customer and their usage.
- Usage limits assume "ordinary, individual usage."

The documentation for Anthropic's Agent SDK (its toolkit for building agents) says: "Unless previously approved, Anthropic does not allow third party developers to offer claude.ai login or rate limits for their products."

**Anthropic changed this policy many times in 2026:**

- **Jan 9:** blocked subscription logins in outside tools [2°].
- **Feb:** updated its terms.
- **Mar 19:** sent legal demands to OpenCode, which then removed Anthropic login.
- **Apr 4:** cut off OpenClaw.
- **Apr 21:** allowed OpenClaw-style use again.
- **May 13–14:** announced that this usage would move to a separate monthly credit.
- **Jun 15:** paused that move.
- **Oct 7:** stated that "Claude Agent SDK, `claude -p`, and third-party app usage still draw from your subscription limits" ([support](https://support.claude.com/en/articles/15036540)).

Two related facts:

- The Max plan now includes $100–$200 per month in API credits. It is **[unverified]** whether those credits can pay for an outside app.
- In April 2026, Anthropic briefly tested removing Claude Code from the Pro plan for 2% of new sign-ups.

### OpenAI (ChatGPT Plus/Pro)

**Short answer:** there is an official route, but commercial apps must be approved.

- OpenAI announced **Sign in with ChatGPT with plan usage** on 2026-09-29. Requests the customer makes in your app count against their ChatGPT plan. It "does not add a new allowance."
- Customers set a weekly limit for each app, as a share of their plan.
- Apps cannot read the customer's ChatGPT conversations or memories.
- Sources: [docs](https://learn.chatgpt.com/docs/sign-in-with-chatgpt), [DevDay](https://learn.chatgpt.com/docs/whats-new/devday-2026).

Access:

- "Commercial sign-in is in a limited trial with selected partners." You must fill in a form to request access.
- Open-source apps can register themselves.
- Launch partners include Conductor, OpenCode, OpenClaw, Devin, Notion, Vercel, Warp, Amp, and Kilo Code.

Technical limits **[2°]**:

- Requests must use the settings `store:false` and `stream:true`. The `temperature` setting is not allowed.
- On Plus, one 5-hour usage limit is shared across all apps.

Other OpenAI options:

- **Codex App Server:** an open protocol for building Codex, including its sign-in, into other products ([docs](https://learn.chatgpt.com/docs/app-server)).
- **Apps in ChatGPT:** a way to reach ChatGPT users. Recent reports say apps cannot sell digital goods inside ChatGPT **[2°]**.

### Google (AI Pro/Ultra)

**Short answer:** reusing the customer's Google login token in your own app is banned. Running Google's official command-line tool appears to be allowed.

- Google detects "using Gemini CLI oAuth with third-party software" ([GitHub](https://github.com/google-gemini/gemini-cli/discussions/22970)).
- In February 2026, Google banned AI Pro and Ultra subscribers who used OpenClaw ([WinBuzzer](https://winbuzzer.com/2026/02/23/google-bans-ai-subscribers-openclaw-no-refunds-xcxwbn/)).
- From 2026-06-18, Gemini CLI no longer served consumer plans. Google replaced it with Antigravity CLI, which is not open source.
- A forum answer (2026-09-07) said: "Spawning the official CLI locally using documented structured flags… for single-user workflows is permitted." It is **[unverified]** whether the person who answered works for Google ([forum](https://discuss.ai.google.dev/t/is-orchestrating-the-official-antigravity-cli-from-a-local-multi-agent-coding-application-allowed/181088)).

### GitHub Copilot

**Short answer:** unclear.

- The Copilot SDK became generally available on 2026-06-02. It is "available to all existing GitHub Copilot subscribers."
- It is **[unverified]** whether a commercial app may use its customers' Copilot plans.
- BrowserOS lets users sign in with their Copilot account.

### Business model options

1. **Run each company's official command-line agent.** The customer installs Claude Code, Codex, or Antigravity and signs in to it. AI usage costs us nothing, and we charge for running agents in parallel, cloud features, and team features. This is how Conductor works.
   - Policy has changed five or more times in nine months.
   - Usage limits are designed for "ordinary, individual usage," which may clash with many agents running in parallel.
   - Installing a command-line tool is hard for non-developers.
   - Vibe Kanban shut down because its users did not pay.
2. **Sign in with ChatGPT.** The best experience for consumers. Apply for the commercial trial now.
3. **Plug into Claude or ChatGPT** (an MCP server, a ChatGPT app, or a Claude plugin). The customer's subscription pays, but we lose control of the multi-agent screen.
4. **Customers bring their own API key.** Always allowed, but hard for non-developers.
5. **Sell our own credits.** Customers complain about this model more than any other.

**Suggested approach:** use options 1 and 2 by default. Offer clear, per-task billing on our own AI as a fallback.

## 4. Gaps in the market

1. **No product offers all four parts together:** easy for non-developers, agents running in parallel, the customer's existing subscription, and the customer's own logged-in browser.
2. **Customers worry about billing more than anything else in this category.** "Your existing subscription pays, and we show what each task costs" is a clear advantage.
3. **No review screen for browser work.** Coding tools show exactly what changed. Browser tools show nothing similar.
4. **Trust and safety on sites where the customer is logged in.** One customer lost their App Store Connect account (see quote 3 below). Bot protection, the systems websites use to block automated visitors, is the top reliability problem. Today, only products for large companies let you restrict which sites an agent may use or require confirmation before it acts.
5. **Working across AI companies.** Customers pay for several subscriptions. No single AI company will build a tool that routes each task to whichever plan has usage left.
6. **Show once, run many times.** Recording a workflow so an agent can repeat it exists only inside single companies' products. No product offers a library of reusable routines that works across agents.
7. **Threat:** the big AI companies are absorbing this space. Cowork and ChatGPT Work will probably add ways to manage several tasks.

## 5. What users say (exact quotes)

1. "Things like Claude in the browser are super slow, mostly because they just rely on the UI." ([HN, 2026-07-17](https://news.ycombinator.com/item?id=48945987))
2. "Whenever I dread logging in because I know the simple sounding task requires me to click through countless menus I use an agent browser. With confirmations of course. However, while the agent clicks through these (oftentimes dog slow) UIs I can do other things. Once it requires permission, I read, decide and act." ([HN, 2026-08-07](https://news.ycombinator.com/item?id=49215102))
3. "I was using Claude Cowork — Anthropic's research preview that controls your browser — to help fill out App Store Connect forms… About 24 hours later I got a termination letter citing 'fraudulent conduct'…" ([HN, 2026-03-03](https://news.ycombinator.com/item?id=47232860))
4. "Running 9 agents right now… The problem is you can't realistically review everything they do. But letting them run completely unchecked means you only find out something went wrong after it already happened." ([HN, 2026-03-18](https://news.ycombinator.com/item?id=47426071))
5. "Bot protections are obviously the biggest pain point and make these kind of autmations less reliable." ([HN, 2026-06-12](https://news.ycombinator.com/item?id=48509773))
6. "I built Unbrowse because browser automation for OpenClaw agents is absurdly slow." ([HN, 2026-02-03](https://news.ycombinator.com/item?id=46875336))
7. "But there are a lot of users who are not developers for whom that isn't a viable path." ([HN, 2026-01-26](https://news.ycombinator.com/item?id=46763716))
8. "Normal office work is wildly different from what we read about on HN… its a hard problem and yet I feel this is where the true money is." ([HN, 2026-07-02](https://news.ycombinator.com/item?id=48755616))
9. "Say I have an app (potentially a paid one) and want my users to use their Codex quota in it, is it permitted to do? As you can probably imagine that would unlock a lot of uses cases given smaller actors can't subsidize as much token costs" ([HN, 2026-04-21](https://news.ycombinator.com/item?id=47854328))
10. "If I pay $200/month for a Max subscription, I can access ALL of Anthropic's tools (CC, Design, Cowork, etc.). If I pay $200/month for API access, then the only thing I can use is the API." ([HN, 2026-04-22](https://news.ycombinator.com/item?id=47861761))
11. "I don't use Claude for my daily work anymore(due to OAuth restrictions on third party agents)" ([HN, 2026-08-15](https://news.ycombinator.com/item?id=49306978))
12. "I like conductor.build, they are doing amazing job, but I don't want to give up my freedom and get heavily reliant on closed source" ([HN, 2026-02-08](https://news.ycombinator.com/item?id=46936390))
13. "I find it slower than chatpgpt agent mode. And the pricing is not great for individual users." (about Manus; [HN, 2025-12-30](https://news.ycombinator.com/item?id=46429309))
14. "You get 750 tasks which get used up in 3 days with only two zaps (flows). Yet they advertise it as a monthly plan." (Zapier, [Trustpilot, 2026-09-21](https://www.trustpilot.com/review/zapier.com))
15. "After more than 7 hours, copilot could not make the appointment dates and times appear in plain English." (Zapier, [Trustpilot, 2026-07-16](https://www.trustpilot.com/review/zapier.com))
16. "…we'd burned through roughly 4,000 credits just setting up 4 tasks…The credits are black box. You have no idea how they get spent." (Lindy, [Trustpilot, 2026-03-15](https://www.trustpilot.com/review/lindy.ai))
17. "The pricing structure penalizing users with higher cost tokens for using more of the service forcing you to NOT want to use more." (Lindy, [Trustpilot, 2026-08-26](https://www.trustpilot.com/review/lindy.ai))
18. "I ran a prompt and spent 10k (yes, TEN THOUSAND) credits. Manus didn't follow the prompt I provided, ADMITTED IT" ([Trustpilot, 2026-09-07](https://www.trustpilot.com/review/manus.im))
19. "Paid $194.15 and received 44,073 credits. When the next billing cycle started, 31,132 unused credits expired." (Manus, [Trustpilot, 2026-10-06](https://www.trustpilot.com/review/manus.im))
20. "Unlimited chat has been removed and replaced with a weekly usage limit." (Genspark, [Trustpilot, 2026-09-18](https://www.trustpilot.com/review/genspark.ai))
21. "Launched with potential, got some funding and fell off. Current product is glitchy, has been lack of updates, and lack of AI integration." (Browse AI, [Trustpilot, 2026-04-16](https://www.trustpilot.com/review/browse.ai))

## Items not verified

- **Prices from only one secondary source:** Make, Gumloop, Genspark, Manus, Browse AI, and Kortix.
- **Product status:**
  - Browserbase Director: its site returned HTTP 429 (too many requests), so its current status is unknown.
  - Jules: whether consumers can still use it.
  - Gumloop and n8n: whether they have their own browser features.
- **How products and policies work:**
  - How Do Browser connects to a customer's subscription.
  - Whether Max API credits can be used in outside apps.
  - Whether the person who answered on Google's forum works for Google.
  - Whether GitHub Copilot's terms allow commercial apps to use customers' plans.
