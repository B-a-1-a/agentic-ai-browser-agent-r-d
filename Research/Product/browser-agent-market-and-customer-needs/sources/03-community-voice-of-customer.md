# Source notes 03: what users say in online communities

These are raw findings from one research stream, collected on 2026-10-12. They are 70 comments copied word for word from Hacker News, the OpenAI, Make and n8n community forums, the Chrome Web Store, Lemmy and Bluesky. All 70 are dated October 2025 to October 2026.

**Important gaps:**

- **No Reddit or X data.** The research tools could not reach reddit.com, and X returned HTTP 402 (a payment-required error). Nobody tried to get around these blocks. This means the subreddits where most non-developers talk are missing: r/ChatGPT, r/ClaudeAI, r/perplexity_ai, r/realtors, r/smallbusiness, r/VirtualAssistant and r/Accounting.
- **Hacker News dominates.** 51 of the 70 entries come from Hacker News, so the sample leans toward developers. Much of the non-technical signal is second-hand, for example a developer describing their spouse, mother or friends.
- **Accuracy of the quotes.** Hacker News, Bluesky and Lemmy text came through public APIs and is exact. Forum posts and Chrome Web Store reviews came through a page-fetch tool, so a small transcription risk remains.

Tags used in the table:

| Tag | Meaning |
|---|---|
| #outcome | A result the user got, or wants |
| #pain | A problem or frustration |
| #want | Something the user asks for |
| #objection | A reason the user hesitates or refuses |
| #trigger | What made the user look for a tool |
| #alternative | Another way the user gets the job done |
| #competitor | A mention of a competing product |
| #language | Wording worth noting because it shows how users describe the job |

## 1. Extracted entries

