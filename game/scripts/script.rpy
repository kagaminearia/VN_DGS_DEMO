# The game starts here.

label start:
    $ quick_menu = False
    scene black with dissolve
    show screen disclaimer with dissolve
    pause
    hide screen disclaimer with dissolve
    pause
    
    call ch0
    call ch1_1
    call ch1_2
    return


