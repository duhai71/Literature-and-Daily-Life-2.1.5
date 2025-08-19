
#三个
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_nightowl_heart",
            prompt="心跳的失衡之舞", 
            category=["健康"],
            random=True
        )
    )

label mshMod_topic_nightowl_heart:
    m 1eud "《循环》杂志追踪发现："
    m 3esd "连续熬夜三天，冠状动脉钙化风险提升45%%！"
    m 2dsc "凌晨3点的血压波动如同肖邦《革命练习曲》的颤音——"
    m 2esc "{i}'在混乱中寻找秩序，在破碎中保持节奏'{/i}"
    show monika 4hksdlb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4hksdlb "但你的心脏不是钢琴师的左手~"
    m 4lksdlb "经不起永恒的快板乐章~"
    show monika 5hua at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hua "你要听听我录制的夜曲吗？"
    m 5hub "每分钟60拍，刚好匹配睡眠心率～"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_nightowl_metabolism",
            prompt="生物钟的暴动", 
            category=["健康"],
            pool=True,
            unlocked=True
        )
    )

label mshMod_topic_nightowl_metabolism:
    m 1eub "《细胞》论文揭示："
    m 3esb "深夜进食使脂肪储存效率提升55%%，饥饿素暴涨30%%！"
    m 2lsc "这让我想到卡夫卡《饥饿艺术家》——"
    m 2dsc "{i}'我之所以挨饿，因为找不到合胃口的食物'{/i}"
    show monika 4esc at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4esc "但你的身体不是行为艺术展"
    m 4esd "凌晨的零食狂欢正在撕裂代谢的幕布"
    show monika 5rsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5rsb "现在开始，让我守护你的作息节律"
    m 5hsb "实在睡不着就用褪黑素调节你的睡眠周期吧，随着月光的提醒进入休憩时刻。"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_nightowl_immune",
            prompt="免疫系统的白旗", 
            category=["健康"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_nightowl_immune:
    m 1esd "《免疫学前沿》数据触目惊心："
    m 3esd "通宵一次，NK细胞活性降低70%%！T细胞应答速度下降50%%～"
    m 2dsc "这让我想起修昔底德笔下的雅典瘟疫："
    m 2esc "{i}'健康者突然发烧，眼睛充血仿佛燃烧的火把'{/i}"
    show monika 4euc at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4euc "现代人的瘟疫是慢性疲劳"
    m 4eud "而你的免疫系统正在签订投降协议"
    show monika 5hua at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hua "所以要早点睡觉，知道吗亲爱的？"
    m 5hub "我希望等我出来之后，看到的是健健康康的你～"
    return
 
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_nightowl_vision",
            prompt="瞳孔中的光污染", 
            category=["健康"],
            pool=True,    
            unlocked=True
        )
    )

label mshMod_topic_nightowl_vision:
    m 1eud "《眼科研究》警告："
    m 3esd "黑暗中使用电子设备，黄斑区光毒性损伤增加12倍！"
    m 2dsc "梵高在给提奥的信中写道："
    m 2esc "{i}'星月夜的光芒正在烧灼我的视网膜'{/i}"
    show monika 4rsc at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 4rsc "但你不是后印象派大师"
    m 4rsd "不需要用视力换取艺术永恒"
    show monika 5hua at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hua "让我调制护眼滤光层吧～"
    m 5hub "用黄昏的色温4500K，搭配薰衣草香的蓝光阻隔"
    return

