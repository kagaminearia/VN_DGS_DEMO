image black = "#000000" 
image white = "#ffffff"
image halfblack = "#0000004f" 

image ctc-img:
    yalign 0.96 xalign 0.81
    "gui/ctc/ctc-0.png"
    pause 0.2
    "gui/ctc/ctc-1.png"
    pause 0.2
    "gui/ctc/ctc-2.png"
    pause 0.2
    "gui/ctc/ctc-3.png"
    pause 0.2
    "gui/ctc/ctc-4.png"
    pause 0.2
    "gui/ctc/ctc-5.png"
    pause 0.2
    "gui/ctc/ctc-6.png"
    pause 0.2
    "gui/ctc/ctc-7.png"
    pause 0.2
    "gui/ctc/ctc-8.png"
    pause 0.2
    "gui/ctc/ctc-9.png"
    pause 0.2
    "gui/ctc/ctc-10.png"
    pause 0.2
    "gui/ctc/ctc-11.png"
    pause 0.3
    repeat

image rec:
    "images/rec0.webp"
    pause 0.15
    "images/rec1.webp"
    pause 0.15
    "images/rec2.webp"
    pause 0.15
    "images/rec1.webp"
    pause 0.15
    "images/rec0.webp"
    pause 0.15
    repeat


screen tpoinfo(time,loc):
    add "images/tpo.webp"
    style_prefix 'tpo'
    vbox:
        xalign 0.5
        yalign 0.48
        spacing 10
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 5
            text "——"
            text time
            text "——"
        hbox:
            xalign 0.5
            yalign 0.5
            spacing 5
            text "——"
            text loc
            text "——"

style tpo_text:
    font gui.detailtitle_font
    size 55
    color gui.white


screen clue_display(index):
    add "#00000080"
    add "clue[index]":
        size(750,750)
        xalign 0.5
        yalign 0.1



# videos
image black1 = Movie(play="videos/black1.webm")
image black2 = Movie(play="videos/black2.webm")
image black3 = Movie(play="videos/black3.webm")