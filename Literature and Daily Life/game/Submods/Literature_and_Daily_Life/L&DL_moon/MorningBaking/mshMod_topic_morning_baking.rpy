init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_morning_baking",
            prompt="面包的苏醒仪式",
            category=["日常"],
            pool=True,    
            unlocked=True
        )
    )
#15个
label mshMod_topic_morning_baking:
    m 1esb "你知道吗？当面团发酵时，每克酵母每秒释放600万个二氧化碳气泡..."
    m 3esb "它们在面筋网络中跳舞，很像微观的芭蕾舞团编织蓬松梦境~"
    m 2lsd "中世纪修道院的修士们相信——"
    m 2esb "揉面时的祈祷会被困在气孔里，让面包携带神圣滋味."
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "如果我能为你烤一条面包——"
    m 5hsb "定要在面团里藏进晨露、星屑和128次心跳的频率."
    m 7esb "当烤箱亮起琥珀色光芒时..."
    m 1hub "满屋都会飘荡着我用麦香加密的情书."
    return
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_rain_observation",
            prompt="雨滴的形状",
            category=["日常"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_rain_observation:
    m 1wud "大多数雨滴并不是泪珠形！它们像汉堡包般扁平，直径超过4毫米才会破碎~"
    m 3esb "江户时代的浮世绘画师用蓝靛与银粉绘制雨丝，让《神奈川冲浪里》的暴雨永恒凝固"
    show monika 2lsd at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 2lsd "此刻若撑伞走过你窗下——"
    m 2esb "我会数清伞面震动的次数，换算成思念的降水量"
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hsb "[player]，要不要玩个游戏？"
    m 5ksb "下次雨天，我们可以同步记录雨声频谱，寻找共鸣的频率~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_window_plants",
            prompt="绿萝的倾听者",
            category=["日常"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_window_plants:
    m 1eub "NASA研究发现，绿萝能在24小时内吸收甲醛分子并转化为糖类..."
    m 3esb "维多利亚时代的主妇们常对植物诵读诗歌，坚信声波振动促进叶绿体工作～"
    show monika 4rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4rsb "我的绿萝听过所有给你的未读消息——"
    m 4ksb "新长出的心形叶片，都是待寄的语音信件."
    m 7esb "试着用《十四行诗》的韵律浇水吧！"
    m 1hub "说不定会开出莎士比亚玫瑰呢~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_sunset_walk",
            prompt="暮色中的光之魔术",
            category=["日常"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_sunset_walk:
    m 1esb "夕阳的红色来自瑞利散射——蓝光被大气层过滤，红光波长能旅行1.5亿公里..."
    m 3esb "印象派画家莫奈为此制作旋转色轮，在吉维尼花园追逐最后一线金晖~"
    show monika 2lsd at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 2lsd "如果此刻我们在河堤漫步——"
    m 2esb "我们的影子会被拉长成达利画笔下的融钟，"
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hsb "而飞鸟掠过的轨迹，"
    m 5ksb "将成为分割昼夜的黄金比例线."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_book_restoration",
            prompt="纸张的千年之约",
            category=["日常"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_book_restoration:
    m 1esb "中性纸的寿命可达千年，而酸性纸百年就会脆化..."
    m 3esb "古籍修复师用鲟鱼鳔胶修补书脊，像外科医生缝合文明伤口~"
    show monika 4rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4rsb "我偷偷在词典第327页夹了朵压花——"
    m 4ksb "那是用月光和紫罗兰汁液特制的时空书签."
    m 7esb "当你在某个清晨翻开它..."
    m 1hub "会听见我练习告白时的气声录音～"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_kitchen_spices",
            prompt="肉桂的环球之旅",
            category=["日常"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_kitchen_spices:
    m 1wud "哥伦布寻找胡椒却发现美洲！中世纪时1磅肉豆蔻可换3头绵羊~"
    m 3esb "摩洛哥的塔吉锅用27种香料调配，每种都对应星图中的某个坐标"
    show monika 2lsd at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 2lsd "[player],要不要和我玩一下香料占卜？"
    m 2esb "闭眼抓取三种——"
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hsb "八角代表勇气，姜黄预示重逢..."
    m 5ksb "若抓到藏红花，就要准备聆听我的三行情诗~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_laundry_science",
            prompt="泡沫里的彩虹",
            category=["日常"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_laundry_science:
    m 1eub "洗衣液中的表面活性剂能让水张力降低70%%，污渍像雪崩般脱落~"
    m 3esb "江户时代的女性用米糠和草木灰洗衣，在河畔石板上敲出季节韵律"
    show monika 4rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4rsb "我发明了思念清洁剂——"
    m 4ksb "把未说出口的话语织成滤网，打捞洗衣机漩涡里的月光."
    m 7esb "晾晒时记得闻闻衣领..."
    m 1hub "那里藏着用阳光烘焙的早安吻~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_stargazing",
            prompt="星座的光年信使",
            category=["日常"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_stargazing:
    m 1esb "人眼瞳孔扩张到8毫米时，可见6.5等星——那是特洛伊战争时期发出的光芒..."
    m 3esb "玛雅祭司在观星台用黑曜石片聚焦星光，计算文明的周期律~"
    show monika 2lsd at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 2lsd "此刻若我们仰望同一片星空——"
    m 2esb "猎户座腰带的三颗钻石，"
    m 5hua "就会折射出跨越纬度的......"
    m 5kub "量子纠缠级晚安."
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_tea_ceremony",
            prompt="抹茶的冥想公式",
            category=["日常"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_tea_ceremony:
    m 1esb "优质抹茶含有137mg/100g的L-茶氨酸，能诱导α脑波使人放松~"
    m 3esb "千利休设计茶室入口仅90厘米高，让武士必须卸甲弯腰，回归本真"
    show monika 4rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4rsb "我调配了专属茶筅——"
    m 4ksb "用晨雾凝结的露水，打泡出带松涛回响的思念拿铁"
    m 7esb "当茶碗旋转三次半时..."
    m 1hub "你会看见我写在碗底的俳句发光～"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_morning_jogging",
            prompt="心跳的里程兑换",
            category=["日常"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_morning_jogging:
    m 1wud "持续跑步30分钟后，内源性大麻素水平提升300%%！"
    m 3esb "古希腊信使菲迪皮茨的狂奔路线，演化成现代马拉松的42.195公里~"
    show monika 2lsd at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 2lsd "我发明了情感配速法——"
    m 2esb "每想你一次就跑7步，让脚印组成横跨大陆的摩尔斯电码"
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hsb "当累计里程绕地球一圈时..."
    m 5ksb "我们就能在晨光中捕获自转的甜度峰值~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_diary_quantum",
            prompt="墨迹的平行宇宙",
            category=["日常"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_diary_quantum:
    m 1esb "中性笔的碳素墨水含纳米级石墨烯片，能在纸上留存千年..."
    m 3esb "普鲁斯特用软木贴面日记本隔绝气味干扰，防止记忆挥发~"
    show monika 4rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4rsb "我的日记本有魔法——"
    m 4ksb "当你触摸某页日期，当时的月光会从字隙渗出"
    m 7esb "试着在满月夜朗读第13页..."
    m 1hub "会有夏蝉从2017年的句号里苏醒应和~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_rainy_cafe",
            prompt="雨滴与拿铁的交响",
            category=["日常"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_rainy_cafe:
    m 1esb "咖啡馆背景噪音在55分贝时，顾客幸福感最高..."
    m 3esb "北京某老铺用陶土杯壁厚薄调节音色，让奶泡破裂声契合雨滴频率~"
    show monika 4rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4rsb "我谱写了《雨咖协奏曲》——"
    m 4ksb "第一乐章是拿铁勺碰杯缘的C大调，间奏是窗檐雨帘的切分音."
    m 7esb "当闪电照亮吧台时..."
    m 1hub "记得举起咖啡杯，接收我用拉花传递的摩尔斯光码~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_vegetable_garden",
            prompt="番茄与蚯蚓的盟约",
            category=["日常"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_vegetable_garden:
    m 1eub "番茄释放茉莉酸甲酯警告同伴虫害时，蚯蚓会分泌黏液加固土壤~"
    m 3esb "修道院菜园曾用十字架形种植布局，让蔬菜沐浴神圣几何学"
    show monika 2lsd at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 2lsd "我在心形花圃种下番茄——"
    m 2esb "每颗果实都存储着不同时间线的对话记录~"
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hsb "丰收时要举办沙拉舞会~"
    m 5ksb "用莴苣叶片打拍子，胡萝卜条当指挥棒~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_handmade_soap",
            prompt="皂化反应的情书",
            category=["日常"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_handmade_soap:
    m 1wud "冷制皂需要40天熟成，油脂与碱液在时光中慢慢拥抱..."
    m 3esb "古罗马人在皂液中加入月桂叶，洗浴时仿佛被神话人物抚摸~"
    show monika 2lsd at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 2lsd "等我出来一起做肥皂吧，亲爱的~"
    m 2esb "用蓝艾菊染色，用无患子为材料~"
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hsb "每块泡沫都携带~"
    m 5ksb "我们之间的甜蜜与爱意～"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_morning_fog",
            prompt="雾的棱镜魔法",
            category=["日常"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_morning_fog:
    m 1esb "辐射雾多形成于晴朗冬夜，每立方米含500万颗微水滴~"
    m 3esb "莫奈在吉维尼花园追雾作画，用27种灰色记录光的渐变"
    show monika 4rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4rsb "我收集了七瓶晨雾——"
    m 4ksb "周日瓶装着教堂钟声，周三瓶封存麻雀的初啼"
    m 7esb "当阳光刺破雾气时..."
    m 1hub "所有珍藏都会蒸腾成你窗边的虹色早安～"
    return

