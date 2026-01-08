
## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

# Global variable to store the on screen text
default say_what = ""

screen say(who, what):
    key "mousedown_4" action ShowMenu("history")
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    on "show" action SetVariable("say_what", what)

    ## If there's a side image, display it in front of the text.
    add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

# Style for the dialogue window
style window:
    xalign 0.5
    yalign 1.0
    xysize (1300, 270)
    padding (60, 30, 40, 40)
    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

# Style for the dialogue
style say_dialogue:
    color '#000000'
    adjust_spacing False
    ypos 35
    xpos 0

# The style for dialogue said by the narrator
style say_thought:
    is say_dialogue

# Style for the box containing the speaker's name
style namebox:
    xpos -60
    ypos -105
    xysize (230, 100)
    background Frame("gui/namebox.png", 5, 5, 5, 5, tile=True, xalign=0.0)
    padding (5, 5, 5, 5)

# Style for the text with the speaker's name
style say_label:
    color '#000000'
    xalign 0.5
    yalign 0.5
    size gui.name_text_size
    font gui.name_text_font


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

# control mouse location
# init python:
#     def get_mouse():
#         global mouse_xy
#         mouse_xy = renpy.get_mouse_pos()

# default mouse_xy = (0, 0)

screen quick_menu():

    on "show" action Stop(channel="text")

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:
        imagebutton:
            xalign 1.0
            yalign 1.0
            xoffset -230
            yoffset -170
            idle "gui/quickmenu_btn/btn_auto_idle.png"
            hover "gui/quickmenu_btn/btn_auto_hover.png"
            selected "gui/quickmenu_btn/btn_auto_hover.png"
            action Preference("auto-forward", "toggle")
            tooltip _("自动")

        imagebutton:
            xalign 1.0
            yalign 1.0
            xoffset -130
            yoffset -170
            auto "gui/quickmenu_btn/btn_skip_%s.png"
            action Skip() alternate Skip(fast=True, confirm=True)
            tooltip _("快进")

        imagebutton:
            xalign 1.0
            yalign 1.0
            xoffset -30
            yoffset -170
            auto "gui/quickmenu_btn/btn_log_%s.png"
            action ShowMenu('history')
            tooltip _("历史记录")

        imagebutton:
            xalign 1.0
            yalign 1.0
            xoffset -230
            yoffset -90
            auto "gui/quickmenu_btn/btn_save_%s.png"
            action ShowMenu('save')
            tooltip _("保存进度")

        imagebutton:
            xalign 1.0
            yalign 1.0
            xoffset -130
            yoffset -90
            auto "gui/quickmenu_btn/btn_load_%s.png"
            action ShowMenu('load')
            tooltip _("读取进度")

        imagebutton:
            xalign 1.0
            yalign 1.0
            xoffset -30
            yoffset -90
            auto "gui/quickmenu_btn/btn_config_%s.png"
            action ShowMenu('preferences')
            tooltip _("游戏设置")

        imagebutton:
            xalign 1.0
            yalign 1.0
            xoffset -230
            yoffset -10
            auto "gui/quickmenu_btn/btn_dict_%s.png"
            action ShowMenu('detail_screen')
            tooltip _("线索")

        imagebutton:
            xalign 1.0
            yalign 1.0
            xoffset -130
            yoffset -10
            auto "gui/quickmenu_btn/btn_return_%s.png"
            action MainMenu()
            tooltip _("回到主页")

        imagebutton:
            xalign 1.0
            yalign 1.0
            xoffset -30
            yoffset -10
            auto "gui/quickmenu_btn/btn_hide_%s.png"
            action HideInterface()
            tooltip _("隐藏对话")
        
        $ tooltip = GetTooltip()
        if tooltip:
            # style_prefix "tooltip"
            # timer 0.1 repeat True action Function(get_mouse)
            # $ mx = mouse_xy[0] - 30
            # $ my = mouse_xy[1] + 30
            text tooltip:
                font gui.interface_text_font
                pos(1630, 810)
                size 33
                outlines [(2, "#000005", 0, 0)]

        


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_hbox:
    xalign 0.5
    yalign 1.0 yoffset -8
    spacing 8

style quick_button:
    background None
    padding (15, 6, 15, 0)

style quick_button_text:
    size 21
    selected_color '#f93c3e'
    idle_color "#aaa"

## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):
    if nvl_mode == "phone":
        use PhoneDialogue(dialogue, items)
    else:
        window:
            style "nvl_window"

            has vbox
            spacing 15

            use nvl_dialogue(dialogue)

            ## Displays the menu, if given. The menu may be displayed incorrectly if
            ## config.narrator_menu is set to True.
            for i in items:

                textbutton i.caption:
                    action i.action
                    style "nvl_button"

        add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit True

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = 6

# The style for the NVL "textbox"
style nvl_window:
    is default
    xfill True yfill True
    background "gui/nvl.png"
    padding (0, 15, 0, 30)

# The style for the text of the speaker's name
style nvl_label:
    is say_label
    xpos 645 xanchor 1.0
    ypos 0 yanchor 0.0
    xsize 225
    min_width 225
    textalign 1.0

# The style for dialogue in NVL
style nvl_dialogue:
    is say_dialogue
    xpos 675
    ypos 12
    xsize 885
    min_width 885

# The style for dialogue said by the narrator in NVL
style nvl_thought:
    is nvl_dialogue

style nvl_button:
    xpos 675
    xanchor 0.0


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window:
    is empty
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    is empty
    xalign 0.5

style bubble_who:
    is default
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    is default
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}
