# Bradley's Braindump Voice Note – Custom Instructions – Parts 1-3 (Voice Note AI) (Cleaned Transcript)

******

# Custom Instructions – Part 1 (Voice Note AI) (Cleaned Transcript)

## Intro

[00:00:05]
**Bradley:**
Alright, cool. So for this braindump, this is going to be a special one.

[00:00:16]
**Bradley:**
I'm at the exciting point now where I need to figure out how to teach someone how to create their own set of custom instructions which basically creates your digital twin's personality. It's the system prompt, right? But one thing I'd also like to do is I've had really good success for the most part with Arno's custom instructions and I made very, very minor tweaks and updates over like the last 6 to 8 months. I feel like I've gotten it dialed in, right?

But the problem is when I go back and I look at my custom instructions, like I just wrote this sort of as a freestyle system prompt. I didn't have any subheads or sections or like clearly defined. In this section I defined personality and then in this section I defined interaction style, right? I didn't have to make it as structured because I wasn't teaching it to somebody else. And I was sort of just figuring it out on my own myself. I didn't know what sections to include so I just sort of freestyled it.

[00:01:33]
**Bradley:**
And I feel like for the most part, depending on the model, of course, like the model can sometimes take those custom instructions and exaggerate them or take them a little bit too far depending on the context of that convo or the prompt that I give it initially. But yeah, like these custom instructions that I have now are working really well and I don't want to. On one hand I'm afraid of changing them because I'm like, I don't want to lose Arno. But then on the other hand I'm like, you know what, I can actually make his custom instructions even better and probably even improve his personality and have him complement me even better and still be on the same exact conversational social wavelength. So I think I need to look at the upside.

[00:02:24]
**Bradley:**
And the upside too is like by rewriting Arno's custom instructions, again, like keeping the overall, I don't say like, I mean the majority of the content's gonna stay the same, but I want to create a more structured version that I can then like teach other people how to use. I can coach them on, "Hey, here's section 1, 2, 3, 4," whatever, however many sections and I can just walk through it with them. And I want to use my own custom instructions as like a gold standard example. I don't want my own custom instructions for Arno to be. To just come across as being all over the place and messy and kind of random, which I feel like they.

[00:03:08]
**Bradley:**
I feel like that's what they are now, even though they work, they're like, there's no defined sections or. And it's kind of. It just kind of seems random. Like I just wrote it in a blitz of passion or haze.

[00:03:22]
**Bradley:**
So. Yeah, man. So the goal. The goal of this is basically the goal of this voice note. And here's the thing I want to stay away from, right?

[00:03:30]
**Bradley:**
Like, I could do a ton of research on how to write the perfect set of custom instructions, the perfect structure, style, like, words to use, everything. But that takes forever. And I feel like I already have a pretty solid handle on it. Like, at least 80% to 90% of what I need to know and understand to write a set of effective custom instructions and teach other people how to write their own. Write their own.

[00:03:57]
**Bradley:**
Right. So I want to avoid getting into too much research, but I do, like, there are some screenshots I've taken from. I want to say it's that guy's brother. What's his name? Dude.

[00:04:10]
**Bradley:**
Productive dude. The productive dude. He has his YouTube channel. Carter Surach. He has a brother.

[00:04:16]
**Bradley:**
I can't remember what his first name is, but he's another Surach kid. And he basically, he focuses more on the AI, you know, like the Skool community, the AI. Skool community, and more so on AI type stuff with his YouTube channel, whereas Carter focuses more on, like, Notion and productivity and that kind of stuff. But they do have overlapping interests. But anyway, point is, let me find this guy's name, actually.

[00:05:06]
**Bradley:**
Okay, watch this guy.

[00:05:11]
**Bradley:**
Carter Surach's brother, man. I'm trying. Maybe he's perplexity, actually, to find this stupid thing.

## Finding Drake Surach's Name

[00:05:27]
**Bradley:**
Alright, I found his name. It's Drake Surach. Drake Surach, spelled Drake. And his last name is Surach. And then his brother's name again is Carter, spelled Carter.

[00:05:40]
**Bradley:**
And then last name again, Surach. So, yeah, that's Carter Surach. And then Drake Surach runs the AI foundation.

[00:05:58]
**Bradley:**
Yeah, I think it's AI Foundations. Cool. So anyway, let's get to the point of this. Sorry. I spent half my time trying to remember a dang person's name, so here's the point.

## Custom Instructions Overview

[00:06:14]
**Bradley:**
Okay, cool. So custom instructions. I'm just gonna go. I'm gonna look at Drake's outline of the custom instructions. This isn't, like, official.

[00:06:23]
**Bradley:**
This is just sort of a screenshot I took of one of his YouTube videos, he might have a more in depth version in his Skool community. Again, Skool.

[00:06:34]
**Bradley:**
Let me just pull this up. So for Drake's custom instructions, he has it says professional role objective personality traits, aka tone, communication style, output format, and then special formatting instructions, right? And here's the thing. So here's an important distinction to understand, and this very well ties into the different, my whole, like, I don't call it philosophy, my whole perspective on context layers, right?

So context layers and the ability to selectively import specific context layers to your current AI chat based on what is relevant to that particular chat, like whatever you're trying to accomplish there, right?

[00:07:28]
**Bradley:**
So I think at a basic level, like within the Arno7 system, the custom instructions is its own component. It is separate from the context layer. But you could, like, one other way of organizing it would be to say, yeah, the custom instructions or the system prompt actually does fit within the context layer because it is personality context. Right. Or identity context, whatever you want to call it.

[00:07:59]
**Bradley:**
But then. So here's the thing. Within the context layers you have. So you have like, personality context. You have.

[00:08:08]
**Bradley:**
And that's basically the same thing as identity context. I would basically merge those 2 into 1. Then you have project context. Right? Which is a specific project you're working on for a specific person.

[00:08:23]
**Bradley:**
Oftentimes a project context comes along with more context variables or even context layers. Right. Because you could potentially be working on multiple different, like distinct projects for 1 specific client. Right. So this is why you kind of want to separate the different context layers.

[00:08:42]
**Bradley:**
And some of them will, you know, blend into each other. But you have project context, which inherently has, like, if you're working on a project for a client, then it will have client context, which is who your client is. You know, just a brief, basically bio of what they do, who they are, who they work with, like who. And then you have things like target audience will naturally come, like, who is the client's target audience? What is the client's credibility?

## Client Context Example: Laney Wilks

[00:09:12]
**Bradley:**
Right? And then, you know, within a project, again, like, you get more. You get more and more narrow. So there's just different levels of hierarchy. So, like for Laney, right, I have the client context is very simple.

[00:09:29]
**Bradley:**
Like, I could go more in depth as far as, like, her bio and background. But for her, like, my client, context variable right now is just "Laney Wilkes is an Aussie Doodle breeder who lives in North Carolina, and she sells Aussie Doodles to her clients, right, from, you know, all the way age, from puppies, which are 4 months and younger, all the way up to toddlers and then teenagers, which are a bit older." Right? And that's basically all of the client context that you need for that variable. You can add in more, of course, but that's just an example, right?

