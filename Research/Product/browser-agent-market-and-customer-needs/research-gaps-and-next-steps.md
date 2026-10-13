# Research gaps and next steps

This file covers three things:

- what this study could not answer
- which of the team's beliefs to test, and what evidence would show each belief is wrong
- a plan for direct research: interviews and a survey

The interview and survey plan follows Mode 3 of the customer-research skill (`.agents/skills/customer-research/references/interviews-and-surveys.md`).

## 1. What we still don't know

| Gap | Why it matters | How to close it |
|---|---|---|
| **We heard very little directly from non-technical users.** Our tools could not reach Reddit or X. Most of what we know about non-developers comes from store reviews, surveys, or other people describing them. | Our target customer is non-developers. Rankings built mostly from developer and Hacker News comments may put the wrong problems first. | Do Sales Safari by hand (see section 3). Run interviews (section 4). |
| **Willingness to pay on top of an existing AI subscription** | Vibe Kanban, a free tool for coordinating agents, shut down because its users would not pay. If the customer's own subscription pays for the AI, our app has to earn money on its own value. | Interview questions on spending and alternatives. A fake-door pricing test (a pricing page that measures interest before the product exists). A survey question asking about price in ranges. |
| **Whether non-developers value one dashboard that works across AI vendors** | This is the clearest gap in the market, but we found little evidence that customers ask for it. | Interviews: ask how many AI subscriptions they pay for, and what they do when one hits its usage limit or changes. |
| **How many people pay for more than one AI subscription** | Running across vendors only matters for this group. | Survey. |
| **Whether a logged-in local profile gets blocked less than a cloud browser** | Our positioning assumes running locally is more reliable. We have not tested this. | Run a technical experiment (section 6). |
| **How fast parallel agents use up subscription limits** | Plus has a 5-hour cap, and Pro users run out of tokens. Running agents in parallel could hit those caps within minutes. | Run a technical experiment (section 6). |
| **The legal and policy position of each way to use a customer's own subscription** | Anthropic changed its policy at least 5 times in 2026. Google has banned users. OpenAI's commercial sign-in is limited to approved partners. | Review the terms with a lawyer. Apply to OpenAI's commercial "Sign in with ChatGPT" trial. Ask Anthropic and Google directly. |
| **Data from G2, Capterra, and TrustRadius** | These sites blocked our research tools. Business-buyer views of Zapier, Make, n8n, and UiPath are thin. | Read them by hand in a normal browser. Concentrate on 3- and 4-star reviews of competitors. |
| **The words customers use, by segment** | The quote bank leans toward developers and power users. | Interviews and Sales Safari. |
| **Single-source or conflicting market numbers** | Several figures rest on one source, including ChatGPT Agent's roughly 75% drop, Comet's monthly active users, and ChatGPT Work's 10 million users. | Check them against primary sources before anyone outside the team sees them. |

## 2. Beliefs to try to disprove

The skill's rule is "prove yourself wrong, not right." For each belief, decide in advance what evidence would show it is wrong.

| # | Our current belief | Evidence that would show it is wrong |
|---|---|---|
| H1 | Non-developers who pay for AI have recurring browser chores that they would hand to an agent. | Fewer than about 1 in 3 interviewees can name a recurring web chore from the last month. Or most say "I'd just do it myself." |
| H2 | Monitoring websites and sending an alert when something changes is the job most likely to become a habit. | Interviewees rank one-off form filling or research far above monitoring. Or nobody can name a site they check repeatedly. |
| H3 | Running agents in the background, each in its own separate browser, matters more to non-developers than speed. | Interviewees say they would rather watch the agent work, or they care mostly about speed. |
| H4 | "Works with the AI plan you already pay for" makes people more likely to buy. | Interviewees don't know their plan's limits or don't care. Or they would happily pay us for usage if the price is clear. |
| H5 | Proof that a task was done (evidence, plus "couldn't do X") builds more trust than a higher success rate. | Interviewees ignore the evidence and only care whether the task succeeded. |
| H6 | Non-developers will accept approvals by type of action (read: no approval; write: ask; pay: always stop) instead of approving every step. | Interviewees want to approve every step, or want no approvals at all. |
| H7 | People want one dashboard across AI vendors. | Most interviewees pay for only one AI subscription and are loyal to it. |
| H8 | Users would pay at least about $10–20 a month on top of their AI subscription. | Most interviewees name $0–5, or say the AI vendor should include this for free. |

