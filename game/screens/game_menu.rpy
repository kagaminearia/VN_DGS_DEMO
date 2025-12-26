## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the title and navigation.
##
## This screen no longer includes a background, and it no longer transcludes
## its contents. It is intended to be easily removable from any given menu
## screen and thus you are required to do some of the heavy lifting for
## setting up containers for the contents of your menu screens.
##

screen game_menu(title):
    style_prefix "game_menu"

    hbox:
        xalign 0.5
        yalign 1.0
        yoffset -40
        spacing 60

        if _in_replay:
            textbutton _("结束回放") action EndReplay(confirm=True)

        elif not main_menu:
            textbutton _("回到主页") action MainMenu()
            textbutton _("历史记录") action ShowMenu("history")
            textbutton _("保存进度") action ShowMenu("save")

        if main_menu:
            textbutton _("关于游戏") action ShowMenu("about")
        #     textbutton _("Start") action Start()


        textbutton _("读取进度") action ShowMenu("load")
        textbutton _("游戏设置") action ShowMenu("preferences")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            ## Help isn't necessary or relevant to mobile devices.
            textbutton _("游戏帮助") action ShowMenu("help")

        if renpy.variant("pc"):
            ## The quit button is banned on iOS and
            ## unnecessary on Android and Web.
            textbutton _("退出游戏") action Quit(confirm=not main_menu)

    imagebutton:
        idle "gui/button/return_idle.png"
        hover "gui/button/return_hover.png"
        xalign 0.0
        yalign 0.5
        xoffset 70
        action Return()

    ## Remove this line if you don't want to show the screen
    ## title text as a label (for example, if it's baked into
    ## the background image.)
    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

style return_button:
    xpos 60
    yalign 1.0
    yoffset -45

style game_menu_viewport:
    xsize config.screen_width
    ysize config.screen_height
    align (0.5, 0.5)

style game_menu_side:
    yfill True
    align (1.0, 0.5)

style game_menu_vscrollbar:
    unscrollable "hide"

style game_menu_label:
    align(0.5, 0.0)
    yoffset 20
    padding (10, 10)

style game_menu_label_text:
    size 65
    color gui.white

style game_menu_button_text:
    size 45
    color gui.white
    hover_color gui.white
    selected_color gui.white
    hover_underline True
    selected_underline True
    selected_hover_underline True
