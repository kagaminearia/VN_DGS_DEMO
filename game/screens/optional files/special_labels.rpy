## Special Labels ##############################################################
##
## These are special labels that Ren'Py automatically recognizes if they
## are included with the game. Read more here:
## https://www.renpy.org/doc/html/label.html#special-labels
##

## Splash Screen ###############################################################
##
## Put the splash screen code here. It runs when the game is launched.
##
label splashscreen():
    $ quick_menu = False
    scene black with dissolve
    show screen demo with dissolve
    pause 1.5
    hide screen demo with dissolve
    pause 0.5
    return

## After Load ##################################################################
##
## Adjust any variables etc in the after_load label
## Also consider: define config.after_load_callbacks = [ ... ]
##
label after_load():
    return


screen demo:
    add "#000000"
    vbox:
        style_prefix "disclaimer"
        xalign 0.5
        yalign 0.5
        spacing 20
        vbox:
            label _("本程序为独立游戏《如梦金色雪》的试玩版。")
            text _("——仅展示游戏风格，不代表游戏的正式内容。")
    

style demo_label_text:
    color gui.white
    size 35
    font gui.detailtitle_font

style demo_text:
    color gui.white
    size 28
    font gui.detail_font