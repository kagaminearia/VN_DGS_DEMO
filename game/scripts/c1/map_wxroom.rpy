label wxroom:
    window hide
    $ quick_menu = False
    show screen wxroom_screen
    pause
    jump wxroom
    return


define loc_wxroom = [
    {
        "name": "客厅-餐桌",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "wxroom_table",
        "xpos": 1231,
        "ypos": 696
    },
    {
        "name": "客厅-床铺",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "wxroom_bed",
        "xpos": 1820,
        "ypos": 602
    },
    {
        "name": "灶台-燃气灶",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "wxroom_stove",
        "xpos": 32,
        "ypos": 715
    },
    {
        "name": "灶台-垃圾桶",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "wxroom_garbage",
        "xpos": 286,
        "ypos": 836
    },
    {
        "name": "洗手间-窗户",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "wxroom_window",
        "xpos": 657,
        "ypos": 500
    },
    {
        "name": "储物柜-药盒",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "wxroom_medicine",
        "xpos": 1368,
        "ypos": 566
    },
    {
        "name": "门口-备忘录",
        "idle_image": "images/map/star_idle.png",
        "hover_image": "images/map/star_hover.png",
        "label": "wxroom_note",
        "xpos": 336,
        "ypos": 289
    },
    {
        "name": "白一",
        "idle_image": "images/map/qby_idle.webp",
        "hover_image": "images/map/qby_hover.webp",
        "label": "wxroom_by",
        "xpos": 1275,
        "ypos": 20
    },
]


screen wxroom_screen:
    modal True
    add "images/map/wxroom.webp"

    # buttons for each location
    for location in loc_wxroom:
        imagebutton:
            idle location["idle_image"]
            hover location["hover_image"]
            xpos location["xpos"]
            ypos location["ypos"]
            action [Hide("wxroom_screen"), Jump(location["label"])]


label wxroom_table:
    $ quick_menu = True
    $ persistent.clue[1] = 1
    show screen clue_display(1) with dissolve
    "抽屉里有一双木质筷子，一双一次性筷子，上面刻有“湘味”的字迹。"
    hide screen clue_display with dissolve
    by eye_def o "一双？\n……好怪。"
    me "怎么了？"
    by eye_def o "谁会买一次性筷子只买一双啊。这能方便到哪。"
    me "嗯……或许不是买的吧？"
    by eye_still o "啥？"
    me "你看顶端那里，有刻字，叫“湘味”的。"
    by eye_def o "没想到你还有点用嘛。啊，竟然是这家店。"
    by eye_def e "哦……那我知道了。"
    me "什么？"
    by eye_def o "就是说……这是一家我吃不起的餐厅，连一次性筷子都要定制。"
    by eye_def e "不是买的，估计是从店里顺来的吧。"
    me "……就一双而已啊？"
    by eye_still o "怎么，看不起啊，一双也是可以用的啊。"
    me "我只是觉得没必要……"
    by eye_def o "反正不要钱，能拿一个是一个呗。"
    by eye_def e "如果是我估计也会拿着收起来。"
    me "是，是这样吗……"
    by eye_move e "我们穷人是这样子哒。"
    me "……怎么还“哒”起来了。"
    "不过，好沉重的话题……"
    jump wxroom
    return

label wxroom_bed:
    $ quick_menu = True
    $ persistent.clue[2] = 1
    show screen clue_display(2) with dissolve
    "床上的被子已经被掀开，堆在一边。床单很旧，有不少补丁，但很干净。枕头上有两个人躺过的痕迹。枕头下有一个小盒子。"
    hide screen clue_display with dissolve
    by eye_wacky e "我之前就跟她躺在这吗……"
    me "看起来是的。"
    by eye_wacky e "难以置信……我竟然会跟不熟的人睡一起……要死啊，到底发生了什么……"
    me "噗嗤……谁知道呢。"
    by eye_wacky def "啧……你别忘了你现在用的是我的身体。"
    "白一轻嗤一声，意有所指，撩起左手的衣袖，佯装要在小臂上用力。"
    me "……"
    "我不想再继续说话了，总觉得她真的能做出这种伤敌八百自损一千的事情。"
    "不过……"
    me "枕头底下好像有东西。"
    by eye_def o "啥啊？我不能碰吧。嗯……我看看。"
    "白一凑近，蹲下身，眯起眼睛。"
    by eye_def o "哦，好像是骨灰盒。"
    me "……啥？？？"
    by eye_def e "好像是的吧，你这是什么反应，又不是你的。"
    me "不，等等……是这个问题吗？"
    by eye_still o "啊，不然呢。"
    me "我是说……你之前就睡在骨灰盒上……？"
    by eye_def e "哦……"
    by eye_move o "还好吧，我都跟别人睡同一张床了，这也无所谓吧。"
    me "喂……"
    "和陌生人同睡一张床比睡在骨灰盒上更严重吗……"

    jump wxroom
    return

