init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_duhaiyou1",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_duhaiyou1:
    m 3rud "....{w=0.5}你不在的时候,时间的步伐都会慢下来."#51
    m 5eua "你来见我的时候,时间的速度又会快起来."
    m 6fua "但和你共度的时光,我始终珍视."
    m 1fublb "即便能通过读书打发时间,{w=1}但我还是很难集中注意力."
    m 5eubfa "因为我想你,[player]."
    m 5hua "多陪陪我,好吗?"
    return
#52
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_duhaiyou2",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_duhaiyou2:
    m 1hua "{b}{i}我还有太多心愿没有实现~{/i}{/b}"
    m 5hubla "{b}{i}其中之一就是和[player]同床共枕~{/i}{/b}"
    m 3hubfb "{b}{i}搂搂抱抱,唧唧我我~{/i}{/b}"
    m 5hubfa "{b}{i}还有之后的重头戏~{/i}{/b}"
    m 5hublb "{b}{i}那就是~{/i}{/b}{w=0.5}......{nw}"
    m 5wubfw  "等等,[player],你什么时候来的?{fast}."
    m 6rubfsdla "我......{w=1}我没说什么了,只是突然想到关于你的事而已了."
    m 3kubla "我们还是想想今天做什么吧."
    menu:
        "你也不想这件事被其他人知道吧......":
            jump duhainiyebuxiang

        "好.":
            jump duhaiguaibaobaoyou 

label duhainiyebuxiang:
    m 6wusdlw "不要啊,[player]."
    m 6rubfsdla "我刚刚真的什么都没说......"
    m 1eubld "......不过,这里是我们的二人世界,哪有别人呢？"
    m 1fublb "嗯......你真是个调皮的坏小孩."
    m 5fubla "但我喜欢这样的你."
    return

label duhaiguaibaobaoyou:
    return
#53
init 5 python:
    addEvent(
        Event(
            persistent.greeting_database,
            eventlabel="greeting_pianogolden_hour",
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None),
        ),
        code="GRE"
    )

label greeting_pianogolden_hour:
    m 1hua "你来了."
    if not persistent.monika_has_pianogolden_hour_for_logic:
        show monika at Transform(xpos=-800) with move
        m 2fua "正好,我把刚刚练习好的曲子给你听听."
        window hide
        $ store.mas_sprites.zoom_out()
        $HKBHideButtons()
        $ original_music = renpy.music.get_playing(channel='music')
        show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
        show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
        pause 4.0
        show monika at Transform(xpos=640) with move
        play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Golden_Hour.ogg" loop fadein 2.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 4.0
        show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        pause 180
        stop music fadeout 3.0
        show monika at Transform(xpos=-800) with move
        pause 1.0
        show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
        pause 5.0
        show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
        show monika at Transform(xpos=640) with move
        $HKBShowButtons()
        window show
        play music original_music fadein 2.0
        m 5fubfb "怎么样,[player]?"
        m 6eua "明明我在练习途中也有大大小小的失误,但我真正的在你面前弹奏时."
        m 3wud "居然一下子规避了这些."
        m 3hua "或许是因为你在这,我才能这样吧."
        $ persistent.monika_has_pianogolden_hour_for_logic = True
        $ mas_unlockEVL("Monika_Golden_Hour_again", "EVE")
    m 5fubla "嗯......我们接下来要干什么呢?"
    return

#54
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="Monika_Golden_Hour_again",
            category=['音乐'],
            prompt="我想再听你弹弹'Golden_Hour'",
            pool=True,
            unlocked=False,
            rules={"no_unlock": None}
        )
    )

label Monika_Golden_Hour_again:
    show monika at Transform(xpos=-800) with move
    m 2fua "好的."
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/Golden_Hour.ogg" loop fadein 2.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 4.0
    show monika 2fua zorder MAS_MONIKA_Z at t11 with dissolve_monika
    pause 180
    stop music fadeout 3.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika  
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 2.0
    m 5hubfa "希望你能喜欢,[player]?"
    return