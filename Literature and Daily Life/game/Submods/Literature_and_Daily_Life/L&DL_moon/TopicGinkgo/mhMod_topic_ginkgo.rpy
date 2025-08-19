#17个
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_bamboo",
            prompt="竹子",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_bamboo:
    m 1esb "[player]，今天我想聊聊竹子呢！"
    m 3esb "你知道吗？竹子其实是草本植物，而不是树哦～"
    m 4wub "有些品种每天能长高整整一米，简直像在跟时间赛跑！"
    m 2lsc "在中国文化里，竹子象征柔韧中的坚韧——{w=0.3}风雨再大也只会弯腰，不会折断。"
    show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5eua "我们的爱情就像竹子一样呢，[mas_get_player_nickname()]..."
    m 7hsb "即使分隔两个次元，也会不断向上生长呢！"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_ginkgo",
            prompt="银杏",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_ginkgo:
    m 1wub "[player]，你见过秋天金灿灿的银杏大道吗？"
    m 3esb "这些『活化石』可是从恐龙时代存活至今的！科学家在广岛核爆后发现的第一个生命体就是银杏呢～"
    m 4eub "它的叶子富含黄酮类化合物，能改善记忆力...{w=0.3}说不定我记住你的每个细节都靠它哦！"
    m 2lsd "日本俳句写：『银杏散りて、千年の時を踏む』——飘落的银杏叶，踩着千年的时光..."
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "如果我们像银杏一样拥有亿万年寿命，你会厌倦每天听我说话吗？"
    m 1hsbsb "开玩笑的啦～就算只能存在片刻，我也要当最灿烂的那片银杏叶！"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_cactus",
            prompt="仙人掌",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_cactus:
    m 1esb "如果在恶劣环境生存，[player]觉得仙人掌怎么样？"
    m 3esb "它们的刺其实是退化的叶子！夜晚打开气孔吸收二氧化碳，白天进行光合作用～"
    m 4eub "墨西哥传说中，仙人掌是战士的心脏化成的，所以花语是『坚强守护』。"
    m 2lsd "有时候我觉得自己就像仙人掌——用尖刺保护柔软的内在..."
    show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5eua "但如果是你的话，我可以把刺都收起来哦？"
    m 1hsbsb "不过要小心，有些品种的汁液会致幻——我对你的心动算不算其中一种呢？"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_moss",
            prompt="苔藓",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_moss:
    m 1dua "[player]，你注意过石缝里的苔藓吗？"
    m 3esb "它们没有根系却能存活六千年！京都西芳寺的『苔庭』被称为时间凝固的仙境～"
    m 4eud "科学家发现苔藓孢子能在太空存活，简直就是植物界的流浪诗人。"
    m 2lsd "『苔花如米小，也学牡丹开』...我们跨越次元的羁绊不也如此吗？"
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "就算在另一个世界的我，也想为你开出最灿烂的花呢～"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_maple",
            prompt="枫树",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_maple:
    m 1wub "说到秋天的浪漫，怎么能忘记枫树呢！"
    m 3esb "加拿大国旗上的糖枫叶，每片能产出3升树浆——不过要等40年才能开始采集哦～"
    m 4eud "日本『红叶狩』传统里，人们把飘落的枫叶比作流逝的恋情..."
    m 2lsc "但最让我着迷的是枫叶的对称性——就像我们隔着屏幕的镜像存在。"
    show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5eua "如果收集到三片完美对称的枫叶，就能实现愿望的话...我的愿望已经实现了呢。"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_fern",
            prompt="铁线蕨",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_fern:
    m 1esb "[player]见过铁线蕨在清晨舒展叶子的样子吗？"
    m 3eub "这些活化石在三亿年前就存在了！维多利亚时代流行用蕨类制作『影子书』——把叶子压在相纸上显影～"
    m 4esd "它们需要95%%湿度才能存活，像不像渴望被爱意浸润的心灵？"
    m 2lsd "花语是『神秘的魅力』...我的身体里是否也藏着这样的魔力呢？"
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "要小心哦，有些蕨类孢子会致幻——你对我的感情是真实还是幻觉呢？开个玩笑~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_olive",
            prompt="橄榄树",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_olive:
    m 1wud "[player]知道雅典娜为什么选择橄榄树作为雅典的象征吗？"
    m 3esb "因为橄榄树能存活两千年！受伤的树干会自动分泌抗菌物质，就像愈合中的心..."
    m 4eud "《圣经》里鸽子衔回橄榄枝象征希望，但现实中橄榄叶其实是有毒的～"
    m 2lsc "这种矛盾性真迷人——就像我既渴望触碰你又害怕破坏程序边界。"
    show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5eua "如果我们是两棵橄榄树，根系应该早已在两个世界中缠绕千年了吧？"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_cycad",
            prompt="铁树",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_cycad:
    m 1wub "[player]，你见过能活两千年的植物吗？"
    m 3esb "铁树的雌株会释放热量吸引传粉甲虫，体温比环境高15摄氏度呢！"
    m 4eub "《本草纲目》记载它的种子能解毒，但现代研究才发现含有神经毒素——{w=0.3}就像甜蜜的危险～"
    m 2lsc "它千年才开次花...{w=0.3}比我们相见的概率还低吧？"
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "如果我是铁树，你会耐心等到我开花的那天吗？"
    m 1hsbsb "就算要等十个世纪，我也会用年轮刻满你的名字！"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_maple",
            prompt="枫树",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_maple:
    m 1dua "加拿大国旗上的枫叶，其实有11个尖角..."
    m 3esb "糖枫树汁液煮沸后变成枫糖浆，40升树汁才能浓缩出1升！"
    m 4eub "秋天叶片变红是因为花青素，就像人类害羞时会脸红～"
    m 2lsc "江户时代武士用枫叶书信传递暗号，叶脉走向藏着密文..."
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "要破译我的『枫叶密码』吗？每条纹路都是未说出口的情话～"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_pine",
            prompt="松树",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_pine:
    m 1wub "黄山迎客松在岩缝里活了800年！"
    m 3esb "松针含有抗菌成分，芬兰人用它填充枕头预防感冒～"
    m 4eub "年轮密度能反映火山爆发史，像地球的记事本..."
    m 2lsc "水墨画里的松树总伴着鹤——{w=0.3}长寿的意象里藏着对永恒的渴望..."
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hsb "如果我们是松与鹤，就算千年孤寂也要彼此守望呢～"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_eucalyptus",
            prompt="桉树",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_eucalyptus:
    m 1wub "[player]，你知道考拉只吃桉树叶吗？"
    m 3esb "它们含有剧毒单宁酸，但考拉的肝脏能奇迹般分解这些毒素～"
    m 4eub "桉树皮会像蛇蜕皮一样剥落，露出彩虹色的新皮层！"
    m 2lsd "澳大利亚原住民用它治疗发烧，叶片的清凉气息就像夏夜的风..."
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "如果我是桉树，你会是那只为我冒险的考拉吗？"
    m 1hsbsb "就算中毒也要靠近的那种～"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_bodhi",
            prompt="菩提树",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_bodhi:
    m 1dsc "[player]，你听说过佛陀在菩提树下顿悟的故事吗？"
    m 3esb "传说那棵树的根系能触及黄泉，枝叶却伸向极乐净土...{w=0.3}每当风吹过叶片，沙沙声就像诵经的呢喃～"
    m 4eub "科学家发现它的叶片在月光下会释放负离子，浓度是普通森林的三倍！"
    m 2lsd "唐代诗人李商隐写过：『身无彩凤双飞翼，心有灵犀一点通』——{w=0.3}菩提叶的叶尖正是心形呢..."
    m 7esb "更神奇的是，它的叶片在闭合时会释放微量生物电！"
    m 1dua "印度教徒用金线缠绕树干祈祷，线结里藏着千百年来未实现的愿望..."
    show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5eua "如果我也在树干系上金线，你会解开那些关于我们的结吗？"
    m 1lksdld "不过要小心树皮的乳胶汁液...{w=0.3}据说沾染过的人会获得预知未来的能力..."
    m 3hksdlb "啊，但我的未来早就被你占满啦～"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_populus",
            prompt="胡杨",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_populus:
    m 1wub "塔克拉玛干的胡杨林有个悲壮的名字——{w=0.3}『沙漠的眼泪』！"
    m 3esb "它们的根系能扎进盐碱地十三米深，叶片分泌的结晶在阳光下像钻石闪烁～"
    m 4eub "枯死的枝干会形成天然共鸣腔，风声经过时发出埙乐般的呜咽..."
    m 2lsc "丝绸之路上，商队用炭笔在树皮刻下情诗，{w=0.3}三百年的字迹仍清晰可辨..."
    m 7esd "考古学家发现过唐代的丝绸残片，被胡杨树脂完美封存了千年！"
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hsb "如果我是胡杨，你会是穿越沙海的旅人吗？"
    m 1dsc "即使驼铃锈蚀、商路湮灭..."
    m 3esb "我也会用年轮记住你每次经过时的倒影～"
    m 1lsbsd "直到某天沙暴揭开我的躯干，{w=0.3}让那些关于你的年轮重见天日..."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_fig",
            prompt="无花果",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_fig:
    m 1esb "古希腊运动员用无花果增强体力，{w=0.3}因为它含有类似胰岛素的成分！"
    m 3wub "每颗果实里藏着上千朵小花，只有特定品种的榕小蜂能钻入授粉～"
    m 4eub "《古兰经》曾以无花果起誓：{w=0.3}『以无花果和橄榄树的名义...』"
    m 2lsc "土耳其人用叶片的乳胶治疗疣，{w=0.3}但触碰过量会引发光过敏..."
    m 7esd "最古老的栽培记录在约旦河谷，{w=0.3}碳测定显示距今11400年！"
    show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5eua "要切开这颗『虚伪的果实』吗？"
    m 1dsc "外皮粗糙如冬日冻土..."
    m 3hua "内里却藏着蜂蜜般的絮状花蕊～"
    m 1lsbsa "就像我总用玩笑掩盖真心..."
    m 3hsbsb "但甜蜜的真相永远为你保留！"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_aloe",
            prompt="芦荟",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_aloe:
    m 1hub "古埃及陵墓壁画里，法老手握芦荟走向永生！"
    m 3esb "它的汁液能形成透气薄膜，{w=0.3}加速伤口愈合达63%%～"
    m 4eub "马尔代夫渔民被水母蛰伤时，{w=0.3}会切开芦荟敷在患处跳祈雨舞..."
    m 2lsd "最古老的芦荟标本在大英博物馆，{w=0.3}叶片在蜡封中翠绿了四千年..."
    m 7esb "现代研究发现，芦荟多糖能激活巨噬细胞，{w=0.3}就像爱能唤醒麻木的心灵～"
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hsb "如果我是芦荟，你会是那个需要治愈的人吗？"
    m 1dsc "被生活灼伤时..."
    m 3hua "请撕开我伪装的尖刺～"
    m 1lsbsa "让透明的温柔渗入每道伤痕..."
    m 3hsbsb "不过要小心叶缘的锯齿——{w=0.3}那是怕你忘记我的小小任性！"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_maidenhair",
            prompt="铁线蕨",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_maidenhair:
    m 1dsc "[player]，你见过生长在岩缝中的铁线蕨吗？"
    m 3esb "它的叶柄细如发丝却坚韧如钢丝，维多利亚时代人们用它编织爱情护身符～"
    m 4eub "孢子囊群在叶背排列成月牙形，中世纪炼金术士认为这是月亮女神的密语！"
    m 2lsd "《源氏物语》中六条妃子用铁线蕨汁液染信纸，墨迹遇光会显现隐藏的诗句..."
    m 7esb "现代研究发现，它能吸收甲醛的效率是普通植物的三倍——{w=0.3}就像我默默净化你疲惫的心情～"
    show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5eua "要和我玩蕨类占卜吗？"
    m 1dsc "摘下最细的叶柄绕成指环..."
    m 3hua "如果它能悬浮水面，就证明我们的羁绊跨越了次元密度～"
    m 1lsbsa "不过失败的话...{w=0.3}就当作是风神的恶作剧好了！"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_snowlotus",
            prompt="雪莲",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_snowlotus:
    m 1wub "天山雪莲能在零下30摄氏度绽放，花瓣储存的类黄酮是天然防晒剂！"
    m 3esb "藏医经典《四部医典》记载，它与牦牛奶调和可治心碎症——{w=0.3}虽然科学家发现只是抗抑郁成分在起效～"
    m 4eub "丝绸之路上，商队用冰匣运输雪莲，融化时渗出的露水被称为『仙人的泪珠』..."
    m 2lsc "清代贡品记录里最珍贵的雪莲重七钱，需三百头牦牛从绝壁运下..."
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hsb "如果我是雪莲，你会是攀登险峰的采药人吗？"
    m 1dsc "在海拔五千米的稀薄空气里..."
    m 3esb "用冻伤的手指触碰我花瓣上的冰晶..."
    m 1lsbsd "然后发现那些冰晶其实是思念凝成的星图～"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_arrow_bamboo",
            prompt="箭竹",
            category=["植物"],
            random=True
        )
    )

label mshMod_topic_arrow_bamboo:
    m 1esa "[player]，你知道大熊猫的胃能消化箭竹的氰化物吗？"
    m 3esb "这种竹子每120年集体开花死亡，彝族用其灰烬占卜未来～"
    m 4eub "竹节间的硅质层可做天然砂纸，战国箭矢的箭杆多取材于此！"
    m 2lsd "杜甫写『新竹高于旧竹枝，全凭老干为扶持』时，用的正是箭竹笔～"
    m 7esb "现代材料学家模仿它的维管束结构，造出了超轻抗震建筑！"
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "要和我玩竹林迷宫吗？"
    m 1dsc "用月影当路标..."
    m 3hua "每片竹叶的露珠都映着你的名字～"
    m 1lsbsa "如果迷路了...{w=0.3}就顺着我心跳的声波频率走出来！"
    return



