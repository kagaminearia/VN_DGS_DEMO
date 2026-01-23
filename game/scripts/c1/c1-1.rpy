label c1_1:
    scene bg_meetingroom with Fade(0.3,0.8,0.3,color="#000")
    show xsimg eye_still smile at char_mid
    $ renpy.music.play(music.texting, loop=True, fadein=0.5)
    "西平离开了，房间里只剩白一和西顺面对面。"
    "两人的眼神相交，都试图从对方的表情中看出些什么。"
    "只是……西顺并不温柔，反而比西平的给白一的感觉还要可怕，可怕得多。"
    "白一屏着呼吸，心脏跳得很快，我的心脏也跳得很快。又或者，是我正在清晰感受着她的心跳。"
    me "那个……她是什么意思？难道她知道什么……？"
    "我有些不安地开口，白一则是捏紧了手掌。"
    show tophalfblk with Dissolve(0.3)
    "她被西顺盯得有些看不下去，稍稍移开了视线，落在干净粗糙的桌面上。"
    by eye_wacky e "我，不明白你在——"
    hide xsimg
    show xsimg eye_still laugh behind tophalfblk at char_mid 
    xs "嗯，我确实知道一些东西，你不想问吗？"
    hide tophalfblk with dissolve
    by eye_shock o "什——"
    "听到这指向性极强的话，白一忘了反驳，也忘了视线的逃避。"
    "她猛地抬起头，瞪大眼睛。"
    me "她，她是……"
    hide xsimg
    show xsimg o at char_mid
    xs "嗯，我听得见那个声音，在你身上。"
    xs "并且，刚刚也还在和你说话。是说，‘看见了今天的日期’？是吗？"
    by eye_shock def "……"
    "{b}……她真的听得见！！{/b}"
    "由西顺亲口说出来，下定论，白一愣住，不知道该说什么。"
    "不知道是应该为这脑海里的声音不是幻觉而放心，还是应该为有人窥见这秘密而惊慌。"
    "但，明明是冬天，白一却出了一身的汗。她僵在原地，背部有些微微发麻。"
    by eye_shock def "……"
    by eye_move e "啊，呃……"
    "白一的脑子都乱成了浆糊，手指下意识又抠住左臂的伤口，感受到不断的刺痛后才停下来。"
    hide xsimg
    show xsimg smile at char_mid
    xs "所以，要不要解释一下，你身上到底发生了什么？"
    by eye_def o "……我什么都不知道。真的。"
    "短暂的怔愣后，白一敛去表情，强打起气势，找回跟她说话时的主动权。"
    by eye_still o "是你们让我留在这里，应该给我解释才对吧。"
    hide xsimg
    show xsimg o at char_mid
    xs "是啊，是因为你和一件案子联系上了，所以你才会在这里。"
    xs "所以我们需要了解你的情况。"
    by eye_def o "都说了我真的不知道，醒来之后就躺在那里。"
    by eye_def e "既然你说你能听见，那你直接跟她说不就好了。"
    xs "哦，可以这样么？"
    by eye_still o "废话。"
    hide xsimg
    show xsimg eye_squint smile at char_mid
    "西顺又笑了，她换了个姿势，靠坐在椅子上。"
    "不知道是不是错觉，我似乎能感觉到，她现在不是看着白一，而是我。"
    hide xsimg
    show xsimg smile at char_mid
    xs "这位……同志？怎么称呼？"
    by eye_wacky e "很好，现在这里有两个人疯了。"
    "随着白一的冷笑，我和西顺在这十足奇怪的场景下，开始了完全不科学，也不符合常理的对话。"
    "然而，不管是我还是白一，似乎都没法给出让西顺满意的答案，询问也在几个“不知道”后陷入停滞状态。"
    stop music fadeout 0.5

    scene bg_meetingroom with fade
    show xsimg at char_mid with dissolve
    by eye_def e "对了，我能问个问题吗。"
    xs "嗯？你说。"
    by eye_def o "你知道讲事情的时候最讨厌哪种人吗？"
    xs "……嗯？"
    by eye_def o "就是明明有话要说，却非要遮遮掩掩，故意说话只说一半的人。"
    hide xsimg
    show xsimg o at char_mid
    xs "……如果我没猜错，你是说我吗？"
    by eye_still o"很显然，是的。"
    hide xsimg
    show xsimg eye_close smile at char_mid
    xs "噗嗤。"
    "西顺被逗笑了，而后一边无奈地揉了揉太阳穴，一边开口。"
    hide xsimg
    show xsimg o at char_mid
    xs "我明白你的意思，也没有不想跟你说，之前只是还有别的因素要考虑。"
    by eye_move def "……哦。"
    "西顺并没有生气，意外的好态度让白一都有些愣神，好一会才闷闷地应了一声。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "就像之前说的，特调组表面上是处理一些危险的特大案件，实际上还会处理一些……不那么科学的东西。"
    hide xsimg
    show xsimg o at char_mid
    xs "嗯，我们把这些事统称为“怪异”。"
    python:
        persistent.dictList.append(("怪异","对“无法用现如今的常识解释的，违反对科学的普遍认知超自然的事件”的统称。\n怪异有多种形态，可单独存在，也可以和生物——活着或死去的生物——相互影响。\n怪异各有不同，一千种怪异可能有一千种特征。它们被收录在城安局的信息系统，也总结出了一套处理公式。"))
        persistent.dictList = list(set(persistent.dictList))
    $ renpy.sound.play(sound.dictionary, channel="dictionary", loop=False)
    $ renpy.notify ("【词典】更新")
    by eye_move o "哦哦，说你呢，不科学的东西，都怪你。"
    "知道能被西顺听见后，白一装也不装了，当着她说话的面就开始把怒火放在我身上。"
    me "……喂，我也很无辜。"
    by eye_move e "呵呵。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "刚刚我们在谈话中已经确认了，你现在是清醒的，你身上的怪异特性也没有对你本人的身体产生负面影响。"
    python:
        persistent.dictList.append(("怪异的负面影响","怪异和生物——尤其是人类——接触后，有大概率产生无法控制的负面影响。\n常见的影响作用于精神层面，如频繁的噩梦，幻觉，扰人心智的呓语。\n但也有影响直接作用于身体，如皮肤溃烂、发黑，器官病变。\n影响大多不可逆，也容易留下心理创伤。"))
        persistent.dictList = list(set(persistent.dictList))
    $ renpy.sound.play(sound.dictionary, channel="dictionary", loop=False)
    $ renpy.notify ("【词典】更新")
    hide xsimg
    show xsimg at char_mid
    xs "嗯，至少目前没有。"
    "西顺中肯地点点头。"
    by eye_def o "这你们也能确认出来？"
    hide xsimg
    show xsimg o at char_mid
    xs "是啊。就像我能听到你们说话，总有你不知道的办法。"
    xs "总之，要确认你是安全的，我们才能继续。"
    by eye_wacky def "……哦。"
    "白一翻了个白眼，但情绪没刚才那么激烈了。"
    "也许是知道了西顺之前一直含糊其辞，现在才进入正题的原因……"
    xs "特调组大概就是这些，至于你身上的事情，目前我们了解的也不够多，不过——"
    hide xsimg
    show xsimg at char_mid
    "西顺留下一个恰到好处的停顿，又深深地看了白一一眼。"
    hide xsimg
    show xsimg o at char_mid
    xs "12月11日下午，民案组接到报案，在晟欧路的一栋民房发现了两具尸体。"
    by eye_def o "哦。"
    "跟我有什么关系？\n白一大概率是想这么说。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "其中一具，是你的尸体。"
    by eye_wacky e "…………谁的？"
    $ renpy.music.play(music.horror, loop=True, fadein=0.5)
    "白一忍不住抬手，揉了揉耳朵，以为自己听到的是幻觉。"
    hide xsimg
    show xsimg at char_mid
    xs "嗯，是你的尸体。当时，已经确认了没有生命体征。"
    hide xsimg
    show xsimg o at char_mid
    xs "他们认为是意外死亡，所以送回来之后也没有进行多余的检查，只是等通知家属来认领。"
    xs "只是，民案组的流程还没走完，你半夜突然就醒过来了。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "或者说，重新活过来了。"
    by eye_wacky o "……我去。"
    "白一不禁想到之前突然打开的房门和爆发的尖叫声。"
    me "……这合理吗？"
    by eye_wacky e "我也想知道，这合理吗？？"
    hide xsimg
    show xsimg eye_close at char_mid
    xs "嗯，把我们的值班小姐姐吓得够呛……之后的事你都知道了。"
    hide xsimg
    show xsimg smile at char_mid
    xs "搞得我大半夜的还要加班，被拉过来救场呢。"
    by eye_wacky e "她吓得够呛？我才要被吓死了。哦，刚好，死了也不用搬运，直接躺下完事。"
    hide xsimg
    show xsimg at char_mid
    "冷冷地抱怨完，白一没再开口，只是沉默地保持之前的姿势。"
    "她的呼吸很急促，却被控制得极轻。"
    "如果不是我能够感觉到她的气息，怕是要以为那些所谓“活过来”都是胡话。"
    "……真的不是胡话吗？"
    "我完全理解白一的反应。就算事情摆在眼前，就算解释无比合理，还是很难不去怀疑，甚至觉得眼前的一切才是虚假的幻觉。"
    "西顺盯着白一，看她似乎冷静下来一些才继续说话。"
    hide xsimg
    show xsimg o at char_mid
    stop music
    xs "怎么样，我说的这些前因后果，你现在理清了没？"
    by eye_def e "呃……大概。"
    xs "你的事情还要后续调查，需要你的配合，最好在影响到你的身体之前解决。"
    by eye_still o "还会影响？你不是说没事？"
    hide xsimg
    show xsimg eye_close at char_mid
    xs "我说的是{b}现在{/b}没事。"
    by eye_wacky def "哈？不就是我死了又活了，反正现在是正常的，就当什么都没发生过不就行了。"
    "白一说得随意，好像身上发生这种事情的不是她本人一样。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "我也希望什么都没发生过，可惜不行。"
    "西顺无奈地耸耸肩膀，态度很明确，这件事到她接手，一定要有始有终。"
    by eye_move def "……啧。"
    xs "从过往数据来看，怪异会对生物产生影响，只是时间问题，你不要有侥幸心理。"
    by eye_def o "我没有。那能不能现在就让她从我身体里滚蛋。"
    hide xsimg
    show xsimg o at char_mid
    xs "我只能说，会尽力。"
    xs "不过，在那之前还有些事要解决，会影响对你后续的处理。"
    by eye_wacky o "到底还有什么，怎么这么多事？"
    hide xsimg
    show xsimg at char_mid
    "白一的耐心实在不多，就算之前是被城安局吓到，好脾气也几乎要耗尽了。"
    "但西顺只是意有所指地叹了口气。"
    hide xsimg
    show xsimg eye_move o at char_mid
    xs "这个，你要问你自己，之前都做了什么。"
    by eye_wacky e "……哈？"
    hide xsimg
    show xsimg o at char_mid
    xs "我们刚才说过，案发现场有两具尸体，当时都被断定为意外死亡。"
    by eye_def o "当时？"
    hide xsimg
    show xsimg at char_mid
    xs "嗯，你，还有另外一个人。"
    by eye_wacky def "……"
    "白一皱起眉毛，莫名有种令人不舒服的，即将被麻烦事缠上的感觉。"
    hide xsimg
    show xsimg o at char_mid
    xs "但现在你重新醒了过来，还和怪异有了联系。"
    by eye_wacky def "所以……"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "所以，事情需要重新调查。"
    hide xsimg
    show xsimg o at char_mid
    xs "她的死亡有可能是自杀或意外，但如果不是——"
    xs "你现在是唯一的嫌疑人。"
    by eye_shock o "{size=45}你们觉得我杀了另外一个人？？{/size}"
    hide xsimg
    show xsimg eye_close at char_mid
    xs "现在只是推测。"
    $ renpy.music.play(music.sus, loop=True, fadein=0.5)
    "西顺很严谨冷静，但白一根本冷静不下来。"
    by eye_wacky o "拜托，说不定就是她自杀拖我下水呢？"
    hide xsimg
    show xsimg at char_mid
    xs "你说的那个，的确也可以是一种可能性。"
    hide xsimg
    show xsimg o at char_mid
    xs "但是，要先从可能性最高的方向开始调查，也就是你。"
    xs "不管是什么，都有必要查清楚。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "毕竟，你也想不起来那天发生了什么不是吗。"
    "西顺两手摊开，做出一个“我也没办法”的表情，换来白一的冷笑。"
    by eye_wacky e "我是失忆，不是傻逼，怎么可能会做这种傻逼事。"
    hide xsimg
    show xsimg o at char_mid
    xs "我也相信，但这不是你或者我说了算的。"
    hide xsimg
    show xsimg o at char_mid
    xs "好了，今天很晚了，先这样。也不至于要让你不眠不休，但之后的时间就麻烦你继续配合啰。"
    by eye_move def "……哦。"
    stop music fadeout 0.5

    $ quick_menu = False
    window hide
    scene bg_byroom3 with Fade(0.3,0.5,0.3)
    show screen tpoinfo("12月12日，星期日","白一的家") with dissolve
    pause 1
    hide screen tpoinfo with dissolve
    window auto
    $ quick_menu = True
    $ renpy.sound.play(sound.cutting_board, channel="sound", loop=True, fadein=0.5)
    "笃，笃，笃……"
    scene bg_byroom3 with vpunchs
    "笃笃笃笃——"
    me "喂……"
    "没有回应。"
    scene bg_byroom3 with vpunchs
    "笃笃笃笃——"
    me "你再切菜板都要坏了。"
    by eye_def o "啊？哦……"
    stop sound
    "再次听到我的声音，白一终于停下手上的动作。"
    "原本要切成长条的肉块，已经被白一刚才的力气剁成了糊状物质。"
    by eye_still e "草……晦气。烦死了……"
    "说完，她又举起菜刀，恶狠狠地拍了两下。"
    "看这架势，怕是把西顺当成了这块被剁的肉……"

    scene bg_byroom3 with fade
    "凌晨回家后，白一就直接睡着了，中午醒来就一直是这一副怨气极深的样子。"
    "不过，想来也能理解。{p}无论是谁，突然被卷入这种事情都很难保持平静吧……"
    "醒来之后，白一已经把家里检查了一遍，但仍然没有想起任何关于那两天的事情。"
    "因而，尽管不想，但现在也只好等着西顺的指示。"
    by eye_def o "你会被饿死吗？"
    me "啊？"
    by eye_def e "……算了，要是你真会被饿死反而方便了。"
    me "喂……"
    by eye_close o "今天午饭没了哦。"
    "她把菜刀摔在灶台上，囫囵地把一坨肉泥塞进保鲜膜，扔到冰箱里。"
    "然后，她砰地一下，把自己扔回床上，呆呆地看着天花板。"
    me "呃，其实……切坏了也能做菜？"
    by eye_wacky e "用你说？"
    by eye_wacky e "我知道啊。没心情而已。"
    by eye_close e "很烦，很困，很冷，还要出门……啧。"

    "白一在床上躺了一会，滚了好几圈，最终还是跳下床，从抽屉里掏出一个面包。"
    "正撕开包装纸时，门铃响了。"

    show xsimg smile at char_mid with moveinleft
    xs "哟，我来早了？不是预留时间给你吃午饭了吗。"
    by eye_wacky e "呵呵，毕竟马上要去自己的死亡现场，很难有食欲。"
    "虽然这么说着，但白一一边说话，一边扯开了包装纸，嚼着面包跟西顺出了门。"

    scene bg_car with fade
    "到了车上，西平和西顺坐在驾驶座和副驾驶，白一则顺势坐在了后座，有些无聊地看向窗外。"
    xs "你看起来好像不怎么害怕啊，没什么想法吗？"
    by eye_move e "……害怕有用吗？"
    by eye_close def "反正都死过一次，大不了就是真死了呗。"
    xs "嗯，你这个心态倒是挺好的。"
    by eye_wacky o "啧……你不就觉得是我杀了她嘛，不用这么虚伪地夸我。"
    "西顺坐在前排整理资料的声音停了，她往后看了一眼，又转过头去。"
    xs "虽然不知道你为什么对我意见很大……但我自认为没有像你心里那样想过。"
    xs "在结果出来之前，我并不会因为任何推测对你有不同的态度。"
    xs "我只是在找真相而已。"
    by eye_move def "……哦。"
    "似乎是没想到西顺会这么说，白一干巴巴地应了一句。"
    "西顺也没有在这个话题上继续，只是重新拿起资料。一阵纸张互相摩擦发出的轻响后，她抽出其中一份递给白一。"
    xs "现在先把事情的资料过一遍吧，虽然因为……他们之前也没有调查多少。"
    $ renpy.music.play(music.clues, loop=True, fadein=0.5)
    by eye_still o "哦……嗯。"
    $ persistent.clue[0] = 1
    show screen clue_display(0) with dissolve
    xs "12月11日下午，死者的同学到死者家中做客，发现一直没人回应敲门的声音，也联系不上死者。"
    xs "她觉得很奇怪，强行叫来保安开门后，发现房间里有两具尸体，噢……这里应该改一下。"
    xs "死者的名字叫温心，和嫌疑人一样都是丰宁育才中学高二六班的学生。"
    xs "死者是一氧化碳中毒身亡，现场没有他人出入痕迹，推测是房间内某处的一氧化碳泄露导致的意外事件。"
    xs "嗯，这边也要改……死者可能是自杀，也有被人杀害的可能性。"
    xs "还有这里……"
    stop music fadeout 0.5
    hide screen clue_display with dissolve
    "正如西顺所说，资料的内容不多，就连解剖尸体的记录也是后来才加上的——之前被定义为意外，他们没有想过解剖。"
    scene bg_car with fade
    by eye_still def "嗯。"
    "西顺简单概括完，白一仍然盯着资料纸。她只是从喉咙里挤出一声，便没再说话。"
    "她的手放在摊开的资料纸上，视线落在温心的名字那一行。"
    "方块黑字，刚打出来还带着些油墨味道。"
    "白一不自觉地把指尖移向那个名字，轻轻地摩挲着，不知道在想些什么。"
    "在晟欧路路口下车，一股淡淡的味道随着冰冷的风吹了过来。"

    scene bg_building2 with dissolve
    by eye_def e "……又冷又臭，服了。"
    show xsimg o at char_right with moveinright
    xs "嗯，这里环境就这样，暂且忍忍吧。"
    "楼房排得很挤，老旧的建筑外墙到处是掉漆和粉尘散落的痕迹，角落堆叠着不少杂物。"
    "白一用力裹了裹外套，跟在西顺身后，走到挂着“12”标牌的楼下。"
    by eye_def o "等等。"
    xs "怎么了？"
    by eye_def e "呃，嗯，没……我鞋带掉了，系一下。"
    xs "哦行，不急，别摔了。"
    "西顺没有对白一突兀的话表示些什么，白一绷着的肩膀放松了，慢吞吞地蹲下身。"

    scene bg_ground with dissolve
    "手指被冻得冰凉，打结也不顺利，白一盯着地面，轻轻吐出一声叹息。"
    me "……你怎么了？"
    by eye_move o "没事啊。"
    me "就是……你大概不知道，我好像能感受到你身体的变化，也能感受到你的情绪。"
    me "比如现在，你好像有点纠结……憋闷……嗯，难受？还有——"
    by eye_shock o "草，别说了！"
    by eye_wacky e "你不要脸啊……"
    "她急急地打断了我的话，而后又叹了口气。"
    "确认不远处的西顺和西平听不到之后，才继续保持着很小的声音。"
    by eye_move def "{size=23}没啥。只是在想，会不会真的是我杀了她。{/size}"
    by eye_move smile "{size=23}呵呵……毕竟我真的什么都不记得了，甚至还会诈尸，还被你这种东西缠上，好像什么都有可能。{/size}"
    by eye_close o "算了，我就随便说说，怎样都无所谓……"
    "她叹了口气，一副真的无所谓的样子。"
    "虽然她这么说，但我似乎能感觉到……她的喉咙发干，心脏也跳得十分慌乱。"
    "也许，不，一定……并没有她嘴上说的那么轻松。"
    "毕竟……她也只有17岁而已。"
    by eye_move def "啧……受不了，冷得要死……"
    by eye_close o "不下雪的降温，简直就是耍流氓。"
    "白一系紧鞋带，倏地站起身。"
    "只剩下最后一句轻飘飘的话，{w=0.5}颤抖着散落在冰冷的空气中。"


    $ quick_menu = False
    window hide
    scene bg_wxroom with fade
    show screen tpoinfo("12月12日，星期日","温心的家") with dissolve
    pause 1
    hide screen tpoinfo with dissolve
    window auto
    $ quick_menu = True

    by eye_def e "咳，咳咳……"
    "楼梯间更加狭窄拥挤。\n爬上来耗费的体力，杂物中飞舞的灰尘，以及冰冷的空气让白一忍不住咳嗽了好一会。"
    "推开门，有些狭小的房间一览无余。"
    "一张木桌贴着一张床在右侧，旁边挨着几个高高的柜子，最左边的柜子通向贴墙的小灶台。中间开了一扇门，通向洗手间。"
    show xsimg o at char_mid with moveinleft
    xs "你过来仔细看看，不要上手动就行。"
    by eye_def o "啊？关我什么事。"
    xs "主要是看看你能不能想起什么，或者她能不能看出些什么。"
    hide xsimg with dissolve
    by eye_def def "哦……"
    by eye_still def "{size=23}看来，还是得看你了。我肯定什么也想不起来。{/size}"
    "白一这句话说得很轻，我知道她是对我说的。"
    $ renpy.music.play(music.clues, loop=True, fadein=0.5)
    show black with dissolve
    pause 0.5
    hide black with dissolve
    jump wxroom
    return



