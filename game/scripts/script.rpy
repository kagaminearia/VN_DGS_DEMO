# The game starts here.

label start:
    $ quick_menu = False
    scene black with dissolve
    show screen disclaimer with dissolve
    pause
    hide screen disclaimer with dissolve
    pause
    
    call c0 from _call_c0
    call c1_1 from _call_c1_1
    call c1_2 from _call_c1_2
    return


