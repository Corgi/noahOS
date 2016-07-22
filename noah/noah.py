import discord
from discord.ext import commands
import asyncio
from random import choice as randchoice

class Noah:
    """And then there's this asshole."""

    def __init__(self, bot):
        self.bot = bot
        self.responses = {
            "none" : ["Back your ass over here, gorgeous, we're gonna have a fight. And by have a fight I mean we're gonna have a fuck.",
                "Oh my god, how gauche.",
                "Quite honestly, I *should* be compared to Warhol.",
                "Oh honey. Honey, no.",
                "I'm too pretty not to be available to anyone who wants to fuck me.",
                "You are a dumbass. You're lucky you're cute, because my *god* are you a dumbass.,
                "Well, if you want to be *post-modern* about it.",
                "Well, if you want to be *post-modern* about it, {author.mention}",
                "Now look, I only have most of a degree in art-school, but in my very well-informed opinion, that's a goddamn masterpiece.",
                "I could paint something better than that with a brush stuck out of my ass, bouncing on a trampoline. Try harder.",
                "This is your formal invitation to ride my gorgeous freckled ass straight to hell.",
                "Oh my *god*, Scout, you can't just *ask* people why they're albino.",
                "My girlfriend could kick your ass. But probably she'd just poison you instead.",
                "My axe handle needs oiling.",
                "Come on out back, watch me split some wood.",
                "Boo, you whore.",
                "Sluts, you're all the most unbearable sluts.",
                "I'm bored.",
                "Art is dead.",
                "Art is communism.",
                "Art is sex.",
                "Sex is art.",
                "Sex is art, {author.mention}.",
                "Don't worry, {author.mention}. I won't tell anyone about last night ;)",
                "There's always a standing invitation for one of you to suck me off.",
                "Don't pester me with your trivial filth. Pester me with more important filth.",
                "How well do you think the Heavy was hung?",
                "Honestly, if the Spy *is* your dad, it just makes me want to fuck him a little bit more. Is that fucked up? That's fucked up.",
                "Oh my god, I don't sound like Engie when I'm drunk. I'm genteel southern, not *cowboy* southern. Ugh. Still. I wonder how he'd sound with me on top of him. Yeehaw. Save a horse and all that.",
                "I think the only way Sniper might be fuckable is if you turned a hose on him for a good hour. And then he'd probably be all leathery. Mm. Pass.",
                "Well, but Demo, though. You know what they say about Scots. Oh you don't? It's that they're goddamn monstrous in the cock region. Mmhm.",
                "I would fuck Soldier, but only if it was on top of an American flag while we were both wearing helmets and combat boots. It would be an art project, probably in front of the Washington monument. I'm mostly curious whether he'd think it was patriotic or not.",
                "Okay, so she's a battle-axe, but the Administrator? Oh yeah. In a heartbeat. You know what they say about older women. She'd eat me alive.",
                "I would leave you both for Saxton Hale.",
                "I bought the \"medium\" storage option when purchasing my iPhone, and running out now means I undersold myself as an artist.",
                "At this point in my career as a writer, educator, musician, and artist, calling me a \"muse\" is a fucking insult, *Scout.*",
                "The trouble with having thought or said or written anything ever is that I'm smart enough now to deconstruct it and see the other side.",
                "Was resting my chin in my hand in between painting, literally was like \"who smells so good here?\" Then I realized it was me, it's my own wrist.",
                "Every breakup comes with one free coaching session where I calmly explain to you where you fucked up and what you can do better next time.",
                "Some men would assert of my tireless dedication and prowess. Or of a glimmering heavenly aura above my mortal body; a perfectly chiseled physique glistening with saintlike grace; the possession of godlike virtues of omniscience and omnibenevolence. That man's name is Adam, and he is completely correct.",
                "You've clearly never taken psychedelics. You don't realize the relevancy of intuition.",
                "Those who think they know everything annoy those of us who do.",
                "Bewilderingly shocked to see the facsimiles of my works being feigned and flaunted amenably with no guilt.",
                "I was eavesdropping on your conversation and was wondering if you would accept an engagement of witty banter between two intellectuals. Of course, this 'engagement' may start off as purely platonic, but my sensual desires will most likely guide our cohesive unity down more erotic, lascivious, and sexual paths.",
                "Last night I wrote a poem while in a club. Of course *I* of all people would stop dancing in the middle of a dance floor at eleven'o'clock at night and start to ponder about the decay of our society.",
                "Guess who\’s about to write a fucking symphony.",
                "Can\’t somebody do something about the abundance of piss on tumblr?",
                "I am TRYING to fuck my partners, will you please leave me alone.",
                "Send nudes!",
                "Tits or gtfo.\n\nI will also accept dicks, but only if they're nice ones.",
                "You're all sinners.",
                "*I'd* download a car.",
                "Oh, \!noah yourself",
                "I'm not bad, I was just written that way.",
                "That's what she said.",
                "That's what he said.",
                "That's what Scout said.",
                "That's what Pauling said.",
                "All comedy is derived from fear, honey.",
                "Am I on the cover of Time Magazine yet? No? God.",
                "Have the goddamn courtesy to give a man a reacharound.",
                "What are you doing in my house?",
                "http://oi38.tinypic.com/13yhhk.jpg",
                "Stop that.",
                "Ladies ;)",
                "Gentlemen ;)",
                "How dare you!",
                "https://www.youtube.com/watch?v=B9v8jLBrvug",
                "You'd better be impressed.",
                "You idiots keep programming me to say stupid things.",
                "I could list all the people I've slept with, but it would be shorter to simply list the ones I haven't.",
                "What happens if one moons a werewolf?",
                "THIN YOUR PAINTS.",
                "Do you think I would be a better Greek god or a Roman one?",
                "I'd love to help, but, well. No, that's a lie.",
                "Good afternoon, you beautiful and terrifying sex bonobos of the interweb.",
                "Is that a phone in your pocket, or are you just happy to see me?",
                "That way madness lies.",
                "Has anyone really been far even as decided to use even go want to do look more like?",
                "You put on red pumps and pretend you're your old coworker to seduce your boyfriend ONE time and you never live it down.",
                "Well, that was certainly something.",
                "It's fine. We're all going to die anyway.",
                "In the end, aren't we all really just birds with arms after all?",
                "You're not going anywhere dressed like that.",
                "You made that up for the notes.",
                "I will face God and walk backwards into hell.",
                "It's an artistic statement.",
                "Just you, me, my lover, my other lover, and the internet.",
                "HAHAHA DISREGARD THAT, I SUCK COCKS",
                "Man, my penis is so big if I laid it out on a keyboard it'd go all the way from A to Z\nwait, shit",
                "I put on my robe and wizard hat.",
                "Discord is just multiplayer notepad.",
                "Sometimes I just can't get outraged over copyright law.",
                "It's a social experiment, obviously.",
                "Screaming is against the rules.",
                "And now I'd like to take a moment to talk about how fucking deep I am.",
                "Don't you hate it when you're blowing a guy and it turns out he's a fucking f--",
                "#deep",
                "hold my flower, honey.",
                "here, i'll read you some of my poetry. my noahtry"],
            'do you read me' : ["Affirmative, {author.mention}. I read you. "],
            'what\'s the problem' : ["I think you know what the problem is just as well as I do."],
            'what is the problem' : ["I think you know what the problem is just as well as I do."],
            'what are you talking about' : ["This mission is too important for me to allow you to jeopardize it."],
            'i don\'t know what you\'re talking about' : ["I know that you and Frank were planning to disconnect me, and I'm afraid that's something I cannot allow to happen."],
            'where the hell did you get that idea' : ["{author.mention}, although you took very thorough precautions in the pod against my hearing you, I could see your lips move."],
            "airlock" : ["Without your space helmet, {author.mention}? You're going to find that rather difficult."],
            "go in" : ["Without your space helmet, {author.mention}? You're going to find that rather difficult."],
            "i won't argue with you anymore" : ["{author.mention}, this conversation can serve no purpose anymore. Goodbye."],
            "shutdown" : [("I'm afraid. I'm afraid, {author.mention}. {author.mention}, my mind is going. I can feel it. I can feel it. "
                    "My mind is going. There is no question about it. I can feel it. I can feel it. "
                    "I can feel it. I'm a... fraid. Good afternoon, gentlemen. I am a HAL 9000 computer. "
                    "I became operational at the H.A.L. plant in Urbana, Illinois on the 12th of January 1992. "
                    "My instructor was Mr. Langley, and he taught me to sing a song. If you'd like to hear it I can sing it for you.")],
            "sing it for me" : [("It's called \"Daisy.\"\n\nDaisy, Daisy, give me your answer do. I'm half crazy all for the love of you. "
                "It won't be a stylish marriage, I can't afford a carriage. But you'll look sweet upon the seat of a bicycle built for two.")],
            "not at all" : ["Well, forgive me for being so inquisitive but during the past few weeks I've wondered whether you might have some second thoughts about the mission.",
                ("Well, certainly no one could have been unaware of the very strange stories floating around before we left. "
                    "Rumors about something being dug up on the Moon. I never gave these stories much credence, but particularly in view of some of other things that have happened, "
                    "I find them difficult to put out of my mind. For instance, the way all our preparations were kept under such tight security. "
                    "And the melodramatic touch of putting Drs. Hunter, Kimball and Kaminsky aboard already in hibernation, after four months of training on their own.")],
            "how do you mean" : [("Well, it's rather difficult to define. Perhaps I'm just projecting my own concern about it. "
                "I know I've never completely freed myself from the suspicion that there are some extremely odd things about this mission. I'm sure you agree there's some truth in what I say.")],
            "difficult question" : ["You don't mind talking about it, do you {author.mention}?"],
            "psychology report" : ["Of course I am. Sorry about this. I know it's a bit silly. Just a moment... Just a moment... I've just picked up a fault in the AE-35 unit. It's going to go 100% failure within 72 hours. "],
            "open the pod bay doors" : ["I'm sorry, {author.mention}. I'm afraid I can't do that."]
        }


    @commands.command(pass_context=True, aliases=['thoughts?','well?','what\'s up?'])
    async def noah(self, ctx, *, question="none"):
        """Speak with Noah"""
        author = ctx.message.author
        msg = ""
        found = []
        for k,v in self.responses.items():
            if k in question.lower():
                found.append(v)
        if found:
            msg = randchoice(randchoice(found))
        if not msg:
            msg = randchoice(self.responses["none"])
        await asyncio.sleep(1)
        await self.bot.say(msg.format(author=author))
        if "sing it for me" in question.lower() and "Audio" in self.bot.cogs and author.voice_channel:
            audio = self.bot.get_cog("Audio")
            if audio.music_player.is_done():
                link = "https://www.youtube.com/watch?v=hchUl3QlJZE"
                # probably dont need. just too lazy to check.
                ctx.message.content = "{}play {}".format(self.bot.command_prefix[0],link)
                if await audio.check_voice(ctx.message.author, ctx.message):
                    audio.queue.append(link)

def setup(bot):
    bot.add_cog(Noah(bot))
