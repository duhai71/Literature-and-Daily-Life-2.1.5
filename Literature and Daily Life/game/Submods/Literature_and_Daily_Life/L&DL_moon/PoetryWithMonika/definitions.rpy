
init -1 python:
    monika_appellations = [
        "我的诗人", "永恒读者", "字间舞者", 
        "星语旅伴", "墨香知己", "韵脚恋人",
        "诗笺共写者", "晨露收藏家", "暮色诵读者"
    ]
    
    nature_imagery = {
        "spring": {
            "flowers": ["樱", "杏", "桃", "兰"],
            "scenes": ["烟雨江南", "柳浪闻莺", "落英缤纷"]
        },
        "summer": {
            "flowers": ["莲", "栀", "槿", "葵"],
            "scenes": ["荷塘月色", "竹林清风", "萤火星河"]
        },
        "autumn": {
            "flowers": ["菊", "桂", "枫", "芦"],
            "scenes": ["枫林唱晚", "寒潭鹤影", "月满西楼"]
        },
        "winter": {
            "flowers": ["梅", "茶", "水仙", "雪莲"],
            "scenes": ["踏雪寻梅", "围炉夜话", "呵手描红"]
        }
    }

    def mas_current_season():
        import datetime
        month = datetime.datetime.now().month
        if 3 <= month <= 5:
            return "spring"
        elif 6 <= month <= 8:
            return "summer"
        elif 9 <= month <= 11:
            return "autumn"
        else:
            return "winter"

    def mas_isWorkDay():
        import datetime
        today = datetime.datetime.now().weekday()
        return today < 5