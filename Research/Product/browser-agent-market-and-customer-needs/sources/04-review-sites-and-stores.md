# Source notes 04: Review sites, app stores, and extension stores

These are the raw findings from one research stream, collected on 2026-10-12.

**What the dataset covers:** about 2,700 reviews dated October 2025 to October 2026. The sources were:

- 15 Chrome Web Store extensions
- 3 iOS apps
- 10 Trustpilot pages
- Product Hunt
- AppSumo

**How the reviews were collected:**

- **Chrome Web Store:** taken directly from the store's own review data, including star ratings.
  - Claude in Chrome: the 500 most recent reviews (2026-04-20 to 2026-10-12).
  - The new ChatGPT extension: all 461 reviews.
- **App Store:** Apple's public review RSS feed, US store only.
- **Trustpilot:** read through a tool that returns a summarized version of each page. Some long reviews were cut off. Quotes #38–43, #46 and #51 come from that summarized version, so check them against the live page before you publish them. All quotes from the Chrome Web Store, App Store and AppSumo are copied exactly from the raw data.
- **Not available:** G2, Capterra, GetApp and TrustRadius all blocked access (HTTP 403).

The raw Chrome Web Store and App Store reviews (3,215 rows) are in [`../data/store-reviews.csv`](../data/store-reviews.csv).

## Main findings

1. **The leading browser agents have low ratings.**
   - Claude in Chrome: 2.9 stars from 1,800 ratings, with 18 million users.
   - The new ChatGPT extension ("Control your browser with ChatGPT"): 2.75 stars from 896 ratings, with 7 million users.
   - Most complaints are about setup problems, the connection to the desktop app breaking, and lost work. Few complaints are about the AI itself being weak.
2. **ChatGPT Atlas appears to have been retired around August 2026.** OpenAI replaced it with this extension, which needs the ChatGPT desktop app and Codex to work. Several former Atlas users say it is "more for app developers than for non-developer AI users."
3. **Paid agents get most of their 1-star reviews because of credits, not because the agent fails.**
   - Credits come up in 45% of the 1–3 star iOS reviews for Manus and in 58% of those for Genspark.
   - Perplexity moved Comet's "Control Browser" feature into a "Computer" mode that charges credits for use. Trustpilot reviews show the backlash.
4. **Several reviewers ask, in their own words, for an orchestrator** (a tool that runs and manages many agents). They want:
   - agents that run in their own separate, dedicated tabs while the user keeps working
   - sessions that survive switching tabs
   - a history of past runs they can check
   - several projects running at the same time

   The strongest 5-star praise describes exactly this setup.
5. **"Works with the subscription I already have" is a selling point in itself.**
   - Do Browser: "works seamlessly with my existing ChatGPT subscription"
   - Claude in Chrome: "you get the same model you already use"

## 1. What reviewers say about each product

