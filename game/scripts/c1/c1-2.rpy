label c1_2:
    scene bg_byroom2 with Fade(0.4,0.5,0.4)
    me "检查结果明天才出来。"
    by eye_def o "啥？我知道啊？"
    me "呃……我是想说……明天才知道，你现在不用这么，紧张？"
    by eye_def def "……"
    by eye_wacky e "哈？你觉得我在紧张吗？"
    me "不是吗，那你为什么一直在床上滚来滚去。"
    me "能别转了么，弄得我头很晕啊……"
    by eye_close o "不能，忍着。"
    me "……"
    me "你——"
    by eye_close e "我没紧张。"
    "白一飞快地接话。"
    me "哦……好吧，你没紧张。"
    me "不过，你是不是忘了我能感觉到——"
    by eye_shock o "{size=45}都说了你感觉错了！{/size}"
    by eye_shock def "……"
    by eye_close o "{size=23}我只是，现在想起来，还是觉得很不真实罢了。{/size}"
    "有人死了，曾经死过，杀人嫌疑……\n一切都不真实。"
    me "嗯……也对。"
    "白一在床上打滚的动作停下后，房间变得很安静，只有她的心脏在慢慢跳动。"
    "就像她的情绪，变得平缓，混杂着无所适从的迷茫，溶解在夜色之中。"

    scene bg_byroom2 with fade
    show tophalfblk with dissolve
    by eye_close e "话说，温心她……其实我跟她不熟，毕竟只是同班同学。"
    by eye_move e"不过要这么说的话就没有同学跟我熟的……"
    me "嗯。"
    "白一忽然开始嘀嘀咕咕。\n我不知道为什么她突然说这个，但我认为，这时候或许只是听着比较好……"
    by eye_close o "在学校里好像说过两句话，但我没印象了。"
    by eye_close o "但是没印象说明也没发生过什么。"
    me "哦……嗯。"
    hide tophalfblk with dissolve
    by eye_move e "所以，我真的会杀了她吗？我为什么要做这种脑残事？？"
    me "嗯……"
    me "既然你觉得不会……那就相信自己呗。"
    by eye_wacky smile "呵呵，我是很想相信，但现在也发生了很多事情。"
    by eye_close o "很多事情，我原本是不信的那些……"
    "面对我苍白的安慰，她只是冷笑一声，啪地把被子扔到自己的头顶。"
    by eye_close e "啊……真的烦死了……"
    "白一轻骂一声，却没有再说话。"
    "房间里再次变得沉默。"
    "被子被揉捏摩擦，发出沙沙作响的声音，仿若不安的心绪。"
    "好在，不知何时，她已然被睡梦侵蚀。"

    $ quick_menu = False
    window hide
    scene bg_meetingroom with fade
    show screen tpoinfo("12月13日，星期一","城安局") with dissolve
    pause 1
    hide screen tpoinfo with dissolve
    window auto
    $ quick_menu = True
    $ renpy.music.play(music.police, loop=True, fadein=0.5)
    "熟悉的时间，熟悉的地方。"
    "面无表情的西平，笑眯眯的西顺，以及满脸不爽的白一在一个房间。"
    "——连表情也如此熟悉。"
    show xsimg o at char_mid with moveinright
    xs "今天主要有三件事。"
    xs "第一个，结果出来了。你跟温心一样，是在差不多的时间服用安眠药的。"
    by eye_def def "哦。所以，这样能证明我不是凶手吗？"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "嗯——不能。理论上，比如，有可能是你知道自己会醒过来，自己吃的。"
    "总而言之，因为白一突然“死而复生”，整件事情变得更加复杂。"
    "除非有直接能够指认凶手的证据，否则，就目前唯一被证明在案发现场的，还和怪异有联系的人，白一很难清除嫌疑。"
    by eye_wacky e "……那你说个屁啊。查出来有什么用？不还是一样。"
    hide xsimg
    show xsimg at char_mid
    xs "不，信息越多，就离真相越近。"
    hide xsimg
    show xsimg o at char_mid
    xs "一件件查下去，会找到的。"
    by eye_move def "……行，你说是就是吧。"
    "白一对此毫无兴趣，也懒得和西顺争论。"
    hide xsimg
    show xsimg smile at char_mid
    xs "嗯，第二件事，之前，不是要给你做检查吗，就顺便多检查了一些。"
    hide xsimg
    show xsimg o at char_mid
    xs "加上查资料，我大概知道了，你身上的情况。"
    by eye_still o "……什么？"
    hide xsimg
    show xsimg at char_mid
    "白一愣了愣，而后，不知为何，微微皱了皱眉。"
    "某种不知名的情绪浮现，似是不满，还有藏在不满心情下的紧张。"
    "被她的情绪感染，我也变得紧张起来。"
    "西顺说的是那个意思吗？她是弄清楚什么了吗？然后……是要解决吗？"
    hide xsimg
    show xsimg o at char_mid
    xs "你身上的情况，和一种古老的诅咒有相似之处。"
    xs "这种诅咒会在被诅咒的人受到致命伤害的时候生效，让身体进入一段时间的假死状态，避开真正的死亡。"
    xs "诅咒生效之后，被咒的人会忘记死之前发生的事情。"
    xs "所以，你才会出现短暂性失忆的情况。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "不过……避开死亡并不是无条件的，它会导致不可预知的副作用。"
    xs "而现在你身上的副作用就是……嗯，类似于，如果不彻底解除诅咒，还是会在三个月之后死掉。"
    by eye_still def "……"
    "这消息实在突然，且信息量巨大。"
    "以至于白一没有任何反应，只是呆呆地愣在原地。"
    hide xsimg
    show xsimg at char_mid
    xs "你真的什么都想不起来吗？现在也是？"
    by eye_wacky o "废话。不然呢？"
    "情绪被打断，白一没什么好气地呛了一句。"
    "西顺只是耸耸肩，继续往下说。"
    hide xsimg
    show xsimg o at char_mid
    xs "好了，我不是故意吊你胃口。"
    xs "我这么问，是因为要解除诅咒，需要你找回死亡时的记忆。"
    by eye_wacky e "……哈？！"
    by eye_wacky def "这又是什么说法。"
    hide xsimg
    show xsimg at char_mid
    xs "别这么看我，我没骗你。"
    hide xsimg
    show xsimg o at char_mid
    xs "等你想起来那段记忆，自然就知道该怎么做——嗯，资料上是这么说的。"
    by eye_still e "……所以……反正基本意思就是，我三个月之后还是会死咯。"
    hide xsimg
    show xsimg at char_mid
    xs "也许，如果找不到解决方法的话。是的。"
    by eye_still "……"
    by eye_close o "哦……"
    by eye_def e "等等，所以关于她的呢？我跟[user]是怎么回事？"
    "想不通，白一干脆转移了对话，好似这样就能一起撇开胸口那股烦闷的感觉。"
    "只是，急忙抛出来的话题，似乎也并没有好到哪里去。"
    hide xsimg
    show xsimg eye_move o at char_mid
    xs "嗯……这个还不知道。"
    by eye_wacky e "哈？！"
    xs "也许这也是副作用的一种吧……{size=23}只是之前没出现过，也没听说过，会联系到完全不相关的人身上……{/size}"
    by eye_wacky def "……"
    "怎么感觉不太靠谱……"
    hide xsimg
    show xsimg o at char_mid
    xs "所以我说，是古老诅咒的相似类型。你和她的这种情况，在记录里从来没有过——啊，当然这次以后就会有了。"
    by eye_still def "这算什么。"
    hide xsimg
    show xsimg at char_mid
    xs "但硬要说也不算奇怪。怪异本就无法用常理判断，世界上的怪异也千变万化。"
    hide xsimg
    show xsimg o at char_mid
    xs "用我们的话说，你遇到了，这就是属于你的“缘”。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "不过，可以确定的是，她因为诅咒绑定你，自然和诅咒一样，有类似的特性。"
    hide xsimg
    show xsimg o at char_mid
    xs "她附着你的身体，会消耗你的生命力，当然，解除之后也会完全消失。"
    by eye_close e "哦……"
    python:
        persistent.dictList.append(("白一身上的诅咒-1","和一种古老的诅咒有相似之处。\n该诅咒有一定概率在极端条件下令人进入假死状态，提供可能的生机。\n诅咒生效后，会产生无法预知的副作用。"))
        persistent.dictList.append(("白一身上的诅咒-2","一体双魂，指的是在一具躯体里强行塞入第二个灵魂。\n这是一种由怪异产生的负面效果，会大量消耗躯体的寿命，直至承受不住。\n这个过程不长，大约有两三个月的时间，身体就会完全崩溃。"))
        persistent.dictList.append(("白一身上的诅咒-3","诅咒生效后必然会产生副作用，为防止人类随意钻空子使用诅咒，怪异会清除掉和诅咒相关的记忆。\n反过来说，只要找回被清除的记忆，就可以彻底清除身上的诅咒。"))
        persistent.dictList = list(set(persistent.dictList))
    $ renpy.sound.play(sound.dictionary, channel="dictionary", loop=False)
    $ renpy.notify ("【词典】更新")

    hide xsimg
    show xsimg eye_move smile at char_mid
    xs "怎么，现在开始舍不得了？"
    by eye_shock o "才没有！怎么可能！"
    hide xsimg
    show xsimg at char_mid
    xs "……"
    hide xsimg
    show xsimg smile at char_mid
    xs "嗯，那就好。"
    hide xsimg
    show xsimg at char_mid
    "西顺挑了挑眉，看着白一轻笑了一会。{p}但她没有继续调侃下去，而是很快收起了笑容。"
    hide xsimg
    show xsimg o at char_mid
    xs "像你们这种情况，共感，同知，可以算是每时每刻在一起。"
    xs "[user]能看见，也能跟你一起思考，你们互相提醒，对于你们解除诅咒是有好处的。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "但是，你们要知道，这些都只是为了解除诅咒，千万不要对此投入太多感情……你们都是。"
    hide xsimg
    show xsimg o at char_mid
    xs "不要被吊桥效应影响。"
    by eye_still def "……哦。你要教我做事？"
    "白一皱起眉毛，语气立马冷了下来，对西顺的提醒嗤之以鼻。"
    by eye_still o "解决这种问题本来就是你们的工作内容吧。我是会配合，但这可不是我的责任。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "不，并不是你想的那样。这只是例行的提醒而已。"
    by "……呵呵。"
    "白一只是冷笑一声，也懒得对这句话做出直接回答。"
    hide xsimg
    show xsimg o at char_mid
    xs "好，那么现在说第三件事。"
    "西顺没有被白一的态度所影响，而是自然地接过了下一个话题。"
    xs "温心的房间。关于我们之前推测的垃圾，暂时还没有发现对应的证据。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "可能已经被处理掉了，当然，也不排除不存在这个东西。"
    by eye_still o "……所以？"
    hide xsimg
    show xsimg o at char_mid
    xs "虽然暂时没找到，但是这个思路是没有问题的，可以继续往下排查，只是——"
    hide xsimg
    show xsimg at char_mid
    by eye_def o "哦，总之你的意思就是全都回到原点了呗？"
    by eye_close e "都说了这是你们的工作，你什么都查不出来，却只会跟我说有的没的，只会教我做事？"
    by eye_still o "像你这样做事，能查到什么东西？能查到才有鬼。"
    hide xsimg
    show xsimg o at char_mid
    xs "首先，你冷静一点，不是你想的那样。"
    by eye_still "……"
    "面对白一的刻意挑衅，西顺的表情没有任何变化，这让白一有一种一拳打到棉花上的感觉，蓄起来的气无处可发。"
    by eye_close o "哦，知道了。"
    "但她也没有要配合的意思，只是沉默地盯着西顺，而后从椅子上站了起来。"
    by eye_close def "我先——"
    $ renpy.music.play(music.shocked, loop=False)
    scene bg_meetingroom with vpunchm
    by eye_shock e "嘶——"
    "即将转身时，一道黑影在眼前飞速闪过。"
    show cg_xp00 at cg0 with w9
    "随后，白一的手腕被扣住，停在了原地。"
    "力气之大，令白一忍不住下意识吸了口凉气。"
    show cg_xp01 at cg0 with vpunchm
    hide cg_xp00
    by eye_shock e "你要干嘛？！"
    "白一又惊又怒，死死地地盯着面前的人——西平突然站起身，用力抓住了她的手腕。"
    show cg_xp00 at cg0 with dissolve
    xp "你等一下，先听她说完。"
    stop music
    
    scene bg_meetingroom with Dissolve(1)
    "西平只是这么说着，放开了手，而后又恢复到平时那没什么存在感的状态。"
    "然而现在，白一可不信她真的没有什么存在感……"
    "不如说，她更像是某种蛰伏的动物，一直观察着白一和西顺。"
    "而稍有不对，就会露出獠牙。"
    "——当然，是对白一露出獠牙。"
    by eye_wacky e "我只是想说我要先去个洗手间！{size=23}……顺便晾一下你们……{/size}你们又要怎样啊？？"
    "夹在中间的那句抱怨很小声，没人听见。"
    "因而西平顿了顿，而后微微颔首。"
    show xpimg o at char_right with moveinright
    xp "抱歉，我刚刚有些着急。"
    by eye_still o "哦。"
    "白一冷冷地应了一声，转身推门出去了。"

    scene bg_restroom1 with fade
    by eye_wacky o "哇靠——她的力气也太大了吧？！这合理吗？"
    "进到洗手间的小隔间，白一强撑的气势立马就泄了下来。"
    by "超级痛，是吧？突然抓着我的手，还那么用力，连手臂都一起扯到了。"
    by "我差点以为我的手要断了，至于吗？真受不了……"
    me "嗯……有点。"
    me "但是……主要是因为，你手上有伤吧……你之前弄的那些……"
    "白一抱怨的声音一下停住。而后，声音变得更加冷硬。"
    by eye_still def "哦，对啊。"
    by eye_wacky smile "是又怎样？你不喜欢吗？"
    me "不……我没那么说……嘶。"
    by eye_close def "可惜了，那你也只能受着。"
    show cg_arm at cg0 with vpunchs
    "她撩起左手的袖口，用力在深深浅浅的伤口上又捏了一把。"
    me "喂……"
    "我没想到只是稍微提一嘴，她的反应就那么大。"
    "说到底，我其实也没有非要问出什么的意思，只是难免会有些好奇而已……"
    "毕竟，那些伤痕深深浅浅，很明显不是最近这一次就能弄成的样子。"
    "但……"
    me "嘶……"
    "又一阵尖锐的刺痛随着白一的动作产生，疼得我恍惚一瞬，忘了思考。"
    by eye_still e "没有不喜欢就好。而且，你不觉得很爽吗？"
    "最新的伤口好像有些裂开了，暴露在冰冷的空气里。"
    hide cg_arm with w21
    me "……不觉得。"
    by eye_close smile "噢，那抱歉。不过那也没办法，毕竟这还是我的身体。"
    "白一有些恶劣地笑了笑，而我不知道该如何回复，只好轻轻地叹了口气。"
    "话题突兀地结束，没有人想要继续说什么，于是继续的只有沉默。"

    scene bg_corri with fade
    "从洗手间出去，白一在转角处看见了倚在墙边的西平。"
    "她手里掐着一张便利贴，看到白一过来，眼神飞速地在手里的东西和白一身上来回扫过。"
    $ renpy.music.play(music.police, loop=True, fadein=0.5)
    by eye_def e "你怎么又来了？"
    show xpimg o at char_right with moveinright
    xp "我想说，刚刚——{p}刚刚的事情，对不起。"
    by eye_def def "……之前不是已经说过一遍了吗？"
    "白一拧着眉毛，十分不解地看着西平。"
    xp "城安局，没打算继续查这个案件。"
    by eye_def o "……啊？"
    xp "你——"
    show xsimg eye_still smile at char_left with moveinleft
    xs "喂，我说西平姐姐，你说的有事，该不会就是指偷偷找我的嫌疑人吧？"
    hide xpimg
    show xpimg at char_right
    xp "……"
    "西顺忽然出现，声音打断了西平要说的话。"
    hide xpimg
    show xpimg eye_still at char_right
    "西平微微拧了拧眉毛，看向西顺，最终还是什么也没说。"
    hide xpimg with moveoutright
    "她只是稍稍后退两步，又变成那副背景板的样子。"
    by eye_wacky o "……你们到底要干嘛啊？别把我扯进去行不行。"
    hide xsimg
    show xsimg eye_close o at char_left
    xs "哎……"
    xp "你没说我不能说。"
    hide xsimg
    show xsimg at char_left
    xs "……我知道，我没在说你。"
    "西顺轻轻拍了拍西平的背，然后回过头，冲着白一无奈地耸耸肩膀。"
    hide xsimg
    show xsimg o at char_left
    xs "大家都在这，还是回房间说吧。"
    by eye_def o "哦……"
    $ persistent.charinfo1[9] = 1

    scene bg_meetingroom with fade
    show xsimg o at char_mid with moveinright
    xs "之前说东西没查到，确实是不好查，但也有别的原因。"
    xs "城安局想要提前结案，他们也不让我继续查下去。"
    by eye_def o "……怎么会这样？"
    hide xsimg
    show xsimg at char_mid
    xs "唔——这件事现在变得很复杂，而它“不值得”变得这么复杂。"
    by eye_wacky e "……哈？什么意思。能不能说清楚点。"
    "白一皱起眉——她最讨厌这样似是而非的说法。"
    hide xsimg
    show xsimg eye_move at char_mid
    xs "怎么说呢，嗯……"
    "西顺看起来像在纠结什么，手指一下又一下地轻轻敲着桌面，发出有规律的轻响。"
    hide xsimg
    show xsimg o at char_mid
    xs "现在能找到和案件有联系的人就三个，温心，你，报案人。"
    hide xsimg
    show xsimg eye_still o at char_mid
    xs "温心是个孤儿，养她长大的奶奶也在不久之前去世了。而你——"
    $ renpy.music.set_pause(True)
    by eye_def o "哦，我也是孤儿。"
    hide xsimg
    show xsimg eye_shock o at char_mid
    xs "你——嗯？？你说什么？"
    hide xsimg
    show xsimg eye_shock at char_mid
    "西顺罕见地愣住，一时间竟然没能接上话，只是呆呆地盯着白一。"
    hide xsimg
    show xsimg eye_shock o at char_mid
    xs "{size=45}咳咳咳！！{/size}不是，你——"
    hide xsimg
    show xsimg eye_shock at char_mid
    by eye_move e "咳——反正，反正差不多就是了。"
    "眼见西顺要说出什么，白一赶紧打断了她的话。"
    by eye_def o "我说，这不是重点吧？你要说什么就快点，别纠结这个。"
    hide xsimg
    show xsimg eye_close o at char_mid
    $ renpy.music.set_pause(False)
    xs "好吧，这确实不重要。总体来说，你和温心都是没什么社会联系的人，高中生，报案人也是个普通的高中生。"
    hide xsimg
    show xsimg o at char_mid
    xs "像你们……你们这样的事情，过程很麻烦，但是涉案人和结果都很简单，不值得动用这么多资源查。"
    by eye_wacky def "哦，我懂了。"
    by eye_close o "就是温心死掉也没什么关系，我有什么事也没什么关系，因为没人在意，是吧？"
    hide xsimg
    show xsimg at char_mid
    xs "嗯……你想这么理解，那也可以。"
    "西顺并没有直接承认，但她的态度跟直接认同白一没什么区别。"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "这不是我的想法。"
    "她强调一遍，轻轻叹了口气，而后抬起手用力捏了捏眉心。"
    by eye_def def "哦，那又怎样？"
    "是谁怎么想都无所谓，白一只是冷淡地看着西顺继续说。"
    hide xsimg
    show xsimg o at char_mid
    xs "昨天我收到通知，被要求马上结束调查这件事，有两个选择。"
    xs "一是公布温心是意外死亡，二是公布你是凶手。"
    hide xsimg
    show xsimg at char_mid
    by eye_close def "……"
    by eye_def def "哦。"
    by eye_def o "所以呢？那你是什么想法？跟我说这么多是什么意思？"
    hide xsimg
    show xsimg o at char_mid
    xs "因为，你——"
    by eye_def o "说得很有道理啊，反正我也很可能是凶手，这样不就是直接搞定了，根本不用麻烦那么多事。"
    by eye_still e "还是说，你的意思是，把这些告诉我，让我看看你是不会那样做的，和其他人不一样。"
    by eye_def o "要让我对你感激涕零吗？"
    hide xsimg
    show xsimg eye_still o at char_mid
    xs "……不，你不要这么想。"
    hide xsimg
    show xsimg o at char_mid
    xs "我不需要你的感谢，我需要你的帮助。"
    by eye_wacky o "……啊？"
    hide xsimg
    show xsimg eye_close o at char_mid
    xs "如你所见，因为城安局，我自己查东西的时候会受到阻碍。之后，需要你帮忙的地方更多了。"
    by eye_move o "哦……免费劳动力是吧。"
    "白一了然，但又有些疑惑。"
    by eye_def e "所以……意思是这么麻烦的事情，你还要继续？而且，你这样不算违规？"
    hide xsimg
    show xsimg eye_move o at char_mid
    xs "嗯，我自然有我的方法。"
    hide xsimg
    show xsimg eye_move at char_mid
    "西顺轻咳两声，很快带过这点，显然也是不想多说。"
    hide xsimg
    show xsimg o at char_mid
    xs "首先，现在明显还有疑点。嫌疑很重，也不代表真的是凶手。"
    xs "其次，就算是你杀了她，也不是让你不明不白地在三个月之后失去生命的理由。这是两码事。"
    hide xsimg
    show xsimg at char_mid
    xs "最后……"
    hide xsimg
    show xsimg o at char_mid
    xs "你不想知道真相吗？"
    by eye_def def "……"
    by eye_move def "……"
    hide xsimg
    show xsimg at char_mid
    "白一陷入了沉默，没有回话。"
    "西顺也并不显得着急，只是静静地看着她的眼睛。"
    by eye_close o "好吧，我知道了。"
    by eye_move e "我听你的就是了。{size=23}反正我也没资格拒绝吧……{/size}"
    by eye_def o "那所以现在这是要干嘛？"
    hide xsimg
    show xsimg o at char_mid
    xs "伸手。"
    hide xsimg
    show xsimg at char_mid
    "白一拧了拧眉毛，还是把右手从桌底下拿上来。"
    "西顺轻轻按住从袖口伸出的手指，而后，白一的指尖溢出一滴鲜血。"
    "血液滴在平摊的纸张上，瞬间，一道红光闪过，纸张上浮现出由曲线构成的印记。"
    by eye_wacky e "喂——"
    hide xsimg
    show xsimg o at char_mid
    xs "保密协议。"
    "西顺像是知道白一要问什么，赶在她出声之前，拿起纸，在白一的眼前晃了晃。"
    "上面的确打印着“保密协议”的墨字，还有几条严谨的条例，右下角则是刚刚才出现的红印。"
    by eye_wacky e "你们搞成这样……真的不是什么邪恶仪式吗。"
    xs "只是限制你不往外说这里的事，不会有别的危害的。"
    by eye_still def "哦……"
    xs "你就放心好了，我还能知法犯法？看，举报电话就在门口，你记一下？"
    by eye_wacky def "……"
    "白一有些无语，朝着西顺明晃晃地翻了个白眼，站起身来。"
    xs "对了，这个给你。"
    by eye_def e "呃……？"
    "西顺的表情变得有些奇怪，好像在憋笑一般，递过了一个小盒子。"
    hide xsimg
    show xsimg eye_move smile at char_mid
    xs "西平送给你的，嗯，估计是让你用的，她担心你吧。"
    "盒子里是一条耳机，白一一时间没反应过来，有些疑惑。"
    by eye_def o "啊？担心什么？"
    hide xsimg
    show xsimg eye_squint smile at char_mid
    xs "担心你平时和[user]说话被人当成脑子有问题呗哈哈哈。"
    "西顺没忍住笑出了声，看起来虽然想憋笑，但完全没成功。"
    by eye_still def "……"
    by eye_wacky e "呵呵。"
    stop music fadeout 0.5

    scene bg_byroom2 with fade
    by eye_def o "喂，那个啥，你还活着吗？"
    "………………"
    $ renpy.music.play(music.qimei, loop=True, fadein=1.0)
    me "……啊？在说我吗？"
    "愣了一会，我后知后觉地出声。"
    by eye_wacky e "难道房间里还有第二个人？"
    me "嗯……噢，在啊。"
    by eye_close o "哦。"
    by eye_def o "那你怎么今天都没怎么说话，我还以为你终于消失了呢。"
    me "……你是在担心还是在幸灾乐祸？"
    by eye_def e "你猜？"
    me "……"
    me "好吧，我没怎么说话吗？"
    by eye_close o "我是看起来像白痴吗？"
    me "……"
    me "好吧……就是，呃，今天西顺不是那么说的吗……"
    by eye_def o "什么？"
    by eye_still o "哦，你——"
    "白一有些疑惑，而后说到一半，像是想起什么，蓦地轻轻嗤笑了一声。"
    by eye_still e "你该不会是在想，西顺说的那个“吊桥效应”吧。"
    by eye_wacky def "被西顺忽悠瘸了？信她的鬼话。"
    me "呃，没……"
    "不知为何，对于这个话题，我好似没有什么欲望谈论下去。"
    by "那你这么紧张干什么，就为了这个刻意不说话？更奇怪了。"
    me "呃……嗯。"
    "我不得不承认她说得有道理。"
    "不说话是为了拉开距离，可在某种程度上，我们的确……密不可分。"
    "不是不说话就能简单撇开的。"
    "可是……可是……"

    scene bg_byroom2 with Fade(0.5,1,0.5)
    "白一沉默了一会，突然睁开眼睛。"
    "眼睛已经熟悉了黑暗，能够在无光的环境里隐约看见熟悉的天花板，一时间竟然有些恍惚。"
    "不知道什么时候开始，这里对我来说，也是逐渐熟悉的天花板了。"
    by eye_close o "明天要去上学。"
    me "是啊。"
    by eye_def o "我竟然还要上学唉？"
    me "……"
    by eye_def o "突然感觉好不习惯，但是好像也没过几天。"
    me "嗯……可能是因为你失忆了一段时间，然后又发生了很多事情吧。"
    by eye_move e "啧，有道理啊……"
    by eye_def e "话说……西顺说去找线索，你有什么想法吗？"
    "因为明面上不让查，西顺也不能以特调组的名义去询问学校里相关的人，这件事只能让白一来做。"
    me "这不是你要考虑的问题嘛？"
    by eye_close o "我不擅长聊天啊，只擅长骂人。"
    me "……"
    by eye_def e "好了，那到时候这件事就交给你帮我做。"
    me "怎么就交给我了？"
    by eye_def o "那你总得有点用处吧？"
    "白一语气抬高，像是听到了什么令人很惊讶的事情。"
    me "……"
    "说不过她，也做不了任何事。我无语地叹了口气，也只好默认了她的说法。"
    me "……"
    me "对了……"
    by eye_close o "嗯……啊？"
    "白一大概已经很困了，意识模糊，过了好一会才发出含糊地回应。"
    me "所以，你……"
    me "你不会像西顺说的那样，对吧？"
    by eye_close o "……哪样……？"
    "不知道为何，我不太想主动提起这件事。"
    "——毕竟实在是显得有些，自我意识过剩。"
    "但她不知道是没听懂，还是故意装傻。我都已经开口，也只好继续。"
    me "就是……她说的吊桥效应啊。"
    by eye_still def "……"
    "许久没有听到回复，我以为她没听清，或是不想回答。"
    "再问一次的勇气也没有了。我安下心，静静地等着她彻底睡着，失去意识。"
    by eye_close smile "哧……"
    "不知道过了多久，枕头与被子之间忽然传来极其轻微的笑声。"
    "而后，白一说话的声音在房间里响起。"
    "她的声音很轻，慢吞吞的，语气却很笃定。"
    by eye_still o "想太多了真的……"
    by eye_close e "你也别太自恋了，就放一百个心好吧……"
    by eye_close e "像她说的那种故事，什么在特殊环境下，产生错误的感情……"
    by eye_close def "那种故事……早就过时了。"
    stop music fadeout 1.5
    return