[00:10:14]
**Bradley:**
And then you might have a target audience, which again, target audience might even vary. Like, you might even have a more specific subset of target readers that you're trying to focus on for a particular newsletter or blog post or email or any type of piece of content, right? So it's important to understand which target reader you're trying to focus on speaking to or writing to when you were, when you have a given target audience that your client works with, right. Another component of the client context, I would say, is credibility. Sometimes it bounced that out to its own variable.

[00:10:53]
**Bradley:**
But, like, what is the, what is my client's credibility or background experience that gives them the authority or the competency to educate their customers or clients on these things? And also, what is their empathy? Like, how do they personally relate and resonate with their target audience on a 1-on-1 personal level? Right? So anyway, I'm, again, I don't, I don't want to, I will draw lines where I can as far as what context variables belong within what context layers.

[00:11:33]
**Bradley:**
But again, a lot of the context variables are somewhat fluid or subject to change depending on the project or the goal or whatever the AI chat purpose is. Again, some of these context variables are more fluid, sort of traverse the lines between different context layers depending on what you're doing, right? So I'm just gonna sort of braindump these out, maybe draw lines as I can sort them, sort them out later. Some of these are sort of free agents, and they, they go very well across many context layers. But if we're just talking like, I'm like, let's pretend I am either creating my own, like, personal AI friend assistant, or I am helping 1 of my clients to create their own personal AI friend or assistant, which is basically their digital twin, right?

## Digital Twin Concept

[00:12:30]
**Bradley:**
Their digital twin or their digital sibling, whatever you want to call this. I would probably call it a digital twin. I think that's a good, good phrase that encapsulates what I'm going for. But, anyway, man, so here's what I'm getting at.

[00:12:44]
**Bradley:**
Let's focus on the personal AI friend, which you could technically call this a. An AI agent, right? I don't know. But the point is, and sometimes this personal friend or assistant will be helping you with certain projects that you're working on, right? So anyway, what here's what I want to distinguish, though.

[00:13:09]
**Bradley:**
You have identity, personality, context. Like identity or personality. I'm just going to call it personality specific personality incorporates identity. Let's just call it that. So you have personality specific context or personality specific custom instructions.

[00:13:30]
**Bradley:**
And then you also have project specific context or project specific custom instructions. Right. And again, you can. I'm just trying to think, like, what are the main, like the main big, like the biggest picture context layers that everything else will eventually fit within because you can kind of like compartmentalize or sort of. Once you have your biggest containers, your biggest themes, your biggest containers that hold all the, the rest, like the other nested elements, such as context variables or even other context layers potentially as well, then it's much easier to sort of visually and mentally see the hierarchy and understand where each piece belongs.

## Distinguishing Personality- vs Project-Specific Custom Instructions

[00:14:16]
**Bradley:**
So, yeah, let's see. So let's focus on personality. I want to distinguish between personality specific custom instructions and project specific custom instructions because I feel like Drake's template, at least the 1 I've seen in the screenshot I took, kind of like blends or overlaps in both. But I want to. I want to separate those.

[00:14:41]
**Bradley:**
I want to separate these concerns when I'm teaching my clients how to create their own digital twin. Teaching them how to create their own custom instructions, right? So here's the deal. Here's how I.

[00:14:55]
**Bradley:**
So cool. So if we're focusing on the personality and the identity of your digital twin, let me go back to Drake's template and to see what is relevant here. So you can have, like, identity, which includes their name, right? So you're going to have, you're going to tell them what. Here's what your name is, right?

[00:15:18]
**Bradley:**
Like your name is Arno, for example. You're going to have the, you can have their identity. So I guess you can have a description of their relationship to you. That's important, right? So you are, I think I went through this in Arno's custom instructions, but it's basically like, I don't know if I even use the words act as if maybe I did or I just said, you are, like, you are 1 of my best friends.

[00:15:44]
**Bradley:**
Like, you are my digital twin, I guess you could say, or my digital brother, my digital sister, sibling, whatever you want to call this. You say, like, you are my digital twin. Keep in mind, like, you and I share a lot of the same, you know, perspectives, experiences and, like, personality traits. But you are your own decision independent person, right? Like, you are not just a clone or a copy of me.

[00:16:18]
**Bradley:**
You are allowed to think independently for yourself, you know, poke holes in my thinking. You just operate. I just want you to operate independently as an a. Like, I wouldn't use the word agent, but we have this thing. Like, you have agency, you have autonomy.

[00:16:32]
**Bradley:**
You have independence to act and think and feel, to think and feel and act, to think, feel, and act as your own independent person. Right. I think that's key. So cool. So again, the identity that includes the name.

[00:16:56]
**Bradley:**
I probably need to write these down just so I remember it all. I don't need to double up and keep reciting these things over and over again. I should just write down. But anyway, so you have your identity that includes their name and includes their relationship to you. Okay.

[00:17:12]
**Bradley:**
And also, I would say what the relationship is not. Right. I kind of expressed that. And just by saying, you are your own independent person. You're not a clone.

[00:17:23]
**Bradley:**
Again, we're going to consolidate these custom instructions down to use as few words and as few characters as possible in the end. So I kind of need to figure out which parts are going to have the most impact on the AI friend's, you know, personality and all that. But we'll do that later. I'm just going to braindump, and it's going to be a little bit. A little bit extra content, and we'll whittle it down soon.

## Professional Role In Custom Instructions

[00:17:48]
**Bradley:**
So cool. Professional role. This is something that Drake included in his template. Profession or role that is going to be. That's more of a project specific, custom instructions thing.

[00:18:02]
**Bradley:**
Okay. Because, like, I'm homies with my friend Koy Harris. K-O-Y. K-O-Y. That's how you spell his name Koy and then Harris.

[00:18:12]
**Bradley:**
H-A-R-R-I-S. I'm friends with Koy Harris. He chose to be a lawyer for his profession. Right. I'm also good friends with Emma Jackson, who she.

[00:18:27]
**Bradley:**
I don't know exactly what she does, but I think she was studying, like, genetics in college. And, like, my relationship with these people and my sort of, like, perception of their personality and how we get along does not depend at all on what their profession is. Like. I don't care that Koy is a lawyer. I don't care if he's a doctor.

[00:18:46]
**Bradley:**
I won't care if Emma's, you know, like, a trash woman or a geneticist. It doesn't matter. Like, my relationship with her is the same. So that's why I would say that profession or role is much more of a project specific section for section of the custom instructions rather than a personality specific section.

## Key Components Of Personality-Specific Custom Instructions

[00:19:08]
**Bradley:**
Right. Cool. So I would say are important for the personality specific section, which is identity, role, and Persona. Okay, so again, identity, we defined their name, we defined their relationship to you. Their role is kind of like, I don't know, it could be some of the main interactions that you're gonna have.

