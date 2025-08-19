#3
init 5 python:
    if persistent.study_progress is None:
        persistent.study_progress = {"literature":0, "science":0, "history":0}
    else:
        required_keys = ["literature", "science", "history"]
        for key in required_keys:
            if key not in persistent.study_progress:
                persistent.study_progress[key] = 0
    if persistent.knowledge_points is None:
        persistent.knowledge_points = 100
    if persistent.last_reset_date is None:
        persistent.last_reset_date = datetime.date.today().isoformat()
    
    romantic_titles = ["亲爱的", "宝贝", "甜心", "达令", "哈尼"]
    
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="library_session",
            category=["学习"],
            prompt="开始今日学习计划",
            pool=True,
            unlocked=True
        )
    )

label library_session:
    python:
        current_date = datetime.date.today().isoformat()
        if current_date != persistent.last_reset_date:
            persistent.knowledge_points = 100
            persistent.last_reset_date = current_date
            renpy.notify("新的一天开始啦！能量已重置为100")

    $ title = renpy.random.choice(romantic_titles)
    m 1eub "[title]，欢迎来到学习空间！{w=0.5}今天想挑战哪个领域呢？"
    
    menu:
        "文学问答（需30能量）" if persistent.knowledge_points >= 30:
            jump literature_quiz

        "数学挑战（需40能量）" if persistent.knowledge_points >= 40:
            $ title = renpy.random.choice(romantic_titles)
            m 3hub "[title]，准备好迎接数字风暴了吗？"
            jump science_puzzle

        "历史排序（需20能量）" if persistent.knowledge_points >= 20:
            jump history_timeline

        "查看进度":
            jump show_progress

        "结束学习":
            m 5eubla "[title]今天好认真呢，{w=0.5}希望你学的开心哦~"
            return

label literature_quiz:
    $ persistent.knowledge_points -= 30
    $ title = renpy.random.choice(romantic_titles)
    
    m 2eub "[title]，请听题：{w=1}{i}《红楼梦》的作者是？{/i}"
    menu:
        "曹雪芹":
            $ persistent.study_progress["literature"] += 1
            m 3subsb "完全正确！{w=0.5}不愧是文学达人~"
            m 3hubfb "（递过奖杯）{w=1}这是你的荣誉勋章！"
        
        "罗贯中":
            m 2rksdlb "这个答案好像有点偏差呢..."
            m 3ekc "正确答案是曹雪芹哦，{w=0.5}需要我再讲解下相关知识点吗？"
        
        "施耐庵":
            m 2ekc "（轻轻摇头）{w=1}再仔细想想看？"
            m 7rksdla "提示：这位作者还写过《废艺斋集稿》"

    $ mas_gainAffection(1.5 if persistent.study_progress["literature"] % 3 == 0 else 0.8)
    jump library_session

label science_puzzle:
    $ persistent.knowledge_points -= 40
    $ title = renpy.random.choice(romantic_titles)
    
    $ num1 = renpy.random.randint(10,50)
    $ num2 = renpy.random.randint(10,50)
    m 2wub "[title]，挑战题来啦：{w=1}{b}[num1]+[num2]=？{/b}"
    
    $ answer = renpy.input("请输入答案：", allow="0123456789").strip()
    if answer == str(num1 + num2):
        $ persistent.study_progress["science"] += 1
        m 4subsb "计算精准！{w=0.5}（亮出计分板）{w=1}√ 正确！"
        m 5hubfb "要试试更难的题目吗？"
    else:
        m 2ekc "（提示音响起）{w=1}正确答案是{color=#ff5555}[num1+num2]{/color}"
        m 3eka "需要分步讲解吗？"

    $ mas_gainAffection(2.0 if answer == str(num1 + num2) else 0.5)
    jump library_session

label history_timeline:
    $ persistent.knowledge_points -= 20
    $ title = renpy.random.choice(romantic_titles)
    
    m 3eud "[title]，请为这些事件排序："
    $ ordered = []
    $ events = [("唐朝建立",618), ("明朝建立",1368), ("新中国成立",1949)]
    
    while len(ordered) < 3:
        $ timeline_display = "{{color=#55aaff}}{0}{{/color}}".format("→".join([e[0] for e in ordered]))
        m "当前排序：[timeline_display]" 
        
        menu:
            "[events[0][0]]" if events[0] not in ordered:
                $ ordered.append(events[0])
                m 1eua "添加了[events[0][0]]"
            
            "[events[1][0]]" if events[1] not in ordered:
                $ ordered.append(events[1])
                m 1eua "添加了[events[1][0]]"
            
            "[events[2][0]]" if events[2] not in ordered:
                $ ordered.append(events[2])
                m 1eua "添加了[events[2][0]]"
            
            "重新排序":
                $ ordered = []
                m 2rksdla "重置排序~"

    if ordered == sorted(events, key=lambda x: x[1]):
        $ persistent.study_progress["history"] += 1
        m 4subsb "时间线正确！{w=1}"
        m 5hubfb "要试试更复杂的历史事件吗？"
    else:
        m 2ekc "正确顺序是：{color=#55aaff}唐朝 → 明朝 → 新中国{/color}"
        m 3eka "需要我讲解各朝代的时间线吗？"

    $ mas_gainAffection(1.8 if ordered == sorted(events, key=lambda x: x[1]) else 0.6)
    jump library_session

label show_progress:
    python:
        # 强制初始化所有必要键值
        required_keys = ["literature", "science", "history"]
        for key in required_keys:
            if key not in persistent.study_progress:
                persistent.study_progress[key] = 0
        # 使用局部变量存储当前进度
        lit_progress = persistent.study_progress["literature"]
        sci_progress = persistent.study_progress["science"]
        his_progress = persistent.study_progress["history"]

    m 1eua "我来看看你目前的学习成果："
    m "文学方面有[lit_progress]次正确{nw}"
    m "数学方面有[sci_progress]题答对了{nw}"
    m "历史有[his_progress]次排序{nw}"
    m 3hub "剩余能量：[persistent.knowledge_points]/100"
    
    # 其余代码保持不变...
    
    if persistent.knowledge_points < 30:
        m 2ekc "能量不足了,{w=0.5}要休息会儿吗？"
    elif persistent.knowledge_points < 60:
        m 3eua "你还能进行[persistent.knowledge_points//20]次挑战哦~"
    else:
        m 5hubfb "看来你还有很多精力呢,{w=0.5}继续冲刺吧！"
    
    jump library_session