| Product (source, rating, sample) | What users hire it to do | Top praise | Top complaint | What they switch from or to | What they wish it did | Who the reviewers are |
|---|---|---|---|---|---|---|
| **Claude in Chrome** ([Chrome Web Store](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn/reviews): 2.89 stars from 1,793 ratings, 18M users. Sample: 500 reviews, 2026-04-20 to 2026-10-12: 242 one-star, 51 two-star, 29 three-star, 25 four-star, 153 five-star) | Hand off boring tasks on websites where the user is logged in. Examples: professional licensing forms, tax forms, Uber receipts, Google Search Console, WordPress, software testing (QA), Jira. Uses the Claude plan they already pay for. | "Saves hours." Works in the user's real, logged-in browser sessions. Uses the same account and AI model. Works in its own tabs while the user keeps working. | Loses its connection to the Claude desktop app, Cowork or Claude Code ("can't reach"). Loses the session and history when the user switches tabs. Asks for approval on every single action. Uses up the plan's usage allowance quickly. A September 2026 update removed the "classic" mode and deleted users' saved shortcuts. | Switching from ChatGPT ("ChatGPT sucks"). Some say Comet and Atlas are "much better and faster." Some leave for rtrvr or "fabric." | History that syncs to the account. Sessions that can be resumed. Separate workspaces for the agent. A per-site "always allow" setting that is remembered. Learning from earlier runs. Choosing the account separately from the Chrome profile. Several projects or tabs at once. Bigger text. | Developers and Claude Code users (who write detailed bug reports). Also solo professionals, SEO and marketing people, software testers, and professionals with a lot of paperwork. Pro and Max subscribers. |
| **ChatGPT extension / ChatGPT Atlas (retired)** ([Chrome Web Store](https://chromewebstore.google.com/detail/chatgpt/hehggadaopoacecdllhhajmbjkdcmajg/reviews): 2.75 stars from 896 ratings, 7M users. Sample: all 461 reviews, 2026-05-07 to 2026-10-12: 236 one-star, 43 two-star, 25 three-star, 16 four-star, 141 five-star) | Let ChatGPT or Codex read and act on pages in the user's own Chrome. Former Atlas users want "chat with the page I'm on" back. | "Feels like AGI when it does work." Can use several tabs and work in the background. | Gets stuck on an "Install the app to use ChatGPT in Chrome" message (49 reviews). Errors from Codex. Forces users into Codex and its usage limits (97 reviews mention Codex). Can't open normal chats or Projects. Broken on Windows and Linux. | Coming from Atlas (33 mention it). Leaving for the Claude extension or Gemini's side panel. | A light, Chrome-only version. A chat mode that knows which page is open. | Codex developers, plus Plus subscribers who don't write code. Many Windows users. A psychiatric nurse practitioner. Software testers. |
| **Perplexity Comet + "Computer" mode** ([iOS App Store](https://apps.apple.com/us/app/comet-ai-browser-assistant/id6748622471?see-all=reviews): 4.8 stars from 7,800 ratings. [Trustpilot for Comet](https://www.trustpilot.com/review/comet.perplexity.ai): 1.8 from 24 reviews. [Trustpilot for Perplexity](https://www.trustpilot.com/review/www.perplexity.ai): 1.4 from 835 reviews) | Summarize, compare and research. "Control Browser" researched across many pages "while I focused on other tasks." Also job searching and printing court files. | Fast and clean. The assistant summarizes and automates. Non-technical users who switched love it. | Browser control was moved behind credits that cost extra, in the middle of users' paid subscriptions. The app switches itself into Computer mode. The AI deleted users' tabs. The purpose of the browser is unclear. | Coming from Chrome, Edge, Safari or Firefox. Leaving for Firefox, Claude or rtrvr. | A predictable cost for each task. A way to stop or export paused tasks without spending credits. A clear explanation of what an AI browser is for. | A broad range of consumers. Students. Job seekers. People who call themselves "non-techy." |
| **Manus + Browser Operator** ([Trustpilot](https://www.trustpilot.com/review/manus.im): 1.2 from 214 reviews, 95% one-star. [iOS](https://apps.apple.com/us/app/id6740909540?see-all=reviews): 4.7 stars from 39,000 ratings; 500 reviews sampled. [Chrome Web Store, Operator](https://chromewebstore.google.com/detail/manus-ai-browser-operator/cecngibhkljoiafhjfmcgbmikfogdiko/reviews): 4.3 stars from 69 ratings) | A general-purpose agent. Operator acts in the user's own logged-in browser. | Powerful. "Shows you step by step." Operator is "using my browser and not creating some slow virtual browser." | Credits are spent on the agent's mistakes. Credits expire. Support is only AI bots. Data was lost. Claims tasks are "complete" when they are not. | Leaving for Base44 and Lovable. | See how many credits a task will cost before running it. A flat-rate plan without credits. | Small business owners, people working on their own, people representing themselves in court, a legally blind user, and people who don't code. |
| **Genspark** ([Trustpilot](https://www.trustpilot.com/review/genspark.ai): 476 reviews; Trustpilot withholds the score for breaking its guidelines. [iOS](https://apps.apple.com/us/app/id6739554054?see-all=reviews): 4.7 stars from 4,300 ratings) | An all-in-one AI tool: slides, research, images. | Good slides. Many AI models in one place. | "Credits fly." Charges for failed tasks. Too many features. | Some cancelled ChatGPT for Genspark, and some went back. | Clear information on what uses credits. | Content creators, contractors, students. Clearly non-technical. |
| **Bardeen** ([Chrome Web Store](https://chromewebstore.google.com/detail/bardeen-automate-browser/ihhkmalpkhkoedlmcnilbbhhbhnicjga/reviews): 4.36 stars from 451 ratings) | Collect sales leads into a spreadsheet or CRM without code. | Accurate data collection. Templates. | Price. Credit costs went up "2-3x." "Most complicated UI." | Some leave for Apify. | Stable, clear credit pricing. A simpler first experience. | Sales and growth teams, recruiters. |
| **Axiom.ai** ([Chrome Web Store](https://chromewebstore.google.com/detail/axiom-ai-browser-automati/cpgamigjcbffkaiciiepndmonbfdimbb/reviews): 4.47 stars from 245 ratings) | No-code bots that enter data and fill forms. | Support from the founder. Saves "days of data entry." | The user must build a whole workflow first. | Compared with iMacros and UI Vision. | "fill forms for me without me needing to setup an entire workflow." | Operations staff, virtual assistants, small businesses. |
| **Browse AI** ([Chrome Web Store](https://chromewebstore.google.com/detail/browse-ai-fast-web-scrapi/obpcenkclppghkfpielmefegceegofeh/reviews): 3.91 stars; [Trustpilot](https://www.trustpilot.com/review/browse.ai): 2.7) | Watch websites for changes and collect data. | "Most powerful scraper." | Unreliable. "fell off." "Claude can do much easier." | Leaving for general-purpose AI. | — | Data and operations staff. |
| **Automa** ([Chrome Web Store](https://chromewebstore.google.com/detail/automa/infppggnoaenmfagbfknfkancpbljcca/reviews): 4.33 stars) | Free browser automation built from blocks. | Free. Powerful "once i learnt." | Requires knowing CSS, HTML and JavaScript. | — | Templates. | Developers and hobbyists. Non-developers give up. |
| **Nanobrowser** ([Chrome Web Store](https://chromewebstore.google.com/detail/nanobrowser-ai-web-agent/imbddededgmcgfhfpcjmijokokekbkal/reviews): 3.59 stars) | An open-source agent where users supply their own API key. | Free, runs locally. | Fails at basic tasks. Setting up the API key is confusing. | — | Scheduling. | Technical users. |
| **Do Browser** ([Chrome Web Store](https://chromewebstore.google.com/detail/do-browser-ai-browser-age/hjcibkpfgnljonndnnanhkholafmgmip/reviews): 3.32 stars) | A browser agent that takes plain-language instructions. | "Works seamlessly with my existing ChatGPT subscription." | Errors. Limits on price and number of steps. | Compared with browser-use. | — | Mixed. |
| **rtrvr.ai / Retriever AI** ([Chrome Web Store](https://chromewebstore.google.com/detail/retriever-ai-browser-agen/jldogdgepmcedfdhgnmclgemehfhpomg/reviews): 4.03 stars) | Collect data and run multi-step tasks in the user's own browser. | Users can record a task once to teach it. Saves reusable "skills." | Makes things up. Errors. | Users arrived after Perplexity Computer started charging. | — | Semi-technical users. |
| **HARPA AI** ([Chrome Web Store](https://chromewebstore.google.com/detail/harpa-ai-ai-automation-ag/eanggfilgoajaocelnaflolkadkeghjp/reviews): 4.69 stars from 3,200 ratings) | Chat about the open page, plus automation and monitoring. | Understands the page. Supports many AI models. | Unreliable, with "no explanation, or log." | — | Logs. Reliability. | Virtual assistants, busy professionals. |
| **Magical / Text Blaze** ([Magical](https://chromewebstore.google.com/detail/magical-ai-agent-for-autof/iibninhmiggehlcdolcilmhacighjamp/reviews): 4.39 stars; [Text Blaze](https://chromewebstore.google.com/detail/text-blaze/idgadaccgipmpannjkmfddolnnhmeklj/reviews): 4.91 stars) | Expand short codes into text and fill forms automatically. | Text Blaze "saves me hours each week" and is reliable. | Magical crashes Chrome and deleted one user's 3 years of saved snippets. | Users move from Magical to Text Blaze. | — | Support staff, office administrators, job seekers. Non-technical. |
| **BrowserAct** ([AppSumo](https://appsumo.com/products/browseract/): 4.44 out of 5 tacos, AppSumo's rating, from 57 reviews) | Collect data from websites without code. | Replaced a scraper the user ran on their own server. | Credit costs. Made-up data. Needs a "degree in programming." | — | Describe the task in words, then edit the steps. | Small businesses and no-code users. |
| **Lindy** ([Trustpilot](https://www.trustpilot.com/review/lindy.ai): 1.7) | AI assistant workflows. | "When Lindy works, it works!" | Burns credits during setup. | — | — | Small businesses, nonprofits. |
| **Zapier / Make / n8n** (Trustpilot: 1.3 / 2.7 / 3.0) | Workflow automation. | n8n is the strongest of the three. | Complicated. Billing problems. | — | — | Small business operators. |
| **Dia, Opera Neon, Simular, Browser Use, BrowserOS, Browser MCP** (Product Hunt, Chrome Web Store) | AI browsers or tools for building agents. | BrowserOS imports logins and shows the agent working live. | Simular feels "intimidating" to non-technical users. Browser MCP "Disconnects all the time." | — | Linux and Windows versions. | Mostly founders and developers. |

## 2. Exact quotes

Each quote has hashtag tags. #pain is a problem or frustration. #want is something the reviewer asks for. #outcome is a result they got. #language is wording worth reusing. #alternative is another tool they mention. #objection is a reason they hesitate or refuse.

**Claude in Chrome** ([Chrome Web Store reviews](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn/reviews))

1. Khun Shawn, 3 stars, 2026-09-25: "When it works, it's genuinely good. It drives my real logged-in sessions (Google Cloud, Search Console, YouTube Studio) and saves me hours of manual clicking. […] Fix the connection stability and this is a 5-star tool. Right now it's a great product I can't fully rely on." #outcome #pain
2. Irina Cheban, 1 star, 2026-10-06: "Now they've changed the UI so it no longer asks thoughtful questions about the tasks, instead I have to approve every single javascript or whatever it is doing. How am I supposed to read and understand those??? I have no idea what Claude is about to do but I am asked to approve it." #pain #language
3. Pando Ridge, 1 star, 2026-09-30: "it asks for permission and only gives the option to allow once which means I'm babysitting this stupid thing all f ing day long" #pain #language
4. Dan, 1 star, 2026-09-28: "Every time I open the panel or leave a tab, it creates a new session and a new tab group, so it's impossible to do any work that involves 2 or more tabs." #pain
5. Casey Doolittle, 1 star, 2026-07-21: "step one has got to be isolation. I should have to share a resource with my agent that's the entire point the agent can do work while I work on something else. If I have to wait for the agent to use the browser how does that make sense to anyone?" #want #pain
6. Maneesh Reddy, 5 stars, 2026-10-10: "this is really good, cuts my time in half by automating the work in dedicated browser tabs, while i can do my work in other tabs with out getting interlinked or disturbed" #outcome
7. Nathan, 5 stars, 2026-10-08: "I just used it to fill out all the credentialing applications for my professional license. Inputting hundreds of information is so tedious, but this literally saved hours of doing this tedious work." #outcome #language
8. Chinmay Chapla, 5 stars, 2026-09-26: "I have been lazy person loosing $$ every month downloading Uber receipts and submitting for reimbursement every month. This $20 Claude subscription and extension made real profit." #outcome
9. Valeri Dilov, 1 star, 2026-07-28: "Users need reliability, persistence, auditability, and the ability to review previous actions. Without these basics, it is difficult to trust the extension with any serious task." #want
10. David Perry, 3 stars, 2026-07-08: "the side panel is tied to the tab it opened in, so switching tabs or letting it close ends the session. Reopening it starts a blank new chat rather than picking back up, and there's currently no history or log to recover what was in progress." #pain
11. Jason J, 1 star, 2026-08-11: "I ended up using all of my 5hr tokens (Pro plan) in under an hour to write 10 rows on a spreadsheet - and that was with Sonnet!!!" #pain
12. Sebastien Bo, 3 stars, 2026-07-02: "Perplexity comet and Chatgpt atlas are much better and faster at browser use. […] When it has solved an executive problem during browser use, it should update itself with that problem->solution-trick that way it only looses time and tokens the first round" #alternative #want
13. Stuart Barlow, 1 star, 2026-07-15: "My paid account email is different to my Chrome account email. […] Unfortunately, there is no option provided to switch account, and thus the extension is unusable." #pain
14. David Strahan, 3 stars, 2026-05-29: "even though the extension requires you to log in as a paid user, it's not actually connected to your account. You can't leverage your personal settings or customization, skills, or chat history." #want
15. Xiang Wang, 1 star, 2026-09-18: "my screen shows a highlight border noting that the agent is viewing it while I tried to pull my account number stuff which is scary. What is this thing doing????" #objection
16. Robert Palmer, 5 stars, 2026-05-13: "Really useful, but a security nightmare. Make sure you only use this extension in a dedicated Profile and not your everyday one thats logged into every account you have access to. Prompt injection is a real threat." #objection
17. Comisionado Desarrollo Tecnologico Scouts de Colombia, 5 stars, 2026-05-12: "What I find most useful is being able to automate tasks for apps that don't have connectors, instead of waiting for an integration to exist, I can just handle it directly here." #outcome
18. Amirmahdi Shokat, 5 stars, 2026-09-29: "The best feature for people who do not want a complicated ai app, and want simply to ask ai to do their daily task on web." #language #outcome
19. Ricky Davis, 1 star, 2026-07-31: "if I need different projects/tabs running at once it never knows which one to connect to. I have to manually restart my computer for it to connect." #want #pain
20. Lee Barnard, 2 stars, 2026-08-31: "Seems generally ok, but WHY are scheduled tasks hidden in "Shortcuts"?" #pain
21. Christian Loor, 1 star, 2026-08-13: "My shortcuts were deleted with this recent UI update! I just used them yesterday and now they are literally gone. That was hours of adjusting and instructions!" #pain
22. Jake Kim, 5 stars, 2026-10-07: "this extention works with your Claude account, so you get the same model you already use" #language
23. Floyd 73, 1 star, 2026-05-12: "now I cannot access chrome from within desktop app (so cannot use any of the scheduled tasks I built for specific sites)" #pain

**ChatGPT extension / Atlas** ([Chrome Web Store reviews](https://chromewebstore.google.com/detail/chatgpt/hehggadaopoacecdllhhajmbjkdcmajg/reviews))

24. Donna Knight, 2 stars, 2026-09-15: "It seems to be more for app developers than for non-developer AI users. ChatGPTs browser has gone backwards instead of getting better." #language #pain
25. Cal Shepherd, 2 stars, 2026-09-03: "requiring a desktop app and Codex for functionality that previously worked well in Chrome is a major regression. Please bring back a lightweight, reliable Chrome-only experience." #want
26. nayuki leung, 1 star, 2026-10-08: "I'm using a MacBook and stuck with "Install the app to use ChatGPT in Chrome Or open the app if already installed". No one going to fix this problem? Aren't you the most advanced AI company?" #pain
27. Luke Rodel, 1 star, 2026-10-11: "It's unclear to me if computer even works on non arm based windows laptops. All the naming is just confusing" #language
28. Aaron Makelky, 5 stars, 2026-05-07: "So much faster and more useful than Claude's Chrome Extension. This is the best way to use Codex in a browser with multiple tabs or have it work in a tab in the background while you do something in another tab" #outcome #alternative
29. Jake Zukowski, 2 stars, 2026-10-08: "there used to be a browser built by OpenAI called ChatGPT Atlas that did the integration flawlessly. Unfortunately now we are stuck with a busted plugin." #alternative
30. Max Phelps, 5 stars, 2026-08-16: "Atlas sucked guys, it was trying too hard to get rid of the browser at the sacrifice of all the things one actually needs like *bookmarks*" #objection
31. Sammir Ahmed, 1 star, 2026-09-09: "Honestly, why rely on this extension when you can just use the Google Gemini side panel? It’s much smoother, completely free, and directly integrated into Chrome." #alternative #objection
32. Ali J, 1 star, 2026-08-16: "Had to stop using my main browser ChatGPT Atlas and lost my browser's history and favorites, passwords." #objection
33. Jason McIntyre, 1 star, 2026-09-24: "Codex messages have limits even on subscription-users like myself, and in order to get more usage out of this extension, I will need to pay for a much more expensive subscription." #pain
34. Farhad Arvin, 3 stars, 2026-06-06: "This plugin needs better per-thread bridge health checks, clearer failure reporting, a real restart/recovery mechanism, and stronger isolation so one thread does not fail while others work." #want

**Perplexity Comet / Computer**

35. SendingOutAnSOS, 1 star, 2026-06-19 ([App Store](https://apps.apple.com/us/app/comet-ai-browser-assistant/id6748622471?see-all=reviews)): "After three months of using this as my main browser, I still don’t understand the purpose of it. The team that developed this browser has done a lousy job showing regular people the purpose of an AI integrated browser." #language #objection
36. BlackFoxAlpha, 1 star, 2026-09-12 (App Store): "If you leave tabs open, or if you feel like you should have literally any agency, avoid this app. Your work will be determined to be worthless by the AI and simply deleted without notice or input." #objection
37. GSrenegade, 5 stars, 2026-06-17 (App Store): "I started using the A.I assistant and was like "yo.... Ive needed A.I all along." It makes everything flow seemlessly." #outcome #language
38. Walter, 1 star, 2026-09-13 ([Trustpilot](https://www.trustpilot.com/review/comet.perplexity.ai)): "I signed up for Perplexity Pro primarily because Comet's 'Control Browser' could autonomously handle multi-page research workflows while I focused on other tasks. […] There is no predictable cost per task" #pain #want
39. Daniel Crothers, 1 star, 2026-09-04 (Trustpilot): "I paid annually for Pro with browser-control assistance as a material feature. During my prepaid term, that functionality was removed from Pro and moved behind an additional paid credit product." #pain
40. Amparo Johnson, 1 star, 2026-09-30 (Trustpilot): "Perplexity should provide clearer warnings before updates that may affect compatibility, a reliable method for exporting existing Computer work without restarting a task, and controls that allow users to prevent paused tasks from automatically using newly available credits." #want
41. garp, 5 stars, 2025-12-26 (Trustpilot): "From the non-techy person here, I switched two months ago from Edge/Chrome and have never looked back. It is fast, intuitive, and just not cluttered like the other browsers." #language #outcome
42. Jay Mehra, 3 stars, 2025-10-28 (Trustpilot): "Sometimes it is cool, but there are scary things too. For one, I wouldn't open by internet banking inside this browser." #objection
43. T J, 1 star, 2026-09-30 ([Trustpilot](https://www.trustpilot.com/review/www.perplexity.ai)): "it switches automatically into computer mode and even the program and support cannot help you move back into basic mode. All activity in computer mode costs credits which are $$." #pain

**Manus**

44. D Dubbya, 2 stars, 2026-06-20 ([iOS](https://apps.apple.com/us/app/id6740909540?see-all=reviews)): "Manus has developed a remarkable habit of confidently announcing that a task is complete while leaving behind little evidence that anything has actually been completed." #pain
45. kateklar, 4 stars, 2026-05-26 (iOS): "If there were an option to buy the amount of credits you need instead of paying $40 a month that would be amazing. Also a way to see how many credits you need for a specific task." #want
46. Josh Nichols, 1 star, 2026-10-05 ([Trustpilot](https://www.trustpilot.com/review/manus.im)): "We've spent more time fighting Manus than improving our systems. We're now migrating away." #pain
47. Tim Miller, 5 stars, 2025-12-20 ([Chrome Web Store, Operator](https://chromewebstore.google.com/detail/manus-ai-browser-operator/cecngibhkljoiafhjfmcgbmikfogdiko/reviews)): "I love the fact that its using my browser and not creating some slow virtual browser stopping to request a pasword for this or for that." #outcome #want
48. igloo, 5 stars, 2026-03-13 (Chrome Web Store, Operator): "i was looking for an agent to perform browser actions and after looking into numerous plugins, manus was the only one that did what i truly wanted. all the others were tools for webscraping and something about workflows." #language #alternative
49. 3Bbird, 1 star, 2026-05-24 (iOS): "suddenly my credits are used up and there’s no explanation for why and the AI agent can’t figure it out that we’re supposed to trust these AI agents to do our work for us really?" #objection

**Genspark, Bardeen, Axiom, Automa, and others**

50. EP from GA, 2 stars, 2026-04-29 (Genspark [iOS](https://apps.apple.com/us/app/id6739554054?see-all=reviews)): "The credit drain rate with little to no transparency or insight into what uses what continues to be a problem. The app and user interface have weird aspects that make me think they could benefit from having more non-tech industry users in their beta group to improve experience." #pain #language
51. Mohammed Borham, 3 stars, 2026-09-10 (Genspark [Trustpilot](https://www.trustpilot.com/review/genspark.ai)): "having so many tools and features can sometimes feel overwhelming, and it's not always easy to know where to find the specific tool you need." #pain
52. Rohith M, 1 star, 2026-05-26 (Bardeen, [Chrome Web Store](https://chromewebstore.google.com/detail/bardeen-automate-browser/ihhkmalpkhkoedlmcnilbbhhbhnicjga/reviews)): "The most complicated UI I have ever seen. I couldn't complete my first action even after spending 15 minutes on it." #pain
53. Dan Pace, 5 stars, 2026-06-23 (Bardeen, Chrome Web Store): "some new configuration is having the same automations cost 2-3x as many credits." #pain
54. Philip, 1 star, 2025-08-24 (Axiom, [Chrome Web Store](https://chromewebstore.google.com/detail/axiom-ai-browser-automati/cpgamigjcbffkaiciiepndmonbfdimbb/reviews); 14 months old): "can this fill forms for me without me needing to setup an entire workflow? doesn't do what i want." #want #language
55. W0RY0, 1 star, 2025-08-21 (Automa, [Chrome Web Store](https://chromewebstore.google.com/detail/automa/infppggnoaenmfagbfknfkancpbljcca/reviews)): "It is a requirement to understand CSS, HTML and javascript at least to a beginner level to be able to use it so it does require coding experience" #objection
56. Daniel Kiss, 5 stars, 2026-03-13 (Do Browser, [Chrome Web Store](https://chromewebstore.google.com/detail/do-browser-ai-browser-age/hjcibkpfgnljonndnnanhkholafmgmip/reviews)): "Love it, and it works seamlessly with my existing ChatGPT subscription." #want #outcome
57. Bruno Costa, 5 stars, 2026-09-24 (rtrvr, [Chrome Web Store](https://chromewebstore.google.com/detail/retriever-ai-browser-agen/jldogdgepmcedfdhgnmclgemehfhpomg/reviews)): "Now that Perplexity Pro started charging for computer use, I was really in need of an alternative for local Scraping sessions and to agentify my browser. The most interesting thing about Retriever.ai is, indeed, the possibility to first do recordings and teach the AI more easily" #alternative #want
58. "Not so easy as it says", 4 tacos, 2026-02-27 (BrowserAct, [AppSumo](https://appsumo.com/products/browseract/)): "I was really hoping that it could be used whithout a degree in programming." #want #language
59. "Couldnt Scrape a Simple Blog", 2 tacos, 2025-10-30 (BrowserAct, AppSumo): "It was cool to watch the live browser move around, but after trying the query five times, it couldn’t do what I wanted. […] In the end, I lost 15,000 credits even though the output was incorrect" #pain
60. James Miera, 2 stars, 2026-05-23 (HARPA, [Chrome Web Store](https://chromewebstore.google.com/detail/harpa-ai-ai-automation-ag/eanggfilgoajaocelnaflolkadkeghjp/reviews)): "the extension is extremely flaky. It won't load or it will seemingly run forever. All with no explanation, or log for troubleshooting for recourse." #pain #want

## 3. Themes across products, ranked by how often they appear and how strongly

The percentages are keyword matches in 1–3 star reviews only. Sample sizes: Claude n=322, ChatGPT n=304, Manus iOS n=216, Genspark iOS n=109. Treat the percentages as rough indicators, not exact measurements.

| Rank | Theme | Evidence | Quotes | What it means for a new product |
|---|---|---|---|---|
| 1 | **The connection between the agent and the browser breaks easily.** This includes pairing failures, "can't reach extension" errors, and updates that break things. | Claude: about 18% of these reviews mention connection problems and 10% say an update broke it. ChatGPT: about 24% mention connection problems, with 49 reviews stuck on the "install the app" message. | #1, #19, #26, #34 | This is the biggest opening. If one desktop app runs its own browser, the fragile chain of desktop app, extension and command-line tool goes away. The app should check its own health, fix problems where it can, and explain failures in plain English. |
| 2 | **Costs are unpredictable, and users pay for failed tasks.** | Credits come up in 45% (Manus) and 58% (Genspark) of negative reviews. The same complaint appears for Perplexity Computer, Lindy, BrowserAct and Bardeen. About 11% of Claude reviews complain about usage running out. | #11, #38, #39, #43, #45, #49, #50, #59 | Running on the subscription the user already pays for is a strong advantage. Also show a cost estimate before each run, let users set a spending limit for each agent, and avoid charging for failed runs where possible. |
| 3 | **Work gets lost: no history, no saved sessions, no record of what happened.** | Claude: about 16%. Manus lost user data. Magical deleted snippets. | #9, #10, #21, #44 | Keep a permanent record of every run that users can replay. Let users resume sessions and export what the agent produced. |
| 4 | **Users are tired of approving every step, but also afraid of what the agent might do.** | Claude: about 10% complain about permission prompts. At the same time, users fear using it on banking pages and fear prompt injection (hidden instructions on a web page that hijack the agent). | #2, #3, #15, #16, #36, #42 | Ask users to approve the overall plan in plain English, not every step. Remember per-site permission rules. Protect banking and payment pages by default. |
| 5 | **Users want agents in separate spaces, running at the same time.** This is the need an orchestrator meets. | Fewer mentions than the themes above, but very strong, and both 1-star and 5-star reviewers raise it. | #4, #5, #6, #19, #28, #34 | Give each agent its own separate browser profile so it runs in the background without taking over the screen. Show all agents on one dashboard. If one agent fails, the others should keep running. |
| 6 | **Setup is built for developers.** | ChatGPT needs a desktop app, Codex and macOS privacy settings. Automa needs CSS and JavaScript. BrowserAct needs a "degree in programming." | #24, #27, #52, #54, #55, #58 | Let users sign in with the subscription they already have, with nothing to configure. Offer templates. Hide model and mode names. |
| 7 | **Vendors remove features or change products without warning.** | Atlas was retired. Comet moved browser control behind credits. Claude removed classic mode and deleted saved shortcuts. | #21, #25, #29, #39 | Position the product as a stable layer that works with any AI model. Users should own their workflows, so their automations keep working when a vendor changes something. |
| 8 | **Account and identity problems.** | Claude: about 7% (the Chrome profile email differs from the email on the paid account). | #13, #14 | Keep the agent's identity separate from the Chrome profile. |
| 9 | **Agents say a task is done when it is not, and make up data.** | Manus, Comet, Claude, BrowserAct. | #44, #59 | Add steps that check the work, save screenshots as evidence, and say "couldn't find" instead of making something up. |
| 10 | **Agents are slow and have to relearn the same task every time.** | Praise for rtrvr's feature that lets users record a task to teach it. | #12, #57 | Save what worked and replay it next time. Let users record a task once to teach the agent. |
| 11 | **Switching to a new browser is costly.** | Atlas users lost bookmarks and passwords. Many reviews say their browser is not supported. | #30, #32 | Import the user's logins and bookmarks. Don't make users give up the browser they already use. |
| 12 | **Support is only AI bots.** | Manus, Perplexity, Magical. | #46 | Real human support can set a product apart. |

## 4. Non-technical reviewers

**What confuses them:**

- Approving low-level technical steps they can't read. They want to approve what the agent intends to do.
- Names of products, modes and models.
- Setup that involves several apps.
- Not knowing what the product is for.
- Credits.
- The agent doing things they did not ask for.

**What delights them:**

- The agent finishing one boring but important form-filling job for them.
- Watching the agent work.
- The agent working in the background, in its own tabs.
- Using the subscription they already pay for.

**The words they use** (useful for marketing copy):

- For the work they want to hand off: "tedious work", "busy work", "mundane tasks", "my daily task on web", "copy-paste grind".
- For the benefit: "saved hours", "cuts my time in half", "my 2nd staff", "secret weapon".
- For frustrations: "babysitting", "goes in circles", "eats/burns tokens", "credits fly", "money grab".
- For fears: "scary", "security nightmare", "trust but verify".
- For what they want: "without needing to setup an entire workflow", "without a degree in programming", "simply ask ai".

**A tension worth noting.** Technical reviewers who give 5 stars often dismiss reviewers who give 1 star ("learn how to use AI"). This gap between experts and ordinary users is exactly the space a product for non-developers can fill.

## 5. Bias in the sample and gaps

- **Sites we could not read:** G2, Capterra, GetApp and TrustRadius blocked access (HTTP 403). Coverage of UiPath, Zapier, Make and n8n is thin.
- **Trustpilot:** quotes come from a summarized version of each page and may be incomplete.
- **Product Hunt:** reviewers are mostly founders and developers, and most reviews are more than 12 months old.
- **App stores:** US data only.
- **ChatGPT Atlas:** the claim that it was retired comes only from what Chrome Web Store reviewers say.
- **Who writes these reviews:**
  - Reviewers of the Claude and ChatGPT extensions are often developers, so setup problems may be overstated compared with what typical consumers experience.
  - Some 5-star reviews are spam.
  - A group of Manus reviews may be coordinated.
  - Trustpilot reviews over-represent billing disputes.
