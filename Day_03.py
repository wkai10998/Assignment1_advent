with open('input/day_03.txt', 'r') as file_object:
    input_text = file_object.read()
#part1
locations_x=0
locations_y=0
location=set()
location.add((locations_x, locations_y))
for i in input_text:
    if i == '^':
        locations_y+=1
    elif i =='v':
        locations_y-= 1
    elif i =='>':
        locations_x+=1
    elif i =='<':
        locations_x-=1
    location.add((locations_x, locations_y))
print(len(location))

#part2
index=0
odd_x=0
odd_y=0
even_x=0
even_y=0
location=set()
location.add((0, 0))
for i in input_text:
    index+=1
    if index%2==0:
        if i == '^':
            even_y+=1
        elif i =='v':
            even_y-= 1
        elif i =='>':
            even_x+=1
        elif i =='<':
            even_x-=1
        location.add((even_x, even_y))
    elif index%2==1:
        if i == '^':
            odd_y+=1
        elif i =='v':
            odd_y-= 1
        elif i =='>':
            odd_x+=1
        elif i =='<':
            odd_x-=1
        location.add((odd_x, odd_y))
print(len(location))