label c1_1_extra:
    me "我觉得……"
    menu:
        "没有他人导致温心死亡":
            me "她……应该是自杀，或者意外死亡？"
            by eye_def e "是吗？你怎么看出来的？"
            jump c1_1_wrongmenu
            return
        "有他人导致温心死亡":
            me "她……应该不是自杀吧。是被人害了。"
            by eye_def def "……嗯。"
            by eye_def o "怎么说？"
            jump c1_1_menu1
            return

# for【没有他人导致温心死亡】
label c1_1_wrongmenu:
    window hide
    $ quick_menu = False
    show screen clue_choice([3,6],"c1_1_wrongmenu_continue","c1_1_wrongmenu_continue","温心的死亡原因？")
    pause
    jump c1_1_wrongmenu
    return


label c1_1_wrongmenu_continue:
    by eye_wacky o "……这和你的结论有什么关系？"
    me "呃……就是，这样，那样？"
    by eye_wacky e "你在搞笑吗？"
    me "……"
    jump c1_1_extra
    return


# for 【有他人导致温心死亡】
label c1_1_menu1:
    window hide
    $ quick_menu = False
    # 【选对笔记-药盒/燃气灶】
    show screen clue_choice([3,6],"c1_1_menu1_wrong","c1_1_menu1_correct","温心的死亡原因？")
    pause
    jump c1_1_menu1
    return


