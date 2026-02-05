# #Part1 My version--wrong output
# with open('input/2025_day_01.txt','r') as f:
#     input=f.read()
#     input=input.split("\n")
#     value = 50
#     count = 0
# for cmd in input:
#     cmd=cmd.strip()
#     if cmd:
#         step = int(cmd[1:])
#         if cmd[0]=='R':
#             if value+step>100:
#                 value=step+value-100
#             elif value+step==100:
#                 value=0
#             else:
#                 value=value+step
#         elif cmd[0]=='L':
#             if value-step<0:
#                 value=100+(value-step)
#             elif value-step==0:
#                 value=0
#             else:
#                 value=value-step
#         if value==0
#             count+=1
# print(count)

#With the help of AI：
# --- 公共工具函数 ---
def get_input_data():
    """读取文件并处理成列表"""
    with open('input/2025_day_01.txt', 'r') as f:
        return [line.strip() for line in f if line.strip()]

# ---逻辑出发点好像错了，第一题能写出来，第二题想排出几个误差的数学逻辑太难想象了，还是应该用指针一个一个转的这种逻辑 ---
# 是因为他通过 i != degree-1 划清了过程和结果的界限。
# 你的数学法：试图用公式一次性算出（过程 + 结果），导致边界极其复杂。
def method_loop(instructions):
    """Part 1：不使用取模，用 While 循环 (你的原始逻辑)"""
    value = 50
    count = 0
    n=0 #计算part2 转过的次数
    for cmd in instructions:
        step = int(cmd[1:])
        direction = cmd[0]
        if direction == 'R':
            value += step
            while value >= 100:
                value -= 100
                if value != 0:
                    n+=1
        elif direction == 'L':
            value -= step
            while value < 0:
                value += 100
                if value != 99:
                    n += 1
        if value == 0:
            count += 1
    print(f"Part 1 (Loop Method): {count}")
    print(f"Part 2 (Loop Method): {count+n}")

# --- 主程序入口 ---
if __name__ == "__main__":
    data = get_input_data()

    print("--- Day 01: ")
    method_loop(data)
