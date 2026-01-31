with open('input/day_01.txt', 'r') as file_object:
    input_text = file_object.read()
#first question
floor=0
for i in input_text:
  if i=="(":
    floor=floor+1
  elif i==")":
    floor-=1
print(floor)

#second question
floor=0
position=0
for i in input_text:
  position+=1
  if i=="(":
    floor=floor+1
  elif i==")":
    floor-=1
  if floor==-1:
    print(position)
    break