label c1_1_menu1_wrong:
    $ quick_menu = True
    # 【选错笔记】
    by eye_wacky o "你是怎么通过这种东西得出刚才的结论的？"
    me "……"
    jump c1_1_extra
    return


label c1_1_menu1_correct:
    $ quick_menu = True
    # 【选对笔记-药盒/燃气灶】
    by eye_def def "看来你跟我想得差不多。"
    me "嗯……也许？"
    by eye_def o "记得资料上说，整个过程是温心吃了安眠药之后在房间里睡死了，然后因为忘记关燃气灶而中毒。"
    by eye_def o "但是……这里根本没有任何安眠药的痕迹……药盒里也只有感冒药。说明她平时可能根本不吃。"
    by eye_def o "然后……燃气灶也有点奇怪。"
    me "对，她房间都收得很干净，也记录有定期清理的习惯，只有灶台堆积了重重的灰尘。"
    by eye_still o "也就是说……她刚好那天吃了安眠药，又刚好忘了关灶台，还刚好遇上燃气灶的喷嘴被堵了。"
    me "哪有这么巧的事？"
    by eye_close e "对啊，信这种事是巧合不如信我是全球首富。"
    me "……嗯，对。"
    xs "说得没错，而且白一你也要做一下药物检测。"
    by eye_def o "……等等你听得见啊？?"
    show xsimg o at char_mid with moveinleft
    xs "你又失忆了？难道这还是间歇性的吗？"
    hide xsimg
    show xsimg at char_mid
    "西顺忽然从旁边插嘴，气得白一大叫起来。"
    by eye_shock o "{size=45}我没失忆！！{/size}"
    by eye_def o "我以为，你是通过设备辅助之类才能在房间里听到声音的。"
    xs "不不，你可以理解为我的体质特殊，所以能听见。"
    by eye_wacky e "靠，开挂啊。"
    hide xsimg
    show xsimg smile at char_mid
    xs "怎么，我是特调组的诶。"
    "言下之意大概是，作为处理这方面事件的人，有一些“特异”才是正常的，并不奇怪。"
    "虽然有道理，但白一莫名觉得有些憋屈——大概是一种被人看破秘密的不爽。"
    hide xsimg
    show xsimg o at char_mid
    xs "温心的死亡有疑点……那么很大可能，她不是意外死亡，也不是自杀，而是被人杀害的。"
    by eye_def o "哦，是啊。所以这个人是谁呢？"
    by eye_close e "呵呵，找来找去，结果反而我是凶手的可能性更大了……"
    hide xsimg with dissolve
    "因为不能破坏现场，白一只好倚靠在墙边，发出自嘲的低笑。"
    me "别啊，也不能证明就是你……"
    by eye_wacky e "呵呵，我也希望，但是又没有证据——不，有吗……？"
    by eye_def o "你觉不觉得……好像还有什么细节？"
    menu:
        "没有了":
            by eye_still def "是吗？但我总觉得好像忘了什么。"
            me "啊？那你说是什么？"
            by eye_close o "这就要问你了啊，你总不能拖我后腿吧？"
            me "……"
        "还有细节":
            me "貌似……还有吧。"
            by eye_def def "我也感觉，但，是什么？"
            me "嗯……"
    me "那么……如果说真的还有被忽略的细节的话……"
    me "应该是……"
    jump c1_1_menu2
    return

    

