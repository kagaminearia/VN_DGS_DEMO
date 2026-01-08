screen detail_screen:
    on "show" action Stop(channel="text")
    default category = "clue"
    add "#0000001a"
    add "gui/ev/ev-bg.png":
        xalign 0.5
        yalign 0.5

    button:
        background "gui/ev/category-btn.png"
        hover_background "gui/ev/category-btn-hover.png"
        selected_background "gui/ev/category-btn-hover.png"
        xysize(150,90)
        pos(490,86)
        text _("词典"):
            align (0.5,0.5)
            color gui.black
            font gui.interface_text_font
            size 35
        action SetScreenVariable("category","dict")

    button:
        background "gui/ev/category-btn.png"
        hover_background "gui/ev/category-btn-hover.png"
        selected_background "gui/ev/category-btn-hover.png"
        xysize(150,90)
        pos(490,204)
        text _("线索"):
            align (0.5,0.5)
            color gui.black
            font gui.interface_text_font
            size 35
        action SetScreenVariable("category","clue")

    button:
        background "gui/ev/category-btn.png"
        hover_background "gui/ev/category-btn-hover.png"
        selected_background "gui/ev/category-btn-hover.png"
        text _("人物"):
            align (0.5,0.5)
            color gui.black
            font gui.interface_text_font
            size 35
        xysize(150,90)
        pos(490,322)
        action SetScreenVariable("category","char")


    imagebutton:
        idle "gui/ev/close-btn.png"
        hover "gui/ev/close-btn-hover.png"
        pos(505,884)
        action Return()


    if category == "clue":
        frame:
            add "#fff"
            style_prefix "detail"
            align (0.5,0.5)
            xysize (520,920)
            vpgrid:
                cols 2
                spacing 30
                draggable True
                mousewheel True

                scrollbars "vertical"

                # Since we have scrollbars, we have to position the side, rather
                # than the vpgrid proper.
                side_xalign 0.8

                for i in range(len(clueList)):
                    if persistent.clue[i] == 1:
                        button:
                            add "clue[i]":
                                size(170,170)
                                align (0.5,0.0)
                                yoffset 20
                            background "gui/ev/ev-btn-idle.png"
                            hover_background "gui/ev/ev-btn-hover.png"
                            text "[clueList[i][0]]":
                                yoffset -20
                                align (0.5,1.0)
                                color gui.black
                                font gui.detailtitle_font
                                size 20
                            xysize(215,250)
                            action [ShowMenu("clue_screen",i)]
                    else:
                        button:
                            add "evlocked":
                                align (0.5,0.0)
                                yoffset 20
                            background "gui/ev/ev-btn-idle.png"
                            hover_background "gui/ev/ev-btn-hover.png"
                            text "暂未解锁":
                                yoffset -20
                                align (0.5,1.0)
                                color gui.black
                                font gui.detailtitle_font
                                size 20
                            xysize(215,250)
                            action Return()
    

    elif category == "dict":
        frame:
            add "#fff"
            style_prefix "detail"
            align (0.5,0.5)
            xysize (520,920)
            if len(persistent.dictList) == 0:
                vbox:
                    text "目录为空":
                        align (0.5,0.5)
                        font gui.detailtitle_font
                        color gui.black
            else:
                viewport:
                    ysize 920
                    xalign 0.5
                    yalign 0.5
                    style_prefix 'detail'
                    mousewheel True draggable True pagekeys True
                    scrollbars "vertical"
                    yinitial 1.0

                    has vbox
                    spacing 30
                    for i in range(len(persistent.dictList)):
                        vbox:
                            text "[persistent.dictList[i][0]]":
                                font gui.detailtitle_font
                                color gui.black
                            text "[persistent.dictList[i][1]]":
                                font gui.detail_font
                                color gui.black
                                size 23
                
    else:
        frame:
            add "#fff"
            style_prefix "detail"
            align (0.5,0.5)
            xysize (520,920)
            vpgrid:
                cols 2
                spacing 30
                draggable True
                mousewheel True

                scrollbars "vertical"

                # Since we have scrollbars, we have to position the side, rather
                # than the vpgrid proper.
                side_xalign 0.8

                for i in range(len(charList)):
                    button:
                        add "images/char_dict/head[i].png":
                            size(170,170)
                            align (0.5,0.0)
                            yoffset 20
                        background "gui/ev/ev-btn-idle.png"
                        hover_background "gui/ev/ev-btn-hover.png"
                        text "[charList[i]]":
                            yoffset -20
                            align (0.5,1.0)
                            color gui.black
                            font gui.detailtitle_font
                            size 20
                        xysize(215,250)
                        action [ShowMenu("char_screen",i)]

