screen ending_particle_text(message):

    zorder 100
    modal True

    default particles = []
    default arrived_count = 0
    default finished = False

    # 字符尺寸（决定排版）
    default char_w = 28
    default char_h = 42

    default text_x = (config.screen_width - len(message) * char_w) // 2
    default text_y = config.screen_height // 2 - char_h // 2

    # 初始化：一个字 = 一个粒子
    python:
        if not particles:
            for i, ch in enumerate(message):
                particles.append({
                    "char": ch,
                    "x": renpy.random.randint(0, config.screen_width),
                    "y": renpy.random.randint(0, config.screen_height),
                    "tx": text_x + i * char_w,
                    "ty": text_y,
                    "arrived": False,
                })

    # 粒子移动
    timer 0.016 repeat True action If(
        not finished,
        SetScreenVariable(
            "particles",
            [
                {
                    **p,
                    "x": p["x"] + (p["tx"] - p["x"]) * 0.18,
                    "y": p["y"] + (p["ty"] - p["y"]) * 0.18,
                    "arrived": abs(p["x"] - p["tx"]) < 1 and abs(p["y"] - p["ty"]) < 1
                }
                for p in particles
            ]
        )
    )

    # 判断是否全部到达
    python:
        arrived_count = sum(1 for p in particles if p["arrived"])
        if arrived_count == len(particles):
            finished = True

    # 绘制粒子字符（拼字完成后不再抖）
    for p in particles:
        text p["char"] pos (int(p["x"]), int(p["y"])) style "ending_char"

    # 拼字完成后，淡入一个稳定的最终文本（视觉更干净）
    if finished:
        text message:
            style "ending_final"
            at transform:
                alpha 0.0
                linear 0.6 alpha 1.0

init python:
    style.ending_char = Style(style.default)
    style.ending_char.size = 32
    style.ending_char.color = "#ffffff"
    style.ending_char.outlines = [(2, "#000000", 0, 0)]

    style.ending_final = Style(style.default)
    style.ending_final.size = 42
    style.ending_final.color = "#ffffff"
    style.ending_final.outlines = [(3, "#000000", 0, 0)]
    style.ending_final.xalign = 0.5
    style.ending_final.yalign = 0.5



label particle:
    # show screen ending_particle_text("测试文字")
    # pause
    scene black with dissolve
    pause
    show screen endinginfo("新人生") with Dissolve(1)
    pause
    return
