# save setting
init python:
    config.has_autosave = False
    config.has_quicksave = False
    config.autosave_on_quit = False
    config.autosave_on_choice = False

# keymap control setting
init python:
    config.keymap['dismiss'].append('mousedown_5')
    config.keymap['dismiss'].append('K_DOWN')
    config.keymap['rollback'] = ('K_UP')


# custom mouse icon setting
define config.mouse = { }
define config.mouse['default'] = [ ( "gui/cursor/cc.png", 0, 0) ]
define config.mouse['pressed_default'] = [ ( "gui/cursor/cc-click.png", 0, 0) ]
# define config.mouse['button'] = [ ( "gui/cursor/cc-btn.png", 0, 0) ]

init:
    define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'ontop' ]