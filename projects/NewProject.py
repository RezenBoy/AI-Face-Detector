import json

f = open('newproj.json')
data = json.load(f)
x=data['question']
x2=data['options']
x3=data['answer']
g=x[0]
g2=x2[0]
g3=x3[0]
print(g)
for i in g2:
    print("o ",i)
f.close()
x=int(input("Enter your choice(1,2,3,4): "))
if(x==g3):
    print("Correct")
else:
    print("Wrong")