label wxroom_stove:
    $ quick_menu = True
    $ persistent.clue[3] = 1
    show screen clue_display(3) with dissolve
    "有长时间开过火的痕迹，燃气灶老旧，燃气喷嘴处有异物堵塞。"
    hide screen clue_display with dissolve
    me "这个灶台，之前好像开了很久……旁边都烧到变形了。"
    me "而且，喷嘴好像有点塞住了，这样会燃烧不完全，产生一氧化碳的吧。"
    by eye_def o "啊？这样的话，这应该是，嗯……她死亡的直接原因。"
    by eye_def o "不过，怎么会堵塞的？"
    me "看起来像太久没用，积了很多灰，没清理过，团结成块了。"
    by eye_def def "真奇怪……"
    jump wxroom
    return

label wxroom_garbage:
    $ quick_menu = True
    $ persistent.clue[4] = 1
    show screen clue_display(4) with dissolve
    "垃圾桶空空如也，没有袋子。"
    hide screen clue_display
    by eye_def o "收拾得好干净啊。"
    me "嗯。"
    by eye_def o "那这里好像没什么好看的。"
    me "对。"
    by eye_still e "……你还能再敷衍一点吗？"
    jump wxroom
    return

label wxroom_window:
    $ quick_menu = True
    $ persistent.clue[5] = 1
    show screen clue_display(5) with dissolve
    "被百叶窗盖住的窗户关闭，被人上了锁。"
    hide screen clue_display with dissolve
    me "嗯？百叶窗后面好像是锁死的。"
    by eye_def e "哦……你能看到，那我就不去碰了。"
    by eye_def o "难怪感觉这里好闷，完全不透气啊。"
    me "那快点出去吧。"
    jump wxroom
    return

label wxroom_medicine:
    $ quick_menu = True
    $ persistent.clue[6] = 1
    show screen clue_display(6) with dissolve
    "透明药盒里有两瓶一样的感冒药，其中一瓶打开过，另一瓶还未拆封。"
    hide screen clue_display with dissolve
    by eye_def o "啊，这个我知道，味道超级苦的感冒药。"
    me "是吗？她好像也吃了，这一瓶是打开过的。"
    by eye_def o "哇，了不起。都怪这鬼天气，实在是太冷了。"
    jump wxroom
    return

label wxroom_note:
    $ quick_menu = True
    $ persistent.clue[7] = 1
    show screen clue_display(7) with dissolve
    "温心的日程表，贴在门边的墙上。纸上的字迹用力，不好看，却很整齐。便签纸有些陈旧，边缘发黄，看起来已经用了很久。"
    hide screen clue_display with dissolve
    by eye_def o "我去，好吓人的日程表。"
    me "你不是吗？同个学校的学生应该都差不多吧。"
    by eye_def o "我可没这么认真学习，受不了。"
    me "……"
    jump wxroom
    return

label wxroom_by:
    $ quick_menu = True
    if persistent.clue[1] and persistent.clue[2] and persistent.clue[3] and persistent.clue[4] and persistent.clue[5] and persistent.clue[6] and persistent.clue[7]:
        scene bg_wxroom with fade
        $ quick_menu = True
        by eye_def o "好像看完了，你觉得是什么情况？"
        me "嗯……"
        jump c1_1_extra
    else:
        by eye_still e "怎么了，继续看啊？"
        me "啊，没，就是觉得你看得还挺认真……"
        by eye_wacky o "呵呵，我都要变成杀人凶手了，能不认真吗？"
        me "……"
        jump wxroom
    return