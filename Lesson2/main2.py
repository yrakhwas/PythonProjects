import math

math.pi


month = input("Enter month you want know : ")
match month:
    case 1 | "1":
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case 13 | "13" | 24:
        print("hello world")
    case _:
        print("Invalid month number")
# if(month==1):
#     print("January")
# elif(month==2):
#     print("February")
# elif(month==3):
#     print("March")
# elif(month==4):
#     print("April")
# elif(month==5):
#     print("May")
# elif(month==6):
#     print("June")
# elif(month==7):
#     print("July")
# elif(month==8):
#     print("August")
# elif(month==9):
#     print("September")
# elif(month==10):
#     print("October")
# elif(month==11):
#     print("November")
# elif(month==12):
#     print("December")
# else:
#     print("Invalid month number")


# print(10>5)
# print(10<5)
# print(10==5)
# print(10!=5)
# a = 30
# if(a%2==0):
#     print("Even")
# if(a%3==0):
#     print("Dividible by 3 without rest")
# else:
#     print("Odd number")
# salary = int(input("Enter your salary : "))
# salary = bool(salary)
# print(salary)
# num = " "
# num = bool(num)
# print(num)