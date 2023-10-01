
define waiter = Character("Waiter")
define kenzo = Character("Kenzo")
define unknown = Character("??")
define sara = Character("Sara")
define priya = Character("Priya")
define ayush = Character("Ayush")
define ichika = Character("Ichika")
define saki = Character("Teacher")

# The game starts here.
label start:
    $help = 0
    $thinking = 0

    play music "music/rest.opus"
    scene dark
    waiter "Sirrrr..."
    image pic = im.Scale("background/dissolve bg.png", 1920, 1580)
    scene pic with fade
    waiter "Sirrr... Wake Up!"
    scene restaurant with fade
    show waiter worried
    waiter "Did you sleep sir?"
    kenzo "No, I was lost in my thoughts."
    scene restaurant
    show waiter weired
    waiter "It's 9'O clock and the restaurant is bout to close."
    kenzo "I'm leaving, can you give me my bill please?"
    scene restaurant
    show waiter good
    waiter "Sure sir, just give me a sec"
    scene res exit with fade
    "You paid your bill and left for the train."
    play music "music/station.opus"
    scene outside
    "It is raining outside and you are having a bad feeling about this."
    scene station
    "You reached the station by 9:30 as it's nearby the restaurant."
    play music "music/train.opus"
    scene train night with fade
    "Luckily you got your train."
    "And it was empty, just like you are from inside."
    scene train tunnel with fade
    "As soon as the train passes throgh a tunnel, you started getting lost in your thoughts again."
    scene dark
    unknown "Hellllpppppp..."
    scene pic with fade
    unknown "Hellllpppppp..."
    play music "music/station.opus"
    scene crying with fade
    unknown "Hhhghhh hgghhh"
    scene pic with fade
    "Within a blink"
    scene rain road with fade
    show unknown cry:
        zoom 1.5
    "She comes close to you."
    unknown "Help me pleasssssssssssssseeeeeeeeeeeeeeeee."
    kenzo "Yeah, Yeah, I will, what's the problem tho?"
    unknown "I'm Sara."
    show sara explaining:
        zoom 1.5
    sara "Someone stole my bag and... and..."
    sara "I lost my phone and I don't have money to go back to home."
    sara "Aaaahhhh"
    kenzo "Ohk, Ohk, Please stop crying, I'll help you."
    show sara good:
        zoom 1.5
    sara "You're a lifesaver."
    "**You in thoughts: Should I really help her?**"

    menu:
        "Yes, I Should!":
            call help
            $help = 1
        "No, She might be trying to scam me!":
            call scam

    "You welcomed her and suddenly..."
    scene pic with fade
    "You start to loose your consciousness."
    scene dark with fade
    scene pic with fade
    play music "music/train.opus"
    scene train night with fade
    "You woke up in the train"
    scene train night no rain with fade
    "You're about to reach your stop."
    scene station one with fade
    "You left the train at your stop."
    "The rain is also about to stop and it's morning already."
    play music "music/good day.opus"
    image pic4 = im.Scale("extra/codewithayu.jpg", 1920, 1580)
    scene pic4 with fade
    "You sat on a bench on the station and starts surfing internet."
    kenzo "Oh, Ayush uploaded a new visual novel, I'll probably try it by today."
    image pic5 = im.Scale("background/road.jpg", 1920, 1580)
    scene pic5 with fade
    menu:
        "Take usual route to go home":
            "You leaves the station to go to your home."
            call usual
        "Take a new route to go home":
            "You leaves the station to go to your home."
            call unusual
    return

label help:
    kenzo "How much money do you need to go back to your home?"
    show sara ask:
        zoom 1.5
    sara "I don't need much, just..."
    sara "Just give me 500 Yen."
    kenzo "Well, ohkkk..."
    "You gave her 500 Yen and felt happy to help someone."
    show sara norm:
        zoom 1.5
    sara "You are really a good person."
    show sara happy:
        zoom 1.5
    sara "Thank You!, You really are an angel."
    return

label scam:
    kenzo "(I Think she's trying to scam me.)"
    kenzo "Well, I really wanna help you, but..."
    show sara ask:
        zoom 1.5
    sara "But what?!?"
    kenzo "But I don't have money myself."
    kenzo "Sorry."
    show sara explaining:
        zoom 1.5
    sara "What?!? But you've just said you'll help!!"
    kenzo "Yeah, I did, but that was just to stop you from crying."
    kenzo "Don't worry, I'll still help you."
    show sara worried:
        zoom 1.5
    sara "How?"
    image pic3 = im.Scale("background/rainy.png", 1920, 1580)
    scene pic3 with fade
    "You turns around and starts moving in opposite direction."
    kenzo "Follow me"
    image pic2 = im.Scale("background/police.jpg", 1920, 1580)
    scene pic2 with fade
    show sara norm
    "You lead her to the nearest police station."
    kenzo "Police will help you reach your home."
    sara "I hope police will help me."
    sara "Well, Thanks anyway."
    return

