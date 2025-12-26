## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save
## https://www.renpy.org/doc/html/screen_special.html#load


## The width and height of thumbnails used by the save slots.
define config.thumbnail_width = 384
define config.thumbnail_height = 216


screen save():
    tag menu
    add "gui/menu_bg.webp"
    use file_slots(_("保存进度"))


screen load():
    tag menu
    add "gui/menu_bg.webp"
    use file_slots(_("读取进度"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(
        pattern=_(""), auto=_("Automatic saves"),
        quick=_("Quick saves"))

    use game_menu(title)

    fixed:
        xsize 1300 xalign 0.5
        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True

        ## The page name, which can be edited by clicking on it.
        ## This can be pretty easily removed if you want.
        ## Don't forget to also remove the `default` at the top if so.
        button:
            style "page_label"
            key_events True
            action page_name_value.Toggle()

            input:
                style "page_label_text"
                value page_name_value

        ## The grid of file slots.
        grid 3 2:
            spacing 40
            style_prefix "slot"

            for i in range(3*2):
                $ slot = i + 1

                button:
                    action FileAction(slot)
                    has vbox
                    add FileScreenshot(slot) xalign 0.5

                    ## https://www.fabriziomusacchio.com/blog/2021-08-15-strftime_Cheat_Sheet/
                    text FileTime(slot,
                            format=_("{#file_time}%A, %B %d %Y, %H:%M"),
                            empty=_("暂未存档")):
                        style "slot_time_text"

                    text FileSaveName(slot) style "slot_name_text"

                    # This means the player can hover this save
                    # slot and hit delete to delete it
                    key "save_delete" action FileDelete(slot)

        ## Buttons to access other pages.
        hbox:
            xalign 0.5 yalign 1.0 yoffset -150
            style_prefix "page"
            textbutton _("<") action FilePagePrevious()

            if config.has_autosave:
                textbutton _("{#auto_page}A") action FilePage("auto")
            if config.has_quicksave:
                textbutton _("{#quick_page}Q") action FilePage("quick")

            ## range(1, 10) gives the numbers from 1 to 9.
            for page in range(1, 10):
                textbutton "[page]" action FilePage(page)
            textbutton _(">") action FilePageNext()

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    font gui.detail_font
    textalign 0.5
    layout "subtitle"
    idle_color gui.white
    hover_color gui.white
    hover_underline True
    selected_underline True
    selected_hover_underline True

style slot_grid:
    xalign 0.5
    yalign 0.5
    spacing 15

style slot_time_text:
    font gui.detail_font
    size 20
    xalign 0.5
    hover_underline True

style slot_vbox:
    spacing 12

style slot_button:
    xysize (414, 309)
    padding (15, 15, 15, 15)
    background "gui/button/slot_[prefix_]background.png"

style slot_button_text:
    size 21
    xalign 0.5
    idle_color gui.white
    hover_color gui.white
    selected_idle_color gui.white
    hover_underline True
    selected_underline True
    selected_hover_underline True

style page_hbox:
    xalign 0.5
    spacing 5

style page_vbox:
    xalign 0.5
    yalign 1.0
    spacing 5

style page_button:
    hover_color gui.gold
    selected_color gui.gold
    padding (15, 6, 15, 6)
    xalign 0.5
    

style page_button_text:
    font gui.detailtitle_font
    hover_color gui.white
    hover_underline True
    selected_underline True
    selected_hover_underline True