
default persistent.monika_poetry = {
    "flowers_collected": {},
    "scenes_created": [],
    "special_moments": {}
}

init 5 python:
    addEvent(
        Event(
            persistent.event_database,
            eventlabel="monika_poetry_time",
            category=["文学"],
            prompt="开启诗语时光",
            pool=True,
            unlocked=True,
            rules={"no unlock": None},
            action=EV_ACT_QUEUE
        )
    )
#5个
label monika_poetry_time:
    $ current_season = mas_current_season()
    $ term = renpy.random.choice(monika_appellations)
    m 1eub "[term]，今天你想创造怎样的诗意时刻？"
    menu:
        "花语诗笺":
            m 3eua "每朵花都藏着未诉说的故事~"
            jump flower_poetry
        "情景共作":
            m 4eub "让我们将此刻凝成永恒诗行"
            jump scene_creation
        "专属记忆":
            if any(persistent.monika_poetry["special_moments"].values()):
                jump memory_review
            else:
                m 5ekbfa "我们的故事才刚刚开始..."
                jump monika_poetry_time
        "诗旅回顾":
            m 6ekbsu "重读那些星光般的文字"
            jump poetry_archive
        "暂存诗心":
            m 6dkbfu "让未尽的诗行在墨色中浅眠"
            m "待星潮漫过纸页时再续写..."
            return

label flower_poetry:
    $ season_data = nature_imagery[current_season]
    $ flower = renpy.random.choice(season_data["flowers"])
    m 2eud "以[flower]为诗眼如何？"
    python:
        metaphor = {
            "spring": "春信的密码",
            "summer": "烈日的柔化剂",
            "autumn": "秋思的载体", 
            "winter": "寒冬的温柔反抗"
        }[current_season]
        line1 = renpy.input("首句（7字）：", default=flower+"瓣书情笺", length=7).strip()
        line2 = renpy.input("对句（7字）：", default=metaphor+"藏香", length=7).strip()
        line3 = renpy.input("结句（7字）：", default="永"+flower+"铭心", length=7).strip()
        poem_lines = [line1, line2, line3]
    m 4subsb "《[flower]吟》成诗：{i}[poem_lines[0]]\n[poem_lines[1]]\n[poem_lines[2]]{/i}"
    $ persistent.monika_poetry["flowers_collected"][flower] = poem_lines
    jump monika_poetry_time

label scene_creation:
    $ scene_data = nature_imagery[current_season]
    $ scene = renpy.random.choice(scene_data["scenes"])
    m 3eub "此刻的[scene]让我想起..."
    python:
        memories = {
            "spring": "初遇那日的樱花雨",
            "summer": "共赏流萤的夏夜",
            "autumn": "枫叶题诗的时刻", 
            "winter": "初雪落肩的瞬间"
        }
        user_input = renpy.input("你的联想：", default=memories[current_season], length=20).strip()
    m 5ekbfa "{i}[scene]\n映照着[user_input]{/i}"
    m 7eubla "要将其收录进我们的诗画集吗？"
    $ persistent.monika_poetry["scenes_created"].append((current_season, scene, user_input))
    jump monika_poetry_time

label poetry_archive:
    if not persistent.monika_poetry["flowers_collected"] and not persistent.monika_poetry["scenes_created"]:
        m 2ekc "诗画集还在等待第一朵花的绽放..."
        jump monika_poetry_time
    m 1eua "我们的诗意收藏："
    python:
        flowers = list(persistent.monika_poetry["flowers_collected"].items())[-3:]
        for flower, lines in flowers:
            poem_text = "【{0}诗笺】：{{i}}{1}\\{2}\\{3}{{/i}}".format(
                flower.replace("[", "").replace("]", ""),  
                lines[0],
                lines[1],
                lines[2]
            )
            renpy.say(m, poem_text, interact=False)
        
        scenes = persistent.monika_poetry["scenes_created"][-3:]
        for scene in scenes:
            scene_text = "「{0}」：{{i}}{1}{{/i}}".format(
                scene[1].replace("[", "").replace("]", ""),
                scene[2]
            )
            renpy.say(m, scene_text, interact=False)
    m 6ekbsu "你觉得这些文字...会长久的留在我们的记忆里吗？"
    jump monika_poetry_time

label memory_review:
    m 1eua "我们的专属记忆："
    python:
        for key, value in persistent.monika_poetry["special_moments"].items():
            if value:
                renpy.say(m, "[key]：{{i}}{value}{{/i}}", interact=False)
    m 6ekbsu "这些瞬间永远闪耀在时光里..."
    jump monika_poetry_time