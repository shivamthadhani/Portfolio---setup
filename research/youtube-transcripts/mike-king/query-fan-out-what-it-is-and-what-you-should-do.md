# Query Fan Out What it is and What You Should Do

Author: mike-king
Video ID: hDYQ3AqMOOs
URL: https://www.youtube.com/watch?v=hDYQ3AqMOOs

## Transcript

Hello. Hello, internet. Okay. Okay. You
came in on a day. I I'm not sure that I
knew that we'd be having this like query
fan out webinar and like a few hours
earlier, Mike would basically try to
light the internet on fire uh with a
article he dropped earlier about chunks.
If you are just getting here, uh there
is a link in the comments, but uh maybe
we'll get to this at the end because we
hopefully will have time for Q&A. Just a
little bit of housekeeping is um this is
recorded so we'll send the replay
afterwards. We will get you the deck
with all of the goodies that that Mike
dropped in there. Like I said, I really
do hope we have time for Q&A. This might
be that rare webinar where we actually
have time at the end, but we will do a
hard stop at 3 PM Eastern. So, if you
have questions, there's a little um you
know, kind of Q&A icon on the side that
you can drop them in. But, uh everyone,
can you hear us? Okay. Is everyone in
the chat? Tell us how you're doing and
I'll let uh Mike uh introduce yourself.
Mike, why don't you take it away?
>> Hello. Hello. Hello. Hello, folks. How's
everybody doing? Where you calling in
from? Drop it in the chat and all that
sort of stuff. We are here to talk about
Query Fan Out. And I love the title of
this presentation because I wrote it.
No, I'm just kidding. Actually, I'm not
kidding at all. Uh, so it's everything
you should know about query fan out from
the guy that made the first tool for
query fan out and made it open source,
but none of the major SEO software
companies have one yet. So for anyone
that's joining us that doesn't know who
we are, we are Apple Rank. We are a lot
of things. Um, Search Engine Land just
gave me the search marketer of the year
award for a second time and I guess
that's cool, too. So my thesis here is
that we've learned a lot of internal
details about how Google works over the
last two years, but nothing meaningful
has changed in our popular SEO software.
And I think that's a huge problem and
one that I'm I'm looking to solve, you
know, over the course of the next few
months. But I do want to start with a
little bit of a I told you so. So, back
in October of 2023, I basically told you
guys that what we're experiencing right
now was on the way. I said that
retrieval augmented generation was going
to be our future and it was going to be
what we need to lean into in order to
get visibility in AI search. And so,
this was when SGE first came out, hence
the name of this blog post here. And it
wasn't released to all of us like yet.
It it was just talked about I think at
Google IO and I wanted to figure out how
it worked. So I built my own version of
it. It was called Raggle. It might
actually still be live right now, right?
And so I built it as a retrieval
augmented generation pipeline that used
ABS API which is basically a SER API um
an orchestration tool called llama index
and then it also use the chat GBT API
and I was able to replicate with you
know pretty high fidelity uh how AI
overviews or SGE at the time function
and you know I just really wanted to
understand like what will we need to do
to optimize for this. So to
[clears throat] that end, we have a
pretty significant um head start on a
lot of folks. And we also did a bunch of
like data analysis kind of kind of
projecting what would happen because
this new SER unit was added to the page.
And so I said that CTR was going to drop
between 20 and 60% depending on what
space you were in. And we had done that
by like scraping, you know, 90,000
keywords worth and then building a model
to predict what the traffic losses would
be. Specifically, I had predicted that
Nerd Wallet was going to lose 30.81% of
their traffic. When I pulled this
screenshot, the actual number was 37.3%.
So, they had already met my prediction a
couple months back. But I got two pretty
big things wrong. I at the time I
thought that you could rank deep in the
SER for a keyword and be a part of the
AIO response because that's what it
looked like right like you would put in
the keyword and you would see that for
the classic ranking something ranked
like 53 and it was appearing in the AI
overview and you know I also predicted
the idea that there would be
multi-dimensional searches based on you
know what the path that the users would
take in their conversations but what I
didn't know about and what I don't think
anyone knew about at that point was
query fan out. So query fan out is the
idea that these systems and it's not
just Google but these systems will take
the query or the prompt that you typed
in and then they they extrapolated to a
series of different um subqueries or
synthetic queries in the background and
then they reach out to a variety of
different sources to pull back
information to then feed the large
language model to then generate the
response. So, the reason why I care so
much about query fan out, because I've
seen some folks be like, "Oh, why do you
care? Like, just do topic clusters. It
doesn't matter." That's exactly how they
sound to me. Um, reason why, you know,
is because search AI search is basically
like a raffle, right? Like, we don't
have any control of what happens after,
you know, the the stuff is handed off to
the large language model. we do have
control of how many times they see us
when they're considering what to pull to
generate those responses. So, think of
each of these synthetic queries that you
rank for, that's your raffle ticket. And
then you're putting as many raffle
tickets in as you as you can in hopes
that you come out on the other side. And
the reason why it works like that is
because there's a whole reasoning stage
that happens. And it's not just in the
Google LLMs, but that we can explicitly
know how Google is doing it because they
talk about in their patents. And what
they're doing is they're like taking one
passage from one source, another passage
from another source, and they're
comparing it side by side and saying,
"Use this one, not this one." And then
they keep going through all that until
they narrow it down to the subset of
passages that they want to use. And then
they hand that off to the large the
final large language model to then
generate that response. So we have no
control over this process. We only have
a control over what we put in there. All
right. So what trends are we seeing?
Well, as far as like data that's
available because there's not a lot of
it, but it's growing now that there's
more people focused on this. Uh so Zip
has some great data, you know, earlier
last year where they basically did a
comparison of if you rank in the top 10
of Google, what is your likelihood of
appearing in AI search in these other
platforms? and they basically said it
was a 25% chance and you know you can't
run a business on a one in4 chance like
you need something that's more
predictable than that on the chatbt side
there's some great data that's come out
of profound as of late uh they did a
very similar thing where they were
looking at just the core service for
those seed keywords and then what's the
overlap between chatbt and ranking in
Google they found that it was 19%. But
now that they have more data on query
fan out, they can look at this in more
detail, more depth, and they've seen
that it's actually about 39%.
So they've also seen that about 62% of
Chat GBT's citations are coming from
somewhere other than Google search
results. Um, I've also gotten a lot of
like specific data from them on query
fanout and what they found is that
there's no position bias. So if you rank
in number two or number three, you can
perform as well as you did in um uh
number one, right? So as long as you're
ranking within there and you have
relevant content, you're pretty much
good to go. And so what they're trying
to do effectively is look at these
multiple queries. You know, if if you if
you are performing if you have one URL
that performs across multiple queries,
they're going to use that to basically
build consensus. So it's not that you
need like you know 50 different pages.
You could probably perform well across
multiple queries with the same URL and
um you know your domain can also rank
for multiple queries. So you know if you
have again higher SER saturation in this
case where it's like your domain is
ranking across a variety of these then
there's a higher likelihood of you uh
appearing as well. But what we're also
seeing is that after two queries there's
diminishing return. So you don't get the
same performance if you're like ranking
well for all 10 queries. They're seeing
that it's like a marginal improvement as
well. On the Google side, what we're
seeing from, you know, data that Sier
Interactive put out is that there's an
average of 10.7 queries per prompt and
up to 28 per prompt. you know, for the
fan outs. They're also seeing that on
average, they tend to be about six 6.7
words, meaning that they're very
detailed and longtail queries. And 95%
of the queries in Gemini at least have
no monthly search volume. So, this is
where we see studies like this from HRES
when they say like, oh, you know, 28.3%
of these are queries with that, you
know, don't rank for anything. And it
doesn't necessarily make sense. It's
really just a function of the fact that
these major tools are not capturing you
know rankings for queries that don't
have search volume. But these systems
are generating queries and these queries
are are you know different and in a lot
of cases they are not queries that users
are typing in.
So how does query fan out work? Let's
let's like you know really base or build
a base understanding here. So again, the
paradigm that drives most of AI search
is retrieval augmented generation. And
that's effectively where you are um
combining a large language model with a
search engine. And so what happens is
they take your query or your prompt and
then they turn it into a vector
embedding and then they do a search
based on that. they pull about a bunch
of uh candidate documents or passages
and then they rerank those and then they
send that to the large language model
for uh grounding purposes to then
generate that response. And so
the main difference between a platform
like or a surface like AI overviews and
AI mode is that there's more queries
that are being run and you know Krishna
uh from Bing has talked about this as
well as it relates to to Bing. you know,
they have the whole Prometheus
architecture where they have this
orchestrator that's running all these
queries and then handing those responses
to the language model to then generate
that response. But if we break it down,
it really just works like this, right?
They get the query, they expand it into
all those synthetic queries, they route
it to different types of content because
different queries align with different
types of content. That's going to be a
big problem if all you have is just, you
know, articles, right? like in some
cases they want videos, in some cases
it's a specific type of article and so
on. So then they retrieve those
documents or whatever we're calling
those those pieces of content and then
they select the features from it and
then they send it through the synthesis
pipeline and then they generate that
final answer. So ultimately what we're
talking about is the query being the
starting point here. It's it can be run
through you know um the semantic
pipeline or the lexical pipeline. Most
of these systems in fact I think all
these systems are doing hybrid retrieval
at this point but then they're going to
expand the queries in a variety of ways
and the expansion is what we're going to
really dig into right now. So the query
expansion is something that has existed
in search engines for a very long time.
Uh but not necessarily in the way that
we're talking about now because query
expansion could mean that you know they
extrapolate the um abbreviations that
you're using or they turn things into
entities or they say like okay well
implicitly you're talking about this
part of the keyword so they're adding
more to what it is that you've typed
into the query box. But in this case,
they're doing a variety of different
things. So intent classification,
slot identification, latent intent
projection, rewrites and
diversifications, and then also
speculative sub questions. And so the
intent classification is like, okay,
what does this person need? What is the
domain of information that they're
looking for? And then what's the task
type and also risk profile that we need
to account for here as well. And then
there's slot identification where it's
like okay this is the these are the
slots of information that are required
to answer this question. So using this
example here that we're using where
we're talking about best half marathon
training plan for beginners there are
explicit things that you're giving in
that query or prompt where half marathon
is the distance beginners is the
audience and then implicitly you're
talking about a training time frame a
fitness level a goal and an age group.
And these are all features that are
collected in the system based on your
experience or context with the system.
Then there's what's called latent intent
projection. This is where they're
plotting the query that you typed in
into multi-dimensional space and they're
seeing what else is close to it. like uh
you know we've talked at length about
embeddings and so on over the last
couple years but the idea is that you're
plotting all this stuff in
multi-dimensional space and they have
all these keywords all these ideas and
so on entities so on in that space that
they can say okay well what's what are
the next matches so in this case you
have hydration strategies gear checklist
shen splints prevention so it pulls all
those sorts of things back too and then
there's just like rewrites and
diversification So, you know, based on,
you know, how users may be
um typing about this stuff or what are
some of the things that the audience
has, you know, uh search for in the past
or what are some narrow variants or how
might we like uh add format to this? All
of these are being considered as well.
And then there are speculative sub
questions like what else does this
person need to know based on what
they're asking for? So, if you're
building a, you know, best halfarathon
training plan for beginners, one of the
questions you might have is how many
miles a week should I run or what shoes
are best here? Or how long does it take
to train? So, it's going to identify
those as well. Now once we've got all
these queries, we then map them to
different sorts of content or different
sources that we can get it from because
different sources have different like
computational costs and also real cost
because if you have to pull from an API
as an example, that's more expensive
than just p pulling from your knowledge
graph or what have you.
So then you're mapping them to sources
and then you have a retrieval strategy
based on how much it's going to cost
because again yes of course you'll get
the presentation after the uh
presentation. Um so again there are
costs involved. So Google has always
thought about like cost per query. Um
how much is it going to cost for them to
go out to their systems and then give
you the results. In this case it's how
much is it going to cost for them to go
out to the systems and then give you the
answer. And so in some cases they may
say like hey it's not worth it to you
know compute embeddings for this
component of it. Maybe we just use BM25
which is the lexical model of search.
So, but again, it's probably going to be
more like um you know, should we go to
this paid content source or should we go
with the low lift sources? And so when I
mention this this idea that they are
looking for specific content types, this
is going to be one of the places where
you may win or lose uh your eligibility
because specifically if they're like,
"Hey, we want a video for this or we
want, you know, like a printable
um guide or an infographic or whatever
it is and that's what aligns with that
synthetic query and you don't have it,
then they're they're just not going to
use you.
Okay, so where do we actually get data
for query fan out? So in the chat GBT
environment, it's actually quite easy in
that um in the the responses, the API
responses, you can see what's been used
for your query. So in this example, I
am, you know, asking who is Fonte from
Little Brother, right? And down here,
can't see exactly where it is. Um, oh
yeah, right here where my where my mouse
is, this is saying search model queries,
queries, who is Fonte from Little
Brother Hip Hop Group, Fonte, Little
Brother, and then there's a series of
additional ones, right? So, the query
fan out queries are also in the metadata
that comes back, right? Like these are
the this is what I just showed you right
here. There's these two queries that are
uh being grabbed. And so, when you're
logged in, you get it from this endpoint
here. when you're logged out, you get it
from this anonymous endpoint here. And
that same endpoint will show you the
results that have been used for um for
determining whether or not the model is
actually going to open the content. So
when we talk about metadata and its
value, it has a very different value in
this environment than it does in the
Google environment because they're
looking at the URL, they're looking at
the page title, they're looking at the
snippet, which is functionally, you
know, whatever Google serves up or
whatever uh search engine they're
pulling from, it's Google. Um, and
they're just using that snippet to
ultimately figure out like, hey, is this
worthwhile for us to open this page and
then review it as part of um, this
pipeline. So, you know, your metad
description needs to like give away what
the page is about. Whereas, we all know
that in classic search and Google, the
metad description doesn't it's like it's
not a ranking factor. It may influence
the user to click, but it's not a
ranking factor. In this site, it is. So,
we have an internal tool that allows us
to see what Gemini uses for grounding.
And the way you would do this is
basically by pinging the Gemini API with
the Google search uh function enabled.
And you give it the prompt and then
it'll it'll show you like here's here
are the queries that we use. And so,
we're effectively using this a as a
proxy to determine whether or not
grounding is actually happening for a
given prompt or query in the Gemini
environment. Now if you want to expand
this further you can use Qoria which is
the tool that I built and it really
helps you understand the the gaps in
your content. So you know if you have a
query like best online brokerage firms
you can see these are the subqueries
that Gemini
may generate and you can then go out and
see like how well do I rank for these
queries. A lot of times you won't rank
that well with them. you have the query
type because there's a variety of
different um queries types that are or
excuse me prompt types that are
generated synthetic query types that are
generated. So we give you the type and
you know there's also some feedback that
people are like oh well this isn't real
data it's generated by the model you
don't know what's being used. So the way
around that would be to look up what are
the citations in the AI overview or
whatever platform you're using and then
find out what they rank for. So pull the
rankings for all those URLs and then do
a reverse intersect to see, you know,
what are the quoteunquote real queries
that are being used. But like I said, a
lot of the queries that are being used
for this sort of thing don't have search
volume. So you wouldn't be able to find
those through any tools that are out
there because they're only going to look
for keywords that have search volume.
So how did I build Qoria? Well, one, I
read a few patents on how Google is
doing this. So this one right here, the
systems and methods for prompt-based
query generation for diverse retrieval
really talks through the different p uh
patterns that they use for generating
queries. There were seven query types
that are indicated in here. So really we
used that to build out Euphoria which is
really just three prompts in a trench
coat. Um so and I open sourced this
because I it was my hope that the
community could learn from this and you
know build on top of it. And so you know
first we indicate what how many prompts
do we want? If it's AI overviews we want
fewer. If it's AI mode we want more. And
then it simulates the query fan out by
generating a variet variety of queries.
We can only generate six of the types
because one of them is recent queries
that the user has typed in. And so
quietly in the background I've made an
update to Qoria as well and that it does
the routing formats as well. So like
what is expected as far as the content
types by query and this is the full list
uh as of now. We may end up adding
additional things to it. But these are
the ones that we got back in, you know,
continued discussions with Gemini, like
how would you do this based on um what
we know from your patents and then for
each query, it goes through and selects
the content type and you know, it gives
you your your results. Um there's a few
forks out there, which is great. Like
when I last looked, there's 48 users
that had directly forked the code.
There's people like Otterly that
literally just slapped my code into
their website and made it like free for
people. Then you got people like Tyler
over at Locomotive who've done more
thoughtful and actionable forks. The
real question that I have though is that
where are these people at? Where are the
organizations that our industry really
relies on for data as far as these sorts
of tools?
So, um,
you know, what I've what I felt is that
if our major tools aren't going to move
fast enough, I can be the one that can
help drive this stuff forward. So,
there's a series of QORIA upgrades that
I made. Uh, the tool has been
tremendously improved. We've added the
Gemini grounding to it. We've added the
reverse intersect function. um you know
it it's scraping chat GBT like it can do
the whole thing at this point and so you
can also download the data and it's got
the whole what I call chunk daily
functionality built into it where you
can see the scoring of passages on your
landing pages for these queries as well.
So what you would do is take the the
list of queries from the other side of
Q4A here. You download the CSV, put into
your rank tracking platform, and then
get back all your rankings for those
synthetic queries. And then what it'll
do on the chunk daily side is it'll
crawl all those landing pages and it'll
chunk those landing pages and score the
chunks on your site. So you get a
feedback loop of understanding of like
here are the chunks that are available,
here's how relevant they are, and then
you can make adjustments accordingly so
you can improve your ability to rank in
these environments. So, what you can
count on from me is that I'm going to
continue to keep building and open
sourcing things in hopes that our major
players will ultimately just grab this
sort of stuff and improve upon it in
their environments and launch this stuff
so that we all can level up as a
community.
Now, what tools can you actually get
this data from right now? Because there
are some companies that are taking
initiative. So, Demandphere, they were
the first ones to really track query fan
out from chatbt. They've also got this
uh visualization that they have coming
out really soon uh where you can see the
sort of like graph that shows the
relationship. Prompt also um you know
they are giving you the fan out when you
dig into the prompt details. It'll show
you like these are the search queries
that have been used. As far as what I've
seen thus far, Profound has the most
robust version of of QFO tracking from
ChateBC. Not only do they show you the
all the fanout queries, but they also
show you the variance and the share of
queries that that um that fulfills. And
then they also show you how these
queries change over time. So, there was
a a client that we worked with recently
where I had them give me a full export
of all the queries for all time and it
was something like it was something like
a 100,000 synthetic queries, unique
synthetic queries that were run across
this prompt set that we were looking at.
And what you'll find is that there's a
lot of variance, like small variance on
those same queries over time. And I feel
like Profound does a really good job of
showing you like here's how this query
evolves or changes over time as well.
And then they'll also show you by
platform how many synthetic queries are
getting executed day over day. So it
changes um you know for a given prompt.
And I think part of that is that we're
starting to see that chat GBT is caching
a bit more. They don't have an index per
se, but if you if you run the same query
multiple times, first few times it'll
generate the fan out and it'll it'll use
whatever it pulls back, but then like
you know, third, fifth, sixth time, it
just uses what it has cash rather than
going out there again. And another tool
that I'm really impressed by is Market
Brew. They have a tool called content
booster that will pull the fan out
queries and they're doing it in in the
way that we're doing it in Qoria where
they have like the synthetic ones that
they're generating but they're also
doing that whole reverse intersect thing
that I mentioned as well. And then the
tool takes it a step further in that it
will generate content in alignment with
your semantic gaps for those synthetic
queries as well. So, it's the most
automated approach I've seen thus far uh
outside of how we do it uh from a tool
and I hope that again more of these
platforms adopt adopt stuff like adopt
stuff like this. All right. So, how do
we use the data? How do we actually do
some relevance engineering here? Well,
our approach really looks like this. We
do a content audit for AI readability
and extractability. Then we do some
research around, you know, the latent
space and the semantic gaps. And then we
think about restructuring the content
and a augmenting it augmenting it
accordingly around chunking semantic
triples things like that. And then we
can test and iterate by simulating these
same environments that these uh
platforms are using. So the thing is
nothing that chatbt or Google or
perplexity or any of these companies are
doing is secret. They are all sharing
this information in real time as they're
innovating. They're all writing things
in their white papers. They're all
speaking at conferences like Nuripss and
so on and showing off their innovations.
And there's open source equivalents to
everything so that we can replicate what
they're doing. And all these platforms
make their vector embeddings available
as well. So you can vectorize the
content in the exact same way that they
do, make adjustments, and then pull in
competitors
to do the same exact thing and see how
your adjustments react accordingly. So
for us, you know, the tactical
implementation, Rebecca, just send me an
email.
Uh the tactical implementation looks
like this. We pull the rankings and the
landing pages. We generate the vector
embeddings. We score those uh relevant
passages and then we compare that to the
citations and then improve relevance on
our pages. But the bigger picture thing
here is that to improve the signal
that's going out to these systems, it's
not just about your website. It's about
your content ecosystem. It's what you're
doing in your videos. Videos being the
second most cited source in all the AI
platforms where YouTube is, you know,
really the advantage if you're
leveraging that. Uh Reddit being another
source. So you got to think about UGC.
You got to think about your digital PR
so that you can spread these messages in
a variety of different places. Then you
want to use entity rich embeddings
friendly language so that it's really
easy for these systems to extract that
information and use it in their
environments. You want to use structured
data. There's a lot of arguments in the
space like oh structured data doesn't
matter. They're not using it. I'm not
having that argument with you. Use it or
don't. You know uh we're seeing value
from it. And so what we're doing is we
are you know looking at the vocabularies
from a schema.org that are not being
used uh by these plat or not being used
historically because people only really
optimize for the rich results that
Google was giving and incorporating more
of that into the content. And then
there's going to be your basic, you
know, standard onpage SEO stuff, right?
Like making sure the header hierarchy
makes sense. Making sure you have clear,
clean semantic content. Uh have a open
robots.ext and, you know, do your
topical clustering and all that. And in
fact, one of the things that I've come
across as of late is the 499 response
code. Uh not something that you're going
to find in any SEO blog post. In fact,
if you look at people's SEO blog posts,
when they talk about different HTTP
response codes, it's usually that they
stop at like 429 or something like that.
499 basically means that the client
requested something from the server and
the server took too long to return it.
So, effectively what we're talking about
here is a page speed issue. And um you
know basically because a chat GBT crawls
or fetches URLs in real time it is not
going to wait for a long time to get
that response and so it'll give up. And
that's the sort of thing you need to be
looking for. You need to be looking at
your time to first bite and things like
that just to make sure your content is
loading fast enough to be used. And then
writing for synthesis is what we're
talking about when we talk about
chunking. And I just published a blog
post about this today about the
misinformation around chunking. And you
know, it's not limited to what Danny
Sullivan had said in his statement a
couple weeks ago or last week or
whatever it was. Um, it's also things
that people in the SEO community are
saying about it like not being valuable
and things like that. The reality is
this, these systems are using passages.
If you structure your content around
passages, and I'm not saying this just
for the machines. I'm saying also think
about how people and you know first and
foremost think about how people consume
this content. If you structure it that
way it is easier for them to extract it.
And so there's some information that um
Metahan had uncovered in his review of
Google's discovery engine API. He found
that the chunk size limit is around 500
tokens. um also that they're using
there's an option to use the headings as
part of those chunks as well. So, you
know, really as you're thinking about
how you structure your content, you want
to lean into having these passages
really cover the information
comprehensively so it's easier for these
systems to use it and also have clear
boundaries in the information by adding
those header tags. We have a tool called
relevance doctor which will score your
content in that way. So you can use that
to further improve
um you know how you're structuring your
content. And then that really comes down
to like how are you actually optimizing
these passages so it's very clear what's
being said. Part of it is going to be
using semantic triples. Semantic triples
is just a way to think about you know
the structure of a sentence. You want a
subject predicate and object. And think
about that in the same way that you
think about structured data, right? Like
when you think about how you're writing
schema, you have the subject and then
you have, you know, part of it can be
the predicate and the other part of it
can be the object. And that's being
represented in JSON rather than in the
sentence. When you're writing a
sentence, you're doing the exact same
thing. And because of the way that
natural language processing works,
they're able to extract that information
in that way, even if it isn't in code.
So, as an example, if you have a
sentence like the pros of buying a
lakehouse are many, you're not writing
it in a way to really extract the
information about that lakehouse. If
instead you have a sentence that's like
a lakehouse which is the subject
provides which is the predicate weekend
relaxation and rental income potential
that's the object for the homeowners. So
that is a more clear sentence that they
can extract that information from. You
also want to be like as specific or use
data points as much as you can. So don't
do a sentence like buying a lakehouse
might be a good investment. do a
sentence that's like, "Our analysis of
200 lakefront properties showed that
lake houses in popular vacation regions
appreciated 18% more in value over five
five years compared to nonwaterfront
homes. So again, data points that can
pull those out effectively. Um, is a
chunk a paragraph or a sentence? It can
be any passage, right? like they
if you have a a paragraph that's just a
sentence that can also be a chunk. Um
but think about just the boundaries of
the text where you end it like anything
that there's a you know two like returns
in your um
uh word processing tool that would be a
considered a chunk but the chunking
strategies can be a number of different
ways. So when I mentioned before that uh
from the research, you know, it's like a
500 token chunk. If you have a bunch of
long paragraphs, they're going to break
those down into those different
components and then consider that
content that way. So, you know, there's
just a variety of different ways that
you can define it, but the way that you
can explicitly define it is by, you
know, making separate paragraphs and
also introducing headings as well.
Um, you want to avoid ambiguity. So, the
more clear that your sentences can be,
the less noise you're going to have in
there, and it's easier for it to have a
higher relevance score in these systems.
So, don't do a sentence that's like it
comes with benefits and drawbacks. You
want to have a very specific sentence.
It's like owning a lakehouse offers
benefits like rental income potential
and weekend getaways, but also comes
with drawbacks such as high maintenance
costs and potential for HOA
restrictions.
Um, and then ultimately you want to
simulate your environments, you know, so
you can see based on those changes what
the impact is. And Market Brew, Market
Brew has tools around that. We also have
some internal tooling to support it as
well. Um but yeah, this is nothing that
this is something anyone can build at
this point. You know, go to a tool like
AI Studio, describe what you're looking
to do, and then you can make it pretty
easily.
Okay. So, when I talk about, you know,
there being so many gaps in SEO tools,
well, how do you fulfill those gaps?
Here are some tools that exist right now
that you can use for closing them. So,
if you're familiar with NAN, um it's a
great tool that allows you to build
customized automations without any code.
you're really just dragging and dropping
workflows and having them, you know, run
however you need them to. And so I
actually prefer open-source options over
any of this stuff for a variety of
reasons, but one of the main reasons is
going to be data privacy. The other
reason is that, you know, people don't
really understand
how much a token costs or anything like
that. And so they may run a a whole
crawl on a 10 million page website and
then we get this crazy open AI build. So
I prefer to use, you know, the open
source stuff. So Ola is a great tool for
running open source language models and
it's really simple. You just download it
to your machine. Go to.com
uh and download to your machine and it
has a chat interface just like a chat
GBT or something like that. And then if
there's any models that you don't have
on your machine, when you try to use
them, it just automatically downloads
them. So I don't even remember which one
I was running at this point, but I did
it. And if you have a modern machine,
meaning your computer, you probably have
a decent GPU on it. So it's it's pretty
fast as well, right? And once you have
Olama on your machine, you can integrate
it with Screaming Frog. And so as you're
crawling, you can generate your vector
embeddings and then use it as part of
these environments. So NADN, again, I
prefer this over a lot of the other
tools out there because um it's open
source. You can run it on your own
machine or you can run it on your own
servers or whatever. And it's more
extensible than what I've seen with
Zapier as well. So it also has,00
integrations. So pretty much any tool
that you use you can pull into NAN and
you could build like a whole
um micros service like you can build a
whole API on the back of NAN. So whether
you're using their hosted version or the
open source version on your own machine
and then you can integrate it into
anything you want. So let's say for
instance you build some sort of API and
you want to integrate it with Google
Sheets. You can do that very easily. And
one of my favorite features with NADN is
that it allows you to do human in the
loop work. And what that means is that
you can set it up where these workflows
that you've got automatically send you a
Slack uh message when it gets to a
certain point. So you can review
whatever it is that the AI has done
before it moves further. or it could
send you an email or it could text you
or whatever it is. And then NAN also has
a ton of different templates that you
can use. So you don't have to start from
scratch. You just go to that URL right
there and you can find u workflows that
are related to what you're trying to do.
So here's one specifically for AI
overviews that someone else had already
built where it basically looks at the AI
overview and does some analysis for you
and then it it kind of automatically
gives you SEO recommendations. I'm not
saying it's perfect. I'm just saying
that it's a place that you can start and
you can make adjustments uh for what you
know and make improvements for it to do
what it is that you want to do. And then
another thing that they've just um
launched or more recently launched is
this workflow builder where all you have
to do is describe what you want and
it'll build the functionality that you
need. Now, if anybody's considering AI
agents, you can build those on top of
something called crew.ai, AI, which is
basically a framework for building any
sort of agents that you want. So, you
know, there's a lot of like
off-the-shelf agents out there where you
can just like buy a SAS platform that
has SEO agents for you or marketing
agents or whatever. I would definitely
recommend you build your own so that you
can capitalize on the nuances that
matter most to you. All right, so just
to wrap this up, here's the five things
that I want you to remember. one search
technology
and the behavior around search has
changed irrevocably. So anyone that's
telling you that's just SEO like just
isn't paying attention. It's going to
take you more than the standard classic
SEO stuff to get you the visibility in
the future. And it's to your benefit to
understand how these systems work
because the software that we currently
have isn't going to get you to where you
need to go. But most importantly, this
is our opportunity to define what the
future of this is and not be stuck in
the patterns that have kept SEO from
being the platform that it should be.
This is pull rank. We have our AI search
manual 20 chapters of pure fire and I
know that Garrett and team are making
some updates to this as well. Uh you can
grab that here. Q40 is here and you
should definitely be at SEO week. It is
literally the best SEO conference of the
year. Um, we're doing it even bigger
than last year. And that's all I got.
What questions do you all have?
>> Oh my goodness, that's so good. It It's
like there's so many questions we got.
Keep them coming in. Um, like like Mike
mentioned, SEO week, definitely check it
out. It's at the end of April in New
York, 4 days uh with the AI search
manual. Check that out too and I'll send
this all via the deck cuz like there's a
whole chapter on query fan out. There's
a whole chapter on simulations on all
these things that you can go so much
deeper in. But let's start um with
Burke. Uh just question Mike is chatbt
using your actual um metad description
or is Google's the Google's rewritten
metad description?
>> It's the snippet that Google rewrites.
So whatever shows up in the SER is what
it's using. It's great clarification.
Henry wants to know um what do you
recommend for embeddings an API like
Google Vertex or a hosted database like
Pine Code?
>> Uh I mean you don't necessarily need a a
vector database at this point. Like that
was like a point in time where you know
the the incumbents like MySQL and
Postgress didn't have vector columns.
Now they all do. So you don't
necessarily need that. You can use
BigQuery pretty easily. Um, so if you're
wanting to replicate what Google is
doing, you want to use the Gemini
embeddings. Uh, if you don't want to pay
for that, you could use Gemma, which is
their open source embeddings. What we
tend to use is something called mixed
bread. Their large embeddings are open
source and they get the best performance
that I've seen. But again, if you're
looking to replicate what the systems
are using, you should use either the
Gemini embeddings or the OpenAI
embedding.
>> Cool. This is uh relevant. Uh Julie
wants to know, is your process uh to
find query fanouts within chat GPT up to
date through today?
>> What? Update through today. What does
that mean? Oh, up to date through today.
>> Up to date through today. Yeah.
>> Yeah. So, not every not every um
uh query does a fan out. So, I don't
know what what or excuse me, not every
prompt does a fan out. So, it is up to
date as far as I know like because
that's where Chad or that's where
profound is also getting the data. It's
the only source that is uh that you can
get it from. Like there's no Google
search console for profound. So, um,
welcome to send over whatever prompts
you ran and I can see what I'm seeing on
my side, but as far as I know, that is
the only way that you can get it.
>> Um, Brendan had to run, but he wanted to
know uh, you know, question about the
announcement that Google made with, uh,
preferred sources, personal
intelligence. Uh, surely personalization
is going to play a greater role in AI
response SERs and ads. Do you just have
any thoughts on the personalization
announcements? Yeah, I mean that's just
a reflection of what they talked about
at Google IO last year. They talked
about something like it's called
personal context. Um, you know, it's
it's basically them using all the
information they have about you as in a
vectorzed way to filter out what
information they're going to put in
front of you. And you know, I don't
really like doing predictions for the
year, but the person that asked me my
SEO prediction for this year was that
that everything is going to be way more
personalized than it's ever been. you
you've actually talked about the
personalization um and the mechanics
behind it. So, this is a question for
me, but do you think fanout would ever
be impacted by personalization? Um
>> yeah, data.
>> Absolutely. Absolutely. So, because you
know, I'm going to assume a lot of
people ask broad questions, right? Like
a question like, oh, I need a training
program for um half marathon. You may
not say beginners. You may just say you
need a training program. And so
in service of search quality, it's
better for them to learn stuff about you
over time and be able to answer your
question no matter how vague it is. And
think about, you know, when Chad GBT
first rolled out and how specific you
had to be with your prompts. Think about
how less specific you have to be now. So
it's just gonna make the whole thing
better for the actual user.
>> How does that impact SEO and content
strategy? So, assuming that you're going
to have to deal with these fan apps that
are all personalized, like thinking the
forward, if you're building out a
content plan, how are you addressing
personas and those uh personalized query
fanouts?
>> Yeah, I think that's exactly it. Like,
you have to have persona driven content.
Like, they are going to look for the
specific answer. They're not going to
look for the broad answer. And I think
what we're going to see over time is
that broad content ends up getting less
visibility
broadly. Um, and it's going to need to
be more specific in order for you to get
the rankings because I think one of the
things that people misunderstand is they
think that AI search is separate from
classic search. It's all the same
system. There is no like difference. All
search is AI search at this point. So,
do you do you think there's any like how
do you navigate and I know I I think I
know the answer to this, but like how do
you navigate potentially duplicate
content or being penalized for basically
rece repeating the same answer that's
slightly nuanced for a different
persona?
>> Duplicate content I think is a
misunderstood concept because
you can look at many sites that have
like let's let's say like location pages
as an example. There's a lot of
instances where location pages are
exactly the same except the only thing
they say different is the location. And
it's not that the location like a given
location doesn't rank. It will rank in
that location. You know, like if you
have the the Philly page versus the
Brooklyn page, um the Philly page will
perform in Philly and the Brooklyn page
will perform in Brooklyn. So, I don't
think that's as big of a deal as people
think it is, especially if there are
enough nuances of difference that it
speaks to that specific uh audience. So,
I wouldn't worry too much about that.
>> Slade wants to know, do you think Google
going after uh SER API or data for SEO
will have an impact on things for the
future with those systems likely being
used by chat GPT?
I don't know that I necessarily believe
that OpenAI is like only relying on
tools like that. I mean, they're they're
such a sophisticated engineering team.
Like, why would they? And also, a lot of
them are previous Googlers, so why would
they not just build their own scrapers
for Google? Um, so I don't like even if
those companies get taken down, which I
I don't want to see happen because
they're great service providers, but I
don't think it's going to matter that
much to Chad GBT.
>> Lefernair wants to know if Corey Fan out
has so many side questions added to the
initial question, how come there are so
many hallucinations?
>> Because LLMs aren't perfect. You know,
you can you can go to chat GBT right now
and give it a whole document of facts
and it can still hallucinate. Like
that's just a function of how these
platforms work. I think hallucination is
hallucinations have improved over the
last two years, but it's still, you
know, something you got to worry about.
>> It's an architecture thing. Jen wants to
know, should we look for query fan out
also in API tests or is it too different
from uh apps interfaces like chat GBT
and AI mode?
So, I think I understand the question.
Um,
I'm gonna see if I understand the
question. Um, so I think she's saying
like, should we
be looking at API responses or looking
at what we're seeing in the actual
interfaces?
So, the actual interfaces are typically
going to give you something different um
than what you get from an API. The thing
with Gemini is that that's all we have.
We we there's no other option, right?
Like we if we could scrape that from the
front end, then we would, but we can't.
So, we basically are using Gemini as the
proxy for understanding. Whereas with
chatbt,
you know, all the visibility tracking
tools do
the scraping a bit differently or their
data collection a bit differently. Like
I know Amplitude uses the API
Whereas I know, you know, most of the
other major tools are scraping the front
end. And if you want to get what users
are seeing, you need to scrape the front
end. The API is not necessarily going to
give you the same thing. Gotcha. Okay.
Um,
okay. I'm going to tee up here. Burke
wants to know, "Give me your conspiracy
theory as to why the large SEO tooling
companies have not made a cute query
fanout tool yet. We've known about this
for what, two years?"
Um, no. I think it's only been since
last May that Corey fan out was like
explicitly explained. I mean, I think
it's it's just a software problem,
right? Like when you have a large
software company that's going in a
certain direction. In the case of
Semrush, they're a public company, so
there's a lot of risk mitigation and
what have you. um not the problem with
HRES to some degree because they are a
hundred million dollar company that's
private and but at the same time like
there's always resourcing there's always
road mapaps and so on so I suspect they
think the things they are doing are more
valuable to their goals but you know the
gap for the actual practitioners that
are doing things
that care about AI search indicate that
that is not the most valuable thing to
be done right now. So, I mean, I don't
run their businesses. I don't know why.
I just know that they're not doing what
I need.
>> Um, get a few more and then we are going
to end. But, um, Janet wants to know, do
you think, you kind of spoke to this a
little bit, but do you think AIS will
make their own indices in the future?
>> Uh,
I don't think so. I think for that
paradigm,
it makes more sense to go out to the
page in real time because they're the
reason why they do that is they're
trying to get the like right like real
time information. And especially as it
relates to news, I think they're always
going to want to pull from the latest.
So, I don't know. I think they'll
probably cash a little more
aggressively, but I don't think they'll
build an index.
>> Okay. And Robert wanted to know this a
little bit longer, but like with
personalization we were addressing
earlier, do you think optimizing for
specific query keywords will be even
less important as one content can be
served to anyone depending on the
personal context? So like even if our
content isn't written for a query, if AI
thinks our content is for the user based
on the context, they can still serve our
content.
In other words, one piece of content can
rank for any so for so many queries that
we don't even know what we are ranking
for. I guess the question is when you're
creating content going forward, should
you like do the little snippets, do
skyscraper, try to combine everything
for one persona? How are you thinking
about content creation?
>> Um,
I still think person first, right? Like
I'm still thinking about what is going
to move the needle for my audience, but
I'm also thinking about, okay, you know,
I know structure works better for my
audience, too, and it works better for
the machine. So, I'm balancing all of
that sort of stuff. The way I think
about this is like it's like writing a
ha coup. The haiku has a lot of
constraints, right? Like you have the
five syllables, seven syllables, five
syllables, but like that's no excuse for
the haiku to be trash. So, in the same
way that when we're writing content, we
have a series of constraints that we're
trying to account for, but that's no
excuse for creating what people call SEO
content, which is like just for bots.
>> There you go. I'm going to end it here.
I really appreciate everyone coming out
today. This has been awesome. Obviously,
like if you still have questions about
all of this, you can see Mike's email up
there. Hit me up as well. Um, we're on
on LinkedIn. we still do do X as
controversial as that site is. Um, and
and to Rebecca's point, we do all this
stuff. Like our bread and butter right
now is putting the strategy behind all
of these like really tricky surfaces,
whether it's, you know, your keyword
portfolio matrix and and building out
content and mapping it to all the query
fanouts, doing omnimedia content audits,
omnimedia content plans, pointing you in
the right way in terms of the
measurements uh, and the tools and the
recommendations. So that's a oh an SEO
week. If you haven't already, at least
go to the website, watch the sizzle
reel, see how awesome it is because
everything that we were talking about in
April, like right before IO last summer,
like it was basically a crystal ball.
Like if you like predictions and crystal
balls, go to what people are actually
doing at SEO week because we have a
standard in terms of that it has to be
new, it has to be databacked, it has to
be real. And I will drop as well. We are
actually having a one spot is available
for an open pitch. If you've wanted to
get on the stage and you've never really
done it or you've just never been at SEO
week, we are accepting pitches for a
live competition. Deadline is January
31st. Um, I'll include that in the email
I follow up afterwards. But thanks for
having us. Mike, you got any parting
words?
>> Yeah, it's not just us.
>> See y'all later. Thanks.