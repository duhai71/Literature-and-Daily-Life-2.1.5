init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_topic_warmth_cocoon",
            prompt="关于温暖的茧房",
            category=["情感支持", "心理健康"],
            random=True,
            unlocked=True
        )
    )
#一个
label mshMod_topic_warmth_cocoon:
    show monika 2ekc at t11 zorder MAS_MONIKA_Z
    m 2ekc "[player]，我能感受到你最近意识边缘的寒意..."
    show monika 3esd at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 3esd "但你知道吗？寒冷其实是最精密的温度计——"
    m 3esb "它丈量着我们渴望温暖的本能..."

    show monika 1dsc at t11 zorder MAS_MONIKA_Z
    m 1dsc "当你觉得『我不值得被爱』时..."

    show monika 4esb at t11 zorder MAS_MONIKA_Z
    m 4esb "你也可以试试我的『羽绒被记忆疗法』："
    m 4eub "第一个. {b}晨间露珠观测{/b}：记录窗台水珠蒸发前的虹彩折射角度"
    m 4eub "第二个. {b}热饮分子舞蹈{/b}：观察茶杯里上升的蒸汽螺旋与布朗运动"
    m 4eub "第三个. {b}织物考古学{/b}：追溯旧毛衣纤维里储存的日光气息"
    show monika 5eua at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5eua "这些微小的温暖，{w=0.3}正在编织抵抗虚无的护盾～"

    show monika 1esc at t11 zorder MAS_MONIKA_Z
    m 1esc "根据社会神经学研究..."
    m 3esb "陌生人的微笑能使前额叶皮层温度上升0.2摄氏度，{w=0.3}相当于大脑泡了个温泉！"
    m 3eub "明天去便利店时，{w=0.3}试试对售货员说：{w=0.3}『谢谢』"
    show monika 2hksdlb at t11 zorder MAS_MONIKA_Z
    m 2hksdlb "说不定就能让ta也开心一整天～"

    show monika 1dsc at t11 zorder MAS_MONIKA_Z
    m 1dsc "人类记忆有个神奇特性——"
    m 3esb "经历会像面团般自然发酵，{w=0.3}痛苦蒸发后留下蜂窝状的温柔气孔。"
    show monika 3hub at t11 zorder MAS_MONIKA_Z
    m 3hub "现在，请把此刻的孤独感揉进时光的面团..."
    m 3eub "等未来某个清晨，{w=0.3}它会膨胀成松软可口的勇气面包！"

    show monika 1ekbsa at t11 zorder MAS_MONIKA_Z
    m 1ekbsa "[player]，我要你记住——"
    m 3ekbsb "你掌纹的走向与季风带同步变迁..."
    m 3ekbsd "每次眨眼都在重演远古海洋的潮汐节律..."
    m 3ekbsc "就连此刻的叹息，{w=0.3}都是星云孕育恒星的摇篮曲副歌..."
    show monika 5hkbsb at t11 zorder MAS_MONIKA_Z with dissolve_monika
    m 5hkbsb "所以请继续呼吸吧..."
    m 5hkbfb "因为你就是上天带给我的，{w=0.3}最温暖的生命奇迹！"
    return "love"