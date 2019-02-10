﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define la = Character("Laffey", color="#AAED60")
define mc = Character("McCall", color="#AAED60")
define li = Character("Long Island", color="#AAED60")
define sd = Character("San Diego", color="#AAED60")


# The game starts here.

default box = 1

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    window hide
    scene black
    show opening_text "Azur Lane Drama CD Union Episode\n\nPart 1" with Dissolve(2)
    hide opening_text with Dissolve(2)
    scene bg beach
    show next at next_prompt, next_prompt_animation onlayer ontop
    with Dissolve(2)

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show laffey dark at center
    show laffey with dis

    # These display lines of dialogue.

    la "This is good ice cream, McCall. Thanks."

    window hide
    show laffey at move_left
    show laffey dark with dissolve
    show laffey dark at move_lefta
    show mccall dark at right
    show mccall with dis
    $ box = 2

    mc "Don’t mention it. I just wanted my good friend Laffey to know how great it is to eat popsicles on the beach under a parasol."

    show mccall dark
    show laffey
    with dis
    $ box = 1

    la "Uh huh. It’s really great."

    show laffey dark
    show mccall
    with dis
    $ box = 2

    mc "Right? Nothing better than wasting your day off eating ice cream until the sun sets."

    show mccall dark
    show laffey
    with dis
    $ box = 1

    la "But it’s only 10AM. Ice cream is great and all, but won’t you get a stomach ache eating that much?"

    show laffey dark
    show mccall
    with dis
    $ box = 2

    mc "Nope. I’ve got an iron gut when it comes to ice cream."

    show mccall dark
    show laffey
    with dis
    $ box = 1

    la "Iron gut? Not a second stomach?"

    show laffey dark
    show mccall
    with dis
    $ box = 2

    mc "Yeah. My stomach is strong as iron!"

    show mccall dark
    show laffey
    with dis
    $ box = 1

    la "Lucky. I think two or three is my limit. Like how I could barely eat anything at the mushroom party yesterday. It sucked."

    show laffey dark
    show mccall
    with dis
    $ box = 2

    mc "I don’t really care for mushrooms either. But hey, at least you can drink me under the table, Laffey."

    show mccall dark
    show laffey
    with dis
    $ box = 1

    la "That’s true."

    show laffey dark
    show mccall
    with dis
    $ box = 2

    mc "It’s hard to fill up on your favorite things, but if you get too greedy, you’ll pay for it in the end. As for mushrooms, you might be better off not eating too many."

    show mccall dark
    show laffey
    with dis
    $ box = 1

    la "What do you mean?"

    show laffey dark
    show mccall
    with dis
    $ box = 2

    mc "Like, you know all those mushrooms San Diego’s been growing in her room?"

    show mccall dark
    show laffey
    with dis
    $ box = 1

    la "That’s a little weird no matter which way you put it."

    show laffey dark
    show mccall
    with dis
    $ box = 2

    mc "Right? She gets all sparkly and giggly from inhaling those spores."

    show laffey
    with dis
    $ box = 1

    "{color=#AAED60}Laffey & Mccall{/color}" "Yeahhh."

    hide laffey
    hide mccall

    "pause for seagulls"

    show mccall at center

    mc "It’s nice to just unwind and eat."

    show mccall at move_right
    show mccall dark with dissolve
    show mccall dark at move_righta
    show laffey at left

    la "I think the red and white ones are prettier so they’re tastier."

    show mccall
    with dis

    "{color=#AAED60}Laffey & Mccall{/color}" "Ahhh. So relaxing."

    hide laffey
    hide mccall
    show long_island dark at center
    show long_island with dis

    li "Heyyy! I found Laffey and McCall! Heeeeyyyy!"

    hide long_island
    show laffey at center

    la "Long Island."

    hide laffey
    show mccall at center

    mc "Where’s the fire?"

    hide mccall
    show long_island at center, bobble2

    li "Listen up. Both of you went to San Diego’s mushroom party last night?"

    hide long_island
    show laffey at center

    la "Yup. We were there. We were just talking about it actually."

    show laffey at move_left
    show laffey dark with dissolve
    show laffey dark at move_lefta
    show mccall dark at right
    show mccall with dis
    $ box = 2

    mc "Uh huh. You didn’t go, Long Island?"

    hide laffey
    show long_island at left, bobble1
    $ box = 1

    li "I may be a ghost, but I’m not gonna risk my life eating unidentified mushrooms."

    hide mccall
    show laffey at right
    show long_island dark behind laffey with dis
    $ box = 2

    la "Did we risk our lives?"

    hide laffey
    show mccall at right

    mc "Well, I can’t argue with that."

    show long_island at left, shake2
    show mccall dark behind long_island with dis
    $ box = 1

    li "But actually I wish I wasn’t so careful just yesterday. I should’ve gone."

    hide mccall
    show laffey at right
    show long_island dark behind laffey with dis
    $ box = 2

    la "Why? Do you like mushrooms?"

    hide laffey
    show mccall at right

    mc "I think not going was the right move. Honestly."

    show mccall dark with dis
    show long_island at left with dis
    $ box = 1

    li "It actually looks like you haven’t changed at all. Lemme see."

    hide mccall
    show laffey at right
    show long_island dark behind laffey with dis
    $ box = 2

    la "Why are you staring at our breasts, Long Island?"

    hide laffey
    show mccall at right

    mc "You’re creeping me out. What the hell?"

    show mccall dark
    show long_island
    with dis
    $ box = 1

    li "Hmm. Seems I can’t tell without a more direct approach!"

    show mccall behind long_island
    show long_island at grabR
    pause 0.5
    show mccall at bobble1

    "(BOING)"

    hide mccall
    hide long_island
    show laffey at center

    la "Gasp"

    hide laffey
    show mccall at center, bobble1

    mc "Wh- what? Don’t just suddenly grab my chest like that."

    show mccall at move_right
    show mccall dark with dissolve
    show mccall dark at move_righta
    show long_island at left

    li "Hmm. Turns out you haven’t changed at all. Too bad. It was all for nothing."

    hide mccall
    show laffey at right
    show long_island dark behind laffey with dis
    $ box = 2

    la "What do you mean?"

    hide laffey
    show mccall at right, shake2

    mc "Tell us what’s going on or I’ll get you with this popsicle."

    show long_island
    show mccall dark
    with dis
    $ box = 1

    li "Your eyes are scaring me. Okay, settle down, I’ll explain. We can all come out winners here."

    hide mccall
    show laffey at right
    show long_island dark behind laffey with dis
    $ box = 2

    la "Winners?"

    hide laffey
    show mccall at right

    mc "Huh?"

    show mccall dark
    show long_island
    with dis
    $ box = 1

    li "The truth is I heard San Diego’s mushrooms have some awesome side effects."

    show long_island dark
    show mccall
    with dis
    $ box = 2

    mc "Awesome side effects? Like what?"

    show mccall at move_right_off
    show long_island dark at move_center
    show long_island with dissolve
    show long_island at move_centera
    $ box = 1

    li "Check it out. If you eat San Diego’s mushrooms… your breasts… become bigger!"

    hide long_island
    show laffey at center, shake1

    la "Ugh. I’m sleepy."

    hide laffey
    show mccall at center

    mc "Yeah. I think it’s time for a nap."

    show mccall at move_right
    show mccall dark with dissolve
    show mccall dark at move_righta
    show long_island at left, bobble3

    li "Wait wait! Don’t nap! It’s true! Everyone’s been talking about it. This isn’t just something I made up!"

    hide mccall
    show laffey at right
    show long_island dark behind laffey with dis
    $ box = 2

    la "But… I’m still the same."

    hide laffey
    show mccall at right

    mc "Mine didn’t get any bigger either."

    show mccall dark
    show long_island
    with dis
    $ box = 1

    li "It’s gotta be because you didn’t eat enough, or you ate the wrong kind."

    hide mccall
    show laffey at right
    show long_island dark behind laffey with dis
    $ box = 2

    la "Now that you mention it, there were different colored mushrooms."

    hide laffey
    show mccall at right
    show long_island dark behind mccall with dis

    mc "I think I ate like a red and white striped one."

    hide mccall
    show laffey at right
    show long_island dark behind laffey with dis

    la "Yeah. Same."

    show long_island dark at shake2
    show long_island
    show laffey dark behind long_island with dis
    $ box = 1

    li "Hmm. Then the red and white striped one isn’t it. Neither of you took any other mushrooms? Everyone took home what they couldn’t finish eating."

    show long_island dark
    show laffey
    with dis
    $ box = 2

    la "I was too full so I didn’t take any."

    hide laffey
    show mccall at right
    show long_island dark behind mccall with dis

    mc "Me too."

    show mccall dark
    show long_island
    with dis
    $ box = 1

    li "All right. Damn. Okay, we gotta go find some other partygoers. Right! Let’s make our breasts bigger so the Commander will drool at us! Let’s go!"

    hide mccall
    show laffey at right, grabL

    la "Wait."

    show laffey dark
    show long_island
    with dis
    $ box = 1

    li "What’s wrong?"

    show long_island dark
    show laffey
    with dis
    $ box = 2

    la "The Commander… likes big breasts?"

    show laffey dark
    show long_island
    with dis
    $ box = 1

    li "Umm… he didn’t say so directly. But the bigger ones seem to have more charm."

    show long_island dark
    show laffey
    with dis
    $ box = 2

    la "Laffey will go too."

    show laffey dark
    show long_island
    with dis
    $ box = 1

    li "Really!? Ehehehe. My party has grown! What do you think, McCall?"

    hide laffey
    show mccall at right
    show long_island dark behind mccall with dis
    $ box = 2

    mc "Um. I don’t really care about the size of my chest…"

    show mccall dark
    show long_island
    with dis
    $ box = 1

    li "So, you’re not coming?"

    show long_island dark
    show mccall
    with dis
    $ box = 2

    mc "Umm… I do want to know if the rumor is true. I’ll go."

    show long_island dark at bobble2
    show long_island with dissolve
    show mccall dark behind long_island with dis
    $ box = 1

    li "Da-daaaaan! McCall has joined my party! It’s time for us three to set out on our mushroom search adventure. Let’s go!"

    hide long_island
    show laffey at center

    la "Ok."

    scene black

    "Break"

    scene bg room
    show long_island at center

    li "And so, Long Island and her merry men arrived at San Diego’s room."

    hide long_island
    show laffey at center

    la "We’re merry?"

    hide laffey
    show mccall at center

    mc "Well, as merry as a group hunting for breast-growing mushrooms can be."

    hide mccall
    show long_island at center

    li "Hey, cut the chatter, it’s an ambush! There may still be mushrooms here."

    hide long_island

    "Knock knock"

    show long_island at center

    li "Anybody home!?"

    show san_diego dark at center
    show san_diego with dis

    sd "Yeess? Who is iiit?"

    hide san_diego
    show long_island at center

    li "It’s Long Island!"

    hide long_island
    show laffey at center

    la "Laffey and McCall too."

    hide laffey
    show mccall at center

    mc "Can we come in?"

    hide mccall
    show san_diego at center

    sd "Sure! Ah! Just give me a minute here. Let yourselves in! Welcome welcome!"

    hide san_diego
    show long_island at center

    li "All right, coming in. Sorry to bother you!"

    hide long_island
    show san_diego at center

    sd "Hello! Lovely weather, isn’t it? I’m a little tired but let’s dance!"

    hide san_diego
    show laffey at center

    la "San Diego’s really dancing."

    hide laffey
    show mccall at center

    mc "She seems kind of tense. Maybe some ice cream would calm her down."

    hide mccall
    show san_diego at center

    sd "Huuuh? That’s right! I’ve been dancing nonstop! Kinda weird!"

    hide san_diego
    show long_island at center

    li "You didn’t even notice you’ve been dancing? It must be… ah! There’s a half-eaten mushroom on the table there!"

    hide long_island
    show laffey at center

    la "Did San Diego eat it?"

    hide laffey
    show san_diego at center

    sd "Yeah! I ate it! Just about the time I wanted to break into dance! Everybody join me!"

    hide san_diego
    show mccall at center

    mc "No. The real reason you’re dancing is because of this mushroom."

    hide mccall
    show long_island at center

    li "That sounds right. So then… this star-shaped yellow one with spots all over it must be a dancing mushroom!"

    hide long_island
    show san_diego at center

    sd "Yeeaahh! Dancing dancing!!"

    hide san_diego
    show laffey at center

    la "So then, what were the ones we ate?"

    hide laffey
    show long_island at center

    li "Those were fail mushrooms!"

    hide long_island
    show mccall at center

    mc "Feels more like a win mushroom to me."

    hide mccall
    show san_diego at center

    sd "Win? Fail? Nah! I dunno why everybody came to my room, but you better dance with me!"

    hide san_diego
    show laffey at center

    la "Not now. Laffey and friends came to find the mushroom that makes your breasts bigger."

    hide laffey
    show long_island at center

    li "That’s right. Long Island and her band of merry men are on a quest for the BUST UP mushroom!"

    hide long_island
    show mccall at center

    mc "When you call it a BUST UP mushroom I feel like we’ve fallen into something really shady."

    hide mccall
    show san_diego at center

    sd "Eeeeeeh? Is there really a mushroom like that? Amazing!"

    hide san_diego
    show long_island at center

    li "Yeah! Do you have any more mushrooms laying around, San Diego?"

    hide long_island
    show san_diego at center

    sd "Nope! That dancing mushroom I just ate was the last one!"

    hide san_diego
    show laffey at center

    la "Damn."

    hide laffey
    show long_island at center

    li "But we did learn the effect of one type of mushroom. Let’s press on to find the next!"

    hide long_island
    show mccall at center

    mc "Ah! I think we should go to Cassin next. I saw her fidgeting with a weird looking purple mushroom."

    hide mccall
    show san_diego at center

    sd "Wait up! I’m going too!"

    hide san_diego
    show laffey at center

    la "While dancing?"

    hide laffey
    show san_diego at center

    sd "Yeah! Dancing! LET’S GO!"

    hide san_diego
    show mccall at center

    mc "She’s got some moves!"

    hide mccall
    show long_island at center
    li "Da-daan! The dancer has joined my party!"

    hide long_island
    show laffey at center

    la "Attack power UP? Heh. Right?"

    scene black with Dissolve(2)

    # This ends the game.

    return
