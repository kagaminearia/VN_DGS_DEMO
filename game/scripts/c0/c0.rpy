default user = ""
label c0:
    stop music fadeout 1.5
    $ quick_menu = True
    # scene bg_black
    scene black1 with w20
    "………………"
    "好黑……"
    "什么东西……"
    $ quick_menu = False
    window hide
    scene bg_sickroom with vpunchm
    show screen tpoinfo("12月12日，星期日","？？？") with dissolve
    pause 1
    hide screen tpoinfo with dissolve
    window auto
    $ quick_menu = True
    $ renpy.music.play(music.sus, loop=True, fadein=0.5)
    "——嗯？！"
    "短暂的眩晕后，眼前的场景变了。"
    "仍然很黑，但不是漆黑一片，而是能够在昏暗中看见隐约的轮廓，似乎是个拥挤的房间。"
    "房间没有开灯，看不清具体的边界，显得空荡荡的。"
    "这似乎是个完全陌生的地方。"
    "而我并不清楚发生了什么。"
    by eye_still e "什么，情况……"
    "……………………………………"
    "………………嗯……？"
    me "…………还有人，吗？"
    "——刚才的，不是我自己的声音。"
    "房间里还有另一个人，让我顿时收紧了心神。"
    "有些沙哑的女声声音不大，却像惊雷一样在我的耳畔炸开。"
    by eye_shock o "{size=45}谁在说话？！{/size}"
    scene bg_sickroom with vpunchm
    "视线猛地晃动一下，随后，变得明显的呼吸声传来，有些急促。"
    "她似乎比我更加慌张，声音微颤。"
    "但，这到底是什么情况……"
    by eye_shock e "{size=23}还有人吧？声音很近……{/size}"
    scene bg_sickroom with vpunchm
    by eye_shock o "你在哪？出来？"
    "视野开始摇晃，向左，向右，扫视一圈后又回到原地。"
    me "嗯……"
    "确认刚才的都不是错觉后，我含糊地应了声，一时间不知道怎么继续接话。"
    by eye_wacky o "有人是吗，躲哪了，为什么我看不见你？"
    "她的声音稍微提高一些，胸口的心脏也开始用力地快速跳动。"
    "不知道是错觉，还是黑暗和陌生的环境影响，憋闷感逐渐出现，令人难受。"
    "纠结好一会，我静静感受完，才斟酌开口。"
    me "我……你，嗯……"
    me "似乎……有可能……我在你身体里？"
    by eye_shock o "{size=45}什么？你在说什么鬼话？{/size}"
    scene bg_sickroom with vpunchm
    "刷地一声，她猛地站起来，双腿似乎因为躺得太久，有些发软。"
    me "你不觉得我的声音在你脑子里吗？"
    "在这一点上，于我而言也差不多。我不敢相信，却似乎又不得不相信。"
    "她说话时，声音就好像从我自己胸口发出，传到外界……"
    by eye_wacky def "……"
    "她陷入沉默，没有说话。"
    "而后，不知道沉默了多久，她猛地从口袋里抽出什么。"
    show blood1 onlayer ontop with Dissolve(0.1)
    stop music
    pause 0.1
    hide blood1 onlayer ontop
    me "呜——"
    "手指紧紧地捏着一根笔杆，而后用力地划过左臂。"
    me "啊……？"
    "那不是笔，是小刀。鲜血一点点从皮肤上被割开的缝隙中渗出，伴随着尖锐的刺痛感。"
    me "等等你——"
    show blood1 onlayer ontop with Dissolve(0.1)
    pause 0.1
    hide blood1 onlayer ontop
    "刷。"
    "又是一下。她的动作很快，第二条血口子出现在左手臂上。"
    "她在干嘛呢？？！！"
    show blood1 onlayer ontop with Dissolve(0.1)
    pause 0.1
    hide blood1 onlayer ontop
    "第三条。"
    me "嘶……"
    show blood1 onlayer ontop with Dissolve(0.1)
    pause 0.1
    hide blood1 onlayer ontop
    "第四条。"
    show blood1 onlayer ontop with Dissolve(0.1)
    pause 0.1
    hide blood1 onlayer ontop
    "第……"

    scene bg_sickroom with Fade(0.5,0.8,0.5)
    "……"
    me "……喂……！！！"
    "她的动作毫不犹豫，又快又突然，以至于我完全惊呆了，现在才反应过来。"
    me "你在干嘛呢？！"
    by eye_still def "……"
    "她停下动作，却好像也跟我一样迷茫。"
    by eye_wacky e "…………还是听得到？"
    me "啊？"
    by eye_wacky def "是真的……不是做梦？不是幻觉？……这科学吗？"
    by eye_shock o "………………我终于疯了？"
    "她捏着刀顿了顿，随后把手上的东西塞回口袋，小声地喃喃自语。"
    by eye_move e "也没听过第二人格能跟主人格同时出现，还能对话啊……"
    me "……"
    me "不……你应该没疯，我应该也很清醒。"
    by eye_still e "……那你到底是谁？"
    by eye_still o "不……你到底是什么东西？"
    me "……"
    "怎么还带骂人的？"
    "尽管这么说，我也很无奈。"
    "事实上，我什么都不记得，就这样出现在这里，看到她，或者说……跟在她身上。"
    by eye_def o "刚刚你在那大叫什么。吓死人啊。"
    me "谁让你一言不合就动手啊……很痛的。"
    by eye_def o "……你能感觉到痛？我的身体你也能感觉？"
    me "是啊。"
    by eye_still "……真的是附身啊。\n{size=23}这不就是背后灵……{/size}"
    by eye_def e "那，你会跟我抢身体吗？"
    me "嗯……我只是能跟你说话，看到你看到的东西，还有感受……"
    by eye_move o "你知道我是谁吗？你真的不是幻觉？不是我自己的妄想？"
    me "不，我……"
    "我的话刚说出口，又被她连珠炮似的语句打断。"
    by eye_def o "你不认识我对吧。那你又是谁？\n为什么在我脑子里，你是什么东西，什么新型病毒吗，致幻的？"
    me "……我不知道……"
    by eye_wacky o "哈？？？"
    me "我不知道啊……别的我什么都不记得，听到你的声音的时候就在这里了。"
    by eye_move e "哦……好吧。{p}我知道了，你比我还没用。"
    me "……"
    "你才没用。"
    by eye_def o "所以，你有什么是知道的。"
    me "你身上的事，难道不应该问你自己吗？"
    by eye_move e "我，呃，我也不记得……{p}不知道为什么。我明明记得之前还在家里睡觉，醒之后就在这里了。"
    "被我这么问，她没了咄咄逼人，大概是自觉理亏。"
    "她的话一出，我们双双陷入沉默。"
    "无论从哪个方面说，这事都太过超出常理，让人没有任何头绪。"
    by eye_move o "那怎么办，你不能滚——呃，你不能从我身上离开吗？"
    me "……"
    me "应该不能……你说话就不能温柔一点吗。"
    by eye_wacky o "面对你这种非要占着别人脑子的东西怎么温柔啊？"
    me "你以为我想啊？怪我有用吗？"
    by eye_still o "不怪你难道怪我自己吗？你想得美啊。"
    me "……"
    "这话……还挺有道理。\n……如果我不是那个被怪的人就更好了。"
    by eye_wacky e "不过看起来你很没用。你应该不会把我弄死吧。"
    me "……不会。准确地说，我什么都做不了。"
    "现在没有任何办法，也只能维持现状——她大概也是这么想，声音也不再那么暴躁。"
    me "嗯……我好像，就只是，必须跟在你身上。"

    scene bg_sickroom with Fade(0.5,1,0.5)
    "……"
    "花了一段时间接受现实。"
    "既然我们被强行联系在一起，至少要熟悉一下……"
    by eye_def e "啊……好吧……我知道了。"
    by eye_def o "所以……你叫什么，怎么称呼？"
    $ persistent.inputstyle = 0
    python:
        user = renpy.input("想被称呼为？", length=15)
        user = user.strip()
        renpy.save_persistent() # ensure the data will not be lost
        if not user:
            user = "喂"
    if user == "喂":
        me "……"
        by eye_still e "不想说就拉倒。无所谓。"
        by eye_def e "啊，对，就叫你“喂”好了。"
        by eye_close o "喂，你觉得，怎么样？"
        me "……哦，嗯。"
        "她自说自话很快，我也懒得解释，干脆就顺从地应声。"
    else:
        me "你可以叫我[user]。"
        by eye_still o "哦，那，你好。"

    me "……你呢？"
    by eye_wacky smile "嗯……要不，你可以叫我老板？"
    me "……"
    "这是从哪里学到的称呼……"
    "不过……"
    me "……你是不是叫白一？"
    by eye_shock o "嗯……{size=45}嗯？？！！{/size}"
    by eye_shock "你……你说什么？"
    me "我是不是说对了？"
    by eye_move e "不，没有。你想多了，你都不认识我，怎么可能知道我的名字，瞎说什么。"
    me "真的吗？我觉得我没说错啊。"
    by eye_move def "……"
    by eye_still o "……好吧。你——说得没错……但你怎么会知道？"
    me "我好像可以“看见”一些东西。"
    by eye_wacky e "哈？那是什么意思？"
    "{i}咔哒。{/i}"
    me "这很难解释，我和你看到的东西也许不一样，就像是一个屏幕——"

    scene bg_sickroom with vpunchm
    unknown "{size=45}啊——！！！！{/size}"
    $ renpy.music.play(music.shocked, loop=False, fadein=0.5)
    "巨大的尖叫声打断了我要说的话。"
    "白一转过头，而后四肢僵硬，愣在原地。"
    "不远处的门被打开——似乎是刚才对话时没注意其他声音——门后，灯光亮起，有些刺眼。"
    scene black with dissolve
    "光芒的最中间，黑洞洞的枪口对准了白一。"

    $ quick_menu = False
    stop music
    window hide
    scene bg_meetingroom with Fade(0.3,0.5,0.3,color="#000")
    window hide
    show screen tpoinfo("12月12日，星期日","城安局") with dissolve
    pause 1
    hide screen tpoinfo with dissolve
    window auto
    $ quick_menu = True
    by eye_def e "什么情况……有毛病？这些人又要干嘛啊……"
    me "不知道。不过……这里，好像是城安局。"
    me "话说，城安局是什么地方？"
    by eye_wacky o "……啊？你连城安局是什么都不知道，却知道这里就是？\n真是有够奇怪的……"
    python:
        persistent.dictList.append(("城安局","全称为城市安全管理局，顾名思义，负责处理影响到城市安全的事件。\n内部人员一般分为三个组，民案组，刑事组，特调组。"))
        persistent.dictList = list(set(persistent.dictList))
    $ renpy.sound.play(sound.dictionary, channel="dictionary", loop=False)
    $ renpy.notify ("【词典】更新")
    by eye_def e "就是{b}城市安全管理局{/b}啊，看名字就懂了吧。"
    me "哦……"
    by eye_move o "这么看，这里应该是询问室了。啧……我怎么这么倒霉。"
    "白一坐在角落的凳子上，双手紧绷着握拳，似乎意识到什么，放低了说话声音。"
    "——刚才，经过短暂的对峙后，持枪的人扣住白一的手，把她拉到这个房间。"
    "房间里只有空空荡荡的书桌和凳子，让头上的顶灯更加晃人心神。"
    by eye_move e "可能有人正在看我……我会不会被当成精神病？哦，我可能就是。"
    by eye_still o "{size=23}待会有人进来，我不能这样跟你说话……你要是真的能“看见”什么，记得告诉我。{/size}"
    "她的声音越来越小，几乎只是在喉咙口吹气。除了能感受到她身体的我，大概没人能听清。"
    me "好。"

    scene bg_meetingroom with fade
    show xpimg o at char_mid with moveinright
    xp "刚才的事很抱歉，是误会。只是我们有些问题想要问你。"
    by eye_def o "噢……好。"
    hide xpimg
    show xpimg at char_mid
    "白一突然出现在这里，还失去意识，无论怎么想都十分奇怪，对方要询问也是理所当然。"
    "况且最重要的是，无论如何，在这个地方，白一并没有反抗的能力和资格……"
    hide xpimg
    show xpimg o at char_mid
    xp "前天下午和晚上的时候，你在哪里，做什么？前天，12月10日。"
    by eye_def o "……12月10号？是……"
    "白一愣了愣，尽力含糊其辞——我知道，她是不记得之前的事情了。"
    me "今天是12月12号，星期日。\n噢，是我“看见”的。"
    "放在桌子下的右手悄悄移动，放在左臂上。白一用力按了按伤口，大概是表示听到了我的话。"
    by eye_move o "嗯，周五，我……应该在家。"
    xp "是吗？有人看到你下午经过晟欧路路口。"
    by "那——可能是我记错了……"
    me "……这好像是前天发生的事吧，又不是前年，谁会相信啊。"
    hide xpimg
    show xpimg at char_mid
    "的确，西平也只是顿了顿，而后加重语气，重复了一遍。"
    hide xpimg
    show xpimg eye_still o at char_mid
    xp "你确定吗？"
    by eye_move def "……"
    by eye_def o "好吧……其实，我好像失忆了，不记得那天发生的事情。"
    hide xpimg
    show xpimg eye_still at char_mid
    "房间里陷入沉默，但意外的是，这次对面的人并没有在第一时间驳斥白一，而是拧起了眉毛，看着白一，似乎在等她继续说下去。"
    "没得到反应，白一吞了吞口水，只好轻轻地，缓缓地吐出一口气。"
    by eye_def o "呃，就是，我只记得周四，我跟平时一样上学放学，晚上在家里睡觉。"
    by eye_still o "然后，睡着，醒来之后……就是刚才了。"
    hide xpimg
    show xpimg o at char_mid
    xp "之前的事情全部还记得，只有这两天的事忘了？"
    by eye_def e "嗯……对。就是从，那天开始。"
    xp "那么，没有发生过其他事情吗？任何不确定的细节都可以。"
    by eye_def def"……没有。"
    "短发女人没再说话，安静地坐在凳子上。"
    "正当白一开始觉得不耐烦，要开口询问时，门再次被打开，另一个长发女人走了进来。"

    scene bg_meetingroom with fade
    "和西平不同，西顺进来后就对白一露出一个安抚的笑容，看起来温柔许多。"
    "白一被轻轻拍了拍肩膀，似乎也没那么紧张了。"
    show xsimg o at char_mid with moveinleft
    xs "这位同学，知道“特调组”吗？"
    by eye_def o "……啊？"
    "面对突如其来的问题，白一显得十分疑惑，但还是老老实实地回答。"
    by eye_def o "当然知道啊。特别案件调查组……是吧。"
    python:
        persistent.dictList.append(("特调组-1","全称为特别案件调查组，是城安局的主要部门之一，负责解决已经对社会产生重大恶劣影响的事件。"))
        persistent.dictList = list(set(persistent.dictList))
    $ renpy.sound.play(sound.dictionary, channel="dictionary", loop=False)
    $ renpy.notify ("【词典】更新")
    by eye_still e "所以，是不是有什么危险的事情，跟我有关，所以你们才……？"
    xs "嗯，你说得没错，但也不完全是。不过你那么想也没问题。"
    hide xsimg
    show xsimg smile at char_mid with dissolve
    $ renpy.music.play(music.texting, loop=True, fadein=0.5)
    "西顺忽然露出一个浅笑，眼睛直勾勾盯着白一。"
    "深黑色的眸子在灯下隐约闪烁着反光，如同深邃的漩涡，摄取人的心神。"
    hide xsimg
    show xsimg o at char_mid
    xs "嗯，让我这样解释……特调组，还有另外一个名字。"
    hide xsimg
    show xsimg at char_mid
    xs "特殊怪异事件调查组。"
    python:
        persistent.dictList.append(("特调组-2","除了对外的说辞，组内更重要的任务是处理一些无法用常理解释的非正常事件，因此也称为特殊怪异事件调查组。\n更多时候，其他重大事件是作为“非正常事件”的幌子，避免大众察觉。"))
        persistent.dictList = list(set(persistent.dictList))
    $ renpy.sound.play(sound.dictionary, channel="dictionary", loop=False)
    $ renpy.notify ("【词典】更新")
    by eye_wacky def "……"
    "不知为何——也许是一种说不清楚的直觉——白一的呼吸短暂停止了一瞬间。"
    "但只是一瞬间。\n她很快又恢复气息，装作没有任何反应的样子。"
    by eye_move o "……你跟我解释这个干嘛？"
    hide xsimg
    show xsimg eye_still smile at char_mid
    xs "嗯，这个啊，意思就是——"
    show black with dissolve
    hide xsimg
    pause(0.15)
    scene cg_xs10 at cg0 with dissolve
    stop music
    xs "你，或者说，{p}在你身上的{b}那个东西{/b}——"
    show cg_xs11 at cg0 with dissolve
    xs "到底是什么？"
    
    return
