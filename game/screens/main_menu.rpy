
## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    ## This ensures that any other menu screen is replaced.
    tag menu
    on "show" action Stop(channel="text")
    add "images/main/main.webp"
    # add "images/main/main-title.webp"
    add ConditionSwitch(
        "_preferences.language == 'english'", "images/en/main/main-title.webp",
        "_preferences.language == 'None'", "images/main/main-title.webp",
        "True", "images/main/main-title.webp"  # fallback
    )
    hbox:
        yalign 0.85
        vbox:
            style_prefix "main_navigation"
            xpos 175
            yalign 0.85
            spacing 10
            
            textbutton _("开始游戏") action Start()
            textbutton _("读取进度") action ShowMenu("load")
            textbutton _("游戏设置") action ShowMenu("preferences")
            textbutton _("关于游戏") action ShowMenu("about")

            if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
                # Help isn't necessary or relevant to mobile devices.
                textbutton _("游戏帮助"):
                    action ShowMenu("help")
            if renpy.variant("pc"):
                # The quit button is banned on iOS and unnecessary on Android and Web.
                textbutton _("退出游戏") action Quit(confirm=not main_menu)
            


style main_navigation_button_text:
    color gui.white
    hover_color gui.white
    size 50
    hover_underline True
    selected_underline True
    selected_hover_underline True

init python:
    def clear_all_persistent():
        for k in list(vars(persistent).keys()):
            if not k.startswith("_"):
                delattr(persistent, k)

        renpy.save_persistent()