style char_info_text:
    font gui.detail_font
    color gui.black
    size 22

screen char_screen(index):
    on "show" action Stop(channel="text")
    modal True
    add "#0000003d"
    add "gui/ev/clue-bg.webp":
        pos(637,72)

    frame:
        add "#ffffff"
        align (0.5,0.35)
        xysize (550,700)
        vbox:
            spacing 30
            hbox:
                spacing 10
                add "images/char_dict/side[index].webp"
                vbox:
                    spacing 60
                    text "[charList[index]]":
                        color gui.black
                        font gui.detailtitle_font
                        size 55
                    vbox:
                        text "[charBasic[index][0]]":
                            color gui.black
                            font gui.detail_font
                            size 22
                        text "[charBasic[index][1]]":
                            color gui.black
                            font gui.detail_font
                            size 22
                    if persistent.charhex[index] == 0:
                        add "images/char_dict/hexd.png":
                            size(275,275)
                    else:
                        add "images/char_dict/hex[index].webp":
                            size(275,275)
            vbox:
                style_prefix "char_info"
                spacing 3
                if persistent.charinfo1[index] == 0:
                    text "■" * len(charInfoContent[index][0])
                else:
                    text "[charInfoContent[index][0]]"
                if persistent.charinfo2[index] == 0:
                    text "■" * len(charInfoContent[index][1])
                else:
                    text "[charInfoContent[index][1]]"
                if persistent.charinfo3[index] == 0:
                    text "■" * len(charInfoContent[index][2])
                else:
                    text "[charInfoContent[index][2]]"

    imagebutton:
        idle "gui/ev/close-btn.png"
        hover "gui/ev/close-btn-hover.png"
        pos(905,897)
        action [Hide("char_screen")]


screen clue_screen(index):
    on "show" action Stop(channel="text")
    modal True
    add "#0000003d"
    add "gui/ev/clue-bg.webp":
        pos(637,72)

    frame:
        add "#ffffff"
        align (0.5,0.35)
        xoffset -5
        xysize (500,700)
        vbox:
            spacing 25
            add "clue[index]":
                size(500,500)
            vbox:
                spacing 6
                text [clueList[index][0]]:
                    font gui.detailtitle_font
                    size 30
                    color gui.black
                text [clueList[index][1]]:
                    font gui.detail_font
                    size 20
                    color gui.black
    imagebutton:
        idle "gui/ev/close-btn.png"
        hover "gui/ev/close-btn-hover.png"
        pos(905,897)
        action [Hide("clue_screen")]


style detail_vscrollbar:
    xsize 25
    base_bar Frame("gui/scrollbar/ev-vsc-bar.png", 6, 6, 6, 6, tile=False)
    thumb Frame("gui/scrollbar/ev-vsc-thumb.png", 6, 6, 6, 6, tile=False)
    unscrollable 'hide'
    xoffset 150


label clue_choice_label:
    window hide
    $ quick_menu = False
    show screen clue_choice
    pause
    jump clue_choice_label
    return

screen clue_choice(correctchoice,wronglabel,correctlabel,question=""):
    add "#0000003d"
    add "gui/ev/ev-bg.png":
        xalign 0.5
        yalign 0.5
        
    text "[question]":
        vertical True
        xalign 0.5
        yalign 0.5
        xoffset -400
        size 40
        color gui.black
        font gui.detailtitle_font
        outlines[(6,"#ffffff")]

    frame:
        add "#fff"
        style_prefix "detail"
        align (0.5,0.5)
        xysize (520,920)
        vpgrid:
            cols 2
            spacing 30
            draggable True
            mousewheel True

            scrollbars "vertical"
            side_xalign 0.8

            # change for correct choices
            for i in range(len(clueList)):
                if persistent.clue[i] == 1:
                    button:
                        add "clue[i]":
                            size(170,170)
                            align (0.5,0.0)
                            yoffset 20
                        background "gui/ev/ev-btn-idle.png"
                        hover_background "gui/ev/ev-btn-hover.png"
                        text "[clueList[i][0]]":
                            yoffset -20
                            align (0.5,1.0)
                            color gui.black
                            font gui.detailtitle_font
                            size 20
                        xysize(215,250)
                        if i in correctchoice:
                            action [Hide("clue_choice"),Jump(correctlabel)]
                        else:
                            action [Hide("clue_choice"), Jump(wronglabel)]



