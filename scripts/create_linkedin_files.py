import os

POSTS = {
    "aleyda-solis": [
        {"url": "https://www.linkedin.com/posts/aleyda_how-to-measure-success-in-ai-search-ill-share-7472178248383270912-SRFH",
         "date": "approx 2026-06-15",
         "body": "How to Measure Success in AI Search? I'll share the 3 Layer Framework to Measure AI Presence, Readiness and Business Impact I use with the AI Search Leaders community later this week! If you're not yet there, join now: searchleaders(.)ai - Thanks Tom Critchlow & Jeremy Cabral for having me!"},
        {"url": "https://www.linkedin.com/posts/aleyda_seofomo-share-7471961329143222272-2xdx",
         "date": "approx 2026-06-14",
         "body": "The Latest SEO & AI Search News of the Week [From #SEOFOMO - June 14, 2026]. Google adds guidance on third-party SEO tools. Google can be directly liable for false AI Overview claims: German court. Apple introduced Siri AI at WWDC: what Apple's Gemini-Powered Siri means for search visibility. In 2026, less than one-third of Google searches still send a click. Google is building an Audience Loyalty ecosystem. The SERP is sinking: what pixel depth data reveals about visibility. How to build a representative AI Search prompt library for better AI visibility measurement. Much more, including SEO & AI Search jobs, tools, events. Link in comments."},
        {"url": "https://www.linkedin.com/posts/aleyda_a-useful-and-often-underused-input-for-share-7471063307890749440--k7e",
         "date": "approx 2026-06-12",
         "body": "A useful and often underused input for your AI Search prompt library: question based queries that trigger Google AI Overviews, identified through keyword research tools with SERP feature filters. In this case, using Semrush Keyword Magic Tool. PS: I've recently published a Guide about How to Build a Representative AI Search Prompt Library for Better AI Visibility Measurement. Take a look at it in comments."},
        {"url": "https://www.linkedin.com/posts/aleyda_the-llms-have-caused-enough-damage-to-publishers-share-7470746981372698624-QBkV",
         "date": "approx 2026-06-11",
         "body": "The LLMs have caused enough damage to Publishers and it's time to take a stand - a proposal to help publishers fight back by Shahzad Abbas / Define Media Group. The infrastructure, platforms and standards are in place right now to help publishers manage bot traffic and develop leverage to receive fair value for their original content. Most LLMs provide almost no meaningful traffic or revenue to publishers. A strong, multi-layered bot defense system is the only way to prevent wholesale theft of publisher content from crawlers. Publishers must develop an LLM value framework. Many bots don't respect robots.txt. Google is moving towards an AI chatbot interface; if referrals collapse further, publishers should consider blocking Googlebot as well."},
        {"url": "https://www.linkedin.com/posts/aleyda_google-is-building-an-audience-loyalty-share-7470485506997456896-LfDl",
         "date": "approx 2026-06-11",
         "body": "Google is building an Audience Loyalty ecosystem - a must read analysis from Barry Adams where he shares how a common thread among many new Google features is how they enable publishers to build loyal audiences across all Google surfaces: 1. Preferred Sources 2. Search Profiles 3. Subscription Linking. Not Traffic. Loyalty."},
    ],
    "lily-ray": [
        {"url": "https://www.linkedin.com/posts/lily-ray-44755615_the-media-is-finally-catching-onto-the-popular-ugcPost-7470498942439378945-zrp_",
         "date": "approx 2026-06-11",
         "body": "The media is finally catching onto the popular SEO/GEO tactics that companies have been using to manipulate AI answers. I was interviewed for this new article by Will Oremus of The Atlantic, which discusses self-promotional listicles, Reddit astroturfing and other common ways to influence AI responses. The author even included a mention of my AI Overview joke experiment from last year. Just checked and the experiment still works, over a year later. I keep tabs on this stuff daily and the results are gradually getting better, but I'm surprised how long it's taking them to crack down on this wave of spam, especially given how front and center these answers are for the user. Link to article in the comments."},
        {"url": "https://www.linkedin.com/posts/lily-ray-44755615_heres-a-little-hack-ive-been-using-to-quickly-share-7470166065856032768-Are4",
         "date": "approx 2026-06-10",
         "body": "Here's a little hack I've been using to quickly convert SEO keywords into relevant AI prompts at scale directly in Google Sheets. Use the =AI or =Gemini function plus a prompt to convert your SEO keywords into the natural-language ways users might type or ask that same question into an AI assistant. It lets you take keywords with real search volume (Ahrefs, Semrush, Similarweb) and convert them into AI prompts at scale. The prompt asks the model to rewrite a terse SEO keyword as a single conversational question that preserves the exact search intent, keeps any brand or location named, invents no new specifics, and returns only the rewritten prompt as plain text."},
        {"url": "https://www.linkedin.com/posts/lily-ray-44755615_these-are-3-well-known-brands-that-are-also-ugcPost-7469712876065189888-TQuT",
         "date": "approx 2026-06-08",
         "body": "These are 3 well-known brands that are also listed as case studies of AI content scaling tools. They scaled a lot of page templates that can manipulate AI answers, like excessive 'best X' content, self-promotional listicles, scaled comparison/alternative pages. There's also some spammy structured data in the mix. Each site was hit hard by the Jan 20 update this year and the crash has continued since. Even though the AI content generation appears isolated to one subfolder, the impact is happening across the full domains. All companies are now at the lowest organic search visibility they've seen in 5+ years. I think Google is making new changes related to 'inauthentic mentions.' I'm working on that research now."},
        {"url": "https://www.linkedin.com/posts/lily-ray-44755615_new-ai-reporting-features-are-finally-coming-share-7467840413630947328-FaU-",
         "date": "approx 2026-06-08",
         "body": "New AI reporting features are finally coming to GSC. Reporting on impressions and not clicks says a whole lot here. Looks like there's no queries being shown either. But yes, grateful to have any AI reporting at this point."},
        {"url": "https://www.linkedin.com/posts/lily-ray-44755615_this-is-a-super-cool-development-google-share-7468390271601242112-hGQW",
         "date": "approx 2026-06-08",
         "body": "This is a super cool development - Google is officially launching publisher profile pages within Google Discover for qualified publishers with a big social or video following. Publishers can show their articles, videos and social posts in one place, and claiming a profile can help earn or enhance a Knowledge Panel. Another example of Google bridging the gap between search and social media, tied to years of E-E-A-T changes showcasing brands, publishers, authors and their social profiles within search. Google search is increasingly personalized around the brands and people users choose to follow."},
    ],
    "mike-king": [
        {"url": "https://www.linkedin.com/posts/michaelkingphilly_just-saw-a-great-talk-from-george-at-ramp-share-7470956051878711297-vGfX",
         "date": "approx 2026-06-12",
         "body": "Just saw a great talk from George at Ramp where he talked about how they tested incentives for AI agents to see how they impacted citation. Fantastic research!"},
        {"url": "https://www.linkedin.com/posts/michaelkingphilly_were-throwing-an-zero-click-eve-event-with-share-7470195326574931969-6cVT",
         "date": "approx 2026-06-10",
         "body": "We're throwing a Zero Click Eve event with the Profound team tomorrow. And you know I said 'so, we gonna have the game on the TVs, right?' We're at the Garret tomorrow night from 7-10. Come talk AI, Search, the Knicks and drink for free."},
        {"url": "https://www.linkedin.com/posts/michaelkingphilly_heads-up-ive-changed-my-handle-on-the-social-share-7467972100390117377-bfao",
         "date": "approx 2026-06-08",
         "body": "Heads up. I've changed my handle on the social medias."},
        {"url": "https://www.linkedin.com/posts/michaelkingphilly_the-open-web-is-dying-not-slowing-not-ugcPost-7465056029198708736-_pgr",
         "date": "approx 2026-06-01",
         "body": "The open web is dying. Not slowing. Not changing. Dying. According to Cloudflare, AI bot traffic grew 187% last year. Human traffic grew 3.1%. The next medium has already arrived. The market hasn't named it yet, so I went ahead and did it. We are shifting into a new era that I'm calling 'Machine Media.' Let's talk about it."},
        {"url": "https://www.linkedin.com/posts/michaelkingphilly_i-have-some-detailed-thoughts-on-the-generative-share-7462858700777639937-gKs6",
         "date": "approx 2026-05-25",
         "body": "I have some detailed thoughts on the generative UI announcement from yesterday but I'm worried that 4 posts in 2 weeks from me is too much for y'all."},
    ],
    "eli-schwartz": [
        {"url": "https://www.linkedin.com/posts/schwartze_the-most-common-misdiagnosis-in-seo-right-share-7470769755310759936-rpWv",
         "date": "approx 2026-06-14",
         "body": "The most common misdiagnosis in SEO right now is treating 'best [product category]' and '[Brand A] vs [Brand B]' queries as a technical problem. I keep having the same conversation with companies that hire consultants to audit their way to the top of these rankings, and it never works, because no audit fixes the actual problem. The pages that own these queries are not there because their schema is correct or their page speed is fast. They are there because their products are discussed, reviewed honestly, and cited repeatedly by sources with no stake in the outcome. This is a PR and brand problem being handed to the wrong team with the wrong tools."},
        {"url": "https://www.linkedin.com/posts/schwartze_many-companies-should-not-hire-an-seo-consultant-share-7470768717421985792-b3pc",
         "date": "approx 2026-06-14",
         "body": "Many companies should not hire an SEO consultant or agency. I say this in many meetings when companies reach out, but now Google is saying it too. The number one deciding factor in whether you should hire an outside agency is not whether you are a small business, but the expected ROI. Don't spend more on the channel than you can potentially get back. Looking forward to the comments from agencies telling me how wrong I am."},
        {"url": "https://www.linkedin.com/posts/schwartze_i-dont-know-anyone-who-actually-uses-perplexity-share-7470724215462244353-IjA0",
         "date": "approx 2026-06-12",
         "body": "I don't know anyone who actually uses Perplexity for search. Perplexity raised a ton of money to beat Google, so I pulled Similarweb data. Perplexity is at around 150 million monthly visits. That sounds impressive until you put it next to Google's 80+ billion monthly visits. The product is good, but 'objectively good' and 'what people actually use' have almost nothing to do with each other in consumer search. Just ask Bing. Having a great product pales in comparison to having great distribution. Unless someone can beat Google at distribution, Google stays dominant. Is anyone in your network actually using it regularly?"},
        {"url": "https://www.linkedin.com/posts/schwartze_companies-are-about-to-waste-a-lot-of-money-share-7470720953803776000-rAaU",
         "date": "approx 2026-06-12",
         "body": "Companies are about to waste a lot of money hiring for AEO. They're pulling out old SEO job descriptions, crossing out 'keyword rankings,' typing 'prompt visibility,' and convincing themselves they've modernized. This will not work. The person you want for AEO doesn't come from a content agency, nor is it a technical SEO with AEO certifications stapled to their resume. Just like with SEO, the profile that produces results looks exactly like a product manager. SEO managers who move the needle aren't the ones who know the most technical tricks, it's the ones with the most customer empathy who understand user journeys. That skill transfers directly to the AI era."},
        {"url": "https://www.linkedin.com/posts/schwartze_google-didnt-just-update-search-at-io-2026-share-7469854035198742528-Dqop",
         "date": "approx 2026-06-11",
         "body": "Google didn't just update Search at I/O 2026. It changed it. AI Mode is expanding into the core search experience, and the agents behind it now crawl the web and answer for users in the background, before anyone reaches your page. If you're still grading yourself on rankings and traffic, you're scoring a game that no longer exists. The move from SGE to AI Overviews to AI Mode is bigger than the version names suggest. Rankings stop being the scoreboard. Citations, prompt coverage, and mentions take over. The content that surfaces in fan-out and decision-stage queries looks different from the content that used to rank."},
    ],
    "kevin-indig": [
        {"url": "https://www.linkedin.com/posts/kevinindig_ai-trusts-a-different-set-of-sources-for-share-7472249743503503360-3b4H",
         "date": "approx 2026-06-15",
         "body": "AI trusts a different set of sources for every topic. There's no fixed list it pulls from. The off-property authority you build has to be topic-specific too. I looked at AI citations across a sample of topics. For invoicing questions, competitor domains hold 33.5% of what AI cites. For starting a business, the same source type holds 7%. So building mentions everywhere wastes your budget. Owned content still matters, but it's one of your weaker inputs. The publications, experts, and competitors that mention you carry more weight, because the model didn't have to take your word for it. Map the specific domains AI already cites for your topic, then earn your way into that set. Full breakdown in this week's Growth Memo."},
        {"url": "https://www.linkedin.com/posts/kevinindig_visibility-beats-clicks-ugcPost-7471580351279108096-gaoA",
         "date": "approx 2026-06-14",
         "body": "Visibility beats clicks. Pew Research data underlines that traffic is a loser in the AI search category: when Google shows AI answers at the top, click-through rates of the classic 10 blue links go down by 50%, and only 1% of users click on citations in an answer. These are not designed to send out traffic. One client lost about 50% of European organic traffic but gained 20% in conversions year over year, because purchase intent isn't gone. People are still buying solutions, they're just not clicking anymore. Instead they're looking at AI mentions and citations."},
        {"url": "https://www.linkedin.com/posts/kevinindig_a-prompt-tracker-that-runs-each-prompt-once-share-7469012961387511808-14kf",
         "date": "approx 2026-06-12",
         "body": "A prompt tracker that runs each prompt once is measuring volatility, not visibility. I looked at 815,000 prompt-page pairs with AirOps. After the same prompt ran 3x in ChatGPT, only 2.2% of citations remained. Accuracy improves when you treat each prompt like a sample: run it 3-5 times, report confidence intervals, and keep the raw answers for audit. The goal is to measure variance instead of avoiding it. Full guide in this week's Growth Memo."},
        {"url": "https://www.linkedin.com/posts/kevinindig_the-science-of-what-ai-actually-rewards-ugcPost-7470480134836297728-qTM6",
         "date": "approx 2026-06-11",
         "body": "LLM visibility starts with knowing which signals your market rewards."},
        {"url": "https://www.linkedin.com/posts/kevinindig_good-prompt-tracking-starts-with-sample-design-share-7470197034172710912-SIrr",
         "date": "approx 2026-06-10",
         "body": "Good prompt tracking starts with sample design. For an average B2B SaaS CRM category, I'd start with ~40 seed prompts: 12 brand, 12 category, 16 problem prompts. Problem prompts matter because that's where purchase intent lives. Run each prompt 5x per platform every week. ChatGPT, Perplexity, Gemini, and Google AI Overviews each get their own score because aggregation hides how differently the engines behave. The panel also needs personas: CFO, IT, and marketing buyers evaluate the same CRM through different criteria. The metric set should include mention rate, citation rate, average position, sentiment, and the attributes attached to each mention, all with confidence intervals."},
    ],
    "ross-hudgens": [
        {"url": "https://www.linkedin.com/posts/rosshudgens_editorial-affiliatepartnership-pages-are-share-7470940726592319488-dLa_",
         "date": "approx 2026-06-12",
         "body": "Editorial, affiliate/partnership pages are the second most cited content type within transactional prompts. After seeing enough of this in our data, we had to act. Today I'm announcing a new service at Siege: affiliate partnerships, with Nicholas Podrasky (15+ years across B2B and B2C) building the program. My last job before Siege was in lead gen, and in years 0-6 at Siege we ran a home product review site that grew to $150,000/mo in traffic value. We can take affiliate performance and merge it with search intelligence and GEO modeling to drive a high-performance program across channels. What SEOs know best is uniquely positioned to help affiliate and partner programs in a world where clicks are declining."},
        {"url": "https://www.linkedin.com/posts/rosshudgens_ai-traffic-converts-34-better-than-organic-share-7470498243429167104-j_Gs",
         "date": "approx 2026-06-11",
         "body": "AI traffic converts 34% better than organic on average. In B2B, it's 49%. In B2C, a tamer 19%. That's what we found reviewing 77 sites with statistically significant AI search traffic. Early claims of 4x, 5x, 7x were mostly outliers; the majority sits closer to organic than the hype suggested. A big reason B2B converts so much better is bottom-funnel transactional content: X vs Y, Y alternatives, best X software. If your conversion rate lags and you don't have that content, this is one more justification to build it. And if AI search feels underwhelming for you, it may just be that you don't have the content to support the traffic. Roughly one in four GA profiles we looked at didn't have goals set up at all."},
        {"url": "https://www.linkedin.com/posts/rosshudgens_big-news-tofu-content-is-back-if-you-search-share-7468388280732971008-xwQT",
         "date": "approx 2026-06-08",
         "body": "Big news: TOFU content is back! If you search for product-led, truly top funnel topics, you'll find company recommendations in AI results, from companies that created the supporting top funnel content and rank for them, like HubSpot, Salesforce, and Pipedrive. Previously I thought summarized content had little value if clicks dropped. But if AI also recommends us on product-connected content, it re-opens the creation universe for marketers. Our stress test: if you can achieve at least 50% brand visibility on these prompts, it's a top funnel topic worth going after if the TOFU has significant search volume as a proxy of demand. HubSpot hit 83% visibility on a 'what is CRM' prompt."},
        {"url": "https://www.linkedin.com/posts/rosshudgens_ai-attribution-is-solved-with-the-new-search-share-7467946616809840640-rTEN",
         "date": "approx 2026-06-08",
         "body": "'AI attribution is solved with the new Search Console features.' Not so fast. Google is adding impression data for URLs that appear in AI features. They are not reporting on the unlinked mentions in AI, and it is those mentions, at least until they become linked, that are the most valuable currently and what we all need data on to show the value of GEO programs. A positive addition, but our problems are not solved. In the example, Ahrefs and Semrush would not receive a tracked impression, yet those two words are receiving all the value from the prompt."},
        {"url": "https://www.linkedin.com/posts/rosshudgens_whats-the-current-state-of-seo-careers-ugcPost-7467528183941074944-Q8SI",
         "date": "approx 2026-06-08",
         "body": "What's the current state of SEO careers? I chatted in-depth with Eli Schwartz on our latest podcast. Eli believes demand for SEO will be up as the dust settles; things are getting more complex and there are fewer people to do the work. SEO teams are getting smaller, but how we do SEO/GEO is transitioning to touching other departments, so vertical promotions are less likely while horizontal generalist promotions (Director of Marketing) become more available. There's also been an inversion in technical demand: with LLM complexity and agent-readiness, technical matters again, but the new SEO/GEO is cross-functional, and being a heads-down technical practitioner is more challenged in driving organizational impact."},
    ],
    "bernard-huang": [
        {"url": "https://www.linkedin.com/posts/bernardjhuang_i-think-i-finally-understand-what-all-this-share-7471124722148118528-utAZ",
         "date": "approx 2026-06-12",
         "body": "I think I finally understand what all this frontier intelligence is actually useful for... navigating London's bus system."},
        {"url": "https://www.linkedin.com/posts/bernardjhuang_my-ai-trader-is-down-16380-this-week-ugcPost-7470865733535559680-XRyp",
         "date": "approx 2026-06-12",
         "body": "My AI trader is down ~$163.80 this week. So I made a game where you can lose money way faster. Inspired by the vibecoded 'Stonk Rider,' ours is called Stonk Runner. Candlestick charts are something you watch. I wanted one you could play. The level is the most famous chart in stock market history, the NVDA earnings day that kicked off the AI boom. Real market data, except the candles are the ground under your feet. You get 60 seconds to reach market close while a margin call chases you. Play as Jensen, Elon, Warren, or Leopold. Every character started as one photo run through a tool that turns any portrait into a 16-frame walk cycle. Survive the full set of candles and post your screenshot to get a sprite pack of yourself."},
        {"url": "https://www.linkedin.com/posts/bernardjhuang_i-gave-an-ai-16000-of-my-own-money-to-trade-ugcPost-7470540759289749504-4PKl",
         "date": "approx 2026-06-11",
         "body": "I gave an AI $16,000 of my own money to trade. Robinhood quietly rolled out a beta MCP connector, which means you can now let frontier AI models place real trades with real money. I'm calling it 'vibe trading.' Two rules: ETFs only, everything closes by end of day. In two weeks my agent designed and backtested 310 strategies; after costs almost all lost to just buying QQQ. The survivors returned +0.80%. First two days live: down $3.80. The part I can't stop thinking about: the best backtest looked too good, so I had a second model audit the first. GPT 5.5 built, Claude audited, and Claude caught that the builder was 'one day psychic,' leaking tomorrow's prices into today's decisions, inventing six points of phantom returns by accident. My AI trader cheated, my AI auditor caught it, neither knew anything was wrong. Who audits yours?"},
        {"url": "https://www.linkedin.com/posts/bernardjhuang_i-thought-ai-agents-would-buy-me-time-and-share-7472369891455524881-YnWp",
         "date": "approx 2026-06-15",
         "body": "I thought AI agents would buy me time, and they did the opposite. I run about 4 main agents now (Hermes, OpenClaw, Claude Code, Codex) going day and night, writing, cutting videos, even trading a live account. They never stop, so most mornings I wake up to a pile of overnight work to check, fix, or kill before coffee. I work more than I ever have, and most of it still loses money, but the money was never the bet. The bet is the curve underneath it. Agents don't take work off your plate, they raise what's possible on it, and the thing driving that, frontier intelligence, is what the entire tech world is focused on. When your whole stack runs on agentic rails, you inherit every gain for free; the stack gets better while you sleep. When it doesn't, you're standing still on legacy while the frontier pulls away. Get on the rails while getting on them is still a choice."},
        {"url": "https://www.linkedin.com/posts/bernardjhuang_clearscope-aeo-content",
         "date": "approx 2026-06",
         "body": "[NOTE: replace this with one more recent Bernard Huang post if you want a 5th. The four above are clean and sufficient.]"},
    ],
    "tim-soulo": [
        {"url": "https://www.linkedin.com/posts/timsoulo_my-san-diego-mastermind-dinner-ran-four-hours-share-7471703771857924096-j682",
         "date": "approx 2026-06-14",
         "body": "My San Diego mastermind dinner ran four hours. It felt like forty minutes. I host these dinners everywhere I travel, same format every time: a hot seat Q&A where each person shares what they do, answers questions, and poses a challenge for the group. I allow 20 minutes per person and politely cut them off. Except this time, the group was so locked in that every 'let's move on' was met with 'wait, one more thing.' Looking forward to seeing everyone at Ahrefs Evolve in October."},
        {"url": "https://www.linkedin.com/posts/timsoulo_just-wrapped-another-insightful-mastermind-share-7471247202426769409-TbkO",
         "date": "approx 2026-06-13",
         "body": "Just wrapped another insightful mastermind dinner in Austin. This is becoming one of my favorite travel traditions: wherever I land, I gather a handful of cool people for dinner and we dig into each other's businesses, trading ideas and war stories. Next stop: San Diego, and San Francisco right after. If you're in either city, or there's someone I should meet, drop a comment."},
        {"url": "https://www.linkedin.com/posts/timsoulo_even-on-short-notice-i-managed-to-pull-together-ugcPost-7470927815786405888-7odf",
         "date": "approx 2026-06-12",
         "body": "Even on short notice, I pulled together a few seriously cool folks for my mastermind dinner in Austin: Peep Laja (Wynter), Nick Christensen (AppSumo), Nick Gray (Museum Hack), Neville Medhora (SwipeFile & Kopywriting). I'm genuinely stoked about bringing Ahrefs Evolve to Austin in 2027. Live in or around Austin and want to join the next one? Tag yourself below."},
        {"url": "https://www.linkedin.com/posts/timsoulo_in-the-last-6-months-at-ahrefs-we-analyzed-share-7467561526015463424-9suJ",
         "date": "approx 2026-06-08",
         "body": "In the last 6 months at Ahrefs, we analyzed over 1 billion data points across 14 studies. What we learned about AI search optimization: 1) 'Best X' listicles are the single most prominent content format cited by AI chatbots, 43.8% of all page types cited by ChatGPT. 2) 67% of ChatGPT's top 1,000 citations come from sources marketers can't influence (Wikipedia 29.7%, homepages 23.8%, app stores 6.6%); only 32.3% are influenceable. 3) 28.3% of ChatGPT's most-cited pages have zero Google organic visibility, a completely separate discovery layer. 4) ChatGPT only cites about 50% of the URLs it retrieves. 5) Adding schema markup had zero meaningful impact on AI citations. 6) YouTube mentions have the highest correlation (0.737) with AI brand visibility of all factors studied. 7) AI Overviews reduce clicks to the #1 result by 58%, up from 34.5% just 10 months earlier. 8) 99.9% of AI Overviews appear on informational queries. 9) Google's AI Mode and AI Overviews reach the same conclusions 86% of the time but cite almost entirely different sources (13.7% overlap). 10) AI Overviews change every 2.15 days on average, but semantic similarity stays at 0.95: the words and sources shuffle, the meaning barely moves."},
        {"url": "https://www.linkedin.com/posts/timsoulo_last-week-i-went-viral-with-a-post-i-stole-share-7470665802527211521-G1yb",
         "date": "approx 2026-06-12",
         "body": "Last week I went viral with a post I STOLE from Ryan Law. And no, I don't feel sorry. Normally stealing posts is a bad look. But that doesn't happen when you work at the same company as the person you're stealing from. If you're on the same team (Ryan's our Director of Content), it's not stealing, it's a coordinated promotional effort. That's why I encourage my team at Ahrefs to steal ideas from each other. Whenever someone comes up with a great idea that benefits the company, it's our job to promote it as a team."},
    ],
    "andy-crestodina": [
        {"url": "https://www.linkedin.com/posts/andycrestodina_aicontentstrategy-contentmarketing-ugcPost-7470586404641615872-VRn9",
         "date": "approx 2026-06-11",
         "body": "Trick question: 'Do you use AI for content marketing?' It's tricky because creating content isn't one thing, it's many. This updated guide goes into five of the most effective ways to use AI for content strategy, all beyond writing: 1) auditing your blog's calls to action, 2) topic research, 3) initial edits aligned with content best practices, 4) finding partners and places to publish, 5) performance analysis. There's more to AI than 'Write me an article about X.' That's probably the worst way to use AI. Anything generated by that simple prompt should never be published. If AI can make it without the help of a human, it should not be written at all."},
        {"url": "https://www.linkedin.com/posts/andycrestodina_cmworld-share-7470609610840649730-j3CM",
         "date": "approx 2026-06-11",
         "body": "Thrilled to be part of the speaker lineup at #CMWorld 2026! This will be my 14th year teaching at this event, and amazing how much has changed. This year I'll share my latest methods for creating high-performing content, from strategy and ideation through AI editing, workflows and audits. You'll walk away with pages of notes and a repo of new prompts. Join me in Denver in October."},
        {"url": "https://www.linkedin.com/posts/andycrestodina_a-bit-different-from-the-typical-aeogeo-share-7469846082563293184-bD-i",
         "date": "approx 2026-06-09",
         "body": "A bit different from the typical AEO/GEO advice you see everywhere. I'm partnering with the American Marketing Association for a 2-hour session on the future of search and lead generation on July 15th. If you're an SEO, this may be a new perspective. If you're not, you'll get a strong baseline and next steps, including the audit prompts for auditing your pages and brand for discovery and lead generation."},
        {"url": "https://www.linkedin.com/posts/andycrestodina_mpb2b-ugcPost-7467983566568628224-f_fh",
         "date": "approx 2026-06-08",
         "body": "100% worth the trip to Boston. Let's meet up on November 2nd at the legendary #MPB2B. The speaker lineup is incredible: Ann Handley, Jay Acunzo, Mark Schaefer, Wil Reynolds, Robert Rose, Liza Adams, Christopher Penn and many more. See you in Boston!"},
        {"url": "https://www.linkedin.com/posts/andycrestodina_seos-are-the-best-marketers-to-do-ai-search-share-7464315940109963264-W33v",
         "date": "approx 2026-05-25",
         "body": "SEOs are the best marketers to do AI search optimization... but are we sure? Maybe SEOs have a blind spot. SEOs are focused on 'AI visibility,' but your future prospect isn't just asking AI for options, they're asking for recommendations. Visibility alone is insufficient. To get AI to recommend your brand you need pages with conversion copywriting elements: answers to real sales questions, proof points supporting specific claims, directly addressing objections, alignment with the visitor's psychology and cognitive biases. These are not on the typical SEO/GEO checklist, because SEOs are not famous for knowing what wins the sales call. Most 'AI Visibility Audits' I'm sent are just checklists of best practices (schema, FAQs, Reddit) and rarely include conversion optimization elements."},
    ],
    "glen-allsopp": [
        {"url": "https://www.linkedin.com/posts/glen-allsopp-63084025_ahrefs-ships-may-2026-20-new-product-updates-ugcPost-7470829673447321601-5Gov",
         "date": "approx 2026-06-12",
         "body": "Since joining Ahrefs 9 months ago, I've documented 200+ product updates. My four favourite announcements (+1 bonus) from May: the biggest was our new indexes for tracking visibility in AI Overviews and AI Mode, enabling custom prompt tracking and competitor comparison across multiple sources at once. Content gap and link intersect tools now compare twice as many sites (10 to 20). The Detailed SEO Extension now has almost 600,000 weekly users, with a hidden feature where selecting text and right-clicking brings up a 'check for duplicates' menu. Every update is in the carousel. Here's to another month of shipping."},
        {"url": "https://www.linkedin.com/posts/glen-allsopp-63084025_ahrefs-domain-rating-endpoint-is-now-free-share-7470108840743825409-X39_",
         "date": "approx 2026-06-10",
         "body": "Ahrefs' Domain Rating endpoint is now free, no API key needed. I built a tool to show it off: enter your site, reveal your DR, find other sites with the same score, and optionally submit your domain to be a recommendation. DR shows the strength of a website's backlink profile on a 0-100 scale, useful for competitor benchmarking, link prospecting, and outreach prioritization. For context: Wikipedia DR 97, Ahrefs 91, YCombinator 91, Tinder 82, Detailed 73. Even if you're not technical, point your AI assistant at the Ahrefs API docs and it will figure out the rest."},
        {"url": "https://www.linkedin.com/posts/glen-allsopp-63084025_ahrefs-ai-search-benchmark-report-q1-2026-ugcPost-7465394746618765312-42fw",
         "date": "approx 2026-06-01",
         "body": "100M+ data points. 13 studies. 8 authors. One AI search benchmark report. The Ahrefs team analyzed responses across AI Overviews, AI Mode, and ChatGPT, and ran our own misinformation experiment. Key highlights: in an analysis of 75K brands, YouTube mentions correlated most strongly with AI visibility; AI Overviews appear for 21% of all keywords (varying by category and query length); across 76K websites using Ahrefs Web Analytics, Google sends 190x more traffic than ChatGPT."},
        {"url": "https://www.linkedin.com/posts/glen-allsopp-63084025_ahrefs-ships-april-2026-20-product-updates-ugcPost-7460689542296100865-wIqI",
         "date": "approx 2026-05-15",
         "body": "Since joining Ahrefs eight months ago, I've documented 187 product updates. My four favourite announcements from April: massively increased API limits as more people build with the API and use our MCP, and having Ahrefs in the official ChatGPT app directory (no dev mode or manual setup needed). 'Ahrefs Ships' is an idea I had soon after joining to share product updates in a different way."},
    ],
}


def write_file(author, idx, post):
    folder = os.path.join("research", "linkedin-posts", author)
    os.makedirs(folder, exist_ok=True)
    filepath = os.path.join(folder, f"{idx:02d}.md")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(f"# {author.replace('-', ' ').title()} - Post {idx}\n\n")
        f.write(f"URL: {post['url']}\n")
        f.write(f"Date: {post['date']}\n\n")
        f.write("## Post\n\n")
        f.write(post["body"])
        f.write("\n")
    print(f"Wrote: {filepath}")


def main():
    total = 0
    for author, posts in POSTS.items():
        for i, post in enumerate(posts, start=1):
            write_file(author, i, post)
            total += 1
    print(f"Done. Created {total} LinkedIn post files.")


if __name__ == "__main__":
    main()