# Source notes 01: AI-native browsers and browser agents from the big AI companies

These notes come from one research stream, gathered 2026-10-12. They describe the competitive picture as of October 2026.

**Caveats:**

- The web-search budget ran out partway through this stream. Some items have only one source and are tagged **[UNVERIFIED]** or **[CONFLICTING]**.
- Some sites blocked the fetch tool: OpenAI's help center, openai.com, theverge.com, TechNewsWorld and Neowin.
- Quotes came through a fetch tool. Check them against the live pages before you publish them.

## Headline takeaways

1. **The big AI companies are moving browser agents out of separate browsers and into their main assistant apps.**
   - OpenAI shut down ChatGPT Atlas on 9 Aug 2026, 292 days after launch. It also removed ChatGPT agent. In their place it offers ChatGPT Work (an assistant that runs on a remote computer with its own browser), a browser built into the ChatGPT desktop app, and a Chrome extension.
   - Google shut down Project Mariner on 4 May 2026. Its features moved into Chrome auto browse and Gemini Spark.
   - Microsoft retired Copilot Mode in its Edge browser in May 2026.
   - Dia, now owned by Atlassian, stopped selling its consumer Pro plan and turned to business customers.
2. **Every major AI company now has a "background agent" product that runs tasks in parallel.** Examples are Comet Background Assistants, Perplexity Computer, ChatGPT Work, Claude Cowork with Dispatch, and Gemini Spark. Each one runs only that company's model inside that company's app. No consumer product lets a user control ChatGPT, Claude and Gemini subscriptions from one dashboard.
3. **The best evidence for a "bring your own agent" approach is Opera Neon and BrowserOS.** Since 14 Aug 2026, Opera Neon has been free for any outside agent to control through MCP (Model Context Protocol, a standard way for AI apps to connect to tools). BrowserOS "neo" is open source. It runs agents in parallel and has a live dashboard and session replay. Both products are aimed at developers.
4. **Reliability is still the main problem on long, real-world tasks.** On the OSWorld 2.0 benchmark (long computer tasks), the best agent fully completed 20.6% of tasks at launch in June 2026. By September 2026 the best score was 44.3%. Reviewers who test the products by hand keep reporting the same failures: logins, CAPTCHAs, date pickers, and deceptive page designs ("dark patterns").
5. **Security is the main objection in the market.**
   - In December 2025, Gartner (a research and advisory firm) told company security chiefs to block AI browsers.
   - In June 2026, a University of Washington study found that Atlas, Gemini in Chrome, Claude for Chrome and Comet can all be tricked into bypassing the same-origin policy, the browser rule that stops one website from reading another site's data.
   - In March 2026, Zenity's "PleaseFix" attack took control of Comet through a calendar invite.

## 1. Competitor table