label c1_1_menu2:
    window hide
    $ quick_menu = False
    # 【选垃圾桶/餐桌/备忘录】
    show screen clue_choice([1,4,7],"c1_1_menu2_wrong","c1_1_menu2_correct","被忽略的细节？")
    pause
    jump c1_1_menu2
    return


label c1_1_menu2_wrong:
    $ quick_menu = True
    by "不对，这里好像没什么东西，你再看看别的。"
    jump c1_1_menu2
    return
    

label c1_1_menu2_correct:
    $ quick_menu = True
    me "我不确定，但有样东西可能不见了。"
    by eye_def def "嗯？什么意思。"
    "白一冲我指的方向看了一眼，而后思考片刻，敲了敲手背。"
    by eye_def o "哦，我也知道了。垃圾桶……很干净。"
    me "对，虽然也可能就是没有东西，但是……"
    by eye_def e "但是就会显得很奇怪。"
    by eye_def o "她会把一次性筷子收起来，平时应该很节约，然后习惯了。就是，不用的话也不会丢掉。"
    by eye_def o "但她如果这么节约，按理说不应该会吃“湘味”那家店才对。"
    by eye_def o "或者她就是想吃……那外卖也不知道去哪里了。平时八点扔垃圾，但那天她八点之前就……死了。"
    me "所以最有可能的是，有另外一个人点了外卖，然后处理掉了。"
    by eye_def e "对……而且这个人不是我，可以查我的消费记录。"
    me "……但这只是猜测，并不知道有没有第三个人存在。"
    "虽然很希望，但我还是忍不住提醒了一句，生怕这是所谓虚假的希望。"
    by eye_still e "废话，我知道……我当然知道。"
    show xsimg eye_still o at char_mid with dissolve
    xs "这方面你们不用担心，你……总之，我们会找出真凶的。"
    hide xsimg
    show xsimg at char_mid
    "西顺放下手机，重新加入了对话。"
    hide xsimg
    show xsimg eye_still at char_mid
    "她的表情有些凝重，似乎是刚才的电话里听到了什么不好的事情。"
    hide xsimg
    show xsimg at char_mid
    "但这只是一瞬间，很快又恢复成标准的淡然，好似刚才的只是错觉。"
    by eye_move o "哦，最好是。"
    by eye_close def "那我是不是该避嫌了？毕竟我现在可是头号嫌疑人。"
    hide xsimg
    show xsimg smile at char_mid
    xs "这个啊……暂时还需要你的帮助。"
    by eye_wacky o "哈？"
    hide xsimg
    show xsimg laugh at char_mid
    xs "比如——你跟我回去，做一下身体检查。"
    by eye_close o "啊——好吧。"
    "白一翻了个白眼，然后像号丧一样，长长地吐出一口气，认命地跟在西顺身后。"
    stop music fadeout 0.5
    return