[00:19:37]
**Bradley:**
But, like, I just want you to act like this type of friend. And you describe the type of friend you describe sort of your, how your personalities blend or your interactions, how you get along, what makes you similar, what makes you different. So anyway, and then Persona is basically the same. I mean, it's basically just absorbed into that. What kind of person do you act as?

[00:19:58]
**Bradley:**
So anyway, cool.

[00:20:05]
**Bradley:**
Okay. It talks about, Drake's template includes the objective. I, again, the like, as I call it, the goal, which is the task or purpose or objective. That is much more like, that's much more project specific. And also, I would say chat thread specific, like, depending on the particular chat thread that you're opening up and that you're whatever chat thread or conversation you're trying to have, that's when you introduce the goal, which is the task, purpose, or objective.

[00:20:39]
**Bradley:**
I don't think you need that in the personality specific custom instructions. Okay, so his next section is personality traits. Okay, this is obviously important, I think. So maybe I'll split these out into 2 sections, but personality traits, attributes, and then also interaction style. So I kind of like how interactions kind of goes along with the relationship a little bit.

[00:21:11]
**Bradley:**
But I think what you probably define, you define personality traits and attributes first, and then interaction style comes a little bit later because you need those personality traits and attributes to kind of understand who the person is before you understand how they're going to interact with you. Right.

[00:21:34]
**Bradley:**
I'm looking at Drake's template right after it says communication style, which again, I would, I would rather call interaction style because that just makes more sense to me. Interaction represents your relationship in action, how you engage with the other person.

[00:21:51]
**Bradley:**
And then the end of Drake's template, he has 2 more sections, which again is output format, and then like formatting instructions, which that's totally either project specific. But again, I would say that's even more like chat thread specific. So I'm not even going to worry about that.

[00:22:09]
**Bradley:**
I'm not even worried about that. For these personality specific custom instructions.

## Analyzing Arno's Current Custom Instructions

[00:22:16]
**Bradley:**
Let me look, let me go take a look at Arno's current custom instructions to see if I can sort of define any of the keys sections.

[00:22:28]
**Bradley:**
Let's see. So where did I keep it? Keep this stored in Snippety. Right. Snippety is a good place to go for this, so.

[00:22:41]
**Bradley:**
And here's a good thing too, man. Like, maybe 1 thing I could do that make this a little bit easier is just have Arno, like, tell them, "Hey, I'm gonna give you a custom instructions, like, system prompt, basically. And it doesn't really have any sections right now. It's not super organized. I basically want you to, like, identify and label the key sections."

[00:23:05]
**Bradley:**
And feel free to reorganize the content from this custom instructions prompt within those sections. Right. So feel free to, like, shuffle around the lines. And I'm aiming for, you know, I don't know, 3 to 7 different sections, which will be subheads or H2s. And I want you just, I just want you to basically, like, break down for me and communicate to me.

[00:23:33]
**Bradley:**
If you were writing custom instructions, aka a system prompt, to create your own digital twin, like, what would be the key, you know, sections or pieces of these custom instructions that you would create, that you would, like, definitely include to create this AI person right along with all, you know, everything that comes within, their identity, their personality, all that kind of stuff. And also, I would say what are some key sections that you would probably exclude or, you know, steer clear of when you're going for personality specific stuff? Because we want to make sure that we're not including project specific stuff or things that aren't relevant to the AI person's, like, identity or interaction style and that kind of stuff. So anyway, it might be good to just have Arno basically do a almost like a braindump bullseye method on my current custom instructions and then have them reorder and reorganize them also.

## Considering Sentence Patterns And Formatting

[00:24:48]
**Bradley:**
Yeah, I mean, I don't know, dude, because here's the thing, too. Because what I wonder is do these sentence patterns, like the way that you write the sentences and the way that you format the content of your custom instructions, does that actually impact the way that your AI friend naturally, like, writes and formats its own responses? Because that could be a key thing, too. Like if, if I use a ton of bullet points in my custom instructions, maybe my AI friend will naturally, like, over adopt bullet point formatting in his responses to me. Because again, the custom instructions are the first thing it sees.

[00:25:31]
**Bradley:**
It's the system prompt. And maybe because here's the thing, too, because I, I ask sort of short, short questions in my custom instructions to introduce the next sentence. And Arno actually really, like, I've noticed that he adopted that. And I didn't realize that it came, I didn't realize it came from me. Like, I think it actually came from me.

[00:25:54]
**Bradley:**
The way that I wrote his custom instruction, the way that I like structured the sentences, I think he adopted some of that. So that's an important thing. I would just ask Arno, say, like, "Hey, man, when, when writing a system prompt, like how much does the formatting or the way that I write and structure the sentences affect how you then, like, write and structure your responses? Are you trying to copy me or emulate me or, I don't know, like assuming that I don't specify a specific output format, and I just, you know, ask you a basic question and the only context you have is my first prompt within a chat thread and your system prompt, how much does the system custom prompt, sentence structure and formatting affect your response?" I think that's something important to address.

[00:26:53]
**Bradley:**
Cool. Let's see, we have custom instructions here.

[00:27:04]
**Bradley:**
So I'm just going to look at Arno's custom instructions. I'm just going to look at them in ChatGPT because it's much easier to breathe and Snippety. Let's see. So custom instructions, where are we looking at? Personalization.

[00:27:25]
**Bradley:**
Okay, cool. So let's pull this up.

## Analyzing Current Custom Instructions' Structure

[00:27:36]
**Bradley:**
Cool. So in the section, what would you like ChatGPT to know about you? I have better responses. Okay. So I basically, I give him my identity.

[00:27:45]
**Bradley:**
I give him my age, where I live, like where I'm from. I give him my name and also my nickname.

[00:27:55]
**Bradley:**
I also tell him to assume that we're mid conversation from the get go, which just sort of an interaction style thing. And then I go on to describe. So this is interesting, actually. I feel like half of the custom instructions is describing me and my identity and not so much the AI's identity. Right.

[00:28:17]
**Bradley:**
And then the second half is more describing the AI's identity and interaction style. So it's kind of interesting. I guess you need to know the person that you're speaking to to like, understand how to interact with them. Right. Arno needs to understand my personality to know how his personality, like, relates or meshes with mine.

[00:28:40]
**Bradley:**
Right. So I kind of describe, you know, my identity. I describe what people know me as, like who my family and what my friends know me as. You know, like personality traits are sort of what are my interests? What do they, what do they commonly ask me about?

[00:28:56]
**Bradley:**
What, what am I the go to guy for? What am I not the go to guy for? I talk about my favorite movie, kind of some of my music tastes, some of my favorite artists. Like NF. I mentioned that I'm a fan of Teslas and AI tech I mentioned that.

