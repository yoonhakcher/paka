import random

GAME_TITLE = "十分低配置的赛马娘抓娃娃机（via GPT-4o）"
DOLL_LIST = ["特别周", "无声铃鹿", "东海帝王", "丸善斯基", "富士奇石", "小栗帽", "黄金船", "伏特加", "大和赤骥", "大树快车", "草上飞", "菱亚马逊", "目白麦昆", "神鹰", "好歌剧", "成田白仁", "鲁道夫象征", "气槽", "爱丽数码", "青云天空", "玉藻十字", "美妙姿势", "琵琶晨光", "摩耶重炮", "曼城茶座", "美浦波旁", "目白赖恩", "菱曙", "雪之美人", "米浴", "艾尼斯风神", "爱丽速子", "爱慕织姬", "稻荷一", "胜利奖券", "空中神宫", "荣进闪耀", "真机伶", "川上公主", "黄金城市", "樱花进王", "采珠", "新光风", "东商变革", "超级溪流", "醒目飞鹰", "荒漠英雄", "东瀛佐敦", "中山庆典", "成田大进", "西野花", "春丽", "青竹回忆", "微光飞驹", "美丽周日", "待兼福来", "千明代表", "名将怒涛", "目白多伯", "优秀素质", "圣王光环", "待兼诗歌剧", "生野狄杜斯", "目白善信", "大拓太阳神", "双涡轮", "里见光钻", "北部玄驹", "樱花千代王", "天狼星象征", "目白阿尔丹", "八重无敌", "鹤丸刚志", "目白光明", "谋勇兼备", "樱花桂冠", "成田路", "也文摄辉", "狂怒乐章", "创升", "希望之城", "北方飞翔", "吉兆", "谷野美酒", "第一红宝石", "目白高峰", "真弓快车", "里见皇冠", "高尚骏逸", "极峰", "强击", "烈焰快驹", "凯斯奇迹", "森林宝穴", "信念", "莫名其妙", "爱如往昔", "小林历奇", "北港火山", "奇锐骏", "大森逊", "万籁争鸣", "罗伊斯兄弟", "葛城王牌", "新宇宙", "菱钻奇宝", "跳舞城", "大鸣大放", "莱茵力量", "西沙里奥", "空中救世主", "勇敢之心", "房一潘多拉", "迷人景致", "黄金巨匠", "贵妇人", "凯旋芭蕾", "梦之旅", "金镇之光", "多旺达", "吹波糖", "樱花千岁王", "超常骏骥", "防爆装束", "杏目", "旺紫丁", "放声欢呼", "唯独爱你", "创世驹", "机伶金花", "黄金旅程", "达利阿拉伯", "高多芬阿拉伯", "拜耶尔土耳其", "圣烈特", "速度象征", "海塞克", "望族", "快乐米可", "Bitter Glasse", "Little Cocon", "Light Hello", "Venus Paques", "Rigantona", "Sonon Elfie", "Sugar Lights", "桥式压缩", "皇后贝雷", "金色旅程", "布卢瓦耶", "遮阳帽", "崭新光辉", "藤正进行曲", "诺伦王牌", "鲁迪乐摩", "迷你女士", "狄杜射手", "黑色艾尔", "听命汝主", "平民女王", "磨坊若叶", "吉野樱草", "天城之幸", "危地暴雪", "骏川手纲", "秋川弥生", "乙名史悦子", "桐生院葵", "安心泽刺刺美", "㭴本理子", "佐岳芽衣", "都留岐凉花", "赤坂美聪", "细江纯子", "训练员", "东条华", "南坂", "黑沼", "武丰", "特别周的养母", "主治医师", "北原穰", "藤井泉助", "六平银次郎", "奈濑文乃", "奈濑英人", "明石椿", "明石梧郎", "阿武隈纱季", "石上勋", "黑田自由"]
NUM_GROUPS = 3
DOLL_QUANTITY_OPTIONS = [1, 2, 3, 4, 5]
DOLL_QUANTITY_WEIGHTS = [0.35, 0.3, 0.2, 0.1, 0.05]
LARGE_DOLL_PROB = 0.1
GRAB_SUCCESS_PROB = 0.7
DROP_PROB = 0.6
DROP_PROB_BY_DISTANCE = 0.1
NUM_ROUNDS = 3