| # | Source | Date | Verbatim quote | Tags | Profile signals |
|---|---|---|---|---|---|
| 1 | [HN](https://news.ycombinator.com/item?id=45658810) | 2025-10-21 | "I recently used Comet to find out of print movies that were never released on DVD/Bluray, then find them on ebay, then find the best value, then provide me with a list to order. It felt like magic watching it work, and saved me many hours of either doing it myself or scripting it. I did have to repeatedly break it into ever smaller tasks to get everything to fit within the context windows" | #outcome #pain #competitor | Technical; shopping for personal use |
| 2 | [HN](https://news.ycombinator.com/item?id=45664101) | 2025-10-22 | "I had it do a proximity based search for me in Google Maps and then populate a new Google Sheet with this data and it just went off and did it right the first time. […] this is the first truly usable browser automation tool I've ever used and I spent years working with Selenium." | #outcome #competitor (Atlas) | Former Selenium engineer |
| 3 | [HN](https://news.ycombinator.com/item?id=45685396) | 2025-10-23 | "there's no world in which I just hand over my computer and browser with all my logins to an agent - just like I'd never do that with a human. It's insane. […] how do you get your human assistant to book you a flight? They have a corporate credit card with limits on it where they can't spend on just anything." | #objection #want | Technical; compares the agent to a human assistant |
| 4 | [HN](https://news.ycombinator.com/item?id=45659747) | 2025-10-21 | "With these "agentic browsers" you are one prompt injection away from having your data stolen by a malicious website with some form that you cannot see." | #objection | Technical; security-aware |
| 5 | [HN](https://news.ycombinator.com/item?id=45669527) | 2025-10-22 | "What 'tasks' does the average person use browsers for that the model can help with? I'm trying to think of what part of my daily routine would this benefit me and I'm drawing a blank..." | #objection | Technical skeptic |
| 6 | [HN](https://news.ycombinator.com/item?id=46176322) | 2025-12-06 | "It gave me back control to input my username and password, but alas, since I had used my google account to sign in, I had to go through Google login portal, which put an end to my experiment since it deemed the agent's browser wasn't trustworthy." | #pain (login) | Technical |
| 7 | [HN](https://news.ycombinator.com/item?id=46341919) | 2025-12-21 | "I used this in earnest yesterday on my Zillow saved listings. I prompted it to analyze the listings (I've got about 70 or so saved) and summarize the most recent price drops for each one and it mostly failed at the task. It gave the impression that it paginated through all the listings, but I don't think it actually did." | #pain (failure that looked like success) | Former AI skeptic; house hunting |
| 8 | [HN](https://news.ycombinator.com/item?id=46345194) | 2025-12-21 | "I had it navigate a complex ATS and prepare a hiring website (for humans, no less!) and drop in all the JDs, configure hiring settings, etc. It saved me hours of time." | #outcome | Hiring manager or founder |
| 9 | [HN](https://news.ycombinator.com/item?id=46348336) | 2025-12-21 | "My personal benchmark for ChatGPT Atlas and Claude for Chrome is how fast they can run through a list of 100+ Hertz CDP codes scraped from the internet, and narrow down the best offers for a mid-sized SUV rental in my destination. Atlas has problem where it just gives up and quits after a few minutes, but Claude doesn't seem to have a time limit" | #competitor #pain #outcome | Technical; hunting travel deals |
| 10 | [HN](https://news.ycombinator.com/item?id=46345490) | 2025-12-21 | "It's happening on my machine, in the browser I would use to access my accounts, not a middleman that is given access to my accounts. 2. Scheduling! This is a god send to be able to get a digest of everything I need to know for the day." | #want #outcome | Distrusts connectors that link the AI to other services |
| 11 | [HN](https://news.ycombinator.com/item?id=46344476) | 2025-12-21 | "I use it to file taxes: claude reads local pdf files and then writes the numbers in the page" | #outcome | Technical; copies data from local files into web forms |
| 12 | [HN](https://news.ycombinator.com/item?id=46593801) | 2026-01-12 | "I don't think this is for _hard_ things but rather for repetitive tasks, or tasks where a human would bring no value. I've used Claude for Chrome to search for stays in Airbnb for example; something that is not hard but takes a lot of time to do by hand when you have some precise requirements." | #language #outcome | Technical |
| 13 | [HN](https://news.ycombinator.com/item?id=46593428) | 2026-01-12 | "I use claude code to classify my expenses (given a bank statement CSV) for VAT reporting, and fill in the spreadsheet that my accountant sends me. Or for noting down line items for invoices and then generating those invoices at the end of the month. Or even booking a tennis court at a good time given which ones are available" | #outcome | Freelancer (handles VAT and invoices) |
| 14 | [HN](https://news.ycombinator.com/item?id=46594168) | 2026-01-12 | "any security mechanism which relies on users to read and intelligently respond to approval prompts is doomed to fail over time, even if the prompts are well designed. Approval fatigue will kick in and people will just start either clicking through without reading" | #objection #want | Security practitioner |
| 15 | [HN](https://news.ycombinator.com/item?id=46806679) | 2026-01-29 | "Stuff like skip the story and give me the recipe, or click through the pointless extra steps, or reformat my address into the bizarre format the website wants. […] I know exactly what to do, it's just very tedious to actually do it. Which seems like the perfect use case for an agent." | #want #language | Technical |
| 16 | [HN](https://news.ycombinator.com/item?id=46820472) | 2026-01-30 | "Tedium often means a large context window. Lots of personal information to be entered, in different formats, that must be exactly right. Thats exactly what an agent regularly fails at." | #objection | Technical skeptic |
| 17 | [HN](https://news.ycombinator.com/item?id=46806847) | 2026-01-29 | "I use AI-controlled browsers for everyday tasks like "Find me a Michelin starred restaurant in Paris with availability for 4 people at 8PM today". Also for things like locating a product available to pick up in a nearby store" | #outcome | Consumer power user |
| 18 | [HN](https://news.ycombinator.com/item?id=46806766) | 2026-01-29 | "I use claude's chrome plugin all the time. As well Chatgpt's agent mode. I prefer Agent mode when I don't need to login but want it to do search. However, Gemini in Chrome requires you to allow them to use your data to improve their model, which I won't consent to." | #competitor #objection | Pays for more than one AI subscription |
| 19 | [HN](https://news.ycombinator.com/item?id=46806900) | 2026-01-29 | "I've seen at least one decent use case from "normies" around me: Bypassing stupid company processes to achieve actual automated productivity in your rote processes instead of the theatre of it. […] someone who currently doesn't want to spend their own money on something like Claude for Cowork and the Chrome extension to drive the browser, or open a terminal to have Claude Code do it." | #trigger #pain (cost) | Describes non-technical coworkers at a 100-person startup |
| 20 | [HN](https://news.ycombinator.com/item?id=47340970) | 2026-03-11 | "My job relies on following many German laws, bureaucracy pages and the like. […] No tools seem to have a debounce feature, even though I only need to check for updates once per month" | #want #alternative (Wachete) | Publisher who tracks German government pages |
| 21 | [HN](https://news.ycombinator.com/item?id=47546241) | 2026-03-27 | "I also find it more useful that the Chrome MCP uses my current profile since I might want Claude to look at some page I'm already logged in to. […] I mainly use use browser MCP to get around the fact that 30% of servers block agent traffic" | #want #pain (sites block agents) | Developer |
| 22 | [HN](https://news.ycombinator.com/item?id=47783142) | 2026-04-15 | "Twice a day, Claude Cowork searched SpareRoom, OpenRent, Rightmove and Zoopla, filtered out student flats and 3+ bed houses, wrote personalised outreach messages forevery good listing, and emailed me a digest I could act on from my phone." | #outcome #want (scheduled tasks) | Renter in London |
| 23 | [HN](https://news.ycombinator.com/item?id=47784153) | 2026-04-15 | "I didn't give it free reign on my computer due to obvious security concerns so sandboxed it to a docker container instead. I think for a lot of tasks it's probably more trouble to set this up than to just DIY it." | #pain (setup) #alternative | Technical |
| 24 | [HN](https://news.ycombinator.com/item?id=47785456) | 2026-04-15 | "I spent about 40-50 bucks in one week just working through kinks and having it fix itself […] the morning debriefer worked maybe once or twice a week and broke every other morning, telling me that it fixed itself and it would never happen again." | #pain (cost, reliability) | Hobbyist |
| 25 | [HN](https://news.ycombinator.com/item?id=47784780) | 2026-04-15 | "I have it just read and summarise my email, calendar events and git repo in a daily briefing format, it only has readonly access to both, as I dont trust it to do stuff for me or on my behalf." | #objection #want (read-only access) | Developer |
| 26 | [HN](https://news.ycombinator.com/item?id=47785368) | 2026-04-15 | "I find Chrome Claude extension more useful for automating tasks online. Before ai I was writing my own macros which basically did the same thing in a more reliable deterministic way." | #alternative #competitor | Technical |
| 27 | [HN](https://news.ycombinator.com/item?id=47787710) | 2026-04-16 | "The category of task I have it do is basically the pattern of "scrape some certain websites on a regular schedule, do some light data processing/understanding/analyzing, report the result to me [all or sometimes only when there is something worth mentioning]"." | #want (monitoring) | Technical |
| 28 | [HN](https://news.ycombinator.com/item?id=47786987) | 2026-04-16 | "very few people are actually willing to hand over full autonomy to anything where significant value / liability is in play. […] If I can prompt an AI to write an actual deterministic process to solve a problem in a couple of minutes (still potentially AI assisted, just in a deterministic manner), why would I delegate it to a non-deterministic AI?" | #objection #alternative | Technical |
| 29 | [HN](https://news.ycombinator.com/item?id=47797483) | 2026-04-16 | "For old and shitty healthcare websites it's easier to just show the workflow than explain it" | #want (teach by showing) | Builds automation tools; works with healthcare sites |
| 30 | [HN](https://news.ycombinator.com/item?id=47796817) | 2026-04-16 | "Non-technical users expect a CEO's secretary from TV/movies: you do a vague request, the secretary does everything for you. LLMs cannot give you that by their own nature." | #language #objection | Technical skeptic |
| 31 | [HN](https://news.ycombinator.com/item?id=47796899) | 2026-04-16 | "they're very powerful and helpful once people get up and running, but people struggle to get up and running. […] the people who were using Cowork already were mostly blind approving all requests without reading what it was asking." | #pain (getting started) #objection | Set up Cowork for several non-technical friends |
| 32 | [HN](https://news.ycombinator.com/item?id=48753295) | 2026-07-01 | "I was finding it very hard to apply jobs […] I bit a bullet and built this AP application agent and found i got interviewed at Cohere, Scale AI etc. which otherwise I would have never got these calls." | #outcome #trigger | Developer looking for a job |
| 33 | [HN](https://news.ycombinator.com/item?id=48849382) | 2026-07-09 | "just let Cowork spin for 20 minutes, find the best new and best used options that meet your requirements […] I've done it enough that I'm starting to loathe clicking through these sites myself." | #outcome #language | Researches purchases |
| 34 | [HN](https://news.ycombinator.com/item?id=49504911) | 2026-08-31 | "fill out this multistep immigration electronic travel authorisation form using my passport files saved in the folder", it just asks for the relevant info and handles the rest. […] It gets the task done in 5-10 minutes. It's it bit slow since I'm not paying extra for ultrafast mode, but it gets the job done." | #outcome #pain (speed) | Pays for ChatGPT; government form |
| 35 | [HN](https://news.ycombinator.com/item?id=49511632) | 2026-08-31 | "I would never send my passport details to OpenAI. That's a lot of trust you have on the tech and the company behind it." | #objection | Technical |
| 36 | [HN](https://news.ycombinator.com/item?id=49506473) | 2026-08-31 | "There are very few "actual workflows" in many people's lives (especially if you exclude their job), and many many "one off (few off) workflow". That's the magic. […] that's the kind of task that's tedious and done rarely, so a dedicated tool doesn't help because who would be familiar with that tool and have it handy?" | #language #want | Technical |
| 37 | [HN](https://news.ycombinator.com/item?id=49506388) | 2026-08-31 | "The browser mode is great, except its fully banned by Cloudflare. I tried cancelling a phone subscription but Cloudflare stopped it." | #pain (blocked as a bot) | ChatGPT Work user |
| 38 | [HN](https://news.ycombinator.com/item?id=49509719) | 2026-08-31 | "They aren't trivial for non-technical users to setup, hence the demand for systems like Claude Cowork and ChatGPT Work and Grok Bot." | #trigger #alternative | simonw, a well-known technical blogger |
| 39 | [HN](https://news.ycombinator.com/item?id=49622982) | 2026-09-09 | "I asked it to by me concert tickets, it suggested ticket master for 90$ each, I asked it to find cheaper tickets and found something else 70$ each — I found it really convenient. I asked it to check once a day for the next week and notify me of any price changes" | #outcome #want | Consumer who uses Meta's Muse agent |
| 40 | [HN](https://news.ycombinator.com/item?id=49626889) | 2026-09-09 | "Very tedious, but the best way to make sure you don't miss any savings. Today I asked Muse to do it. It was very slow compared to my repetitive tapping, but it clipped every coupon for me after getting my login credentials for the grocery store's website." | #outcome #pain (speed) | Grocery shopper |
| 41 | [HN](https://news.ycombinator.com/item?id=49622920) | 2026-09-09 | "I'm pretty sure if you asked my mom what problems AI could help solve for her, navigating website's purchasing/account flows and directly answering questions about the contents of her email would be #1 and #2." | #want | Speaks for a non-technical parent |
| 42 | [HN](https://news.ycombinator.com/item?id=49616884) | 2026-09-08 | "My wife and tried over the summer. I told her Claude+Siri could do this in 30s, and she would try by hand. 20 minutes later she was done adding each event manually, and I still couldn't get beyond trying to convince Calendar on my iPhone to open an ics" | #pain #alternative (doing it by hand) | Parent; family calendar |
| 43 | [HN](https://news.ycombinator.com/item?id=49617050) | 2026-09-08 | "I personally don't want to trust an AI agent with checkout. research is fine, but I don't want the AI to go on a shopping spree" | #objection (payments) | Technical |
| 44 | [HN](https://news.ycombinator.com/item?id=49621833) | 2026-09-09 | "Highlighting a confirm button existing is recognizing the problem, but isn't a fix. You can see this not working in existing products. Alexa could book a flight for you in 2018. I've never heard of anyone using that feature." | #objection | Technical |
| 45 | [HN](https://news.ycombinator.com/item?id=49904198) | 2026-09-30 | "it goes on it's little cloud computer and completes the booking form then comes back and asks me if it should book it...so annoying. […] login triggers a 2fa code to your email, even tho it has access to your email, it won't get it and enter it, you have to do it" | #pain (too many confirmations, two-step login codes) #competitor (OpenAI Dots) | Early user of OpenAI Dots; travel |
| 46 | [HN](https://news.ycombinator.com/item?id=49910604) | 2026-09-30 | "Simple example is booking a dentist appointment. Email, wait for response, find time on the calendar etc. I don't need to be in the loop for each step and I don't want to have to keep checking myself." | #want (run in the background) | Technical |
| 47 | [HN](https://news.ycombinator.com/item?id=49898223) | 2026-09-29 | "What if it does something I would not have approved and I only found out about it later? […] I would prefer to white list tasks one at a time as I gained trust." | #objection #want | Technical |
| 48 | [HN](https://news.ycombinator.com/item?id=49904634) | 2026-09-30 | "The approval-every-call model does train you to say yes, so it stops being a control. What I've found works better is gating on the class of action rather than each call." | #want (approvals) | Technical |
| 49 | [HN](https://news.ycombinator.com/item?id=49911515) | 2026-09-30 | "Regularly get insurance (car/home) quotes" […] "Negotiate medical bills / help understand bills in general" […] "Taxes and rebates, deal with IRS" […] "So it's practical time saving use cases...not a restaurant reservation or remind me about X or help me clean my mailbox BS cases." | #want | Passes on someone else's wish list |
| 50 | [HN](https://news.ycombinator.com/item?id=49948732) | 2026-10-03 | "The privacy issue blocks me from adopting this or other personal assistants: do I want to give muse my identity data and access to my mail, calendar, and phone so it can do even basic tasks like make appointments or pay bills?" | #objection | Technical |
| 51 | [HN](https://news.ycombinator.com/item?id=49979338) | 2026-10-06 | "People don't care about privacy. They want something that just works." | #language (how people think about trust) | Speaks for parents and Gen Z |
| 52 | [OpenAI Community](https://community.openai.com/t/1364876) | 2025-11-03 | "Just making the browser to apply for 10 jobs can burn at least 7 prompts because every follow-up answer you provide is also counted. I have already maxed out my 40 for this month in 3 days and i have 27 days left of the subscription." | #pain (usage limits) | ChatGPT Plus subscriber applying for jobs |
| 53 | [OpenAI Community](https://community.openai.com/t/1389601) | 2026-08-08 | "Agent Mode had a very specific capability: it spawned a virtual computer, opened a real browser, visually interpreted rendered websites, clicked through interfaces, handled dynamic UIs, and could hand control to the user for authentication before continuing. […] So this was not a migration. A distinct capability was simply removed." | #pain (feature removed) #competitor | Paying user; researches online stores and shipping options |
| 54 | [OpenAI Community](https://community.openai.com/t/1395620) | 2026-09-07 | "He is not interested in AI technology. He just wants to say: "Translate this Swedish description and find the image for this article number." When I showed him Work, he saw the number of settings and options and immediately felt that he would first have to learn how the system works. So he went back to normal Chat. The capability was useful to him. The interface created the barrier. […] Asking for help should be faster than doing it myself" | #language #pain (interface) #want | Retail manager at a sports webshop who pays for ChatGPT himself; non-technical (described by his partner) |
| 55 | [OpenAI Community](https://community.openai.com/t/1399157) | 2026-09-19 | "Some of us simply want to turn a repeated task into a reliable tool. […] I do not want it to stop halfway. […] choose a tool → provide the input → receive the completed result." | #want (reusable, reliable tools) | Small-business owner (quotations, payment vouchers, work orders); not a developer |
| 56 | [OpenAI Community](https://community.openai.com/t/1386922) | 2026-07-15 | "ChatGPT Work can connect apps, files, and the web, but it still feels less continuous than Comet as an everyday agent for authenticated browsing." | #competitor | Power user |
| 57 | [OpenAI Community](https://community.openai.com/t/1387898) | 2026-07-22 | "We trusted OpenAI enough to make Atlas our main browser. Please don't take that experience away from the users who want to stay." | #pain (feature removed) | Used Atlas every day |
| 58 | [Chrome Web Store: Claude](https://chromewebstore.google.com/detail/claude/fcoeoabgfenejglbffodgkkbkcdhcgfn/reviews) | 2026-10-08 | "I just used it to fill out all the credentialing applications for my professional license. Inputting hundreds of information is so tedious, but this literally saved hours of doing this tedious work. I love you, Claude!" | #outcome | Licensed professional |
| 59 | Chrome Web Store: Claude | 2026-10-08 | "I am impresed how this thing filled my German tax declaration." | #outcome | Consumer; government website |
| 60 | Chrome Web Store: Claude | 2026-10-10 | "cuts my time in half by automating the work in dedicated browser tabs, while i can do my work in other tabs with out getting interlinked or disturbed" | #want (run in the background) #outcome | Knowledge worker |
| 61 | Chrome Web Store: Claude (2.9 out of 5 from 1,800 ratings) | 2026-10-12 | "it never works" | #pain | Unknown |
| 62 | [Chrome Web Store: Do Browser](https://chromewebstore.google.com/detail/do-browser-ai-browser-age/hjcibkpfgnljonndnnanhkholafmgmip/reviews) | 2026-03-13 | "Love it, and it works seamlessly with my existing ChatGPT subscription." | #want (use the subscription I already have) | Pays for ChatGPT |
| 63 | [Chrome Web Store: dassi](https://chromewebstore.google.com/detail/dassi-ai-agent-for-chrome/bjcngahpcjeililljmfegmlanlpgibdi/reviews) | 2026-07-10 | "I gave it a simple prompt to research leads and compile contact info from LinkedIn and company sites. It just went and did it. Navigated pages, scrolled, copied data, built me a spreadsheet. No coding, no macros, no BS. […] The fact that I can bring my own API key sealed the deal for me." | #outcome #language | Sales or lead generation; does not code |
| 64 | Chrome Web Store: dassi | 2026-07-30 | "Their pricing model is a scam" | #objection (pricing) | The reviewer misunderstood the pricing: the plan where you bring your own API key does not include AI usage |
| 65 | [Chrome Web Store: Retriever](https://chromewebstore.google.com/detail/retriever-ai-browser-agen/jldogdgepmcedfdhgnmclgemehfhpomg/reviews) | 2026-09-24 | "Now that Perplexity Pro started charging for computer use, I was really in need of an alternative for local Scraping sessions and to agentify my browser. The most interesting thing about Retriever.ai is, indeed, the possibility to first do recordings and teach the AI more easily, especially when the pages are complex" | #trigger (cost) #want (teach by showing) #competitor | Heavy user of web data collection |
| 66 | [Make Community](https://community.make.com/t/107163) | 2026-04-08 | "I want my Make AI Agents log in specific websites (with credentials as sources), then do some actions on them". A Make partner replied: "A make agent essentially can only make API calls use existing modules in make.com. There is not a proper agent browser login like you could have with a native openclaw or other." | #want #alternative (Make cannot do this) | Builds automations without code |
| 67 | [n8n Community](https://community.n8n.io/t/269236) | 2026-02-24 | "I've been working with a client in healthcare who's stuck on a legacy software with no API. We spent weeks trying browser automation and it was a nightmare." | #pain #alternative | Automation consultant |
| 68 | [Lemmy](https://lemmy.world/comment/20557596) | 2025-11-18 | "They work by letting the AI continuously see everything your browser can see, such as your emails, banking details, financial habits, online shopping accounts, etc." | #objection | Privacy-minded user |
| 69 | [Lemmy](https://mander.xyz/comment/23967114) | 2025-12-17 | "Seems useful if done privately and under supervision: […] can fill out forms (eg. you can dump unstructured text and have it fill, instead of copying field by field)" | #want #objection | Has only read about Comet |
| 70 | [Bluesky](https://bsky.app/profile/tauruscoder.bsky.social/post/3mmbk72xl6e2h) | 2026-05-20 | "Spent 3 hours "delegating" to an AI agent that kept asking me for clarifications. Faster to do it myself? Yes. But now the agent handles it solo. That 3h was training, not wasted time." | #pain #outcome | Developer |

## 2. Themes, ranked by how often they appear and how strongly people feel

Counts are out of the 70 entries above. Intensity means how strong the emotion is in the wording.

| Rank | Theme | Entries | Intensity | Example quotes |
|---|---|---|---|---|
| 1 | The agent wins on boring jobs that span many steps and many sites | 20/70 (#1, 2, 8–13, 15, 17, 22, 32–34, 39, 40, 58–60, 63) | Medium-high | "I know exactly what to do, it's just very tedious to actually do it." (#15) |
| 2 | Trust, security and privacy, with a firm line at payments | 16/70 (#3, 4, 10, 14, 18, 25, 28, 31, 35, 43, 44, 47, 50, 51, 68, 69) | High | "research is fine, but I don't want the AI to go on a shopping spree" (#43) |
| 3 | The agent is unreliable, and it sometimes fails in ways that look like success | 10/70 (#1, 7, 9, 16, 24, 26, 42, 55, 61, 67) | High | "It gave the impression that it paginated through all the listings, but I don't think it actually did." (#7) |
| 4 | Slow, needs watching, "faster to do it myself" | 8/70 (#23, 24, 34, 40, 42, 45, 54, 70) | Medium-high | "Asking for help should be faster than doing it myself" (#54) |
| 5 | Scheduled and repeated checks of websites. This is the clearest sign of a habit forming. | 8/70 (#7, 10, 20, 22, 27, 39, 46, 49) | Medium-high | "check once a day for the next week and notify me of any price changes" (#39) |
| 6 | Vendors remove products, and users compare competitors | 8/70 (#1, 2, 9, 18, 53, 56, 57, 65) | Medium-high | "A distinct capability was simply removed." (#53) |
| 7 | What people use instead: doing it by hand, macros, scripts written by AI, Make or Zapier (which cannot log in to websites) | 8/70 (#20, 23, 26, 28, 38, 42, 66, 67) | Medium | "why would I delegate it to a non-deterministic AI?" (#28) |
| 8 | How approvals work: people either approve everything without reading, or get annoyed by repeated confirmations | 7/70 (#3, 14, 31, 44, 45, 47, 48) | Medium-high | "gating on the class of action rather than each call" (#48) |
| 9 | Getting into sites: bot blocking, CAPTCHAs, logins, two-step login codes, sites without an API | 7/70 (#6, 21, 37, 45, 53, 66, 67) | Medium-high | "fully banned by Cloudflare" (#37) |
| 10 | Cost, usage limits and confusing pricing | 7/70 (#19, 24, 52, 62–65) | Medium-high | "works seamlessly with my existing ChatGPT subscription" (#62) |
| 11 | Setup is too hard for non-technical users | 7/70 (#19, 23, 30, 31, 38, 54, 55) | High for our target users | "The capability was useful to him. The interface created the barrier." (#54) |
| 12 | Running in the background or in parallel, using the user's own files and logins | 6/70 (#10, 11, 21, 34, 46, 60) | Medium | "I don't want to have to keep checking myself" (#46) |
| 13 | Reusable workflows, and teaching the agent by showing it | 4/70 (#27, 29, 55, 65) | Medium | "easier to just show the workflow than explain it" (#29) |
| 14 | "What would I even use this for?" | 4/70 (#5, 16, 30, 44), plus many similar comments not in the table | Medium | "I'm drawing a blank..." (#5) |

**How technical and non-technical users think about trust:**

- **Technical users** contain the risk. They run agents in an isolated environment, use a separate browser profile, use read-only access, or block their bank's website.
- **Non-technical users** talk about results and simplicity. They rarely mention security.
- **What technical users say about non-technical users:** "People don't care about privacy" (#51) and "blind approving" (#31). The counter-signal: "Even my parents are wary of their products" ([HN](https://news.ycombinator.com/item?id=49623612)).
- **Both groups** draw the same line at giving the agent payment cards or passport details (#35, #43).

**Words people use for the job:**

- "tedious", "repetitive tasks", "clicking through these sites", "rote processes"
- "the trivial stuff", "digital drudgery"
- "one off (few off) workflow"
- "a CEO's secretary"
- "treat it as a new employee during a trial period"
- "janky magic", "agentify my browser"
- "No coding, no macros, no BS"
- Non-technical users name the document they need, such as a "quotation", "tax declaration" or "credentialing applications". They do not say "agent".

## 3. Top tasks people want automated

These counts come from about 125 items: the 70 entries above plus other comments that support them. One comment can count toward more than one task.

| Rank | Task | Mentions |
|---|---|---|
| 1 | Travel, reservations and appointments | ~16 |
| 2 | Scheduled monitoring and alerts (listings, price drops, items back in stock, legal and government pages, daily digests) | ~15 |
| 3 | Filling in forms (job and license applications, tax, immigration and other government websites). 7 of these involve government or tax websites. | ~13 |
| 4 | Shopping research, comparing deals and prices, and buying | ~13 |
| 5 | Office admin inside web apps (invoices, VAT, quotations, applicant tracking systems, online shop product data, old systems without an API) | ~11 |
| 6 | Web research saved to a spreadsheet, collecting data from websites, lists of sales leads | ~10 |
| 7 | Email, calendar and personal admin briefings | ~8 |
| 8 | Sales outreach, finding prospects, posting on social media | ~6 |
| 9 | Job applications and recruiting | ~6 |
| 10 | Bills, subscriptions, insurance quotes, medical bills | ~6 |
| 11 | Grocery orders and coupons | ~4 |

Not ranked: developers testing their own web apps (6 or more mentions, all from developers).

## 4. Bias in this sample

- No Reddit or X data (see the top of this file).
- Hacker News is 51 of the 70 entries, so the sample leans toward developers. One HN user put it this way: "We aren't representative of what normal people will use or prefer."
- Some startup extensions show bursts of 5-star reviews in a short period (for example dassi in early July 2026). Some of those reviews may have been requested by the company.
- Forum posts lean toward feature requests. Lemmy users lean against AI.
- Some HN commenters build competing tools.
- Background claims about products come from forum posts and HN threads, not from official vendor pages. Examples: OpenAI's Dots, Meta's Muse, and Perplexity Pro charging for computer use.