## 3. Sales Safari by hand (do this first, about 1 day)

Sales Safari, a method from Amy Hoy, means reading where your customers already talk, without asking them anything. Read the communities our tools could not reach. For each useful post, record: Source, Date, Verbatim quote, Tags (#pain #trigger #outcome #language #alternative #objection), and Profile signals.

**Where to read:**

- **AI subscriber communities:** r/ChatGPT, r/ChatGPTPro, r/ClaudeAI, r/perplexity_ai, r/GeminiAI. Search for "agent mode", "Atlas", "Comet", "Claude in Chrome", "Cowork", "ChatGPT Work", "automate", and "every week I have to".
- **Non-technical job communities:** r/realtors, r/smallbusiness, r/Entrepreneur, r/VirtualAssistant, r/Accounting, r/recruiting, r/sales, r/ecommerce, r/nursing, r/Teachers. Search for "repetitive", "portal", "copy paste", "data entry", "every month", "is there a way to automate".
- **Automation communities:** r/nocode, r/automation, r/zapier, r/n8n, r/AI_Agents. Search for "browser", "login", "no API", "Zapier can't".
- **X:** search for `"agent mode" OR "Comet" OR "Claude in Chrome" (useless OR "saved me" OR "wish it")`.
- **G2 and Capterra:** read 3- and 4-star reviews for Zapier, Make, Bardeen, Axiom, and UiPath.

**Goal:** 30–50 entries from non-developers. Then compare them with the needs ranking in [`customer-needs-synthesis.md`](customer-needs-synthesis.md). Note any ranking that changes.

## 4. Interviews (10 per segment is the aim; 5 is enough)

### Who to recruit

Screen for people who meet all of these:

- pay for at least one AI subscription themselves
- do not write code for work
- spend more than 3 hours a week in web apps or on web portals for work or personal admin

Aim for this mix:

- **Segment A:** admin-heavy independent professionals, such as freelancers, licensed health professionals, consultants, and realtors.
- **Segment B:** people who run or operate a small business, such as online shop owners, office or operations managers, and sales or lead-generation staff.
- **Segment C:** people who handle a lot of personal admin, such as someone currently searching for a rental, planning travel, or looking for a job.
- **Plus 3–5 current users of browser agents** (Claude in Chrome, Comet, ChatGPT Work, Cowork), including people who **stopped** using one.

**Where to find them:**

- the team's own networks
- the people who wrote the reviews in [`data/store-reviews.csv`](data/store-reviews.csv), where the platform allows contact
- the communities listed in section 3
- a paid panel such as User Interviews or Respondent, if the budget allows

**Incentive:** $50 for a 30-minute call. At the end of every call, ask "Who else should we talk to?"

### Outreach message

Do not use the words "research study". The goal is a casual chat.

```
Subject: Quick favor — 30 min, on us

Hi [First name],

I'm [name]. We're building something to take tedious website chores off
people's plates, and I'd love to hear how you handle that stuff today —
what's annoying, what you've tried, what you wish existed. No pitch.

As a thank-you I'll send a $50 [gift card].

Would [day] or [day] work? Here's my calendar: [link]

Thanks either way,
[Name]
```

### Interview guide

Ask about what people have actually done, not what they say they would do. Don't pitch the product, and don't describe our solution until the last 5 minutes, if at all.

1. **Warm-up (2 minutes).** "Walk me through what a normal week looks like for you, work and personal admin."
2. **Find the chore (8 minutes).**
   - "Tell me about the last time you had to do something tedious on a website. What was it? How long did it take?"
   - "What other website chores keep coming back? Weekly? Monthly? Once a year?"
   - Keep asking why (3–5 times): "Why did that one matter? What happens if it doesn't get done? Who notices?"
3. **What they do today (5 minutes).**
   - "How do you handle it today? Have you tried anything to make it easier: a VA, Zapier, ChatGPT, a browser extension, a script someone wrote?"
   - "What happened? Why did you stop?" Then ask why again.
4. **Their AI subscriptions (5 minutes).**
   - "Which AI tools do you pay for? Who pays for them? What do you mostly use them for?"
   - "Have you ever hit a usage limit? What did you do?"
   - "Have you tried letting it act in your browser, such as agent mode, Comet, Claude in Chrome, or Cowork? Tell me about the last time." If they stopped: "What made you stop?"
5. **Trust and control (5 minutes).**
   - "Imagine someone else did that chore for you. What would you need to see afterwards to believe it was done right?"
   - "What would you never let an assistant do without asking you?"
   - "Have you ever been burned by software doing something on your behalf?"
6. **Value (3 minutes).**
   - "If that chore just happened every week without you, what would it be worth to you?"
   - "What do you pay today for things that save you time?"
7. **Close (2 minutes).** "Who else do you know who deals with this kind of thing? Could you introduce us?"

**Questions that could prove us wrong.** Ask these in every interview:

- "Is there anything here you'd honestly rather keep doing yourself?" (tests H1)
- "Would you rather watch it work or get a notification when it's done?" (tests H3)
- "If it showed you proof it finished but took twice as long, would that be better or worse?" (tests H5)

### After the interviews

Analyze each interview using Mode 1 of the skill:

- the job the person is trying to get done: what they need to do (functional), how they want to feel (emotional), and how they want others to see them (social)
- their pains, triggers, desired outcomes, exact language, and alternatives

Then update the confidence labels in the synthesis. Evidence from these interviews outweighs evidence scraped from websites when the two conflict.

## 5. Survey (after about 5 interviews, n = 150–300)

Keep it under about 3 minutes. Offer $5 per completed response. Prefer open-ended questions where we want customers' own words.

1. Screener questions:
   - Which AI tools do you pay for yourself? (multi-select, with "employer pays" as a separate option)
   - Do you write code for work? (yes/no)
2. In the last month, which of these did you do on a website? How often? List the top 8 tasks from the synthesis and add an "other" option.
3. Open-ended: "Describe the most tedious thing you did on a website in the last month."
4. How do you handle it today? (by hand / VA or assistant / Zapier or Make / AI chat / AI browser agent / other)
5. Have you used an AI agent that acts in your browser? Choose one: yes, still / yes, stopped / no. If stopped, why? (open-ended)
6. **For current agent users only:** "How would you feel if you could no longer use [their agent]?" (very / somewhat / not disappointed). This is the Sean Ellis product–market fit question, applied to competitors. It shows how loyal users are to the tools we would compete with.
7. Which of these would you let an assistant do **without asking you first**? (read and summarize / fill a form but not submit / submit a form / send a message / buy something under $25 / buy something over $25)
8. How would you prefer to pay for a tool like this? (use my existing AI plan / flat monthly fee / pay per task / wouldn't pay). Then ask what monthly price would feel fair, as a range.

Analyze the results separately by segment and by whether the person currently uses an agent.

## 6. Experiments to run next

Per AGENTS.md, each experiment needs its own directory. These are suggestions only; none has been created yet.

| Proposed directory | Question | Rough design |
|---|---|---|
| `Experiments/local-profile-vs-cloud-browser-blocking/` | Does running in a logged-in local Chromium profile get blocked less by login screens and bot detection than a cloud browser? | Run the same 20 real tasks (forms, retail, travel, government portals) in a local profile and in a cloud browser. Record success, CAPTCHAs, blocks, and login failures. |
| `Experiments/subscription-limit-burn-rate/` | How many browser tasks running in parallel can Plus, Pro, and Max plans support before hitting usage caps? | Run 1, 3, and 5 agents in parallel on standard tasks through each permitted way of using the customer's own subscription. Measure how long until the cap is hit. |
| `Experiments/run-evidence-review-prototype/` | Does a review screen showing proof of completion (counts, screenshots, fields submitted, "couldn't do X") increase trust? | Clickable prototype. 5–8 non-developer users. Compare it with a plain "Done ✓" screen. |
| `Experiments/action-class-approvals-prototype/` | Do non-developers understand and accept approvals by type of action (read, write, pay)? | Clickable prototype of an approval inbox. Test whether users understand it and whether they approve without reading. |
