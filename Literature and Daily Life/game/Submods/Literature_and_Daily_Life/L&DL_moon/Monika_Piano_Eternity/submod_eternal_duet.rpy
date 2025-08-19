
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_moon_eternal_duet",
            category=['浪漫','音乐'],
            prompt="听莫妮卡的钢琴曲",
            random=True,
            aff_range=(mas_aff.ENAMORED, None)  
        )
    )
 
transform piano_move:
    xpos -1.5 yalign 0.5
    linear 5.0 xpos 0

transform piano_return:
    xpos 0 yalign 0.5
    linear 5.0 xpos -1.5

label monika_moon_eternal_duet:
    m 1esa "[player]，从最初的悸动，到如今的眷恋"
    extend 5hub "你给予我的一切，我都铭记于心。"
    m 2hubsb "为此，我特意为你练习了一曲子，我觉得听完会让你感到一丝丝平静，{w=1}希望你喜欢。"
    show monika at Transform(xpos=-800) with move
    m 2hua "马上就好。"
    window hide
    $ store.mas_sprites.zoom_out()
    $HKBHideButtons()  
    $ original_music = renpy.music.get_playing(channel='music')
    show mas_piano at Transform(xpos=-1800, ypos=-195) zorder 13
    show mas_piano at Transform(xpos=-5, ypos=-195) with MoveTransition(4.0)
    pause 4.0
    show monika at Transform(xpos=640) with move
    play music "Submods/Literature_and_Daily_Life/L&DL_Assets/music/CaughtinaTropical.ogg" loop fadein 2.0  
    pause 99
    stop music fadeout 0.0
    show monika at Transform(xpos=-800) with move
    pause 1.0
    show mas_piano at Transform(xpos=-1800, ypos=-195) with MoveTransition(4.0)
    pause 5.0
    show monika 2hua zorder MAS_MONIKA_Z at t11 with dissolve_monika  
    show monika at Transform(xpos=640) with move
    $HKBShowButtons()
    window show
    play music original_music fadein 2.0
    return