label usual:
    play music "music/home.opus"
    image pic10 = im.Scale("background/bedroom.png", 1920, 1580)
    scene pic10 with fade
    "As soon as you reaches your home, you start playing DeadSoul."
    scene playing
    kenzo "This game is love."
    kenzo "I wish I had such crush in my college days."
    image pic11 = im.Scale("background/evening.png", 1920, 1580)
    scene pic11 with fade
    "You kept playing it till evening."
    scene dark
    "You were feeling tired so you closed your eyes."
    play music "music/surp.opus"
    "A girl came in your dream..."
    show priya norm
    priya "Heyy"
    show priya
    priya "You had a crush on someone in high school, remember?"
    kenzo "(Surprised) Who??"
    show priya blush
    priya "That you have to find yourself."
    scene pic
    scene pic11 with fade
    "You woke up in a surprise."
    kenzo "Who was the person I had a crush on?"
    kenzo "Was that just a dream??, Or??"
    kenzo "Was she right?"
    kenzo "Should I try to remember?"

    menu:
        "Yes, I should.":
            call think
            $thinking = 1
        "No, I shouldn't":
            kenzo "I shouldn't I guess."
            kenzo "That's just a waste of time."

    scene pic with fade
    scene dark with fade
    ""
    play music "music/ayush.opus"
    if thinking >=1:
        show ayush angry at center:
            zoom 0.9
        ayush "Her timing was bad, wasn't it?"
        show ayush sad
        ayush "You were about to get your answer."
        show ayush n
    else:
        show ayush n at center:
            zoom 0.9
        ayush "You should have thinked about her"
    ayush "Anyway"
    show ayush smile
    ayush "You helped a girl, remember?"
    if help >= 1:
        kenzo "When?"
        show ayush curious at center:
            zoom 0.9
        ayush "Think about it."
        kenzo "Ummm..."
        scene pic with fade
        scene rain road with fade
        show sara happy:
            zoom 1.5
        scene pic with fade
        scene pic11 with fade
    else:
        ayush "Although you thought that she was a scammer, you helped her."
        scene pic with fade
        scene pic2 with fade
        show sara norm
        scene pic with fade
        scene pic11 with fade
    kenzo "Who was that girl?"
    kenzo "And why Ayush wanted me to recall her?"
    kenzo "Was she my crush?"
    kenzo "Or just a normal girl?"
    kenzo "I wonder..."
    kenzo "I, I wonder..."
    return

label unusual:
    "You started moving using the new path and saw..."
    play music "music/ayush.opus"
    image pic6 = im.Scale("background/accident.jpg", 1920, 1580)
    scene pic6 with fade
    "A truck is bout to hit you from behind and..."
    play music "music/accident.opus"
    image pic7 = im.Scale("background/hit.png", 1920, 1580)
    scene pic7 with fade
    "You got hit..."
    scene dark with fade
    ""
    play music "music/drama.opus"
    show injured
    "You're lying injured there asking for help."
    "You turns your head..."
    scene dark with fade
    image pic8 = im.Scale("background/someone.png", 1920, 1580)
    show pic8:
        zoom 1
        yalign 0.5
        yalign 0.5
    "And saw that a girl is holding your hand."
    scene dark with fade
    ""
    scene pic with fade
    play music "music/rest.opus"
    scene restaurant with fade
    "You woke up and found that you were sleeping in the restaurant"
    "You asked for the bill and..."
    show letter at right:
        zoom 0.35
    "You get a letter with it."
    "The letter reads, 'Thanks for the help, You're an angel."
    scene restaurant with fade
    "You starts thinking that 'Was the thanks for helping that girl?'"
    "Or it's just cause I ate in this restaurant?"
    "Should I ask her?"
    menu:
        "Yes, ask the waiter.":
            kenzo "Heyy, can you help me a bit?"
            waiter "Yes sir, I'm coming."
            show waiter good
            kenzo "Why did you say thanks?"
            show waiter weired
            waiter "It's just cause you ate in our restaurant and gave me the tip."
            show waiter good
            waiter "Thanks again."
            kenzo "Oh, It's nothing."
            kenzo "Thanks..."
        "No, It's nothing.":
            "You (in toughts): That's just cause I ate here, nothing more!"
    scene pic5 with fade
    "You leaves the restaurant and starts going to home."
    "You (in thoights): Was the thanks really cause I visited that restaurant?"
    "You (in thoights): I hope it was."
    "Suddenly you noticed something..."
    play music "music/ayush.opus"
    kenzo "Isn't this road where I met that accident in my dream?"
    kenzo "Was that really a dream?"
    kenzo "I wonder if that was a dream, or..."
    kenzo "or..."
    kenzo "or????"
    kenzo "I wonder"
    return

label think:
    play music "music/good day.opus"
    scene dark
    "You closed your eyes again."
    "You put pressure on your brain cells to remember someone from your past."
    scene pic
    "On the farewell day..."
    image pic9 = im.Scale("background/farewell.png", 1920, 1580)
    scene pic9 with fade
    "Time: 7:46PM, everyone have probably left this place"
    show ichika norm with fade
    "A girl with the beauty of 1000 flowers appears."
    ichika "Hey, Kenzo..."
    kenzo "Yes."
    ichika "The farewell party is over, why didn't you go home?"
    kenzo "(Silently) Was waiting for you"
    show ichika worried
    ichika "What??"
    kenzo "Nothing, I just roaming around as today's our last day."
    show ichika tasting
    ichika "You're probably right, I wish I could have spent more time with you."
    kenzo "(Surprised) What??"
    show ichika blush
    ichika "It's just that, I like you and don't want to get separated."
    kenzo "Do you have a crush on me?"
    show ichika surprised
    kenzo "I mean I, I have a crush on you."
    kenzo "Do You....??...."
    show ichika norm at left
    show saki curious at right with fade:
        zoom 0.35
    saki "What are you two doing here?"
    show saki angry at right:
        zoom 0.35
    saki "Go back home and focus on the things you want to do after school."
    return
