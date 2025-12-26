################################################################################
## Initialization
################################################################################

## The init offset statement causes the initialization statements in this file
## to run before init statements in any other file.
init offset = -2

## Calling gui.init resets the styles to sensible default values, and sets the
## width and height of the game.
init python:
    gui.init(1920, 1080)

define config.check_conflicting_properties = True

################################################################################
## GUI Configuration Variables
################################################################################
## Some choice gui values have been left in, to make them
## easier to adjust for accessibility purposes e.g. to allow
## players to change the default text font or size by rebuilding the gui.
## You may add more back if you need to adjust them, or find-and-replace
## any instances where they are used directly with their value.


# The text fonts and size for different screens
define gui.text_font = "fonts/站酷仓耳渔阳体-W02.ttf"
define gui.interface_text_font = "fonts/站酷高端黑.ttf"
define gui.text_size = 30
define gui.name_text_font = "fonts/站酷仓耳渔阳体-W03.ttf"
define gui.name_text_size = 43
define gui.detailtitle_font = "fonts/香萃潮汐宋W40.ttf"
define gui.detail_font = "fonts/香萃潮汐宋W15.ttf"

## Localization ################################################################

## This controls where a line break is permitted. The default is suitable
## for most languages. A list of available values can be found at
## https://www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"


################################################################################
## Style Initialization
################################################################################

init offset = -1

################################################################################
## Styles
################################################################################

define gui.gold = "#ad973f"
define gui.white = "#ffffff"
define gui.black = "#000000"

style default:
    font gui.text_font
    size gui.text_size
    language gui.language

style hyperlink_text:
    hover_underline True
    font gui.detail_font
    color "#ffffff"

style gui_text:
    color '#ffffff'
    size gui.text_size
    font gui.interface_text_font

style button:
    xysize (None, None)
    padding (0, 0)

style button_text:
    is gui_text
    yalign 0.5
    xalign 0.0
    ## The color used for a text button when it is neither selected nor hovered.
    idle_color gui.white
    ## The color that is used for buttons and bars that are hovered.
    hover_color gui.gold
    ## The color used for a text button when it is selected but not focused. A
    ## button is selected if it is the current screen or preference value.
    selected_color '#ffffff'
    ## The color used for a text button when it cannot be selected.
    insensitive_color gui.white

style label_text:
    is gui_text
    size 36
    color gui.white


style bar:
    ysize 38
    left_bar Frame("gui/bar/left.png", 6, 6, 6, 6, tile=False)
    right_bar Frame("gui/bar/right.png", 6, 6, 6, 6, tile=False)

style vbar:
    xsize 38
    top_bar Frame("gui/bar/top.png", 6, 6, 6, 6, tile=False)
    bottom_bar Frame("gui/bar/bottom.png", 6, 6, 6, 6, tile=False)

style scrollbar:
    ysize 18
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", 6, 6, 6, 6, tile=False)
    unscrollable 'hide'

style vscrollbar:
    xsize 18
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", 6, 6, 6, 6, tile=False)
    unscrollable 'hide'

style slider:
    ysize 38
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize 38
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", 6, 6, 6, 6, tile=False)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding (6, 6, 6, 6)
    background Frame("gui/frame.png", 6, 6, 6, 6, tile=False)
