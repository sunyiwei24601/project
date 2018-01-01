import json
num=[0 for i in range(0,7)]
with open("user_details.txt") as f:
    num[0]=json.load(f)
with open("user_details2.txt") as f:
    num[1]=json.load(f)
with open("user_details100-200.txt") as f:
    num[2]=json.load(f)
with open("user_details164-200.txt") as f:
    num[3]=json.load(f)
with open("user_details200-300.txt") as f:
    num[4]=json.load(f)
with open("user_details300-400.txt") as f:
    num[5]=json.load(f)
with open("user_details400-500.txt") as f:
    num[6] = json.load(f)
details=[]
for n in num:
    for i in n:
        details.append(i)

with open("user_details1-500.txt","w") as f:
    json.dump(details,f)