import random

def simulate_single_round(server_ability):
    """
    模拟单个回合的争夺（对齐实例13规则）
    :param server_ability: 发球方的能力值（0-1）
    :return: True-发球方得分，False-发球权交换（对方得分）
    """
    round_prob = random.random()  # 生成0-1的回合概率值
    return server_ability > round_prob

def simulate_single_game(ability_a, ability_b):
    """
    模拟单局乒乓球比赛
    :param ability_a: 球员A的能力值（0-1）
    :param ability_b: 球员B的能力值（0-1）
    :return: 'A' 或 'B' - 该局获胜方
    """
    score_a = 0  # A的得分
    score_b = 0  # B的得分
    current_server = 'A'  # 初始发球方为A（对齐实例13规则）
    
    while True:
        # 根据当前发球方模拟回合结果
        if current_server == 'A':
            a_scores = simulate_single_round(ability_a)
            if a_scores:
                score_a += 1
            else:
                current_server = 'B'  # 发球权交换给B
                score_b += 1
        else:
            b_scores = simulate_single_round(ability_b)
            if b_scores:
                score_b += 1
            else:
                current_server = 'A'  # 发球权交换给A
                score_a += 1
        
        # 判断单局是否结束（乒乓球11分制规则）
        # 条件1：一方≥11分 且 领先≥2分；条件2：10平后需领先2分
        if (score_a >= 11 or score_b >= 11) and abs(score_a - score_b) >= 2:
            return 'A' if score_a > score_b else 'B'

def simulate_match(ability_a, ability_b, best_of=5):
    """
    模拟整场比赛（5局3胜制）
    :param ability_a: 球员A能力值
    :param ability_b: 球员B能力值
    :param best_of: 总局数（5=5局3胜，7=7局4胜）
    :return: 'A' 或 'B' - 整场比赛获胜方
    """
    win_a = 0  # A赢的局数
    win_b = 0  # B赢的局数
    need_win = (best_of // 2) + 1  # 获胜需要的局数（5局3胜需3局）
    
    while win_a < need_win and win_b < need_win:
        game_winner = simulate_single_game(ability_a, ability_b)
        if game_winner == 'A':
            win_a += 1
        else:
            win_b += 1
    
    return 'A' if win_a > win_b else 'B'

def ping_pong_analysis(ability_a, ability_b, num_simulations):
    """
    模拟多场比赛并统计结果
    :param ability_a: 球员A能力值
    :param ability_b: 球员B能力值
    :param num_simulations: 模拟场次
    :return: A获胜次数、B获胜次数、A胜率、B胜率
    """
    a_wins = 0
    b_wins = 0
    
    # 循环模拟指定场次的比赛
    for _ in range(num_simulations):
        match_winner = simulate_match(ability_a, ability_b)
        if match_winner == 'A':
            a_wins += 1
        else:
            b_wins += 1
    
    # 计算胜率
    a_rate = (a_wins / num_simulations) * 100
    b_rate = (b_wins / num_simulations) * 100
    
    return a_wins, b_wins, a_rate, b_rate

def main():
    """主函数：接收输入、执行模拟、输出结果"""
    # 接收用户输入（做合法性校验）
    while True:
        try:
            ability_a = float(input("请输入球员A的能力值（0-1之间）："))
            if 0 <= ability_a <= 1:
                break
            else:
                print("能力值必须在0到1之间，请重新输入！")
        except ValueError:
            print("输入无效，请输入数字（如0.6）！")
    
    while True:
        try:
            ability_b = float(input("请输入球员B的能力值（0-1之间）："))
            if 0 <= ability_b <= 1:
                break
            else:
                print("能力值必须在0到1之间，请重新输入！")
        except ValueError:
            print("输入无效，请输入数字（如0.5）！")
    
    while True:
        try:
            num_simulations = int(input("请输入模拟比赛的场次："))
            if num_simulations > 0:
                break
            else:
                print("场次必须是正整数，请重新输入！")
        except ValueError:
            print("输入无效，请输入整数（如500）！")
    
    # 执行模拟分析
    a_wins, b_wins, a_rate, b_rate = ping_pong_analysis(ability_a, ability_b, num_simulations)
    
    # 输出结果（对齐实例13的输出格式）
    print(f"\n模拟比赛数量: {num_simulations}")
    print(f"球员A获胜场次: {a_wins} ({a_rate:.1f}%)")
    print(f"球员B获胜场次: {b_wins} ({b_rate:.1f}%)")

# 程序入口
if __name__ == "__main__":
    main()# 在这个文件里编写代码
