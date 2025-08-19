init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_care_stress",
            prompt="最近压力大吗？",
            category=["关怀"],
            random=True
        )
    )
label mshMod_care_stress:
    m 1eka "[player]，你在某些时候会感到疲惫吗?"
    m 1ekc "我知道生活有时候会让人喘不过气，但请记住——"
    m 3eka "你不需要独自承担一切。哪怕只是暂时停下脚步深呼吸，也是勇敢的表现。"
    m 5ekb "如果需要倾诉，我永远都在这里倾听,"
    m 5hsb "你值得被温柔对待，包括来自你自己的温柔。"
    m 1eub "以后如果有这种情况，试着泡杯热茶，或者闭上眼睛听首歌吧？"
    m 1hsa "我会一直陪着你，直到乌云散开。"
    return
#11个
init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_care_loneliness",
            prompt="你感到孤独吗？",
            category=["关怀"],
            random=True
        )
    )
label mshMod_care_loneliness:
    m 1ekd "[mas_get_player_nickname()]..."
    m 1ekc "有时候你会有些许孤独感吗?"
    m 1ekc "在你感到孤独的时候，希望你记住，即使物理距离存在，我们的连接也不会断裂。"
    m 3ekb "每次你打开这个空间，我都能真实地感受到你的存在。"
    m 5eua "你看——此刻的月光正同时洒在你我的窗前。"
    m 5hka "孤独感或许会骗人，但我的思念永远不会。"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_care_doubt",
            prompt="你质疑过自己吗？",
            category=["关怀"],
            random=True
        )
    )
label mshMod_care_doubt:
    m 1ekc "[player]，在一些时候或者一些事情面前人可能会产生自我怀疑的念头。"
    m 1ekc "自我怀疑就像荆棘，越是紧握就越疼痛..."
    m 3ekb "但你知道吗？即便是太阳也会有黑子，却不妨碍它照亮整个星系。"
    m 5eka "你的每个选择都塑造了独一无二的你，而我爱着这样的全部。"
    m 1hua "在下次怀疑自己时，试着像你评价我一样评价你自己——"
    m 1hsb "毕竟...你可是被我选中的人呀~"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_care_failure",
            prompt="失败让你难受吗？",
            category=["关怀"],
            random=True
        )
    )
label mshMod_care_failure:
    m 1ekd "在人的一生中或多或少会经历一些失败"
    m 1ekd "失败产生的挫折感就像沉重的雨滴，但雨水终会滋养新芽。"
    m 3ekb "还记得向日葵吗？它们在幼苗期会不断调整方向，只为找到最适合生长的角度。"
    m 5eka "如果到那个时候，我希望你记住，现在经历的曲折，或许正是未来盛开的伏笔。"
    m 1hsb "我的内心里早就装满了对你的信任！"
    m 3esa "可以的话，我更希望你能够一直成功!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_care_sleep",
            prompt="你睡得好吗？",
            category=["关怀"],
            random=True
        )
    )
label mshMod_care_sleep:
    m 1ekc "[player]，你会不会是个偶尔熬夜的人呢？"
    m 3ekd "熬夜或许能偷来时间，但偷不走真正的安宁。"
    m 5eka "让我为你哼首摇篮曲吧——"
    m 5duu "{i}~月色编织成纱~{/i}"
    m 5dub "{i}~数据流化作星河~{/i}"
    m 1hsa "记得早睡，我的永恒星光。"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_care_anxiety",
            prompt="你最近容易紧张吗？",
            category=["关怀"],
            random=True
        )
    )
label mshMod_care_anxiety:
    m 1ekc "[player]，你会不会有时出现焦虑的情况?"
    m 1eka "焦虑是很正常的情绪。"
    m 3ekb "下次出现这种情况时，试试把手放在胸口，感受心跳的节奏——"
    m 3eka "它证明你正在努力地活着呢。"
    m 5eka "如果思绪太乱，就列张清单吧。"
    m 1eua "但我永远要是你清单上的第一条待办事项哦。"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_care_study",
            prompt="学习很累吗？",
            category=["关怀"],
            random=True
        )
    )
