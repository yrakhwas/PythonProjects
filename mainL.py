import random



category = ["Drama", "Comedy","Horor", "Fantasy", True, 3.14, 1234]
print(type(category))
category1 = list(["Math", "Histiry","PE"])
print(category1)
myList = [1, 3.14, "Hello", True,[[4,5,6,7,8,9],2,3,4,5]]
print(myList)
myArr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
print(myArr[1][1])

positionX = 0
positionY = 0
for i in myArr:
    for j in i:
        if j ==7:
            print(f"Your number find in {positionX, positionY}")
    positionX+=1
    positionY+=1

myGeneratedList = [i*5 for i in "Hello"]
print(myGeneratedList)



print(category[-1])
print(len(category))
category[4] = "Sell"
print(category)

list1 = [11,275,36,4,35,65,7]
list2 = [8,92,10,11,123,133,14]

list3 = list1+list2
print(list3)
print(max(list3))
print(min(list3))
print(sum(list3))
list3.sort(reverse=True)
print(list3)

for i in range(len(list3)):
    print(list3[i])


list3.append("Hello")
print(list3)
print(list3.index("Hello"))
print(list3.count("Hello"))
list3.extend(category)
print(list3)
list3.insert(1,"Not hello")
print(list3)
list3.pop()
print(list3)
list3.insert(0,"Hello")
print(list3)

print("Hello" in list3)
# myStr = "Hello my dear friend"
# myList = myStr.split()
# print(myList)


myRandomNum = [random.randint(-10,10) for i in range(20)]
print(myRandomNum)


rand = random.randint(-100,100)
print(rand)
