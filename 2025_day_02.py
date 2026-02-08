# Part1 first version_wrong output
# with open('input/2025_day_02.txt','r') as f:
#     input=f.read().split(',')
#     def function_part1(data):
#         for item in data:
#             item_apart=item.split('-')
#             item_apart=item_apart.strip()
#             if item_apart:
#                 x=item.split('-')[0]
#                 y=item.split('-')[1]
#                 for number in range(x:y+1):
#                     if len(number)%2==0:
#                         while int(number[0:len(number)%2-1])==int(number[len(number)%2-1:len(number)-1]):
#                             return number
# function_part1(input)

# Second version
def function_part1_sum(data):
    total = 0
    for item in data:
        item = item.strip()
        if item:
            parts = item.split('-')
            start = int(parts[0])
            end = int(parts[1])
            for number in range(start, end + 1):
                s_num = str(number)
                length = len(s_num)
                if length % 2 == 0:
                    mid = length // 2  # 计算中点
                    # 分割前后半段
                    first_half = s_num[:mid]
                    second_half = s_num[mid:]
                    if first_half == second_half:
                        # 3. 累加而不是返回
                        total += number
    return total
with open('input/2025_day_02.txt', 'r') as f:
    input_data = f.read().split(',')
    result = function_part1_sum(input_data)
    print(f"最终叠加值: {result}")