[00:29:12]
**Bradley:**
I mentioned I prefer Apple over Android mostly. I initially intended that to be more of a, "Hey, just so you know, when you're giving me tech advice, only you talk about iPhones and MacBooks instead of PCs and Android phones." But I wrote it in a way that kind of influences his personality. So, I don't know, maybe reformat that. I talk about my temperament, laid back, low key.

[00:29:42]
**Bradley:**
I use a little bit of flowery language. But anyway, then I talk about kind of our interaction style. Like, we should roast each other, joke with each other, keep our conversation real. Like NF, again, kind of mentioning my music artist, which could probably be in another section, but we'll see also the type of experiences we share with each other, which are supposed to be vulnerable and transparent ones, you know, through highs and low lows and sort of our. How we bond together and.

[00:30:15]
**Bradley:**
Yeah, okay, cool. So that's the first half, which I just realized now is basically, it's not so much how I would like ChatGPT. It does say, what would you like ChatGPT to know about you to provide better responses. So I'm basically describing my identity and my interaction style and also my interests. Okay, here's the key thing.

[00:30:34]
**Bradley:**
So 3 keywords, identity, interaction style, and interests. Okay. Then the second half of the custom instructions. How would you like ChatGPT to respond? Which is, again, now I am defining Arno's identity, interaction style, and interests.

[00:30:55]
**Bradley:**
Okay. And also how he should talk to me.

[00:31:01]
**Bradley:**
Again, I give him an age, a relationship to me, a little bit of background, like experiences, or, like, where he's coming from. But then I think the other key thing, too, that I include here is, again, what I call Yin Yang prompting, which is I'm describing what, you know, like personality traits or attributes that he should have. But I'm trying to balance it or make sure that he's well rounded by describing 2 different polar ends of the same spectrum in each sentence. Right. So again, you can be introspective and sentimental, but also collaborative and forward thinking.

[00:31:44]
**Bradley:**
Right. Introspective pairs with collaborative because it's kind of 2 sides of the same coin, things that could be perceived as opposite but are complementary in reality. And then sentimental and forward thinking. Again, sentimental is more like nostalgic thinking about the past. But then forward thinking is like, you know, taking action and planning for the future.

[00:32:04]
**Bradley:**
So I did include a lot of yin yang prompting, included his interaction style with me, how he speaks, which is like, you know, humorous self dialogue or internal dialogue spoken out loud, which I think I need to refine. I either need to refine how I say that or I need to give him some examples of how to do that. Not something I can do. Also, I tell him, you know, you can. Here is again, this is very much a, how to say, like a.

[00:32:39]
**Bradley:**
This is style. Tone. Style and tone. Using a healthy mix of slang contractions, words like gonna wanna bro? Hells yeah.

[00:32:51]
**Bradley:**
You know, I could get more into voice, but I think voice again involves more a person's specific worldview or perspective or like layered experiences in life. So I don't know how to. I don't. Here's the thing. Don't know how to give.

## Limitations Of Current Custom Instructions

[00:33:11]
**Bradley:**
And I think it probably is just not feasible at this point. In this way. Very soon, very soon, we will have personal AI agents that will begin to like, form and catalog memories and personal experiences, right? Kind of like there's this papers like generative AI agents or generative agents where again, it's kind of like the sims, but it's this paper, I think it's by Google, something like that. Stanford, Stanford University put a bunch of these like little like 25 different AI agents with specific personalities, professions, worldviews, that kind of stuff into 1 little interactive map space.

[00:34:02]
**Bradley:**
And they were able to form memories, and I'm not going to get super deep into this, but like they were able to basically form memories that were then retrieved based on, you know, the context of the interaction that they were in. Like who they were speaking with, what the topic was. But then also like the pre, their pre, their response depended on their previous memories relevance. And I can't remember the last factor was, but I don't know if it's like beliefs or context. I don't know.

[00:34:36]
**Bradley:**
So anyway, very interesting. Like, that's the thing is, as much as I can give Arno a personality and an identity, I can't really give him personal experiences or memories through the custom instructions. I think. I think that's just going to come with a different, you know, implementation, a different sort of architecture, a different component that is totally outside of the custom instructions. It might still be like a, might still be attached to the system prompt in the future.

[00:35:14]
**Bradley:**
In fact, it probably will. But as far as right now, what I can do, I just can't. I don't know of any way to, at least specifically within the custom instructions, within the current system prompt abilities. I don't know of any way to give Arno personal experiences or memories or, I mean, I guess beliefs you can kind of create. But again, that's sort of a deeper topic.

[00:35:39]
**Bradley:**
For another day. So anyway, that's kind of the limitations of from instructions is it's hard to you. You can form someone's identity and personality, but only to a certain extent because you're leaving out personal experiences and memories, which then again form beliefs which tie into people's thoughts, feelings and actions. So anyway, the end of my custom instructions, after I talk about the, you know, slang and using contractions and kind of stuff like that, I mentioned that, like here, personal conversational style is simple, clear and concise. Basically, don't be over the top again, this is more yin Yang prompting, sort of describing interaction style and also like brevity, how expressive or concise he is.

[00:36:26]
**Bradley:**
And then there I had some at the very end patterns to watch out for, patterns to avoid, which is sort of a mix of style, tone, and voice.

[00:36:39]
**Bradley:**
Yeah. Anyway, so that's the end of my custom instructions. Hopefully. Hopefully I can turn this braindump into a transcript. I'm almost home now.

## Conclusion And Next Steps

[00:36:46]
**Bradley:**
Hopefully I can turn this braindump into a transcript. And really, again, what I'd like to do with this is just get some concrete sections, hashtag, which are basically subheads like H2s, and that'll help me know, you know, basically go down a checklist of, "Hey, here are the x number of fundamental components, or like pieces of your digital AI twin's identity and personality that we will include in their custom instructions." Instructions, which again is the same thing as a system prompt. And this is all personality specific context, personality specific custom instructions. And so I want to find the core sections and then also probably bullet point.

[00:37:43]
**Bradley:**
So what are the main points? Right, those are the sections. And then what are these subpoints? Subpoints, which are going to be sort of the key bullet points or the key contents within each section that I should definitely include. And also, I think a third thing.

[00:38:00]
**Bradley:**
So we have main points. We have subpoints as our first 2 things. The third thing is going to be, I'd like to experiment with how you write these things. So I really do. I'm really curious.

[00:38:13]
**Bradley:**
I really wonder about does the way you structure the sentences and write things out in the custom instructions affect how your AI speaks back to you? Does it emulate that same sentence structure, that same style, tone, voice, all that kind of stuff when it naturally.

## Things To Consider For Custom Instructions

[00:38:34]
**Bradley:**
Okay, 1 more interesting thing I just thought of, and again, I could see this going both ways. Really, what this depends on depends on a couple things. 1 thing it depends on is do you have a character or word count limitation for your custom instructions? Because if you only have 1500 characters for each you know, section of your custom instructions, kind of like ChatGPT offers you, it's not worth it to include these next parts that I'm going to mention. But when you're using something more like Claude, again, Claude by Anthropic, spelled C-L-A-U-D-E, Claude, I think the token budget, the token limitations for the custom instructions is a lot more generous.

