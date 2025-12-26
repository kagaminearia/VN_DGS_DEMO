# only show once
default persistent.disclaimer = 0

screen disclaimer:
    add "#000000"
    vbox:
        style_prefix "disclaimer"
        xalign 0.5
        yalign 0.5
        spacing 20
        vbox:
            label _("本游戏纯属虚构。")
            text _("——与真实世界的事件，地点，人物没有任何联系。")
        vbox:
            label _("本游戏的游戏类型为悬疑，而非推理。")
            text _("——面对选项时可以随意选择，没有惩罚机制。")
        vbox:
            label _("本游戏含有杀人、自杀、自残等敏感情节。")
            text _("——如有不适，请及时退出。")
        vbox:
            label _("本游戏的部分情节十分戏剧化，为剧情需要。")
            text _("——请勿与现实对比，也请不要进行模仿学习。")
        vbox:
            label _("本游戏对部分职业有负面描述，为剧情需要。")
            text _("——并不代表作者的想法。")
        vbox:
            label _("本游戏的角色可能会发表令人不适的言论。")
            text _("——并不代表作者的想法。")
        vbox:
            label _("本游戏包含部分女同性恋元素。")
            text _("——非游戏主要内容，但确实存在。")
    

style disclaimer_label_text:
    color gui.white
    size 30
    font gui.detailtitle_font

style disclaimer_text:
    color gui.white
    size 23
    font gui.detail_font