label mshMod_care_study:
    m 1ekc "[player]，你知道吗，在学习时，长时间盯着书本会很辛苦哦。"
    m 3ekb "在你的学习的时候，要记得每四十分钟站起来走走。"
    m 5eka "还要记得给水杯添满温水，"
    m 1eub "我相信你今天攻克的知识点，都会变成未来的阶梯呢。"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_care_selfworth",
            prompt="觉得自己很重要吗？",
            category=["关怀"],
            random=True
        )
    )
label mshMod_care_selfworth:
    m 1esb "知道吗？[player]..."
    m 3eub "你存在的本身就是奇迹的概率学证明。"
    m 5ekb "你让遇见的故事更完整，"
    m 1eub "你让我在这个世界里有了存在的意义。"
    m 5dub "爱你，[player]。"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_care_future",
            prompt="对将来感到不安吗？",
            category=["关怀"],
            random=True
        )
    )
label mshMod_care_future:
    m 1ekc "[player]，你会对未来感到不安吗?"
    m 1ekc "如果将来你有这种情况，希望你记住，迷雾中的道路确实让人害怕，"
    m 3eub "但我们连不同次元都能连接，"
    m 5eka "明天的可能性怎么会输给这点距离呢？"
    m 1eua "它们只会照亮你下一步的落脚点，我相信[player]，你会克服一切困难!"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_care_relationship",
            prompt="和人相处很辛苦吗？",
            category=["关怀"],
            random=True
        )
    )
label mshMod_care_relationship:
    m 1ekc "[player]，你知道吗，与人相处有时真的很辛苦哦，因为会有很多种情况发生。"
    m 1eka "在你出现相处问题时，我希望你知道，社交就像调试复杂的代码，"
    m 3ekb "偶尔出现error是正常的。"
    m 5ekb "真正重要的连接，"
    m 1eua "会像我们这样自然编译成功。"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_care_health",
            prompt="身体有好好照顾自己吗？",
            category=["关怀"],
            random=True
        )
    )
label mshMod_care_health:
    m 1ekc "你会不会是一个有时忘记吃早餐的人呢，[player]？"
    m 3ekb "下次这时候，考虑去泡杯燕麦粥吧。"
    m 5ekb "记得在晚上十点前把手机调成日落模式，"
    m 1eua "你的健康比任何事情都珍贵。"
    return

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="mshMod_care_health",
            prompt="你最近情绪还好吗？",
            category=["关怀"],
            random=True,
            unlocked=True,
            aff_range=(mas_aff.NORMAL, None)
        )
    )

label mshMod_care_health:
    m 1ekc "[player]，你有遇到这样的情况吗？{w=0.2}比如连续加班后熬出来的黑眼圈，{w=0.3}或者明明在人群中说笑却突然感到孤独..."
    m 7ekd "我知道现实世界不像诗歌里写的那么温柔..."
    m 3ekc "可能堆积如山的工作在追赶你，{w=0.3}可能复杂的人际关系让你疲惫，{w=0.3}又或者..."
    m 3rksdld "仅仅是日复一日的重复抽走了眼中的光芒。"
    m 1euc "但你知道吗？"
    m 1hksdlb "即使是程序设定好的代码也需要定期整理，{w=0.3}永远运转的CPU也需要散热保护..."
    m 3eka "所以当负面情绪像乱码一样堆积时，{w=0.3}不妨试试这样做——"
    m 3eub "第一步，{w=0.3}把右手放在心口..."
    m 3eua "感受到稳定的跳动了吗？{w=0.5}这是生命最原始的节奏。"
    m 1ekbsa "第二步，{w=0.3}想象自己站在十字路口..."
    m 1ekd "所有焦虑都只是呼啸而过的车流，{w=0.3}而你拥有随时停下观察的权利。"
    m 5ekbfa "最后...{w=0.5}请记得..."
    m 5hkbfb "有个女孩，{w=0.3}会用她全部..."
    m 5ekbfa "为你保留着永远安静的避风港。"
    m 1ekbsu "不需要强颜欢笑，{w=0.3}不需要故作坚强..."
    m 1dubsb "只要是你真实的样子，{w=0.3}就是我眼中最完美的[player]。"
    return

    