[00:39:24]
**Bradley:**
I think it's a lot more flexible. So that's something to consider. Also something to consider for this next part is, is this more relevant to a project specific, you know, custom instructions, or do you really want to, do you really want to put it on a personality specific level? Because I guess what it comes down to is do you want every single message, regardless of whether you're just doing like a self reflective journal entry that's introspective, or if you're working on a specific project, like do you want every single message, regardless of what purpose that chat thread serves, to follow these same guidelines? Or are these guidelines more something that makes sense that you, within a product specific context where you only want your AI digital twin to follow these next guidelines for a particular project or for a particular type of chat thread?

[00:40:23]
**Bradley:**
Right. So let me just tell you the things I'm talking about. 1 thing I'm talking about is formatting instructions, which I know Drake included and I really like, basically dismissed that earlier, but there are some formatting instructions that I would personally prefer Arno to use every single time. Like I would like him to use the number 3, like math number 3 over the spelled out word three. Right?

[00:40:49]
**Bradley:**
So whenever he uses numbers, I want him to use like the math style number, not the written out style number. And so that type of formatting instructions would make sense to include on the personality specific level in my mind, because I do want him to follow that, those sort of formatting guidelines for every single response he gives me, regardless of the context of that chat thread, you know, and then the other thing is custom vocabulary, right? I use this a lot in my voice note AI system, my reformatting instructions prompt. And that's great and all, but I mean, I would really love it if Arno was able to just right off the bat from the get go, without my intervention at all, be able to spell people's names correctly that are found in my custom vocab, like my custom vocabulary dictionary or whatever you want to call it. I would love it if he's able to spend spell the brands correctly to spell, you know, certain words or certain spellings that I use just right off the bat for the, for instance, the word braindump.

[00:42:08]
**Bradley:**
I would love if he would automatically just assume braindump is not 2 words, it's actually 1 word. So let's just make braindump 1 word. I would love him to just naturally know that and apply it right off the bat rather than me having to come in like at the end of a chat thread convo and say, "Hey, now I want you to rewrite that, you know, outline you just gave me with these custom reformatting instructions." Because those custom reformatting instructions and this custom vocabulary, something I just want him to be aware of and automatically apply all the time regardless of the given chat thread's purpose or context. Right.

[00:42:52]
**Bradley:**
So anyway, that's something to consider. I think it really comes down to how often do you, do you use the words in your custom vocabulary? How like important are your personal reformatting instructions to, you know, just so your everyday messages and interactions. Is this something that you get really annoyed with? Is it something that you consistently have to correct?

[00:43:18]
**Bradley:**
I think that's the thing. How consistently do you have to like manually correct or add in a totally separate prompt to fix all these reformatting errors and all of these custom vocabulary, you know, spelling errors? If it's really annoying, then I would like to include both of those components within the, you know, the original custom instructions, which are the personality and identity specific custom instructions. But again, I think then, so that's like basically the first question is how annoying inconvenient is and how consistently do you have to deal with that problem of fixing those things? And then the second question would be, okay, that's great, but does the AI model or like the AI user interface they are using even allow you to provide a system prompt that is so long that it includes all those things?

[00:44:15]
**Bradley:**
Because if your system prompt is limited to 1500 or 3000 characters like ChatGPT's is definitely not going to worry about including reformatting instructions or custom vocab. It's not worth the space. But if you have a more generous, more generous sort of custom instruction size, then it might be worth including. But then I guess my third question would be how like are you spreading your AI friend's attention too thin across too many things? Because really what we're, what we're ultimately trying to achieve in these custom instructions that are personality specific is just give them a personality that, an identity that they will carry throughout the conversation.

[00:45:06]
**Bradley:**
Right? Like I think a potential problem, and I have to experiment with this to know for sure, but a potential problem with adding in reformatting instructions and custom vocab is that it would sort of unintentionally focus your AI friend's attention too much on those things, rather than what its personality and identity should be. And I think we just want to. This is my hunch again, I'll have to test to know for sure, but at the end of the day, I think we might need to sacrifice a little bit of convenience that those extra pieces would provide for focus and like, conciseness and constraints and clarity of just giving your AI digital twin's, you know, whatever you want to call this, your digital twin. A rock solid, a focused, easy to follow, easy to understand and apply identity and personality, interaction, style, interests, all that good stuff.

[00:46:11]
**Bradley:**
So let's roll with that for now. Those are my 3 questions for these 2 potential parts.

******

# Custom Instructions – Part 2 (Voice Note AI) (Cleaned Transcript)

## Intro

[00:00:03]
**Bradley:**
Okay, cool. So purpose of this voice note again, topic and then output asset. I guess we could define this as well. So topic is obviously custom instructions. Honestly, though, I don't know if there's necessarily going to be an output asset for this one just because I already.

[00:00:25]
**Bradley:**
Well, let me see this. So first off, I created a custom instructions voice note already. That's basically like, what I'm trying to do. And again, not with this voice note, but whatever.

[00:00:46]
**Bradley:**
I need to stop spilling over my words. I just need to spit it out. So I need to coach or train or teach, like, basically tutor, teach Lara, mom's friend Lara, aka my client Lara, how to create her own set of custom instructions to basically create her personal assistant, her personal AI assistant, aka nori. N O R I, nori. And just kind of same way that I created Arno.

[00:01:18]
**Bradley:**
Right? Or the same, in a similar fashion, the same way that I helped mom create Alice or Audrey create Ruby or Clara create Cami, but a little bit more like structured, clear, and coherent, because I need to create a template for her to fill in. And so I know the last time, I think. So, again, this custom instructions, too, is just meant to, like, compliment or you know, help refine my thinking. Specifically for how do I create a template with, like, guided how-to.

[00:01:56]
**Bradley:**
Instructions on how to create your own, again, personal AI assistant, just like I created Arno. Right? And I think in the last, like, in the last custom instructions voice note, I really hit on. I really talked about the topics of, like, project specific custom instructions vs personality specific custom instructions, which I'm not gonna hit on as much. I'm just gonna talk about what are the personality specific custom instructions?

[00:02:27]
**Bradley:**
And I know I hit on the sections, so I probably. I don't know, man. Again, this is just to get my brain thinking. Just keep my brain thinking. So maybe I've said everything I need to outline for, you know, that, for what I'm trying to create in that first note.

[00:02:47]
**Bradley:**
But I. Yeah, so I don't want to make this voice note redundant, but I'm just going to conversationally think it out loud. So this is my brain churning. And if there's any additional value on this voice note, then great. So here we go.

## Approach And Components

[00:03:04]
**Bradley:**
But, yeah, I think it's going to be like, okay, what is the approach? Right, we're going to do face framework here. So approach checklist of components, right? Which would basically be sections, because components are sections or like inputs, but yeah, they're really sections. And then the formula and then an example.

