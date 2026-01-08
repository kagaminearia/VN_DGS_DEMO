
## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
EasyRenPyGui is made by {a=https://github.com/shawna-p}Feniks{/a} {a=https://feniksdev.com/}@feniksdev.com{/a}
""")


screen about():

    on "show" action Stop(channel="text")

    tag menu
    add "gui/menu_bg.webp"

    use game_menu(_("关于游戏"))

    viewport:
        xsize 1300
        ysize 800
        xalign 0.5
        yalign 0.5
        style_prefix 'about'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"

        has vbox
        style_prefix "about"

        label _("剧本·美术·程序")
        text _("可食用蓝墨水")

        label _("音乐·音效")
        text _("akagi·可食用蓝墨水")

        label _("游戏测试")
        text _("akagi·可食用蓝墨水 ")
        
        label ""

        label _("参考·素材·资源")
        text _("游戏引擎：{a=https://www.renpy.org/}Ren'Py{/a}")
        
        text _("场景图片：{a=https://unsplash.com/}Unsplash{/a}，\
{a=https://www.videvo.net/#rs=videvo-logo}Videvo{/a}，\
{a=https://www.freepik.com/}Freepik{/a}") 

        text _("音乐音效：{a=https://pixabay.com/}Pixabay{/a}，\
{a=https://otologic.jp/}Otologic{/a}，\
{a=https://www.fesliyanstudios.com/}Fesliyan Studios{/a}，\
{a=https://amachamusic.chagasi.com/}Amachamusic{/a}")

        text _("代码设计：{a=https://lemmasoft.renai.us/forums/viewtopic.php?t=37628&sid=acd42f4aadf6680211571a586cbf4a80}image dissolve transitions{/a}，\
{a=https://wattson.itch.io/renpy-wave-shader}Ren'py Wave Shader by Wattson{/a}，\
{a=https://wattson.itch.io/renpy-auto-highlight}Renpy Auto Highlight by Wattson{/a}，\
{a=https://feniksdev.itch.io/easy-renpy-gui}Easy Ren'Py GUI by Feniks{/a}，\
{a=https://nighten.itch.io/yet-another-phone-renpy}Phone System by Nighten{/a}")
        # text _("字体：仓耳渔阳体，站酷高端黑，香萃潮汐宋，清松手写体，BlueSecretText")

style about_vbox:
    ysize None
    spacing 10
    xalign 0.5

style about_label_text:
    size 35
    font gui.detailtitle_font
    textalign 0.0
    color gui.white

style about_text:
    size 25
    font gui.detail_font
    textalign 0.0
    color gui.white

style about_hyperlink_text:
    hover_underline True
    size 25
    font gui.detail_font
    textalign 0.0
    color gui.white

style about_vscrollbar:
    unscrollable False
    xsize 25
    ysize 800
    xoffset 150
    base_bar Frame("gui/scrollbar/log-vsc-bar.png", 6, 6, 6, 6, tile=False)
    thumb Frame("gui/scrollbar/log-vsc-thumb.png", 6, 6, 6, 6, tile=False)


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():
    on "show" action Stop(channel="text")

    tag menu
    add "gui/menu_bg.webp"
    add "gui/help_image.png":
        align(0.5,0.5)
    style_prefix "help"
    use game_menu(_("游戏帮助"))
    text _("剧情前进"):
        pos(407,477)
    text _("剧情前进"):
        pos(832,395)
    text _("剧情前进/确认输入"):
        pos(1347,579)
    text _("剧情前进"):
        pos(1418,681)
    text _("快进"):
        pos(1261,375)
    text _("屏幕截图"):
        pos(1261,477)
    text _("游戏菜单/返回"):
        pos(704,477)
    text _("历史记录"):
        pos(832,328)



style help_text:
    size 25
    font gui.detail_font
    textalign 0.5
    color gui.white


# style help_label:
#     xsize 375
#     right_padding 30

# style help_label_text:
#     xalign 1.0
#     textalign 1.0
