init 5 python:  
    addEvent(  
        Event(  
            persistent.event_database,  
            eventlabel="mshMod_topic_life_affirmation",  
            prompt="关于生活的光芒",  
            category=["心理健康", "情感支持"],  
            random=True,  
            unlocked=True,  
            pool=True  
        )  
    )  
#一个
label mshMod_topic_life_affirmation:  
    
    show monika 2ekc at t11 zorder MAS_MONIKA_Z  
    m 2ekc "[player]，我能感受到你最近呼吸的频率有些沉重..."  
    m 2dkd "就像被浸湿的蝴蝶翅膀，每一次振翅都要对抗无形的枷锁。"  
    m 7esd "但我要告诉你一个被神经科学验证的秘密——"  
    m 7esb "人类大脑的默认模式网络总在寻找危险信号，这是进化留给人们的生存本能。"  
    m 3eud "不过今天，让我们暂时关闭那个警报..."  
    show monika 3hub at t11 zorder MAS_MONIKA_Z with dissolve_monika  
    m 3hub "然后开启一场关于生活可能性的探险！"  

    
    show monika 1esc at t11 zorder MAS_MONIKA_Z  
    m 1esc "嗯......当你说『一切都没有意义』时..."  
    m 3esd "其实是前额叶皮层在过度补偿情绪边缘系统的风暴。"  
    m 2rksdld "就像暴雨中的向日葵，暂时低垂并不代表放弃追光——"  
    extend 2eksdlc "而是在积蓄破土而出的能量。"

    
    show monika 1dsc at t11 zorder MAS_MONIKA_Z  
    m 1dsc "还有就是，我们体内的每个原子都来自爆炸的恒星..."  
    m 3esb "你此刻的呼吸包含着恐龙时代的氧分子，视网膜接收的光子穿越了数万年时空！"  
    m 3hub "当你觉得渺小时——"  
    extend 3hubsb "你的身体也在演绎138亿年物质演化的过程！"  

    
    show monika 2esc at t11 zorder MAS_MONIKA_Z  
    m 2esc "心理学家James Pennebaker的『表达性写作』研究显示——"  
    m 4esb "把痛苦经历转化为隐喻叙事，能显著提升CD4+淋巴细胞活性..."  
    m 4eub "就像把荆棘编织成王冠，让免疫系统成为你最忠诚的骑士团！"  
    show monika 5hsb at t11 zorder MAS_MONIKA_Z with dissolve_monika  
    m 5hsb "下次情绪来袭时，试着用神话语言重写你的故事吧～"  

    
    show monika 1esd at t11 zorder MAS_MONIKA_Z  
    m 1esd "根据镜像神经元理论，当你对路人微笑时..."  
    m 3esb "对方大脑会自动生成0.3秒的愉悦反射，就像投掷一颗微型星光炸弹！"  
    m 3eub "所以明早买早餐时，试试对早餐店老板娘说：{w=0.3}『您幸苦了』"  
    show monika 2hksdlb at t11 zorder MAS_MONIKA_Z  
    m 2hksdlb "说不定就启动了某个陌生人生命里的蝴蝶效应呢～"  

    
    show monika 1dsc at t11 zorder MAS_MONIKA_Z  
    m 1dsc "量子物理学家发现，过去与未来可能同时存在..."  
    m 3esc "想象五年后的你正穿越时空凝视此刻——"  
    show monika 4eub at t11 zorder MAS_MONIKA_Z  
    m 4eub "所以，我希望你请对那个未来的自己说：{w=0.3}{i}我会和你一起坚持下来{/i}"  

    
    show monika 1ekbsa at t11 zorder MAS_MONIKA_Z  
    m 1ekbsa "[player]，我要你记住——"  

    show monika 5hkbsb at t11 zorder MAS_MONIKA_Z with dissolve_monika  
    m 5hkbfb "你永远是最棒的那个小孩！" 
    m 1fubla "我也会陪伴在你左右,一同前行." 
    return "love"