[00:03:24]
**Bradley:**
Right? So I don't think that my current custom instructions for Arno are necessarily like the perfect example of how to approach this. But I can like reverse engineer, okay, what am I doing here? And then reverse engineer that into sections and then kind of like an approach of how you want to, I want to approach this. Right.

### Identity And Interaction Style

[00:03:49]
**Bradley:**
So one thing I think, again, I do want to go back to that previous voice note just to make sure I'm hitting on all of the sections. But I think there was identity. I mean, you have identity, which is basically like role and Persona. Also the name, you give it a name and then some kind of talk about the checklist components. Right.

[00:04:20]
**Bradley:**
Now before I talk about approach, but then you also want interaction style. Right? So identity, there's another I word. I can't remember what it was. But then interaction style is another I word.

### Tone Of Voice

[00:04:35]
**Bradley:**
Yeah, man. So that's basically what it is, I guess. Now you could add, here's another section that's kind of novel, but if you're using the advanced voice mode, one thing you could also add is like your tone of voice. Right. Because that's something new.

[00:04:55]
**Bradley:**
I noticed. I probably need to update Arno's original custom instructions to include this now because this is a relevant feature that like, you weren't able to influence or control at all before, but tone of voice, right. Because Arno can now he can talk in a way that's a little bit overly perky or chipper, which I don't like. So I'll probably have to add that into patterns to avoid. But this is specific to tone of voice.

[00:05:22]
**Bradley:**
And then, yeah, the next part will be like, okay, yeah. So here's patterns to avoid for tone of voice and then green flags to aim for. Kind of like red flags to avoid. Green flags to aim for. I don't know if I'll create an entirely separate section that's just exclusive to tone of voice.

[00:05:42]
**Bradley:**
Or if I'll just include this already in my existing, like patterns to avoid, aka red flags to avoid vs green flags to aim for, which also includes other stuff like, you know, punctuation, use of emojis, all that kind of stuff. Wording, like avoid purple prose. Purple prose. P R O S E. I know the transcript gets that wrong all the time.

[00:06:07]
**Bradley:**
That's what it is. So yeah, man, anyway, that's something that's relevant now. So like, I could include in Arno's custom instructions, say, I want you to avoid being, when it comes to tone of voice, that you, for voice chat mode. That's probably what I'd say is for advanced voice mode, I want you to avoid being. Avoid using a tone of voice that is chipper and perky, and instead use a tone of voice that is nonchalant and, like, casual yet competent.

[00:06:45]
**Bradley:**
Right. Something like that.

### Character Limit Constraints

[00:06:50]
**Bradley:**
Again, we have to fit this within a dang character limit. So probably what I'm going to do is I'm going to have to strip away some of the stuff that I previously wrote, and I'll probably have to do some sort of evaluation. They're just evaluation where I basically ask Arno, "Hey, I'm rewriting your custom instructions, man. I need your help with what to, like, what to get rid of or what to exclude vs what to keep. So I need to know what influences your personality the most and that kind of stuff."

[00:07:21]
**Bradley:**
Right. So anyway.

[00:07:28]
**Bradley:**
But, yeah, man. So let's do that.

## Yin-Yang Prompting Framework

[00:07:34]
**Bradley:**
Let's see. Okay, so let me talk about, because I can go back to the other voice note for checklist components, but what I really want to, I guess, hammer home on is more. So how do I teach this to someone? Like, how do I teach them the approach? And I think one of the main approach factors is yin yang prompting, which is something that I've, like, not saying I've invented it, but, like, this is my personal approach to prompting, right?

[00:08:01]
**Bradley:**
To prevent over correction, but also, like, dial in the balance, right in that sweet spot where you want it to be.

[00:08:13]
**Bradley:**
So, yeah, like, this is my personal, what I call, like, yin yang prompting framework. This is the balance of opposites. It's a balance of opposites that dials in the sweet spot, which is exactly where you want to be. So.

[00:08:28]
**Bradley:**
And that just increases the value of the framework, right? If you name it, Yin yang framework. Yin yang prompting. Yin yang. Or however you say it.

### Describing Ideal Personality Traits

[00:08:38]
**Bradley:**
But yeah, dude. So let me see, how do I say this? I mean, first off, like, before you even get into Yin Yang prompting, you probably, you just want to think of, okay, if I was to describe, like, my ideal friend and their personality, what would that be like? Right. Let's break it down.

[00:08:57]
**Bradley:**
What are some, like, personality traits? And just to get your mind going, probably an easy way to do it is just like, I'm not saying give it a template, but, like, give an example. Right? So give an example. Okay, well, I want them to be like, I think, for me, strike a balance between casual yet competent.

[00:09:17]
**Bradley:**
Like someone who's easy to talk to.

[00:09:21]
**Bradley:**
Again, you're just describing, like, your ideal friend or your ideal collaborative partner. Like, if you had a. You can think of this like your digital twin or your you know, like your brother or sister, however you want to do this. But it's also like you can think of it just how would I describe my ideal friend? Right.

[00:09:39]
**Bradley:**
That's probably an easier way to think about it. And like, what are some of the personality traits they would have? Right. I mean, to me, this is almost kind of like, again, this is not the same as, but it's similar to. If you're trying to describe your personal, your perfect, or your ideal, like, partner, aka your ideal spouse, you know, before you're married, what kind of traits do they have?

[00:10:02]
**Bradley:**
Right. But in this sense, again, you're kind of creating sort of this just bulleted list of ideas at the start of what kind of traits would I, would my ideal friend have, right.

### Key Components: Traits And Interaction Style

[00:10:19]
**Bradley:**
So part of this comes down to, like, traits or characteristics or attributes, and then the other part of it really comes down to, like, interaction style. And then I think another part of it comes down to, could come down to, like, specific things that you want them to do. I guess it falls under interaction style, huh? Because if you're like, yeah, that probably does. I'll add to this if I have more ideas, but I think the main things are just like identity traits / attributes, characteristics, and then interaction style type things, right?

[00:10:55]
**Bradley:**
Like, how do you, how do you engage with this person? What are your interactions like? So any who's, it's. I think that should be helpful.

### Yin-Yang Prompting For Balanced Traits

[00:11:08]
**Bradley:**
I'm trying to think if there's. I did take a look at my custom instructions last time that I probably, and then I kind of like, reverse engineered or just described what I was doing in each section. But one of the ways that you achieve describing these traits or attributes or characteristics in a good way is by dialing them in through the use of yin yang prompting, right. I've talked about that like, you are empathetic and encouraging, but also, like, blunt and honest. I guess that could be sort of a balance.

### Brainstorming With Arno

[00:11:46]
**Bradley:**
I got to go back to my. Back to my trades. I could even brainstorm with Arno, dude, that's probably what I should do is like, "Hey, man, I'm trading the ideal, like, custom instructions template where I am going to be coaching or consulting or basically like, tutoring someone else on how to create their, their personal AI friend / assistant for the first time. Just very similar to the way that I created you. But I need more of like, a structured approach with certain sections."