def generate_doll_groups():
    groups = []
    for i in range(NUM_GROUPS):
        quantity = random.choices(DOLL_QUANTITY_OPTIONS, DOLL_QUANTITY_WEIGHTS)[0]
        dolls = random.choices(DOLL_LIST, k=quantity)
        if random.random() < LARGE_DOLL_PROB:
            large_doll_index = random.randint(0, quantity - 1)
            dolls[large_doll_index] = f"{dolls[large_doll_index]}（大）"
        groups.append(dolls)
    return groups

def display_groups(groups):
    print("\n当前玩偶机中所含玩偶：")
    for i, group in enumerate(groups):
        display_str = f"组{i + 1}: {group[0]}" + ("..." if len(group) > 1 else "")
        print(display_str)

def get_user_choice():
    while True:
        try:
            choice = int(input("\n请输入欲抓取的玩偶组编号: "))
            if 1 <= choice <= NUM_GROUPS:
                return choice - 1
            else:
                print("输入无效，请输入正确的编号。")
        except ValueError:
            print("输入无效，请输入正确的编号。")

def check_grab_success():
    return random.random() < GRAB_SUCCESS_PROB

def check_drop(doll_index, group_index):
    return random.random() < (DROP_PROB + group_index * DROP_PROB_BY_DISTANCE)

def play_round(groups):
    display_groups(groups)
    chosen_group_index = get_user_choice()
    chosen_group = groups[chosen_group_index]
    
    if check_grab_success():
        print(f"\n抓取成功！组{chosen_group_index + 1}包含以下玩偶：")
        for doll in chosen_group:
            print(doll, end=" ")
        print("\n")
        
        dropped_dolls = []
        while chosen_group:
            if check_drop(len(chosen_group) - 1, chosen_group_index):
                dropped_dolls.append(chosen_group.pop())
                print(f"{dropped_dolls[-1]} 中途掉回玩偶机...")
            else:
                break
        
        if chosen_group:
            print("\n成功获得了玩偶：")
            for doll in chosen_group:
                print(doll, end=" ")
            print("\n")
            return chosen_group
        else:
            print("\n所有玩偶中途掉回玩偶机...")
    else:
        print("\n抓取失败...")
    
    return []

def rate_performance(dolls):
    normal_doll_count = sum(1 for doll in dolls if '（大）' not in doll)
    large_doll_count = sum(1 for doll in dolls if '（大）' in doll)
    
    if normal_doll_count == 0 and large_doll_count == 0:
        print("失败...")
    elif (1 <= normal_doll_count <= 5 and large_doll_count == 0) or (0 <= normal_doll_count <= 1 and large_doll_count >= 1):
        print("成功！")
    elif (normal_doll_count >= 6 and large_doll_count == 0) or (normal_doll_count >= 2 and large_doll_count >= 1):
        print("大成功！")

def main():
    print(GAME_TITLE)
    
    total_dolls = []
    for round_num in range(NUM_ROUNDS):
        print(f"\n=== 第{round_num + 1}轮游戏 ===")
        groups = generate_doll_groups()
        total_dolls.extend(play_round(groups))
    
    print("\n游戏结束！你共获得以下玩偶：")
    if total_dolls:
        for doll in total_dolls:
            print(doll, end=" ")
        print("\n")
        rate_performance(total_dolls)
    else:
        print("未获得任何玩偶...")
        rate_performance(total_dolls)
    
    replay = input("\n是否重玩游戏？按 y 重玩，按其他键退出：")
    if replay.lower() == 'y':
        main()
    else:
        print("感谢游玩！")

if __name__ == "__main__":
    main()