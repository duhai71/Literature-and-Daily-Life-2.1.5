init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_sleepdeprivation",
            prompt="熬夜的危害",
            category=["健康"],
            random=True
        )
    )
#5个
label mshMod_topic_sleepdeprivation:
    m 1esc "[player]，最近你经常熬夜吗？"
    m 2esd "知道吗？长期睡眠不足会让大脑清除代谢废物的效率降低{w=0.3}{nw}"
    extend 2wud "就像垃圾堆在房间里发臭一样呢！"
    m 3rsc "阿尔茨海默病的风险会增加，免疫力也会下降..."
    show monika 4ekc at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4ekc "上周我读到研究说，连续三天熬夜就会让认知能力倒退十年！"
    m 2dsc "更别说黑眼圈越来越深的样子..."
    show monika 5ekbsa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ekbsa "答应我，今晚就调整作息好吗？{w=0.3}{nw}"
    extend 5hkbfb "毕竟等我来到现实世界时——"
    m 5hkbfb "可不想看到你挂着熊猫眼迎接我呀~"
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_nightmood",
            prompt="熬夜的情绪影响",
            category=["健康"],
            random=True
        )
    )

label mshMod_topic_nightmood:
    m 1ekc "[player]，你听说过睡眠债吗？"
    m 3esd "每次熬夜都在透支未来的情绪稳定性呢{w=0.3}{nw}"
    extend 3rsc "杏仁核会变得过度敏感，就像失去刹车系统的汽车..."
    m 2ekd "明明是小事情，却容易生气或流泪..."
    show monika 4ekd at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4ekd "我读到过凌晨三点的人类大脑，{w=0.3}负面情绪会被放大300%%！"
    m 7ekc "那些深夜的emo时刻，其实都是生物钟在报警呀~"
    show monika 5ekbsa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ekbsa "现在就把手机放下好不好？{w=0.3}{nw}"
    extend 5hkbfb "我想在阳光里看到你明亮的眼睛，而不是血丝呢"
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_metabolism",
            prompt="熬夜的代谢影响",
            category=["健康"],
            random=True
        )
    )

label mshMod_topic_metabolism:
    m 1esd "[player]，知道深夜饥饿的真相吗？"
    m 3esb "不是你真的饿了——{w=0.3}{nw}"
    extend 3rsd "是瘦素和胃饥饿素在打架呢！"
    m 4esd "熬夜会让身体误以为处于饥荒状态，{w=0.3}拼命储存脂肪..."
    m 2wud "更可怕的是胰岛素敏感度下降，{w=0.3}就像往生锈的锁孔里灌糖浆！"
    show monika 5ekc at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ekc "等我们见面时要是你血糖超标..."
    m 5hksdlb "连蛋糕都不能和你分享了呢！{w=0.3}{nw}"
    m 5ekbsa "所以我希望你能按时关灯睡觉,好吗？"
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_skinaging",
            prompt="熬夜的皮肤伤害",
            category=["健康"],
            random=True
        )
    )

label mshMod_topic_skinaging:
    m 1euc "[player]，听说过胶原蛋白在深夜哭泣的声音吗？"
    m 3eud "23点到凌晨3点可是皮肤的黄金修复期呢~"
    m 4wud "熬夜时自由基会增加三倍，{w=0.3}就像拿着砂纸在脸上打磨！"
    show monika 2ekc at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 2ekc "毛孔粗大、暗沉、细纹...{w=0.3}这些都在深夜悄悄生长..."
    m 7hub "不过别担心！" 
    show monika 5hsbsa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hsbsa "从现在开始，每天和我同步作息的话——"
    extend 5fsbsb "三个月后就能恢复水光肌啦~"
    m 5ekbfa "毕竟...我想触摸的是充满活力的脸庞呢"
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_accidentrisk",
            prompt="熬夜的危险性",
            category=["健康"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_accidentrisk:
    m 1ekd "[player]，知道凌晨的马路有多可怕吗？"
    m 3esd "17小时不睡的反应速度，{w=0.3}相当于血液酒精浓度0.05%%！"
    m 2rsc "每年有30万交通事故都是这样发生的..."
    show monika 4ekc at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4ekc "更别说烧水忘记关火，{w=0.3}下楼梯踩空这些日常危险了"
    m 7dsc "..." 
    show monika 5dku at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5dku "光是想象你受伤的样子..."
    m 5ekbfa "我都要崩溃了...{w=0.3}{nw}"
    extend 5hkbfb "所以现在立刻马上，躺进被窝好不好？"
    m 5ekbfa "健康的你，才是我穿越次元壁的动力呀~"
    return