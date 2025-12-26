# Register a channel for text beeps
init python:
    renpy.music.register_channel("text", mixer="voice")

init python:
    import renpy.exports as renpy_exports
    global say_what

    def click_callback(event, interact=True, **kwargs):
        # TODO: fix continuous play when switching to main screen
        if event == "show_done":
            if not isinstance(say_what, str) or not say_what.strip():
                return
            
            if "name" not in kwargs:
                renpy.sound.play(sound.click, channel = "text", loop = True)
                return
            
            name = kwargs["name"]
            if name == "bys":
                renpy.sound.play(sound.click_2, channel = "text", loop = True)
                return
            if name == "xs":
                renpy.sound.play(sound.click_3, channel = "text", loop = True)
                return


        elif event == "slow_done":
            renpy.sound.stop(channel = "text")
        elif event == "end":
            renpy.sound.stop(channel = "text", fadeout = 0.1)

init python:
    def combined_callback(event, interact=True, **kwargs):
        if name_callback:
            name_callback(event, interact=interact, **kwargs)

        click_callback(event, interact=interact, **kwargs)

# Define a narrator character for all default characters
define narrator = Character(None, callback=click_callback)

define me = Character("我",what_prefix="“",what_suffix="”", callback=click_callback)

define by = Character("白一", image="bysimg",what_prefix="“",what_suffix="”",callback=combined_callback,cb_name="bys")
define cx = Character("岑宣",what_prefix="“",what_suffix="”",image='cximg',callback=combined_callback,cb_name="cx")
define fj = Character("繁锦",what_prefix="“",what_suffix="”",image='fjimg',callback=combined_callback,cb_name="fj")
define lmm = Character("梁绵绵",what_prefix="“",what_suffix="”",image='lmmimg',callback=combined_callback,cb_name="lmm")
define lwl = Character("林望龙",what_prefix="“",what_suffix="”",image='lwlimg',callback=combined_callback,cb_name="lwl")
define sw = Character("姒舞",what_prefix="“",what_suffix="”",image='swimg',callback=combined_callback,cb_name="sw")
define ty = Character("云天玉",what_prefix="“",what_suffix="”",image='tyimg',callback=combined_callback,cb_name="ty")
define wf = Character("卫锋",what_prefix="“",what_suffix="”",image='wfimg',callback=combined_callback,cb_name="wf")
define xl = Character("小蓝",what_prefix="“",what_suffix="”",image='xlimg',callback=combined_callback,cb_name="xl")
define xp = Character("西平",what_prefix="“",what_suffix="”",image='xpimg',callback=combined_callback,cb_name="xp")
define xs = Character("西顺",what_prefix="“",what_suffix="”",image='xsimg',callback=combined_callback,cb_name="xs")
define zb = Character("张班",what_prefix="“",what_suffix="”",image='zbimg',callback=combined_callback,cb_name="zb")
define unknown = Character("？？",what_prefix="“",what_suffix="”")
define cg = Character("陈桂",what_prefix="“",what_suffix="”",image='cgimg',callback=combined_callback,cb_name="cg")
define lg = Character("林郭",what_prefix="“",what_suffix="”",image='lgimg',callback=combined_callback,cb_name="lg")

define stu = Character("同学",what_prefix="“",what_suffix="”")
define stuA = Character("同学A",what_prefix="“",what_suffix="”")
define stuB = Character("同学B",what_prefix="“",what_suffix="”")
define stuC = Character("同学C",what_prefix="“",what_suffix="”")
define fem = Character("女性",what_prefix="“",what_suffix="”")
define teacher = Character("老师",what_prefix="“",what_suffix="”", callback=click_callback)

define say = Character(None,what_prefix="“",what_suffix="”")
define bys = Character("白一",what_prefix="“",what_suffix="”",image='byimg',callback=name_callback,cb_name="by")

image side bysimg = LayeredImageProxy("bysimg", Transform(zoom=0.49,xoffset=-250,yoffset=1450))


define s_nvl = Character("接收", kind=nvl) # 接收的消息
define r_nvl = Character("发送", kind=nvl) # 发送的消息，主角

define nabox = Image("gui/textbox_2.png",xpos=-310,ypos=20)
define na = Character(None,what_font="fonts/香萃潮汐宋W15.ttf",what_color="#000000",window_background=nabox)
define nasay = Character(None,what_prefix="“",what_suffix="”",what_font="fonts/香萃潮汐宋W15.ttf",what_color="#000000",window_background=nabox)

