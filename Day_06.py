#insight：因为有toggle所以不是简单加减法，需要有位置属性以及对应状态
#字典写法

#二维表格写法(wiht the help of AI)
#第一步 创建原始坐标
light_grid = []
for x in range(1000):
    one_row = []
    for y in range(1000):
        one_row.append(False)
    light_grid.append(one_row)
#第二步 清理数据
with open('input/day_06.txt', 'r') as file_object:
    clean_input=list()
    for line in file_object:
         clean_line = line.strip()
         if clean_line: #防止有空行返回空值
              clean_input.append(clean_line)
#第三步 拆分数据，提取「操作类型」和「坐标字符串」
for cmd in clean_input:
    cmd_part = cmd.split(' ')
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    if cmd_part[0] == 'toggle':
        op = 'toggle'
        pos1 = cmd_part[1]
        pos2 = cmd_part[3]
    elif cmd_part[1] == 'on':
        op = 'on'
        pos1 = cmd_part[2]
        pos2 = cmd_part[4]
    elif cmd_part[1] == 'off':
        op = 'off'
        pos1 = cmd_part[2]
        pos2 = cmd_part[4]
    #把坐标字符串转为包含两个元素的列表
    pos1_list = pos1.split(',')  # "0,0" → ["0", "0"]
    x1 = int(pos1_list[0])
    y1 = int(pos1_list[1])
    pos2_list = pos2.split(',')
    x2 = int(pos2_list[0])
    y2 = int(pos2_list[1])
# 第四步 计算坐标范围
    # 遍历所有x：range左闭右开）
    for current_x in range(x1, x2 + 1):
        for current_y in range(y1, y2 + 1):
            # 【5. 定义开关规则】
            if op == 'on':
                light_grid[current_x][current_y] = True
            elif op == 'off':
                light_grid[current_x][current_y] = False
            elif op == 'toggle':
                if light_grid[current_x][current_y] == True:
                    light_grid[current_x][current_y] = False
                else:
                    light_grid[current_x][current_y] = True

#第五步 统计最终亮着的灯数
on_count = 0
for x in range(1000):
    for y in range(1000):
        if light_grid[x][y] == True:
            on_count += 1

print('最终亮起的灯总数：', on_count)

