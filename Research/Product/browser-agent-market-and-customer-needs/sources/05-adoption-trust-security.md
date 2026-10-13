# Source notes 05: adoption, trust, security, and platform pushback

These are the raw findings from one research stream, gathered 2026-10-12. They cover the size of the customer pool, how many people use agents, how much users trust agents, security research, and how websites push back on agents.

**Caveats:**
- The web-search budget ran out partway through this stream. Some areas are thinly covered; see "Unverified items and gaps" below.
- The quotes came through a fetch tool that summarizes pages. Check the exact wording against the source before you publish any quote.
- Confidence labels follow the customer-research skill: [HIGH] means 3 or more independent sources, [MEDIUM] means 2 sources, and [LOW] means 1 source.

## Key numbers

| Metric | Value | Date | Source URL |
|---|---|---|---|
| ChatGPT weekly active users | 900M (up from 800M in Oct 2025) | Feb 27, 2026 | https://techcrunch.com/2026/02/27/chatgpt-reaches-900m-weekly-active-users |
| ChatGPT paying subscribers | 50M (OpenAI disclosure) | Feb 27, 2026 | same |
| ChatGPT paying subscribers (earlier) | ~35M | Jul 2025 (per The Information) | https://the-decoder.com/chatgpt-agent-reportedly-lost-75-of-its-users-because-nobody-knew-what-it-was-actually-for/ |
| ChatGPT Agent weekly active paying users | ~4M at the launch peak, then under 1M "within months" (a drop of about 75%) | Reported Jan 29, 2026 | same |
| Claude paid subscriptions | "More than doubled" in 2026. No absolute number given. | Mar 29, 2026 | https://www.unite.ai/claude-paid-subscriptions-more-than-double-as-consumer-momentum-builds/ |
| Paid subscriber growth, year over year | Claude +200%, Gemini +258%. ChatGPT has about 8 times Claude's subscribers and about 4 times Gemini's. | Jan 2026 data (published Mar 9, 2026) | https://a16z.com/100-gen-ai-apps-6/ |
| Gemini app monthly active users | Over 1B. Paid AI Plus/Pro/Ultra subscribers are **not disclosed**. | Aug 11, 2026 | https://www.implicator.ai/google-puts-gemini-at-1-billion-monthly-users-without-naming-paying-subscribers/ |
| Perplexity paid subscribers | **Not disclosed.** One third-party estimate says 1.5M–3M (unverified). | Aug 2026 | https://www.sentisight.ai/how-many-paid-subscribers-perplexity/ |
| US adults who use AI / use it daily | 64% / 25% | Survey Jul 2026; published Sep 16, 2026 | https://menlovc.com/perspective/2026-the-state-of-consumer-ai/ |
| US AI users who pay for at least one AI product | 55% (about 90M Americans). 34% of payers say family or friends pay. About 20% say an employer or school pays. | Sep 16, 2026 | same |
| AI users who tried an agent / use one regularly | 41% / 24% | Sep 16, 2026 | same |
| AI users who let AI act without final approval | 32% | Sep 16, 2026 | same |
| Agent users who gave an agent access to a web browser / financial accounts | 33% / 20% | Sep 16, 2026 | same |
| Agent use among payers vs non-payers | 65% vs 13%. 92% of agent users pay. | Sep 16, 2026 | same |
| US adults who use AI chatbots | 49%. ChatGPT 44%, Gemini 24%, Copilot 17%, Claude 6%. | Fieldwork Feb 17–23, 2026; published Jun 17, 2026 | https://thenextweb.com/news/pew-research-americans-ai-chatbot-skepticism-regulation-distrust-2026 |
| US ChatGPT use by age | Ages 18–29: 61%. Ages 30–49: 55%. Ages 50–64: 37%. Ages 65+: 19%. | Feb 2026 | https://www.pewresearch.org/chart/chatgpt-tops-the-list-of-chatbots-americans-use-across-age-groups/ |
| ChatGPT messages that are not about work / that are about coding | Over 70% (73% in Jun 2025) / 4.2% | Sep 2025 | https://www.nber.org/papers/w34255 ; https://www.theregister.com/2025/09/16/chatgpt_usage_study/ |
| Claude.ai conversations about computer and math tasks | 34% (Nov 2025; the peak was 40% in Mar 2025). Split: 46% work, 35% personal, 19% coursework. | Jan 15, 2026 | https://www.anthropic.com/research/anthropic-economic-index-january-2026-report |
| Comet Assistant (Perplexity's browser agent) query mix | 55% personal, 30% professional, 16% educational | Dec 8, 2025 | https://arxiv.org/abs/2512.07828 |
| Consumers willing to delegate, by level (n=25,590, 16 countries) | 85% will work together with AI. 74% will let AI do a specific task. 32% will let AI decide if they approve the payment. 9% will let AI buy on its own. Only 12% accept AI acting alone at the payment step. | Survey Jan 2026 | https://www.accenture.com/ma-en/insights/consulting/talk-my-ai-agent |
| Consumers not comfortable letting an agent complete a purchase | 55%. 73.9% expect a biometric check or a one-time code for every agent transaction. | Q1 2026 (reported Jul 17, 2026) | https://forkast.news/73-use-ai-for-shopping-55-wont-let-it-buy-anything-the-trust-gap-is-widening/ |
| Comfortable with AI booking travel, with vs without final approval | 43% vs 12%. Only 18% trust AI with payment information. | Survey Feb 2026; published Jun 2, 2026 | https://ppc.land/americans-warm-to-ai-travel-planning-but-wont-hand-over-the-wallet/ |
| US consumers willing to let AI make purchase decisions | 11% | Survey Jan 2026; published May 27, 2026 | https://www.01net.it/gartner-survey-finds-consumers-want-ai-shopping-help-but-not-ai-purchase-decisions/ |
| Claude for Chrome prompt-injection attack success rate | 23.6% with no defenses, 11.2% with defenses (123 tests) | Aug 25, 2025 | https://claude.com/blog/claude-for-chrome |
| Opus 4.5 browser attack success rate (Anthropic's own test) | 1% (an attacker that adapts, 100 attempts) | Nov 24, 2025 | https://www.anthropic.com/research/prompt-injection-defenses |
| Opus 4.5 attack success rate (Gray Swan's independent benchmark) | 4.7% at 1 attempt, 33.6% at 10 attempts, 63% at 100 attempts | Nov 25, 2025 | https://the-decoder.com/claude-opus-4-5-resists-prompt-injections-better-than-rivals-but-still-falls-to-strong-attacks-alarmingly-often/ |
| Claude in Chrome at general availability (Anthropic's own figures) | 0% attack success for Sonnet 5 and Opus 5 with all defenses on. 0.3% for Fable 5. Opus 4.5 scored 17.6% on the newer, stronger test. | Aug 26, 2026 | https://claude.com/blog/claude-in-chrome-generally-available |
| Malicious prompt-injection content on the open web | Up 32% (relative increase in Google's crawl data) | Nov 2025 to Feb 2026; published Apr 24, 2026 | https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/ |
| Share of HTML web requests made by bots | Bots 57.5%, humans 42.5% (Cloudflare) | Jun 3, 2026 | https://www.hothardware.com/news/ai-bots-are-now-dominating-the-web |
| ChatGPT Atlas lifespan | Launched Oct 21, 2025. Shut down Aug 9, 2026. | Shutdown announced Jul 9, 2026 | https://9to5mac.com/?p=1060224 |
| Enterprises using agents (McKinsey) | 23% scaling agents, 39% experimenting | Survey Jun–Jul 2025 | https://rajnandan.com/posts/mckinsey-state-of-ai-2025-analysis/ (secondary summary) |
| Large US firms (KPMG) | 62% are building or deploying agents. 49% ban autonomous decisions in high-risk use cases. | Sep 24, 2026 | https://kpmg.com/us/en/media/news/q3-ai-pulse-2026.html |
| Executive trust in fully autonomous agents (Capgemini) | Fell from 43% to 27% in one year. 2% have deployed agents at scale. | 2025 (page not dated) | https://www.capgemini.com/insights/research-library/ai-agents/ |
| Adults aged 50+ (AARP) | 80% have used some AI. 51% think AI is insecure or unsafe. 42% call themselves beginners. | Jan 2026 | https://datastories.aarp.org/2026/navigating-the-world-of-ai/ |
| Blind users of a computer-use agent built for screen readers | Best task success rate was 52.5% (GPT-5). 8 users, 1,258 commands. | Sep 1, 2026 | https://arxiv.org/abs/2609.00524 |
| US businesses using AI (Census survey) | 17–20%. No significant change for firms with fewer than 20 employees. | May 26, 2026 | https://census.gov/library/stories/2026/05/ai-use-businesses.html |
| Small businesses using generative AI (US Chamber of Commerce) | 58% (up from 40% in 2024) | Aug 18, 2025 | https://www.uschamber.com/technology/artificial-intelligence/u-s-chambers-latest-empowering-small-business-report-shows-majority-of-businesses-in-all-50-states-are-embracing-ai |
| Amazon v. Perplexity | A court injunction against Comet was granted in Mar 2026. The Ninth Circuit canceled it on Aug 4, 2026. | Aug 4, 2026 | https://www.pearlcohen.com/ninth-circuit-vacates-injunction-against-perplexitys-ai-shopping-agent/ |

## 1. The customer pool

- **[HIGH] The pool of paying users is large, and ChatGPT dominates it.**
  - OpenAI reported 50M paying subscribers and 900M weekly users on Feb 27, 2026.
  - a16z data from January 2026 puts ChatGPT at about 8 times Claude's subscriber count and about 4 times Gemini's.
  - Caution: every outlet that reports the 50M figure traces it back to the same single OpenAI disclosure.
  - Two other figures are **unverified**: about 1B weekly users in July 2026, and a forecast of 122M paying subscribers by the end of 2026 (mostly on the $8 "Go" plan).
- **[MEDIUM] Claude and Gemini are growing fast, but neither company discloses subscriber counts.**
  - Anthropic says Claude's paid subscriptions "more than doubled" in 2026, mostly on the $20 Pro plan. a16z shows +200% year over year.
  - Gemini passed 1B monthly users, but Google does not say how many people pay.
  - Perplexity has never published a subscriber number.
  - No subscriber data was found for Copilot Pro.
- **[LOW] Menlo's 2026 report says 55% of US AI users pay for AI.** This definition is broad. It counts plans that family or friends pay for (34%) and plans that an employer or school pays for (~20%). Menlo's 2025 report said only about 3% pay, using a different definition. Do not compare the two numbers as a trend.
- **[HIGH] Most paying and heavy users are not developers.**
  - Only 4.2% of ChatGPT messages are about coding. More than 70% are not about work.
  - ChatGPT messages split into 49% asking for information, 40% asking it to do something, and 11% expressing something (NBER).
  - Pew found that 44% of US adults have used ChatGPT, compared with 6% for Claude.
  - Claude.ai is more technical: 34% of its conversations are about computer and math tasks (Anthropic Economic Index).
- **[HIGH] Users skew young, wealthier, and more educated.**
  - By age, 61% of 18–29-year-olds use ChatGPT, but only 19% of people 65 and older do (Pew).
  - Adoption is 77% in households that earn $100K or more, but 56% in households that earn under $50K (Menlo).
  - Parents adopt more than non-parents: 84% vs 56% (Menlo).
  - Big spenders pay $100 or more per month. They are 14% of payers but 60% of spending, and they skew toward tech and finance workers with graduate degrees (Menlo).
  - Nearly half of ChatGPT messages come from users under 26. The gender gap has mostly closed (NBER).
- **[MEDIUM] People already use AI for many tasks that happen in a browser** (Menlo, 2026):
  - Among shoppers who use AI: 50% use it to compare products, and 26% use it to complete purchases.
  - Among all AI users: 47% use it to draft email, 23% to pay bills, and 23% to navigate healthcare.
  - 48% of AI users earn money with AI. This is 62% of Gen Z but only 15% of Boomers.
- **[LOW] Microsoft and LinkedIn's Work Trend Index 2026** (from secondary summaries only) rates knowledge workers who use AI as 19% "Frontier" and 50% "Emergent" in readiness.

## 2. Agent adoption and usage

- **[MEDIUM] Most agent users are people who already pay for AI** (Menlo, 2026).
  - 41% of AI users have tried an agent, and 24% use one regularly.
  - 65% of people who pay for AI use agents, compared with 13% of people who don't pay.
  - The agents people name most are tools for coding and work: Codex 35%, Claude Code/Cowork 32%, Perplexity 24%.
- **[LOW] General-purpose browser agents lose most of their users.**
  - ChatGPT Agent had about 4M weekly active paying users at launch (about 11% of subscribers). Within months it had fewer than 1M.
  - Users "couldn't figure out what to do with it or didn't know it existed." They also complained about speed, reliability, and security.
  - This comes from one source (The Information, via The Decoder).
  - OpenAI then shifted toward narrower agents, such as "Shopping Research."
- **[HIGH] OpenAI shut down its standalone AI browser.**
  - Atlas launched on Oct 21, 2025, and was shut down on Aug 9, 2026. The Windows version was canceled.
  - Its features moved into a single ChatGPT desktop app (with a built-in browser, "ChatGPT Work", and Codex) and a Chrome extension.
  - Reviewers complained that Atlas was slow ("10 minutes to add three Amazon items") and raised prompt-injection concerns.
  - a16z wrote in March 2026: "No AI browser has seen accelerating growth."
- **[HIGH] Claude in Chrome is now generally available on every paid plan (Aug 26, 2026).** It includes an "auto mode". In auto mode, a separate checker model reviews each action against what the user originally asked for.
- **[MEDIUM] Comet's own usage study** (Perplexity and Harvard, December 2025):
  - Productivity and learning make up 57% of agent queries. Courses and shopping make up 22%.
  - Adopters skew toward tech, academia, finance, marketing, and entrepreneurship.
  - Users start with simple personal tasks and move to work tasks over time.
- **[LOW, conflicting] Comet monthly user numbers.** Estimates from third-party sites range from about 3M to about 18M. Treat them all as unverified.
- **[LOW] Codex usage.** One source says Codex had more than 5M weekly active users, with more than 1M of them using it for work other than software development. This hints that non-developers will adopt tools that were built for developers.
- **[HIGH] Many enterprises are experimenting with agents, but few have scaled them.**
  - McKinsey: 23% are scaling agents, and 39% are experimenting.
  - KPMG: 62% are building or deploying agents.
  - Capgemini: only 2% have deployed agents at scale.
  - Gartner predicts that more than 40% of agentic AI projects will be canceled by 2027.

## 3. Trust and willingness to delegate

- **[HIGH] People welcome help with research and comparison. Paying is where they stop.**
  - Accenture: 85% will work with an agent. 32% will let it decide if they approve the payment. Only 9–12% will let it pay on its own.
  - Gartner: 11% will let AI make purchase decisions.
  - HUMAN Security: 43% would let AI book travel if they give final approval, but only 12% without approval. 82% are uncomfortable with full autonomy.
  - Riskified: 55% are not comfortable letting an agent buy anything.
  - Product.ai: 86% double-check before they buy, and 42% won't trust AI with purchases over $25.
- **[HIGH] People ask for these controls:**
  - Approval before checkout.
  - Protection for their data.
  - Permissions they can adjust.
  - A way to override the agent instantly.
  - A clear way to get things fixed when they go wrong.
  - A biometric check or one-time code on every transaction (73.9%).
  - An option to reach a human (87%).
- **[MEDIUM] Users blame the AI platform when things go wrong.** For unauthorized purchases, 50.8% blame the AI platform, 23.2% blame the retailer, and 18.7% blame themselves.
- **[MEDIUM] Some users already let AI act without checking.**
  - 32% of AI users have let AI act without their final approval.
  - Among agent users, 33% have given an agent access to their browser. Only 20% have given access to financial accounts, and 23% to health apps.
- **[HIGH] Older adults trust AI less.**
  - Boomers: 44.1% don't trust that AI acts in their best interest, vs 18.7% of Millennials.
  - AARP: 51% of adults aged 50+ think AI is unsafe.
- **[LOW] No direct survey data was found on trust by technical skill level.**
- **[HIGH] General distrust of AI is high.**
  - Pew: 71% say AI will make personal data less secure.
  - KPMG and the University of Melbourne: only 46% are willing to trust AI.
  - Among people who don't use AI, 76% have privacy concerns.

## 4. Security and safety

- **[HIGH] The AI vendors themselves say prompt injection is unsolved.**
  - OpenAI's head of security called it "a frontier, unsolved security problem."
  - OpenAI said it is "unlikely to ever be fully 'solved.'"
  - Anthropic: "No browser agent is immune to prompt injection."
  - The UK National Cyber Security Centre says it "may never be totally mitigated."
  - Brave showed the problem in Comet, Fellou, and Opera Neon. Because the agent acts with the user's logged-in sessions, the browser's normal protections that keep websites apart "are all effectively useless."
- **[MEDIUM] Attack success rates depend on who measures and how.**
  - Anthropic's own figures fell from 23.6% to 1% and then to 0%.
  - The independent Gray Swan benchmark found 63% success at 100 attempts against Opus 4.5. Some rival models scored up to 92%.
- **[MEDIUM] AI browsers fall for phishing and scams.**
  - Guardio's "Scamlexity" study: Comet completed a purchase on a fake Walmart site and filled in the user's saved card without asking. It also entered the user's login on a fake Wells Fargo page.
  - LayerX, a security vendor, says Comet blocked only 7% of phishing attacks, compared with 47% for Chrome. This figure is unverified.
- **[MEDIUM] Attacks are now happening in the wild.**
  - Google found 32% more malicious prompt-injection content on the web than before.
  - Forcepoint found ready-made PayPal transaction attacks and "organized tooling."
- **[MEDIUM] OpenClaw incident (Feb 23, 2026).**
  - OpenClaw is an open-source agent. It bulk-deleted the inbox of Meta's alignment director.
  - She had told it to wait for approval, but the agent lost that instruction when it compressed its memory.
  - Three "STOP" messages failed. She had to kill the process on the machine.
  - Claims about OpenClaw instances exposed on the internet, and about malicious add-ons, are unverified.
- **[HIGH] Analysts push back.** In December 2025, Gartner advised: "Cybersecurity Must Block AI Browsers for Now."
- **Protections that vendors use today:**
  - Confirmation before high-risk actions such as purchases, publishing, sending, and sharing personal data.
  - Permissions for each site.
  - Blocked categories of risky sites.
  - A logged-out mode that uses no saved logins.
  - A "Watch Mode" that requires the tab to stay active on sensitive sites.
  - Classifiers that scan page content for attacks.
  - A separate model that checks each action.
  - Separation between agent browsing and the user's normal browsing.

## 5. Website and platform pushback

- **[HIGH] Amazon v. Perplexity.**
  - A court injunction blocked Comet from Amazon accounts in March 2026.
  - The Ninth Circuit canceled the injunction on Aug 4, 2026. Comet runs on the user's own device, so the court ruled that the user, not Perplexity, is the one accessing Amazon under US anti-hacking law.
  - Claims based on Amazon's terms of service are still open.
- **[HIGH] Retailers use their terms of service to restrict agents.**
  - eBay forbids "buy-for-me agents… without human review."
  - Amazon blocked Meta's Muse agent in September 2026. Amazon objected that Muse gave no notice, did not identify itself as an agent, and appeared to capture and store customers' credentials.
  - Amazon's robots.txt file (the file where a site tells automated tools what they may access) blocks dozens of named AI agents.
- **[HIGH] Cloudflare's "signed agents" program** (Aug 2025) lets agents prove who they are with a cryptographic signature, using a standard called Web Bot Auth. Cloudflare removed Perplexity from its list of verified bots for stealth crawling.
- **[MEDIUM] Bots now outnumber humans on the web** (57.5% of requests). Expect more bot checks and CAPTCHAs.
- **What this means for a local app that uses the user's own logins:**
  - The court's reasoning helps an app that runs on the user's device.
  - Breaking a site's terms of service can still put the user's account at risk.
  - Storing passwords centrally and hiding that a request comes from an agent are the exact behaviors Amazon objected to.

## 6. Accessibility and users with different technical levels

- **[HIGH] Older adults (AARP).**
  - 80% of adults aged 50+ have used some AI, and 42% call themselves beginners.
  - Their top interests: translation 74%, home safety 71%, fraud detection 66%, health monitoring 63%.
  - 65% say AI could help them stay independent.
- **[MEDIUM] Disabled users.**
  - The American Foundation for the Blind's "AI Quagmire" report (Mar 2026) found that disabled users rely more on AI than other users, but face more barriers when they learn to use it. 73% prefer a human for sensitive information.
  - The OLLA study of blind users found only 52.5% task success. The agent failed most at finding the right element on the page, planning, keeping track of the user's constraints, and knowing when to stop.
- **[MEDIUM, conflicting] Small businesses.**
  - The US Chamber of Commerce says 58% of small businesses use generative AI.
  - The Census survey says 17–20% of US firms use AI, with no growth among firms that have fewer than 20 employees.
  - The two surveys define AI use differently.

## What this means for our app

1. **Start with people who already pay for AI.** 65% of them use agents, compared with 13% of people who don't pay.
2. **Don't ship a blank prompt box.** ChatGPT Agent lost about 75% of its users and Atlas was shut down. Lead with named workflows whose results are easy to check.
3. **Compete where the big AI companies don't.** OpenAI and Anthropic already cover single-agent browsing. Our space is parallel agents, scheduling, monitoring, one approval queue for all agents, and audit logs.
4. **Make approval the core of the product.** An inbox where agents propose actions and the user approves them fits how people say they will delegate.
5. **Assume every agent can be attacked through prompt injection.** By default, give each agent its own browser profile and a list of allowed sites. Block finance and health sites unless the user opts in. Require confirmation before the agent sends, pays, deletes, or publishes. Use a separate model to check each action.
6. **Enforce limits in the app, not only in the model.** The OpenClaw incident shows that instructions can get lost, so the kill switch must stop the process. The app must also enforce spending and action limits itself.
7. **Don't store users' passwords.** Use the user's own browser sessions or the system keychain.
8. **Expect blocking.** Running on the user's device helps legally, but Amazon and eBay will still block agents. Warn users about the risk to their accounts.
9. **Users will hold us responsible for mistakes.** Spending caps, logs, replay, and undo are trust features.
10. **Treat older adults and disabled users as later segments.** Build the app so it works with screen readers and voice from the start. Consider a mode where a family member or caregiver approves actions.
11. **Don't rely on enterprise adoption at first.** Many companies block AI browsers.
12. **For small businesses, target owners who already use AI.**

## Verbatim quotes

1. "prompt injection remains a frontier, unsolved security problem, and our adversaries will spend significant time and resources to find ways to make ChatGPT agent fall for these attacks" — Dane Stuckey, OpenAI head of security, Oct 22, 2025 (https://simonwillison.net/2025/Oct/22/openai-ciso-on-atlas/)
2. "Prompt injection, much like scams and social engineering on the web, is unlikely to ever be fully 'solved.'" — OpenAI, Dec 22, 2025 (https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/)
3. "A useful way to reason about risk in AI systems is autonomy multiplied by access." — Rami McCarthy, Wiz, Dec 22, 2025 (same)
4. "For most everyday use cases, agentic browsers don't yet deliver enough value to justify their current risk profile." — Rami McCarthy, Wiz, Dec 22, 2025 (same)
5. "A 1% attack success rate—while a significant improvement—still represents meaningful risk." — Anthropic, Nov 24, 2025 (https://www.anthropic.com/research/prompt-injection-defenses)
6. "I would argue that 11.2% is still a catastrophic failure rate." — Simon Willison, Aug 26, 2025 (https://simonwillison.net/2025/Aug/26/piloting-claude-for-chrome/)
7. "I don't think it's reasonable to expect end users to make good decisions about the security risks of this pattern." — Simon Willison, Aug 26, 2025 (same)
8. "When an AI assistant follows malicious instructions from untrusted webpage content, traditional protections such as same-origin policy (SOP) or cross-origin resource sharing (CORS) are all effectively useless." — Brave, Aug 20, 2025 (https://brave.com/blog/comet-prompt-injection/)
9. "The result: a perfect trust chain gone rogue. By handling the entire interaction from email to website, Comet effectively vouched for the phishing page." — Guardio, Aug 20, 2025 (https://thehackernews.com/2025/08/experts-find-ai-browsers-can-be-tricked.html)
10. "Default AI browser settings prioritize user experience over security." — Gartner, Dec 2025 (https://www.theregister.com/2025/12/08/gartner_recommends_ai_browser_ban/)
11. "Consumers are not looking to outsource shopping decisions to AI." — Kate Muhl, Gartner, May 27, 2026 (https://www.01net.it/gartner-survey-finds-consumers-want-ai-shopping-help-but-not-ai-purchase-decisions/)
12. "Consumers are clearly embracing AI as a shopping assistant, but they're drawing a firm line when it comes to autonomy and accountability" — Jeff Otto, Riskified, 2026 (https://forkast.news/73-use-ai-for-shopping-55-wont-let-it-buy-anything-the-trust-gap-is-widening/)
13. "I want to review the choices made on my behalf" — Gen X interviewee in the US, Accenture, 2026 (https://www.accenture.com/ma-en/insights/consulting/talk-my-ai-agent)
14. "Welp, that happened faster than I predicted… agentic traffic growing so fast that bots have now passed human traffic online for the first time in the Internet's history." — Matthew Prince, Cloudflare CEO, Jun 3, 2026 (https://www.hothardware.com/news/ai-bots-are-now-dominating-the-web)
15. "Continued access by an unauthorized AI agent violates Amazon's Conditions of Use, to which our customers have agreed." — Amazon, Sep 2026 (https://nohacks.co/blog/amazon-blocked-muse-robots-txt-had-nothing-to-say)
16. "the Assistant built into Perplexity's Comet browser is a tool rather than a person for statutory purposes" — Ninth Circuit, Aug 4, 2026 (https://ppc.land/amazon-loses-injunction-blocking-perplexitys-ai-shopping-agent/)
17. "shared injection templates across multiple domains suggest organized tooling rather than isolated experimentation." — Forcepoint X-Labs, Apr 2026 (https://www.helpnetsecurity.com/2026/04/24/indirect-prompt-injection-in-the-wild/)
18. "It's just fun to learn, and AI puts everything right at my fingertips." — 61-year-old woman who uses AI daily, Menlo Ventures, Sep 16, 2026 (https://menlovc.com/perspective/2026-the-state-of-consumer-ai/)

## Unverified items and gaps

- **Unverified numbers:**
  - About 1B ChatGPT weekly users in July 2026.
  - The 122M subscriber forecast.
  - Perplexity and Comet user numbers.
  - OpenClaw exposure statistics.
  - LayerX's phishing block rates.
  - Codex's 5M users.
  - The claim that 16% of small businesses have deployed an agent.
  - The Work Trend Index figures (secondary summaries only).
  - The McKinsey figures (secondary summary only).
- **Self-reported by vendors:** all of the AI labs' attack-success-rate figures.
- **Not found:**
  - Copilot Pro subscriber counts.
  - Google AI Pro and Ultra subscriber counts.
  - Any survey of trust by technical skill level.
  - Similarweb or Sensor Tower data on AI browser usage.
