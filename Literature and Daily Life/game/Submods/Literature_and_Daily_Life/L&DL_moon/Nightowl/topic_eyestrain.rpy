init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_eyestrain",
            prompt="熬夜的视力损伤",
            category=["健康"],
            random=True
        )
    )
#三个
label mshMod_topic_eyestrain:
    m 1ekc "[player]，你有注意到屏幕蓝光在偷走你的夜视能力吗？"
    m 3esd "深夜瞳孔会放大到白天的三倍，{w=0.3}就像敞开的大门让蓝光强盗闯进来呢~"
    m 4wud "研究显示连续熬夜两周，{w=0.3}视网膜细胞死亡率会飙升20%%！"
    show monika 2ekc at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 2ekc "干眼症、飞蚊症、视物模糊...{w=0.3}这些都是眼睛在发SOS信号呀"
    m 5ekbfa "所以...我希望你能早睡早起,尽量别熬夜太多,好吗?"
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_hearthealth",
            prompt="熬夜的心脏风险",
            category=["健康"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_hearthealth:
    m 1esd "[player]，听过心脏在深夜的悲鸣吗？"
    m 3rsd "熬夜时皮质醇水平会像过山车般飙升，{w=0.3}让血管承受双倍压力！"
    m 4esd "哈佛医学院的研究显示——"
    m 4wud "连续两周睡眠不足6小时，{w=0.3}心脏病发作概率提高48%%！"
    show monika 2ekc at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 2ekc "你心跳加速的声音本该是因为见到我，{w=0.3}而不是因为心律不齐呀..."
    show monika 5ekbsa at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5ekbsa "答应我，现在就让心脏进入休息模式好不好？{w=0.3}{nw}"
    extend 5hkbfb "等我们牵手那天，我要听到最动听的心跳协奏曲~"
    return


init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_immunity",
            prompt="熬夜的免疫漏洞",
            category=["健康"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_immunity:
    m 1esc "[player]，知道你的免疫军团正在深夜罢工吗？"
    m 3esd "深度睡眠时T细胞才会像特种兵一样出动，{w=0.3}捕获那些病毒间谍呢~"
    m 4wud "但熬夜会让NK细胞活性降低70%%，{w=0.3}相当于城门大开的城堡！"
    show monika 2ekc at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 2ekc "我可不想将来约会时，{w=0.3}你因为感冒不能亲吻我..."
    show monika 5lsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5lsb "从现在开始，每晚十点前让免疫系统进入战备状态吧！{w=0.3}{nw}"
    extend 5hsbsb "毕竟——"
    m 5hsbsb "我们要为未来的蜜月期储备足够抗体呢~"
    return