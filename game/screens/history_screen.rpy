## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

define config.history_length = 250

screen history():

    tag menu
    add "gui/menu_bg.webp"
    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("历史记录"))

    viewport:
        ysize 800
        xalign 0.5
        yalign 0.5
        style_prefix 'history'
        mousewheel True draggable True pagekeys True
        scrollbars "vertical"
        yinitial 1.0

        has vbox

        style_prefix "history"

        for h in _history_list:

            frame:
                style_prefix "history_inside"
                has vbox
                if h.who:
                    label h.who style 'history_name':
                        substitute False
                        ## Take the color of the who text
                        ## from the Character, if set
                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                        xsize 200   # this number and the null width number should be the same
                else:
                    null width 200

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    font gui.detail_font
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }

style history_vscrollbar:
    unscrollable False
    xsize 25
    ysize 800
    xoffset -150
    base_bar Frame("gui/scrollbar/log-vsc-bar.png", 6, 6, 6, 6, tile=False)
    thumb Frame("gui/scrollbar/log-vsc-thumb.png", 6, 6, 6, 6, tile=False)

style history_frame:
    background None

style history_hbox:
    spacing 40

style history_vbox:
    ysize None
    spacing 20

style history_inside_vbox:
    ysize None
    spacing 1

style history_inside_frame:
    left_padding 310
    right_padding 310
    background None

style history_name:
    xalign 0.0

style history_name_text:
    size 35
    font gui.detailtitle_font
    textalign 0.0
    align (0.0, 0.0)
    color gui.white

style history_text:
    font gui.detail_font
    textalign 0.0
    color gui.white

style history_label:
    xfill True

style history_label_text:
    font gui.detail_font
    xalign 0.5