| Product | Company | Status / launch | Price / plan | Main agent features | Parallel / background? | Main complaints | Sources |
|---|---|---|---|---|---|---|---|
| **ChatGPT Work** (desktop app browser, cloud browser, Chrome extension) | OpenAI | Launched 9 Jul 2026 with the new ChatGPT desktop app. Available first to Pro, Enterprise and Edu, then Plus and Business. Reportedly reached 10M users in about 3 weeks **[Latent Space only]**. | Plus ($20) and above. Pro costs $100 or $200. Free and Go access: sources disagree **[CONFLICTING]**. Plus got a 5-hour usage cap back on 25 Aug 2026. | Runs on an always-on remote computer. Its Chrome-based cloud browser keeps you logged in between sessions, and the model never sees your passwords. A timeline replays every agent action. Uses helper agents and more than 1,000 plugins. A local mode in the desktop app can use your own files and programs. The Chrome extension only reads pages and starts tasks; it does not act on pages itself. | **Yes.** Runs several tasks and helper agents. Tasks can start on a schedule, on an event, or when a condition is met. Keeps working with your laptop off. Open bug: two parallel chats share one cloud browser. | Logins and CAPTCHAs fail. The manual takeover screen freezes. Does not work in Safari on Mac. The product and its documentation are confusing. Usage caps. Some sites block it through Cloudflare. | [VentureBeat 10 Jul 2026](https://venturebeat.com/orchestration/openai-introduces-chatgpt-work-a-cloud-based-ai-agent-that-manages-tasks-across-email-slack-and-calendars); [Latent Space 4 Aug 2026](https://www.latent.space/p/unpacking-chatgpt-work); [Simon Willison 30 Aug 2026](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/); [MacStories 26 Aug 2026](https://www.macstories.net/stories/hands-on-with-chatgpt-works-new-cloud-browser-feature/); [GitHub #41517](https://github.com/openai/codex/issues/41517); [9to5Mac 24 Aug 2026](https://9to5mac.com/2026/08/24/openai-restores-5-hour-codex-and-work-limits-for-chatgpt-plus-users/) |
| **ChatGPT Atlas** (closed); **ChatGPT agent** and **Operator** (retired) | OpenAI | Atlas launched 21 Oct 2025, on macOS only. Closure announced 9 Jul 2026; it closed 9 Aug 2026. Operator merged into ChatGPT agent in Jul 2025. ChatGPT agent was gone by Aug–Sep 2026 **[secondary sources]**. | Atlas was free. Agent mode needed Plus, Pro or Business. | Chat in a sidebar. Agent mode clicked and typed inside your own logged-in browser session. It remembered your browsing. | Ran one task at a time, in the foreground. | OpenAI said: "the browser is a feature, not the destination." Security flaws: LayerX's "Tainted Memories" attack and the University of Washington proof of concept. | [TechCrunch 9 Jul 2026](https://techcrunch.com/2026/07/09/openai-is-shutting-down-atlas-but-its-ai-browser-ambitions-are-still-growing/); [9to5Mac 9 Jul 2026](https://9to5mac.com/2026/07/09/openai-is-discontinuing-chatgpt-atlas-its-standalone-desktop-browser/); [Wikipedia](https://en.wikipedia.org/wiki/ChatGPT_Atlas) |
| **Perplexity Comet** (Comet Assistant, Background Assistants, Comet Plus) | Perplexity | Launched 9 Jul 2025 for Max subscribers. Free for everyone from 2 Oct 2025. Android Nov 2025, iOS Mar 2026, Enterprise Mar 2026. Monthly users: reports range from 3M–5M to 18M **[CONFLICTING]**. | Free. Comet Plus costs $5. Pro costs $20. **Background Assistants need Max ($200).** Enterprise costs $40 or $325 per seat. | A Chromium-based browser with a side-panel assistant that can see your tabs. Acts inside your real logged-in sessions. Enterprise version offers central device management and audit logs. | **Yes, Max only.** A "mission control" dashboard runs several assistants at once. You can step in or take over. | Security: the CometJacking attack, the PleaseFix attack, and the University of Washington study. The free tier collects browsing data for ads. Amazon sued Perplexity: a court blocked Comet in Mar 2026, an appeals court lifted that block on 4 Aug 2026, and a rehearing was denied on 10 Sep 2026. | [TechCrunch 2 Oct 2025](https://www.techcrunch.com/2025/10/02/perplexitys-comet-ai-browser-now-free-max-users-get-new-background-assistant/); [eesel 9 Jun 2026](https://www.eesel.ai/blog/perplexity-comet-pricing); [Jones Day Sep 2026](https://www.jonesday.com/en/insights/2026/09/ninth-circuit-vacates-cfaa-injunction-against-perplexitys-comet-ai-agent); [CyberScoop 3 Mar 2026](https://cyberscoop.com/agentic-ai-browsers-allow-hijacking-zenity-labs-comet/) |
| **Perplexity Computer** | Perplexity | Launched 25 Feb 2026. Added to Pro with lower limits in Mar 2026. | Max ($200) includes credits. Pro ($20) has reduced limits. You can buy more credits as you go. | Runs on a remote computer with a real browser and file system. Coordinates 19 AI models. | **Yes.** "Run dozens of Perplexity Computers in parallel." | You cannot see what it is doing. One web project used $200 of credits. Links to other services are buggy. | [Perplexity blog 25 Feb 2026](https://www.perplexity.ai/hub/blog/introducing-perplexity-computer); [Builder.io 4 Mar 2026](https://www.builder.io/blog/perplexity-computer) |
| **Claude in Chrome** | Anthropic | Test version Aug 2025. **Generally available 26 Aug 2026** on every paid plan. Since 12 Aug 2026 its side panel opens a full Cowork session. Works in desktop Chrome only. | Pro ($20), Max ($100 or $200), Team, Enterprise. Enterprise admins can allow or block sites. | Clicks, types and fills forms in your real Chrome, using your existing logins. Can act without asking (with a safety checker) or ask before acting on each site. | **Partly.** You can "start a workflow and move on," but there is no dashboard for several agents. | Usage limits on Pro. Chrome only. Anthropic reports these prompt-injection attack success rates: 0% for Sonnet 5, Opus 5 and Mythos 5 with safeguards on; 0.3% for Fable 5; 3.8% for Opus 5 with safeguards off. The test version had a 2.8-star store rating **[UNVERIFIED]**. | [Anthropic 26 Aug 2026](https://claude.com/blog/claude-in-chrome-generally-available); [9to5Mac 12 Aug 2026](https://9to5mac.com/2026/08/12/claude-cowork-chrome/) |
| **Claude Cowork** (desktop agent with a built-in browser) | Anthropic | Test version 12 Jan 2026. Generally available 9 Apr 2026. Scheduled tasks 25 Feb 2026. Dispatch (send tasks from your phone) 17 Mar 2026. Cloud sessions on web and mobile 7 Jul 2026. **Built-in browser 26 Aug 2026.** | All paid plans. | Works with your local files and apps. Its built-in browser runs in an isolated local Chromium. You import logins one site at a time. Banking, email and company-login (SSO) sites are excluded by default. Asks for permission the first time it uses each site. | **Yes.** Tasks you queue "genuinely run in parallel." Also scheduled tasks and Dispatch. The built-in browser needs the desktop app open and online. | Uses up tokens fast. "Not fully reliable for critical workflows." Importing logins one site at a time is tedious. | [AIToolsReview Oct 2026](https://aitoolsreview.co.uk/insights/claude-cowork-browser); [Kingy AI 26 Aug 2026](https://kingy.ai/news/claude-cowork-built-in-browser-web-automation/); [Automaton 31 Jul 2026](https://automatonagency.com/insights/claude-cowork-mobile-and-web); [LowCode 28 Sep 2026](https://www.lowcode.agency/blog/claude-cowork-review) |
| **Gemini in Chrome and auto browse** | Google | Gemini in Chrome: free in the US since Sep 2025. **Auto browse launched 28 Jan 2026** for US AI Pro and Ultra subscribers. Rolled out to Android users in the US on 18 Aug 2026. | Auto browse needs AI Pro ($19.99) or Ultra. There is a daily limit on tasks (one source says 20 per day on Pro and 200 on Ultra **[CONFLICTING]**). US only. | Works in a new tab on your computer. Uses Google Password Manager. Stops and asks before purchases, social media posts and entering passwords. | **Yes, with limits.** Runs in a background tab. Can run several tabs at once. | US only. Vulnerable to prompt injection. Fails on deceptive designs, for example when you try to cancel a subscription. | [9to5Google 28 Jan 2026](https://9to5google.com/2026/01/28/chrome-gemini-auto-browse/); [9to5Google 18 Aug 2026](https://9to5google.com/2026/08/18/gemini-chrome-android-us/); [Sean Kim 20 May 2026](https://blog.imseankim.com/chrome-auto-browse-gemini-agentic-hotel-form-fill-google-io-2026/) |
| **Gemini Spark** (replaced Gemini Agent; took over Project Mariner) | Google | Announced at Google I/O, May 2026. Reached US AI Pro subscribers 27 Jul 2026. Since 30–31 Jul 2026 it can control the Chrome on your own computer. **Mariner shut down 4 May 2026.** | AI Pro ($20, US) and Ultra. Not available in the EU, UK, Switzerland or Nigeria. | Runs 24/7 on temporary remote computers. Uses your signed-in Chrome and saved passwords. Hands control back to you when a decision is needed. | **Yes.** Several tasks at once, plus scheduled jobs. | Not available in the EU. No published reliability data. | [Chromeunboxed 27 Jul 2026](https://chromeunboxed.com/googles-agentic-ai-gemini-spark-is-now-available-on-the-20-pro-tier-in-the-us/); [PiunikaWeb 31 Jul 2026](https://piunikaweb.com/2026/07/31/google-gemini-spark-chrome-integration/); [GIGAZINE 7 May 2026](https://gigazine.net/gsc_news/en/20260507-google-shuts-down-project-mariner/) |
| **Edge "Browse with Copilot"** | Microsoft | Copilot Mode launched Jul 2025 and **was retired 13 May 2026**. Browse with Copilot is broadly available. | Needs Microsoft 365 Premium. US only. Usage limits apply. | Takes actions in Edge, such as making reservations, unsubscribing and filling forms. | Not documented. | Narrow availability. The product's name and approach keep changing. | [Edge blog 13 May 2026](https://blogs.windows.com/msedgedev/2026/05/13/new-updates-to-edge-across-desktop-and-mobile/) |
| **Opera Neon** | Opera | Generally available 11 Dec 2025. MCP connector added 31 Mar 2026. **Free for outside agents from 14 Aug 2026.** | Free: browser, MCP connector and command-line tool. Neon's own agents cost $19.90 per month. | Its own agents keep working on a remote computer while you are offline. Outside agents such as Claude, ChatGPT, n8n and OpenClaw can control Neon using your logged-in sessions. | **Yes.** "Multiple simultaneous projects." | Date pickers break it. Supervising the agent takes longer than doing the task yourself. | [Opera 31 Mar 2026](https://press.opera.com/2026/03/31/opera-neon-adds-mcp-connector/); [Opera 14 Aug 2026](https://blogs.opera.com/news/2026/08/your-ai-agents-can-use-opera-neon-free-of-charge/); [Chris Chinchilla 4 Mar 2026](https://chrischinchilla.com/blog/2026/opera-neon/) |
| **Dia** and **Arc** | The Browser Company (owned by Atlassian) | Atlassian completed its purchase for $610M in Oct 2025. **Dia Pro was discontinued by May 2026** **[CONFLICTING]**. Dia is now aimed at business customers. A Windows version launched 7 Oct 2026, without agent features. Arc stopped getting new features in May 2025. | Free tier. Business plans. | Mostly chat across your open tabs, plus links to work apps. Takes little action on pages by itself. | No. | Consumer users were left behind. | [PiunikaWeb 15 May 2026](https://piunikaweb.com/2026/05/15/dia-appears-to-be-quietly-phasing-out-its-pro-subscription/); [PiunikaWeb 7 Oct 2026](https://piunikaweb.com/2026/10/07/dia-browser-windows-launch/) |
| **Genspark AI Browser** (Autopilot) | Genspark | Launched 2025. Reportedly $250M in annual revenue and a $2.6B valuation (Jun 2026) **[secondary sources]**. | Pay with credits. | Autopilot mode browses, fills forms and adds items to carts. Over 700 tool integrations. | Not documented. | Uses credits fast. Autopilot gives up on tasks halfway. Handles about 60–70% of simple tasks well. | [Layer3Labs 24 Sep 2026](https://www.layer3labs.io/guides/genspark-ai-review) |
| **Fellou** | Fellou | Launched May 2025. Quiet in 2026. | Free tier. Paid plans cost $19–$199 per month. | "Deep Action" agents work across tabs. You can edit the plan before it runs. Shows the credit cost before you start. | **Yes.** Runs in a hidden background workspace. Can schedule tasks. | Gets stuck in loops. "CAPTCHA pages were a complete blocker." | [The Tool Nerd 2 Oct 2025](https://www.thetoolnerd.com/p/fellou-review-agentic-browser-thetoolnerd) |
| **Sigma AI Browser** | Sigma | Active. | Free (company claim). | AI models run on your own computer. | Not documented. | Slow. Most information comes from the company itself **[UNVERIFIED]**. | [Composite 10 Apr 2026](https://composite.com/blog/tested-top-ai-native-browsers-whats-changed) |
| **Brave Leo "AI browsing"** | Brave | You must turn it on in settings. Available in all versions since 5 May 2026. | Free. | Uses a **separate browser profile** with its own cookies and logins. A second model checks each action. | No. | By design it cannot use your logged-in accounts. Still early. | [Brave blog](https://brave.com/blog/ai-browsing/) |
| **Manus** (Browser Operator extension, "My Computer" desktop app) | Manus | Meta bought Manus in Dec 2025. China blocked the deal in Apr 2026. Manus became **independent again on 1 Sep 2026**. User data in affected regions was deleted 23–24 Aug 2026. | Free plan: **1 task at a time**. Paid plans cost $20–$200 per month. Team plan costs $20 per seat. | Long tasks on a remote computer. A browser extension controls your local browser. | **Yes.** How many tasks can run at once depends on your plan. | Uses credits fast. The ownership changes caused data loss. | [Wikipedia](https://en.wikipedia.org/wiki/Manus_(AI_agent)); [Codersera 25 May 2026](https://codersera.com/blog/manus-ai-2026-status-meta-block-desktop-app/) |
| **BrowserOS and "neo"** (open source) | BrowserOS (Y Combinator, summer 2024) | Active. 13.9k GitHub stars. | Free and open source. | You bring your own API keys or local models. "neo" is a second browser just for agents. It imports your Chrome logins and works with Claude Code, Codex and Cursor through MCP. | **Yes.** Runs agents in separate tabs, with a live dashboard and session replay. | Made for developers. | [GitHub](https://github.com/browseros-ai/BrowserOS); [Hacker News 22 Jan 2026](https://news.ycombinator.com/item?id=46721474) |
| Others to watch | — | Firefox Smart Window (test version, Sep 2026). Samsung Internet with Perplexity. Composite (Chrome extension). Yurei (Chrome extension that lets any MCP-connected agent use your Chrome). Cloudflare Kitesurf (a browser built for agents). | — | — | — | — | [nohacks 27 Sep 2026](https://nohacks.co/blog/agentic-browser-landscape-2026) |

## 2. Market signals

**Separate AI browsers are failing. Agents are becoming features of existing apps.**
- OpenAI closed Atlas after 292 days. It said: "the browser is a feature, not the destination."
- Google shut down Project Mariner.
- Microsoft retired Copilot Mode in Edge.
- Dia stopped selling its consumer Pro plan.
- Opera made Neon a free host for outside agents.

**AI-first browsers are a tiny share of the browser market.**
- Together they have **2.66% or less** of global browser sessions (Statcounter data, Jul 2026). [Axis Intelligence, 12 Aug 2026](https://axis-intelligence.com/browser-market-share-statistics/)
- Chrome has about 69–71% of the market. Its roughly 3B users now get auto browse built in.

**AI assistants reach a very large audience.**
- ChatGPT had 900M weekly active users in Feb 2026.
- ChatGPT Work reportedly had 10M users within about 3 weeks **[UNVERIFIED]**.
- Anthropic says **more than 90% of Cowork usage is by non-developers** **[secondary source]**. [Automaton, 31 Jul 2026](https://automatonagency.com/insights/claude-cowork-mobile-and-web)

**Comet has no reliable user numbers.** Reported figures are 3–5M, 10M and 18M monthly users **[CONFLICTING]**.

**Employees adopted these tools before companies approved them.**
- Shortly after launch, 27.7% of companies had at least one employee who had downloaded Atlas.
- Atlas had 62 times more downloads at companies than Comet. [Cyberhaven](https://www.cyberhaven.com/blog/browser-agent-security-risk-chatgpt-atlas)

**Agent startups make real revenue, but it depends on credits.**
- Manus had about $125M in annual revenue by Dec 2025.
- Genspark reportedly had $250M in annual revenue.

**Analysts warn against these tools, and security incidents keep happening.**
- Gartner: "CISOs must block all AI browsers in the foreseeable future."
- Gartner predicts that more than 40% of agent projects will be cancelled by 2027.
- University of Washington (30 Jun 2026): 4 of 7 AI browsers can be tricked into bypassing the same-origin policy.
- Zenity's PleaseFix attack.
- LayerX's "Tainted Memories" attack.

**Courts are leaning toward allowing agents.**
- An appeals court ruled that "it is the user who 'accesses'" a website through an agent.
- eBay's terms now ban orders placed without human review.

**Websites are adapting to agents.**
- Google proposed WebMCP, a way for websites to offer actions directly to agents.
- McKinsey (a consulting firm) projects that shopping done by agents could reach $1T by 2030.

**Usage limits frustrate users.**
- ChatGPT Plus has a 5-hour usage cap.
- Chrome auto browse has a daily task limit.
- The Manus free plan runs only 1 task at a time.

**All the big products now run agents in parallel and in the background, but each one works only with its own company's AI.**
- On Hacker News, the discussion "What should the GUI for AI agents look like?" got 139 points and 85 comments (31 Jul 2026). [HN](https://news.ycombinator.com/item?id=49119274)

## 3. How reliable browser agents really are

| Benchmark | What it measures | Latest numbers | Notes |
|---|---|---|---|
| **OSWorld 2.0** (Jun 2026) | 108 long computer tasks. A human takes about 1.6 hours per task. | At launch, the best agent (Opus 4.8) fully completed **20.6%** of tasks. GPT-5.5 completed about **13%**. By 17 Sep 2026, **Opus 5** fully completed **44.3%** and partly completed 77.7%. | Agents fail because they "lose track of constraints, miss information that arrives mid-task, guess rather than ask the user, and skip verification." [arXiv](https://arxiv.org/abs/2606.29537) |
| **OSWorld-Verified** (version 1.0) | 369 computer tasks. Humans score 72.36%. | Top AI models now beat the human score **[UNVERIFIED]**. | The benchmark is close to its ceiling. |
| **Online-Mind2Web** | 300 tasks on 136 live websites. | In 2025, Operator scored 61.3% and most agents scored about 30%. By 2026, specialist agents report 97–99%. | The top scores come from specialist agent companies, not consumer products. |
| **WebArena** | 812 tasks on copies of real websites. Humans score 78.24%. | The best agents score about 71.6–74.3% **[UNVERIFIED]**. | |
| **BrowseComp** | Searching for facts that are hard to find. | Opus 5 scored 90.8% **[UNVERIFIED]**. | Tests research, not taking actions. |

**Limits of these benchmarks:**
- In April 2026, UC Berkeley researchers built an agent that scored close to 100% on 7 of 8 major benchmarks without solving the tasks. On WebArena, it simply read the answer files.
- A July 2026 study found that 15.3% of the "failed" scores on these benchmarks were wrong.
- Errors add up over many steps. If an agent gets each step right 90% of the time, it completes a 10-step task only about 35% of the time.

**Hands-on tests by reviewers:**
- **Chrome auto browse** completed **4 of 5** real tasks. It **failed to cancel a subscription** because of deceptive page design.
- **ChatGPT Work's cloud browser** did not work in Safari on Mac. CAPTCHAs blocked logins, and the manual takeover screen froze.
- **Opera Neon** failed on date pickers and sometimes switched to German.
- **Perplexity Computer** used $200 of credits while stuck in a loop without telling the user.
- **Genspark** handles about 60–70% of simple tasks.
- **Fellou**: CAPTCHAs blocked it completely.

**Bottom line:** Agents now usually succeed at short tasks on a single site when the user confirms the result at the end. Long tasks still need someone watching. So do logins, CAPTCHAs, unusual page controls and deliberately hostile pages. Reviewers' most common complaint is the time it takes to supervise the agent.

## 4. Gaps a separate multi-agent app could fill

1. **One dashboard for agents from different AI companies.** Every company's parallel-agent product works only with its own AI. A user who pays for ChatGPT Plus and Claude Pro gets two separate task lists, two approval flows and two usage meters. The only browsers that accept outside agents (Opera Neon, BrowserOS neo, Yurei) require MCP or command-line skills.
2. **Monitoring and approvals.** Today these are weak or cost a lot:
   - Comet's dashboard requires the $200 Max plan.
   - With Perplexity Computer you cannot see what the agent is doing.
   - Parallel ChatGPT Work chats share one browser.
   - The gap is one inbox where the user can watch every agent live, review a timeline, replay sessions, approve actions in one queue, and get notifications.
3. **Keeping logins while running in parallel.** Cloud browsers can run many agents at once, but logins fail there. Local agents keep your logins, but they are tied to one browser. The gap is a desktop app that gives each agent its own isolated browser profile with saved logins and runs it in the background. It would hand the task cleanly to the user for two-step login codes or CAPTCHAs. BrowserOS neo comes closest, but it is made for developers.
4. **Help with subscription usage limits.** Usage caps make users angry. The gap is a scheduler that knows each subscription's limits. It would queue tasks, slow them down when needed, use whichever subscription has capacity left, resume after limits reset, and show the expected cost before a run.
5. **Helping tasks finish.** The common failures are predictable. No consumer product offers task recipes, checks that confirm a task succeeded, or a clear "you do this step" handoff.
6. **Safety controls that ordinary users can understand.** Examples: a separate browser profile for each agent, a list of allowed sites, a read-only mode, an activity log, and a rule never to submit forms without asking.
7. **Protection when products shut down.** Atlas, Mariner, Copilot Mode, Dia Pro and ChatGPT agent all shut down, and Manus deleted user data. The gap is saving workflows in a format that does not depend on any single AI company.
8. **Regional and platform limits.** Many of these products work only in the US, only on Mac, or only in Chrome. The gap is an app that works on Windows and outside the US.
9. **Schedules that span several AI companies.** Today each company's scheduler works only with its own agents.
10. **Risk to check first.** The "bring your own subscription" approach depends on whether each AI company allows outside apps to use its consumer plans. This has not been verified.

## 5. Verbatim quotes

1. "In its current form, the idea of having ChatGPT Work browse signed-in websites on your behalf is better than its implementation." — John Voorhees, [MacStories, 26 Aug 2026](https://www.macstories.net/stories/hands-on-with-chatgpt-works-new-cloud-browser-feature/)
2. "However, getting past the initial login screen is still too frustrating." — MacStories, 26 Aug 2026
3. "Other times, the cloud browser asked me to take over manually, but I was unable to do so because the UI was frozen or login panels didn't appear." — MacStories, 26 Aug 2026
4. "It is an extraordinarily confusing and very powerful product." — [Simon Willison, 30 Aug 2026](https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/)
5. "Figuring this all out took way more work than it should have." — Simon Willison, 30 Aug 2026
6. "The time spent supervising the assistant and correcting errors often exceeds the time saved through automation." — [Chris Chinchilla on Opera Neon, 4 Mar 2026](https://chrischinchilla.com/blog/2026/opera-neon/)
7. "Date pickers emerged as the assistant's biggest weakness, which is odd as 'booking a trip' is often the example companies use to demonstrate assistant tools." — Chris Chinchilla, 4 Mar 2026
8. "A non-developer would have burned through credits indefinitely, with zero signal that something fundamental was broken underneath." — [Alice Moore, Builder.io, 4 Mar 2026](https://www.builder.io/blog/perplexity-computer)
9. "Everything happens inside a cloud sandbox with no window in." — Builder.io, 4 Mar 2026
10. "Two days. One page. $200 in compute credits (on top of the subscription)." — Builder.io, 4 Mar 2026
11. "Chrome auto browse is the first agentic AI feature that clears the bar of 'useful enough that a non-developer keeps it on.'" — [Sean Kim, 20 May 2026](https://blog.imseankim.com/chrome-auto-browse-gemini-agentic-hotel-form-fill-google-io-2026/)
12. "hand it back. Subscription cancellation flows are deliberately hostile UX, full of dark patterns and unlabeled buttons." — Sean Kim, 20 May 2026
13. "Multiple tasks genuinely run in parallel, and you can move between them without disruption." — [Christian Pean on Claude Cowork, 24 Jan 2026](https://techysurgeon.substack.com/p/the-6-am-dispatch-how-i-use-claude)
14. "Claude makes PowerPoints, drafts emails, organizes files. All of it needs human review." — Techy Surgeon, 24 Jan 2026
15. "Browser agents aren't ready for the public." — [David Kohlbrenner, University of Washington, 30 Jun 2026](https://www.washington.edu/news/2026/06/30/some-agentic-ai-browsers-come-with-major-cybersecurity-risks-uw-study-finds/)
16. "After 30 years of building up this same-origin policy, this is a big step back for browser security." — Franziska Roesner, University of Washington, 30 Jun 2026
17. "CISOs must block all AI browsers in the foreseeable future to minimize risk exposure." — Gartner, via [Thurrott, 8 Dec 2025](https://www.thurrott.com/a-i/330524/gartner-all-ai-browsers-should-be-blocked-for-foreseeable-future)
18. "The agent is persuaded that what the user actually asked for is what the attacker desires." — [Stav Cohen, Zenity Labs, 3 Mar 2026](https://cyberscoop.com/agentic-ai-browsers-allow-hijacking-zenity-labs-comet/)
19. "This draconian 5-hour rolling cap completely bricked my project mid-sprint" — [Hacker News user kylecorpin, 26 Aug 2026](https://news.ycombinator.com/item?id=49432879)
20. "I want to follow along as all the different sub-agents and tool calls do their work." — [Hacker News user bmurphy1976, 31 Jul 2026](https://news.ycombinator.com/item?id=49119274)
21. "In my experience, claude cowork has been pretty much useless." — [Hacker News user johnwheeler, 9 Jul 2026](https://news.ycombinator.com/item?id=48849059)
22. "Two parallel ChatGPT Work chats under the same account appeared to use one shared Cloud Browser surface without explicit cross-chat ownership or isolation." — [GitHub #41517, 29 Aug 2026](https://github.com/openai/codex/issues/41517)
23. "Agentic browsing is also inherently dangerous." — [Brave](https://brave.com/blog/ai-browsing/)
24. "CAPTCHA pages were a complete blocker." — [The Tool Nerd on Fellou, 2 Oct 2025](https://www.thetoolnerd.com/p/fellou-review-agentic-browser-thetoolnerd)

## Unverified or conflicting items

- Comet's monthly users.
- ChatGPT Work's 10M users, and whether Free and Go users can use it.
- The removal of ChatGPT agent (OpenAI's help center was blocked).
- Daily task limits for auto browse.
- The price of Google AI Ultra.
- Dia Pro's status.
- Genspark's and Fellou's product details.
- Claims about Sigma.
- Claude in Chrome's 2.8-star rating.
- Benchmark scores reported by AI companies.
- Each AI company's current terms for outside apps that use a consumer subscription.
