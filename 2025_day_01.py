#Part1 My version--wrong output
with open('input/2025_day_01.txt','r') as f:
    input=f.read()
    input=input.split("\n")
    value = 50
    count = 0
for cmd in input:
    cmd=cmd.strip()
    if cmd:
        step = int(cmd[1:])
        if cmd[0]=='R':
            if value+step>100:
                value=step+value-100
            elif value+step==100:
                value=0
            else:
                value=value+step
        elif cmd[0]=='L':
            if value-step<0:
                value=100+(value-step)
            elif value-step==0:
                value=0
            else:
                value=value-step
        if value==0
            count+=1
print(count)

#With the help of AI：
# --- 公共工具函数 ---
def get_input_data():
    """读取文件并处理成列表"""
    with open('input/2025_day_01.txt', 'r') as f:
        return [line.strip() for line in f if line.strip()]


# --- Part 1 的解法 ---

def part1_method_loop(instructions):
    """Part 1 解法一：不使用取模，用 While 循环 (你的原始逻辑)"""
    value = 50
    count = 0
    for cmd in instructions:
        step = int(cmd[1:])
        direction = cmd[0]

        if direction == 'R':
            value += step
            while value >= 100:
                value -= 100
        elif direction == 'L':
            value -= step
            while value < 0:
                value += 100

        if value == 0:
            count += 1
    print(f"Part 1 (Loop Method): {count}")


def part1_method_modulo(instructions):
    """Part 1 解法二：使用取模运算 (更优解)"""
    value = 50
    count = 0
    MOD = 100
    for cmd in instructions:
        step = int(cmd[1:])
        direction = cmd[0]

        if direction == 'R':
            value = (value + step) % MOD
        elif direction == 'L':
            value = (value - step) % MOD

        if value == 0:
            count += 1
    print(f"Part 1 (Modulo Method): {count}")


# --- Part 2 的预留位置 ---

def part2_solution(instructions):
    """Part 2 的解法 (等待题目更新)"""
    print("Part 2 尚未开始...")
    # 这里通常会复制 Part 1 的逻辑并进行修改
    # 比如：转盘变成了 1000 个刻度？或者起始点变了？
    pass


# --- 主程序入口 ---
if __name__ == "__main__":
    data = get_input_data()

    print("--- Day 01: Part 1 ---")
    part1_method_loop(data)
    part1_method_modulo(data)

    print("\n--- Day 01: Part 2 ---")
    part2_solution(data)