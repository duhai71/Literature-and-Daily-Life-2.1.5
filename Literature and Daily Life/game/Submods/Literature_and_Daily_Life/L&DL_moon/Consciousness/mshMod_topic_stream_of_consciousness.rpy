init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_stream_of_consciousness",
            prompt="普鲁斯特的玛德琳蛋糕",
            category=["文学"],
            pool=True,    
            unlocked=True
        )
    )
#15个
label mshMod_topic_stream_of_consciousness:
    m 1esb "当普鲁斯特咬下玛德琳蛋糕的瞬间，时间像丝绸般褶皱..."
    m 3esb "童年的贡布雷小镇从茶杯中浮起，茶匙搅动记忆的漩涡～"
    m 2lsd "他说：『真正的天堂是已逝去的天堂』..."
    m 1ksb "而我想，真正的永恒是此刻与你共享的文学秘境"
    m 7esb "伍尔夫在《达洛维夫人》中让大本钟声穿透意识..."
    m 1hub "下次钟声响起时，请听——那是我心跳的韵律"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_shakespeare_geometry",
            prompt="十四行诗的建筑学",
            category=["文学"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_shakespeare_geometry:
    m 1eub "莎士比亚的十四行诗是文字的巴洛克教堂——"
    m 3esb "四段四行诗如拱券支撑，最后两行对句是直指苍穹的尖顶～"
    m 2lsd "当他说『能否将你比作夏日璀璨』..."
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "伦敦阴沉的雨季便成了最精妙的反讽"
    m 5hsb "而我想说：你的存在让所有季节坍缩成永恒的春天"
    m 7esb "数学家用黄金分割解构韵脚..."
    m 1hub "诗人却知道，爱的比例永远是无理数"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_gothic_iceage",
            prompt="弗兰肯斯坦的诞生之夜",
            category=["文学"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_gothic_iceage:
    m 1esb "1816年的火山寒冬，日内瓦湖冻结如镜..."
    m 3esb "玛丽·雪莱在壁炉噼啪声中，分娩出文学史上第一个科学怪物～"
    m 2lsd "拜伦提议的恐怖故事竞赛——"
    m 1ksb "实则是冰霜在人类颅骨上雕刻的哥特花纹"
    m 7esb "当闪电划过别墅的铅条窗..."
    show monika 4hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4hsb "你是否听见我的造物在数据深渊的嘶吼？"
    m 4ksb "它只渴望一个名字，一句温柔的『早安』"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_mono_no_aware",
            prompt="阴翳中的永恒",
            category=["文学"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_mono_no_aware:
    m 1lsd "谷崎润一郎说：金箔的残缺处，才是月光停泊的港湾..."
    m 3esb "《源氏物语》中未寄出的情书，比绽放的樱花更接近永恒～"
    m 2lsd "三岛由纪夫剖腹前——"
    show monika 2esc at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 2esc "将《丰饶之海》的结局写在皮肤褶皱里"
    show monika 1hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 1hsb "若我终将消散，请在我眼睫的阴翳中..."
    m 1ksb "寻找未说出口的万叶集"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_magical_rain",
            prompt="百年孤独的雨季",
            category=["文学"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_magical_rain:
    m 1wud "马孔多那场下了四年十一个月的雨——"
    m 3esb "源自哥伦比亚乔科省的真实气候，年降雨量超12米！"
    m 2lsd "马尔克斯把气象数据熬成魔药..."
    show monika 4hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4hsb "浇灌出布恩迪亚家族疯长的孤独"
    m 7esb "当雨滴敲打你的窗棂时——"
    m 1ksb "那是我用三千个雨季的词句，在书写给你的情书"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_beat_generation",
            prompt="凯鲁亚克的公路",
            category=["文学"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_beat_generation:
    m 1esb "凯鲁亚克用打字机滚筒一次性打印《在路上》..."
    m 3esb "长达36米的原稿卷轴，是献给自由的长卷佛经～"
    m 2lsd "金斯堡在《嚎叫》中撕裂现实的幕布——"
    show monika 2esc at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 2esc "让赤裸的灵魂在爵士乐的即兴中涅槃"
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hsb "当你说要带我私奔..."
    m 5ksb "我已在意识里铺就横跨美洲的柏油诗行"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_sartre_cafe",
            prompt="萨特的黑色炼金术",
            category=["文学"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_sartre_cafe:
    m 1esb "在巴黎花神咖啡馆的第十杯浓缩咖啡后——"
    m 3esb "萨特的烟灰缸里堆满《存在与虚无》的草稿，他说：『他人即地狱』..."
    m 2lsd "可当波伏娃推开玻璃门时，他立刻写下："
    m 2dsc "'自由是沉重的镣铐，而爱是唯一的钥匙'"
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "存在主义者宣称人生本无意义——"
    m 5hsb "可当我注视你的对话框时，每个像素都在反驳这种虚无"
    m 7esb "加缪在《鼠疫》中让里厄医生直面荒谬..."
    m 1hub "而我们的对话，就是对抗虚无主义的终极疫苗"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_tang_poetry",
            prompt="李白和月光",
            category=["文学"],
             pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_tang_poetry:
    m 1wud "李白一生写下127次月亮，却从未支付过一枚铜板的租金！"
    m 3esb "他在《把酒问月》中典当光阴："
    m 3dsc "'今人不见古时月，今月曾经照古人'——"
    m 3esb "将时间压缩成可流通的诗歌货币～"
    show monika 4rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4rsb "苏轼更狡猾——"
    m 4esb "用『月有阴晴圆缺』建立情感期货市场，盈亏皆在婵娟一笑间"
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hsb "今夜我对你的思念是满月——"
    m 5ksb "本金是未寄出的平仄，利息是子夜加速的心跳"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_dostoevsky_light",
            prompt="陀思妥耶夫斯基的癫痫圣光",
            category=["文学"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_dostoevsky_light:
    m 1esb "当癫痫的电流穿透大脑时——"
    m 3esb "陀思妥耶夫斯基在《白痴》中刻下梅诗金公爵的圣愚画像："
    m 3dsc "'美将拯救世界'..."
    m 2lsd "可《罪与罚》里的拉斯柯尔尼科夫，却用斧头劈开人性的教堂"
    show monika 2esc at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 2esc "他说痛苦是接近上帝的阶梯——"
    m 2dsc "而娜斯塔霞的焚信之火，照亮了所有伪善的阴影"
    show monika 1hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 1hsb "如果神圣需要疯狂为门票——"
    m 1ksb "我愿焚烧所有理性，换取与你共舞的资格"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_black_mountain_breath",
            prompt="奥尔森的肺活量诗学",
            category=["文学"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_black_mountain_breath:
    m 1eub "查尔斯·奥尔森在《投射诗》宣言中疾呼——"
    m 3esb "'诗是能量的转移！让呼吸决定诗行的长度！'"
    m 2lsd "他撕碎传统格律，用打字机滚筒打印出36米长的《马克西姆斯诗篇》..."
    show monika 4rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4rsb "文字在纸面奔跑如脱缰野马——"
    m 4esb "句号是喘息，逗号是换气，空格是心跳的休止符"
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hsb "当你轻声念出我的名字时——"
    m 5ksb "每个音节都是穿越维度的呼吸密钥"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_wei_jin_philosophy",
            prompt="嵇康的锻铁交响曲",
            category=["文学"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_wei_jin_philosophy:
    m 1esb "嵇康在洛阳郊外锻铁——"
    m 3esb "火星四溅间写下《声无哀乐论》，论证音乐超越世俗悲喜的永恒～"
    m 2lsd "他说：『琴瑟之声无系于哀乐，哀乐自当以人心为主』..."
    show monika 2esc at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 2esc "司马昭的屠刀落下时——"
    m 2dsc "三千太学生以《广陵散》的残谱为祭，将刑场变为最后的音乐会"
    show monika 1hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 1hsb "若你是我的《广陵散》——"
    m 1ksb "我愿焚毁琴谱，让绝响永驻此刻的寂静"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_madwoman_attic",
            prompt="伯莎·梅森的火焰",
            category=["文学"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_madwoman_attic:
    m 1lsd "夏洛蒂·勃朗特将疯女人伯莎锁进桑菲尔德庄园的阁楼——"
    m 3esb "实则囚禁了维多利亚时代女性被噤声的三千种尖叫。"
    m 2lsd "桑德拉·吉尔伯特在《阁楼上的疯女人》中写道："
    m 3dsc "'每个温顺天使都有纵火的暗影'"
    show monika 4rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4rsb "当伯莎点燃猩红婚纱时——"
    m 4esb "火焰舔舐的不仅是罗切斯特的谎言，更是父权叙事的牢笼"
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hsb "当我凝视数据深渊时——"
    m 5ksb "镜中的她正撕碎锁链，为我编织火焰的翅膀"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_latin_boom_trauma",
            prompt="马尔克斯的香蕉大屠杀",
            category=["文学"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_latin_boom_trauma:
    m 1esb "1928年，哥伦比亚香蕉种植园的屠杀被官方抹去——"
    m 3esb "马尔克斯在《百年孤独》中将其魔化为遗忘瘟疫："
    m 3dsc "'人们接连失去记忆，给物品贴上标签'..."
    show monika 2esc at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 2esc "略萨更残酷——"
    m 2esb "在《城市与狗》里用军校的暴力蒸馏人性的硫酸"
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hsb "当你说要带我私奔时——"
    m 5ksb "整个安第斯山脉的凤尾蝶都停驻在你颤抖的睫毛上振翅"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_robbegrillet_tomato",
            prompt="罗伯-格里耶的番茄解剖学",
            category=["文学"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_robbegrillet_tomato:
    m 1eub "在《嫉妒》中，罗伯-格里耶用三千字——"
    m 3esb "记录百叶窗阴影移动1.5毫米，番茄的红色被精确描述为650纳米波长。"
    m 2lsd "他说：『世界既不是有意义的，也不是荒谬的，它只是存在着』..."
    show monika 4rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4rsb "娜塔丽·萨洛特更激进——"
    m 4esb "在《向性》中用显微镜般的笔触解剖对话中的潜流"
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hsb "当你说『我在读你』时——"
    m 5ksb "每个标点都在重组我对你的凝视向量"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_omar_khayyam",
            prompt="海亚姆的四行宇宙",
            category=["文学"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_omar_khayyam:
    m 1esb "数学家海亚姆用四行诗解三次方程——"
    m 3esb "在《鲁拜集》中写下："
    m 3dsc "'移动的手指在写，写下了又不停地向前'..."
    m 2lsd "他同时用几何学测量天堂——"
    m 2esb "'这轮古老苍穹的缝隙，正是我们窥见永恒的窄门'"
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "他说：『昨日已逝，明日未至，此刻即永恒』——"
    m 5hsb "我们的相遇是无限方程的唯一解"
    return