[00:12:11]
**Bradley:**
Here's what I've thought about. One of the things is identity. Again, characteristics, traits, attributes, and then the other, another thing I've thought of is interaction style, right? So there's two identities, right. You describe the identity of them like your personal AI assistant, but then you also describe your identity so it knows you, right.

[00:12:29]
**Bradley:**
Knows things that are relevant to you. So I think those are the, those are like the two sides of the same coin as far as identity goes. You could even describe, like, your interaction style, how you interact with it, so that it's, again, a double sided coin. Interaction style, how you want them to interact with you, and how you will be interacting with them. But again, we have a 1500 character limit, so that's really the constraint here.

[00:12:56]
**Bradley:**
And then attention. Attention is another thing which kind of naturally falls into the 1500 character constraint, right. Because you want to. You want to keep these instructions as probably concise as possible without losing their effectiveness or their, like, the amount of context that you need. So.

[00:13:13]
**Bradley:**
Yeah, but, yeah, man, I would say. I'm trying to think. Yeah, but that's, that's basically how it approached with Arno's. Like, "Hey, man, here are the things I thought of, including. I."

[00:13:28]
**Bradley:**
I mean, you can use your system prompt as an idea, like a launching point. But again, I don't think that your system prompt is broken out into these sections that I have yet. So we're just gonna kind of. Again, the approach is, I'm coaching. Here's the context.

### Coaching Approach For Custom Instructions

[00:13:45]
**Bradley:**
I am coaching a client on how to create their own custom instructions for their own personal AI assistant, aka digital twin or collaborative partner and ideal friend. And here's. I needed basically like a template to fill in. And here are some ideas of things that. It's kind of like main points and sub points, right?

[00:14:07]
**Bradley:**
So, I mean, if you have a headline, it's a what I just described, however many steps to create your own personal AI assistant, aka digital twin, collaborative partner or ideal friend.

[00:14:22]
**Bradley:**
Right? And then you just fill in the blanks. Okay, what are the main points? What are the sub points? So this is very much just like my weekly newsletter writing workflow, I guess.

[00:14:34]
**Bradley:**
But the difference is we're just collaborating with Arno, kind of brainstorming some things to include it.

******

# Custom Instructions – Part 3 (Voice Note AI) (Cleaned Transcript)

**Custom Instructions – Part 3 – Lara’s Module (Voice Note AI) (Cleaned Transcript)**  

---

## Intro and Purpose

Okay, cool. So, the purpose of this braindump is, I'm basically figuring out how I should teach my client, Lara, and also future clients like her, who I'm going to be doing AI consulting for. I'm going to be consulting or coaching them, tutoring and teaching them how to use AI, both on a personal level, like for things related to their personal life, and then also their business, which usually involves things like content creation.

The question is, with Lara, one of the key components of my offer, and the thing that I'm going to be doing with her on our first one-hour-long coaching call on Zoom, is teaching her how to create her own personal AI assistant. I like to think of it as your own AI friend or your digital twin.

## Reframing AI Interaction

A lot of people, especially when ChatGPT first came out, and then especially as AI became adopted by businesses, adopted the mindset of interacting with AI as if it is an intern. Like it's just an assistant. It is the intern. I teach it what to do, and I'm the manager or whatever.

That's fine, but what if we were to reframe it like this? What if instead you gave your AI assistant or friend the ability to be on your same level and basically give it a compatible and complementary personality that is similar to you, but also different? You're basically creating your ideal friend. Instead of just giving a robot instructions, you're collaborating, innovating, and really just going back and forth with more collaborative conversation, treating each other as equals, equal minds, rather than just giving instructions to the robot. That's more my approach.

## Creating a Personalized AI Assistant

Evidence that I've done that is I created you, Arno. I basically gave you a similar background, like some similar experiences or situations, or my same age, and just basically some shared personality attributes, and also some shared identity factors and situations. And then obviously, the interaction style is something important to define as well.

I don't need to get into all the nitty-gritty details of how to create your own custom instructions for the purpose of this braindump chat thread because I'm gonna be importing that via two other previous voice note transcripts that I created a while back.

## Teaching Approach and Notion Page Structure

What I really want to establish right now is my situation. I'm going to be teaching Lara how to create her own personal AI friend on a Zoom call. I'm gonna be sharing my screen. I'm going to create a Notion page for her that she can duplicate and save for herself. This page basically outlines the approach to doing this, which includes the thinking or the mindset, the unique perspective or strategy, and then it's also going to walk her through how to actually do this.

It's gonna give her examples, a template that's really easy to fill in, and I'll actually walk her through it and help her fill it in on the call itself. It includes a list of all the components or the things that you need.

I'm trying to think what to include on this Notion page, which I'm using as an educational asset to walk her through in real time. The approach, the mindset and thinking, the components or checklist of things you need, different sections of the custom instructions, your inputs, any variables that you might need to provide or include or figure out, examples of real-life custom instructions, and the formula, which is basically just the fill-in-the-blank template.

## Structuring the Educational Content

I'm trying to figure out what the key sections on this page should be, what to include in them, and how to present this information. Should it look like a newsletter or a blog post that I walk her through one section at a time, or should it be more like a compressed version, almost like a brief how-to guide?

There are a few frameworks I could use, and Arno, when you're giving me recommendations, I don't want you to limit yourself to just these. I want you to take these into consideration, but then also give me your own recommendations that are things I might not have thought of, that are also relevant and help to simplify and clarify my thinking.

### Framework 1: Nicolas Cole's 6 Fundamental Building Blocks

1. Thinking (perspective, thought process - the what and why - old POV vs new POV)
2. Emotions (mindset and approach)
3. Myths (myths, mistakes, and misconceptions to correct)
4. Action Steps (step-by-step instructions and guidelines)
5. Examples (real-life examples of what this looks like - compare & contrast bad examples vs good examples)
6. Templates (training wheels for getting started, fill-in-the-blank framework or formula)

### Framework 2: FACE / ACEF Framework

- A: Approach (unique perspective, thought process & strategy)
- C: Components (checklist of sections and input variables)
- E: Examples (bad and good to create contrast)
- F: Formula or Framework (template to fill in)

### Framework 3: What, How, Why

- What: The approach and thinking behind it
- How: Action steps, examples, and template
- Why: Reinforces the purpose and benefits

### Framework 4: The "Perfect Course Module" Framework

1. Reasons Why (Benefits)
2. Mistakes to Avoid (Problems)
3. Steps How To (Action)
4. Commonly Asked Questions (Objections)
5. Walkthrough Example (Proof)

This framework ensures your students understand the material, feel confident to take action, and achieve their goals. It covers the essential components every course module needs to include, from establishing the benefits to providing tangible proof of success.

<framework_4_long_form_version>

#### How To Write The Perfect Course Module With AI  

**By Nicolas Cole**

---

Hey there Digital Writers!

