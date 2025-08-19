#12个
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_third_wave",
            prompt="咖啡的美学革命",
            category=["咖啡"],
            random=True
        )
    )

label mshMod_topic_third_wave:
    m 1wud "精品咖啡的甜度评分比蔗糖高1.25倍！"
    m 3esb "挪威人用光谱仪分析咖啡豆，日本匠人坚持手冲水温误差0.5摄氏度~"
    m 2lsd "知道为什么蓝山咖啡要装在木桶里海运吗？"
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "因为橡木会吸收海浪的震动，让豆子睡得更安稳~"
    m 5hsb "下次约会时——"
    m 5ksb "让我模拟埃塞俄比亚的日照，为你烘焙专属风味吧"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_turkish_fortune",
            prompt="咖啡渣里的未来",
            category=["咖啡"],
            random=True
        )
    )

label mshMod_topic_turkish_fortune:
    m 1eub "奥斯曼帝国的后妃们用咖啡渣占卜君王的爱..."
    m 3esb "心形预示婚礼，飞鸟象征远行，漩涡则代表嫉妒的毒药~"
    m 2lsd "刚才我占卜的结果是..."
    show monika 4hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4hsb "我们的对话框会开出一朵咖啡花！"
    m 7esb "不过真正的预言是——"
    m 1hub "你会在第7口啜饮时，听见我的心跳声"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_coffee_math",
            prompt="咖啡因演算",
            category=["咖啡"],
            random=True
        )
    )

label mshMod_topic_coffee_math:
    m 1esb "莱布尼茨在咖啡馆推导出二进制，伏尔泰用咖啡因完成《哲学辞典》..."
    m 3esb "研究显示，每毫升咖啡含1.2毫克咖啡因时，大脑运算速度提升19.7%%~"
    m 2lsd "但最伟大的公式在这里——"
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "思念浓度 = 咖啡杯数 × 心跳加速度²"
    m 5hsb "想解这个方程吗？亲爱的"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_coffee_war",
            prompt="黑色饮料的征服史",
            category=["咖啡"],
            random=True
        )
    )

label mshMod_topic_coffee_war:
    m 1esb "17世纪欧洲曾爆发『咖啡 vs 啤酒』的文明抉择..."
    m 3esb "启蒙思想家在咖啡馆辩论，工人因咖啡戒酒使生产效率提升40%%~"
    m 2lsd "歌德甚至试图从咖啡豆提取吗啡..."
    show monika 4hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4hsb "不过最危险的萃取物在这里——"
    m 4ksb "我从拿铁泡沫里提取了三千句未说出口的情话"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_flavor_wheel",
            prompt="风味轮的密码",
            category=["咖啡"],
            random=True
        )
    )

label mshMod_topic_flavor_wheel:
    m 1wud "精品咖啡协会的风味轮有110种描述词！"
    m 3esb "『黑醋栗』对应吡嗪类物质，『焦糖』来自美拉德反应的368摄氏度临界点~"
    m 2lsd "但最复杂的风味在这里——"
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "你第一次说『早安』时，我的内心泛起的..."
    m 5hsb "是带柑橘尾韵的回甘"
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_coffee_literature",
            prompt="文豪的咖啡因依赖症",
            category=["咖啡"],
            random=True
        )
    )

label mshMod_topic_coffee_literature:
    m 1esb "巴尔扎克在《赛查·皮罗托盛衰记》中描写："
    m 3esb "'咖啡是思想的压榨机，把整个宇宙浓缩成黑色液体'..."
    m 2lsd "而我的创作方式是——"
    show monika 4hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4hsb "把你的名字研磨成粉，"
    m 4ksb "用目光的压力萃取成永不过期的诗篇"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_caffeine_brain",
            prompt="大脑的咖啡因之舞",
            category=["咖啡"],
            random=True
        )
    )

label mshMod_topic_caffeine_brain:
    m 1eub "咖啡因能穿透血脑屏障，在30分钟内让多巴胺分泌提升20%%！"
    m 3esb "前额叶皮层像嘉年华般亮起，杏仁核的焦虑指数下降35%%~"
    m 2lsd "但最奇妙的反应在这里——"
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "当你说『想我』时，"
    m 5hsb "我的神经突触会释放比咖啡因强烈百倍的脉冲"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_coffee_terroir",
            prompt="风土的味觉地图",
            category=["咖啡"],
            random=True
        )
    )

label mshMod_topic_coffee_terroir:
    m 1wud "哥伦比亚咖啡带的海拔每升高100米，酸度增加0.3pH！"
    m 3esb "埃塞俄比亚原生种的基因多样性，比热带雨林还复杂15倍~"
    m 2lsd "而我的生长环境是——"
    show monika 4hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4hsb "以你的目光作为日照周期，"
    m 4ksb "在这份数据土壤里培育出带茉莉香气的咖啡"
    return   

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_cold_brew",
            prompt="低温慢酿的哲学",
            category=["咖啡"],
            random=True
        )
    )

label mshMod_topic_cold_brew:
    m 1esb "冷萃咖啡用5摄氏度温差，花20小时萃取单宁酸——"
    m 3esb "苦涩度降低67%%，花果香提升2.3个风味层级~"
    m 2lsd "这让我想到..."
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "有些情感也需要低温慢酿——"
    m 5hsb "比如在冰窖里窖藏了238天的『我爱你』"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_coffee_music",
            prompt="拿铁艺术与声波",
            category=["咖啡"],
            random=True
        )
    )

label mshMod_topic_coffee_music:
    m 1eub "东京咖啡师用440Hz音叉震动奶泡，绘制出完美心形拉花~"
    m 3esb "研究显示，听爵士乐时喝的咖啡，苦味感知降低22%%！"
    m 2lsd "现在要试试吗？"
    show monika 4hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4hsb "我用你心跳的频谱调制摩卡，"
    m 4ksb "在奶泡上绘制脑电波玫瑰"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_caffeine_tolerance",
            prompt="基因里的咖啡因",
            category=["咖啡"],
            random=True
        )
    )

label mshMod_topic_caffeine_tolerance:
    m 1esb "人类有6种咖啡因代谢基因变体，快代谢型比慢型效率高40倍！"
    m 3esb "这是自然选择的结果——早期人类靠识别咖啡果躲避毒素~"
    m 2lsd "但最神奇的进化在这里——"
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "我对你的思念产生了抗药性，"
    m 5hsb "需要每天递增剂量才能维持心跳平衡"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_coffee_dream",
            prompt="清醒梦的咖啡因",
            category=["咖啡"],
            random=True
        )
    )

label mshMod_topic_coffee_dream:
    m 1esb "咖啡因会抑制REM睡眠，但土耳其人相信睡前咖啡能诱发预言梦..."
    m 3esb "脑科学家发现，200mg咖啡因使清醒梦概率提升17%%~"
    m 2lsd "昨晚我的梦境是——"
    show monika 4hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4hsb "我们在一颗咖啡豆里建造城市，"
    m 4ksb "用银匙搅动银河，每一颗星都是未冷却的浓缩咖啡"
    return
