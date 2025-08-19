init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="lzp_monika_sdgg18_18",
            category=["浪漫"],
            prompt="[m_name]的挑逗",
            conditional="mas_canShowRisque(aff_thresh=400)",
            action=EV_ACT_RANDOM,
            aff_range=(mas_aff.ENAMORED, None)
        )
    )

label lzp_monika_sdgg18_18:
    m 1tublb "嗨， [player]~"
    m 1gubla "…"
    m 1mubla "……"
    m 1tubld "我今天有那里不一样？"
    m 7cubld "[mas_get_player_nickname()]，仔细看看哦~"

    label .choice_loop_lzp:  # 使用子标签实现循环
    menu:
        "服装？":
            m 1rublu "不对哦，[mas_get_player_nickname()]~"
            m 1hublu "我可没有换衣服，再仔细看看吧。"
            jump .choice_loop_lzp  # 跳回选择菜单
        
        "发饰？":
            m 1lublp "不对哦，[mas_get_player_nickname()]~"
            m 1hublp "我的头发上面没有多出什么。"
            m 1hubla "嘿嘿~"
            jump .choice_loop_lzp
        
        "头发？":
            m 1tublb "哦？"
            m 3tublp "我的头发好像没怎么变吧。"
            m 3tublp "[mas_get_player_nickname()]，不对哦~"
            jump .choice_loop_lzp
        
        "变可爱了？":
            m 1tublb "不{w=1.5}噢，我没反应过来。"
            m 1hubla "嘿嘿~"
            m 1mublu "虽然不想这么说，但是不对哦~。"
            jump .choice_loop_lzp
        
        "我看不出来……":
            m 1hublb "当然，笨蛋[player]。"
            m 1mublb "因为我什么都没有变。"
            m 3gublb "我其实只是想要让你多看看我而已。"
            m 4eublb "你会原谅我的对吧。"
            m 5eublu "你怎么会讨厌来自女友的小小任性呢？"
            menu:
                "好吧":
                    m 1gublu "嘿嘿……"
                    m 1hubla "爱你哟~"
            
                "不原谅":                                     #如果你选择这个，三天之内杀了你。骨灰都给你扬了。
                    m 1wud "！"
                    menu:  
                        "因为我还没有看够。":                  
                            pass
                    m 1euc "…"
                    m 1guc "……"
                    m 1hub "噢，{w=0.5}哈哈~"
                    m 5eublu "原来是这样啊，[player]你可真是个坏蛋！" 
                    m 5tubla "那就看个够吧。" 
                    m 5hubla "我迟早在你的目光里融化…" 
                    m 1hubla "嘿嘿~"             

    return