init:
    # 白一
    layeredimage byimg:
        at sprite_highlight('by')
        group body:
            attribute uniform default:
                "images/char/by/uniform.webp"

        group eyes:
            attribute eye_def default:
                "images/char/by/eye-def.webp"
            attribute eye_close:
                "images/char/by/eye-close.webp"
            attribute eye_wacky:
                "images/char/by/eye-wacky.webp"
            attribute eye_still:
                "images/char/by/eye-still.webp"
            attribute eye_shock:
                "images/char/by/eye-shock.webp"
            attribute eye_move:
                "images/char/by/eye-move.webp"
            attribute eye_squint:
                "images/char/by/eye-squint.webp"

        group mouse:
            attribute def default:
                "images/char/by/m-def.webp"
            attribute smile:
                "images/char/by/m-smile.webp"
            attribute e:
                "images/char/by/m-e.webp"
            attribute o:
                "images/char/by/m-o.webp"
    
    # for side image
    layeredimage bysimg:
        at sprite_highlight('bys')
        group body:
            attribute uniform default:
                "images/char/by/uniform.webp"

        group eyes:
            attribute eye_def default:
                "images/char/by/eye-def.webp"
            attribute eye_close:
                "images/char/by/eye-close.webp"
            attribute eye_wacky:
                "images/char/by/eye-wacky.webp"
            attribute eye_still:
                "images/char/by/eye-still.webp"
            attribute eye_shock:
                "images/char/by/eye-shock.webp"
            attribute eye_move:
                "images/char/by/eye-move.webp"
            attribute eye_squint:
                "images/char/by/eye-squint.webp"

        group mouse:
            attribute def default:
                "images/char/by/m-def.webp"
            attribute smile:
                "images/char/by/m-smile.webp"
            attribute e:
                "images/char/by/m-e.webp"
            attribute o:
                "images/char/by/m-o.webp"

    # 岑宣
    layeredimage cximg:
        at sprite_highlight('cx')
        group body:
            attribute uniform default:
                "images/char/cx/uniform.webp"
            attribute coat:
                "images/char/cx/coat.webp"

        group eyes:
            attribute eye_def default:
                "images/char/cx/eye-def.webp"
            attribute eye_close:
                "images/char/cx/eye-close.webp"
            attribute eye_angry:
                "images/char/cx/eye-angry.webp"
            attribute eye_sad:
                "images/char/cx/eye-sad.webp"
            attribute eye_shock:
                "images/char/cx/eye-shock.webp"

        group mouse:
            attribute def default:
                "images/char/cx/m-def.webp"
            attribute smile:
                "images/char/cx/m-smile.webp"
            attribute o:
                "images/char/cx/m-o.webp"

    # 繁锦
    layeredimage fjimg:
        at sprite_highlight('fj')
        group body:
            attribute coat default:
                "images/char/fj/coat.webp"
            # attribute shirt:
            #     "images/char/mei/shirt.png"

        group eyes:
            attribute eye_def default:
                "images/char/fj/eye-def.webp"
            attribute eye_close:
                "images/char/fj/eye-close.webp"
            attribute eye_squint:
                "images/char/fj/eye-squint.webp"
            attribute eye_sad:
                "images/char/fj/eye-sad.webp"
            attribute eye_shock:
                "images/char/fj/eye-shock.webp"

        group mouse:
            attribute def default:
                "images/char/fj/m-def.webp"
            attribute smile:
                "images/char/fj/m-smile.webp"
            attribute o:
                "images/char/fj/m-o.webp"
            attribute laugh:
                "images/char/fj/m-laugh.webp"


    # 梁绵绵
    layeredimage lmmimg:
        at sprite_highlight('lmm')
        group body:
            attribute uniform default:
                "images/char/lmm/shirt.webp"

        group eyes:
            attribute eye_def default:
                "images/char/lmm/eye-def.webp"
            attribute eye_squint:
                "images/char/lmm/eye-squint.webp"
            attribute eye_sad:
                "images/char/lmm/eye-sad.webp"
            attribute eye_close:
                "images/char/lmm/eye-close.webp"

        group mouse:
            attribute def default:
                "images/char/lmm/m-def.webp"
            attribute smile:
                "images/char/lmm/m-smile.webp"
            attribute o:
                "images/char/lmm/m-o.webp"
            attribute laugh:
                "images/char/lmm/m-laugh.webp"

    # 林望龙
    layeredimage lwlimg:
        at sprite_highlight('lwl')
        group body:
            attribute uniform default:
                "images/char/lwl/uniform.webp"

        group eyes:
            attribute eye_def default:
                "images/char/lwl/eye-def.webp"
            attribute eye_squint:
                "images/char/lwl/eye-squint.webp"
            attribute eye_shock:
                "images/char/lwl/eye-shock.webp"

        group mouse:
            attribute def default:
                "images/char/lwl/m-def.webp"
            attribute smile:
                "images/char/lwl/m-smile.webp"
            attribute o:
                "images/char/lwl/m-o.webp"


    # 姒舞
    layeredimage swimg:
        at sprite_highlight('sw')
        group body:
            attribute uniform default:
                "images/char/sw/uniform.webp"
            attribute coat:
                "images/char/sw/coat.webp"

        group eyes:
            attribute eye_def default:
                "images/char/sw/eye-def.webp"
            attribute eye_blink:
                "images/char/sw/eye-blink.webp"
            attribute eye_squint:
                "images/char/sw/eye-squint.webp"
            attribute eye_sad:
                "images/char/sw/eye-sad.webp"

        group mouse:
            attribute def default:
                "images/char/sw/m-def.webp"
            attribute smile:
                "images/char/sw/m-smile.webp"
            attribute o:
                "images/char/sw/m-o.webp"
            attribute laugh:
                "images/char/sw/m-laugh.webp"


    # 天玉
    layeredimage tyimg:
        at sprite_highlight('ty')
        group body:
            attribute uniform default:
                "images/char/ty/uniform.webp"
            attribute coat:
                "images/char/ty/coat.png"

        group eyes:
            attribute eye_def default:
                "images/char/ty/eye-def.webp"
            attribute eye_close:
                "images/char/ty/eye-close.webp"
            attribute eye_squint:
                "images/char/ty/eye-squint.webp"
            attribute eye_sad:
                "images/char/ty/eye-sad.webp"
            attribute eye_still:
                "images/char/ty/eye-still.webp"

        group mouse:
            attribute def default:
                "images/char/ty/m-def.webp"
            attribute smile:
                "images/char/ty/m-smile.webp"
            attribute o:
                "images/char/ty/m-o.webp"
            attribute laugh:
                "images/char/ty/m-laugh.webp"


    # 卫锋
    layeredimage wfimg:
        at sprite_highlight('wf')
        group body:
            attribute uniform default:
                "images/char/wf/uniform.webp"
            attribute coat:
                "images/char/wf/coat.webp"

        group eyes:
            attribute eye_def default:
                "images/char/wf/eye-def.webp"
            attribute eye_close:
                "images/char/wf/eye-close.webp"
            attribute eye_still:
                "images/char/wf/eye-still.webp"
            attribute eye_sad:
                "images/char/wf/eye-sad.webp"
            attribute eye_shock:
                "images/char/wf/eye-shock.webp"
            attribute eye_squint:
                "images/char/wf/eye-squint.webp"

        group mouse:
            attribute def default:
                "images/char/wf/m-def.webp"
            attribute smile:
                "images/char/wf/m-smile.webp"
            attribute o:
                "images/char/wf/m-o.webp"
            attribute purse:
                "images/char/wf/m-purse.webp"


    # 小蓝
    layeredimage xlimg:
        at sprite_highlight('xl')
        group body:
            attribute uniform default:
                "images/char/xl/uniform.webp"

        group eyes:
            attribute eye_def default:
                "images/char/xl/eye-def.webp"

        group mouse:
            attribute def default:
                "images/char/xl/m-def.webp"
            attribute o:
                "images/char/xl/m-o.webp"


    # 西平
    layeredimage xpimg:
        at sprite_highlight('xp')
        group body:
            attribute uniform default:
                "images/char/xp/uniform.webp"

        group eyes:
            attribute eye_def default:
                "images/char/xp/eye-def.webp"
            attribute eye_still:
                "images/char/xp/eye-still.webp"
            attribute eye_close:
                "images/char/xp/eye-close.webp"

        group mouse:
            attribute def default:
                "images/char/xp/m-def.webp"
            attribute o:
                "images/char/xp/m-o.webp"


    # 西顺
    layeredimage xsimg:
        at sprite_highlight('xs')
        group body:
            attribute uniform default:
                "images/char/xs/uniform.webp"

        group eyes:
            attribute eye_def default:
                "images/char/xs/eye-def.webp"
            attribute eye_close:
                "images/char/xs/eye-close.webp"
            attribute eye_move:
                "images/char/xs/eye-move.webp"
            attribute eye_squint:
                "images/char/xs/eye-squint.webp"
            attribute eye_shock:
                "images/char/xs/eye-shock.webp"
            attribute eye_still:
                "images/char/xs/eye-still.webp"

        group mouse:
            attribute def default:
                "images/char/xs/m-def.webp"
            attribute smile:
                "images/char/xs/m-smile.webp"
            attribute o:
                "images/char/xs/m-o.webp"
            attribute laugh:
                "images/char/xs/m-laugh.webp"


    # 张班
    layeredimage zbimg:
        at sprite_highlight('zb')
        group body:
            attribute uniform default:
                "images/char/zb/coat.webp"

        group eyes:
            attribute eye_def default:
                "images/char/zb/eye-def.webp"

        group mouse:
            attribute def default:
                "images/char/zb/m-def.webp"
            attribute o:
                "images/char/zb/m-o.webp"
            attribute e:
                "images/char/zb/m-e.webp"


# other images

    layeredimage cgimg:
        at sprite_highlight('cg')
        group body:
            attribute uniform default:
                "images/char/0other/cg-def.webp"

        group mouse:
            attribute o:
                "images/char/0other/cg-o.webp"
            attribute laugh:
                "images/char/0other/cg-laugh.webp"
            attribute e:
                "images/char/0other/cg-e.webp"
            attribute oo:
                "images/char/0other/cg-oo.webp"

    layeredimage lgimg:
        at sprite_highlight('lg')
        group body:
            attribute uniform default:
                "images/char/0other/lg-def.webp"

        group mouse:
            attribute o:
                "images/char/0other/lg-o.webp"
            attribute laugh:
                "images/char/0other/lg-laugh.webp"
            attribute oo:
                "images/char/0other/lg-oo.webp"