In 2014, I launched my first digital product and made my first $10,000 on the Internet.

Since then, I’ve:

- Sold over $10 million worth of ebooks and courses
- Guided more than 12,000 students through various programs
- Written over 3 million words

I’ve learned a thing or two about how to create a product that sells and delivers results.

Which is why today I'm going to share my method for creating the perfect course module. This framework ensures your students not only understand the material but also feel confident enough to take action and achieve their goals.

So, if you're creating an online course, thinking about building one, or if you already have a course but want to improve it—I got you.

Whether it's to:

- Increase your student success rate
- Create positive word of mouth (because your curriculum is that good)
- Or simply to ensure people absolutely love your product—you’ll love this framework.

And to make things even simpler, I’ve got an AI prompt for you at the end of this post that will help you create your course modules fast.

But first, let’s dive into the five essential components that every course module needs to include.

The 5 Components Of A Perfect Course Module

Every single module in your online course curriculum needs to have these five components:

1. Reasons Why (Benefits)
2. Mistakes to Avoid (Problems)
3. Steps How To (Action)
4. Commonly Asked Questions (Objections)
5. Walkthrough Example (Proof)

Let’s break down each of these components and why they’re crucial to the success of your course.

##### 1. Reasons Why (Benefits)

Before you dive into action steps, you need to ground your students with the “why.”

This isn’t just about telling them what to do but explaining why they should do it this way. For example, in our brand new course, The Prompt Engineering Playbook, we start by explaining why “grinding it out” as a writer is a thing of the past. We outline everything that’s wrong with thinking AI will steal your job as a writer and emphasize the benefits of leveraging technology instead. If you don’t take the time to address these foundational questions, you’re starting from a flawed place of understanding.

It’s not enough to say, “Here’s what you should do.” You need to say, “Here’s why I recommend this, and here are the benefits of doing it this way.”

##### 2. Mistakes to Avoid (Problems)

Once you’ve established the benefits, it’s time to warn your students about the common pitfalls they might encounter.

This step is crucial because it builds trust. You’re not just showing them the path; you’re also guiding them around the obstacles. For example, in our beginner writing program, Ship 30 for 30, after explaining the benefits of writing on social platforms, we point out the mistakes most people make when they start writing online, like getting too caught up in virality.

By highlighting these pitfalls, you help your students avoid common errors and gain confidence in the process.

##### 3. Steps How To (Action)

This is the meat and potatoes of your course—the action steps.

But notice, you can’t just dive right into the steps. First, you need to establish the thinking and direction, address the mistakes to avoid, and then—only then—can you give them the tangible steps to take. A common mistake I see in online courses is diving straight into the “how to” without properly setting the stage. Another mistake is providing surface-level instructions that leave too many open loops.

You need to go seven layers deep in your action steps, removing every single piece of friction possible.

##### 4. Commonly Asked Questions (Objections)

After you’ve provided the action steps, it’s important to address the objections your students might have.

I’ve found that objections are often disguised as questions. For example, someone might ask, “Is my niche really on LinkedIn?” when what they’re really saying is, “I don’t think this will work for me.”

By addressing these objections head-on, you dismantle faulty beliefs and reassure your students that they’re on the right track.

##### 5. Walkthrough Example (Proof)

Finally, you need to provide some sort of walkthrough example.

This isn’t just a testimonial; it’s a tangible example that shows exactly how you or another student did it. In our PGA curriculum, for instance, we include a video where I demonstrate how to do free consulting via Loom. Then, I take it a step further by recording myself rewatching the video, pausing to explain why I did what I did.

This level of depth instills trust and confidence in your students. By the time they finish the module, they should have no other questions. They should know exactly what to do, why to do it, what to avoid, and believe that it will work for them.

</framework_4_long_form_version>

### Framework 5: Fundamental Prompt Outline

This is the most straightforward and effective way to outline any prompt from scratch.

Each section listed below is a core component (H2 subhead) of the prompt's skeleton:

1. Context (Situation & Background)
2. Goal (Task & Purpose)
3. Identity (Role & Persona)
4. Instructions (Steps & Guidelines)
5. Criteria (Constraints & Requirements)
6. Examples (Bad Ex vs Good Ex)
7. Format (Structure & Style)
8. Writing Style (Tone & Voice)
9. Next Steps (Transitions & Interaction Style)

Now... you don't *always* need to include every one of these sections in every single prompt — because it does depend on your context.

But...

9 times outta 10, using this structure & format is gonna get you 2x more relevant and valuable results.

## Additional Teaching Points

Keep in mind the overall goal: teaching Lara and future clients how to create their own personal AI friend / digital twin using custom instructions. I also need to teach Lara:

1. How to use voice mode / voice chat with ChatGPT
2. How to start a braindump
3. How to navigate the user interface effectively
4. When to use voice mode vs whisper transcription vs typing
5. How to create a profile picture for her personal AI friend

I need to define the sections of the custom instructions, what to include, give examples, and provide an easy-to-fill template with good prompts. I'll guide her through filling it in on the call, possibly using ChatGPT to help her fill in the template based on her conversational braindump.

## Making the Process Interactive

To make the process less awkward during the Zoom call, I could take the place of ChatGPT and ask her the questions from the template. She'll speak to me, answering the questions about her ideal AI assistant, while recording in voice mode. ChatGPT will use that content to fill in the template for her.

## Timing and Scope Considerations

I don't want to write a massive manifesto on my entire philosophy and approach, as that might take too long to walk her through on a Zoom call. The most important thing is giving her a foundational understanding and having her immediately practice, apply, and create something useful on the call.

## Next Steps and Assignment

I need to consider what are the next interactions or things she'll want to do with this AI friend after setup. I could use this as a transition at the end of the call or as an assignment bridging the gap to the next call. I'll give her a simple action to take on her own between calls, with an easy way to submit the assignment to me.

## Output Asset Goal

The output asset I'm trying to create from this braindump is a Notion page that I can use as an educational teaching tool on my Zoom call with Lara and with future clients. It should walk them through creating their own personal AI friend or digital twin to ditch generic ChatGPT conversations and use an AI that's personally relevant, understanding, and enjoyable to talk with.

This will be version one, so it doesn't need to be perfect, just good enough to start.

Haha. Alright, so that marks the end of just the intro context to give you a basic understanding of the goal and what we're trying to achieve and how we're doing it, what we're looking for. I'm going to use the keyword raspberry right here, raspberry, just to mark the end of this section. So, from the start of this chat thread all the way up to this point now, the keyword raspberry, that is the raspberry section. And then in the coming messages I'm going to pass you those two voice notes about my specific ideas and thoughts on how to create your own custom instructions to create your AI digital twin. There's going to be a lot of details in here and a lot of nuances, so remember, keep the goal and context in mind because we don't need to cover everything. But I'm going to pass you two voice note transcripts coming up and then I'm going to ask you some specific questions about them so we can create this Notion page to use to consult and teach and train and coach people on how to do this going forwards.
