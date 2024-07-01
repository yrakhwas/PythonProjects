userMessage = "Hello"
userMessageEnc = userMessage.encode("utf-8")
print(userMessageEnc)
decodeUserMessage = userMessageEnc.decode("utf-8")
print(decodeUserMessage)

stringNew = '''It is my 
new string which 
i want to show you'''
print(stringNew)

stringN = "Pythonb"
# print(stringN[0])
# print(stringN[1])
# print(stringN[2])
# print(stringN[-1])
print(len(stringN))

# newStr = " !!!"
# stringN += " to you".join(newStr)
print(stringN)
print(stringN.capitalize())
print(stringN.title())
print(stringN.swapcase())
# print(stringN.lower())
# print(stringN.upper())
print(stringN)


a = 'b'
print("Count of b " ,stringN.count(a))
print(stringN.find('m'))
print(stringN.startswith("Hello"))
print(stringN.endswith("bYe"))

print(stringN.isalnum())
print(stringN.isalpha())
print(stringN.isdigit())
print(stringN.isspace())

print(stringN.center(5))
print(stringN[:-1:2])


b= "Yurii"
print(f"Hello {b}")
print("Hello {b}, {a}".format(b = "Yurii",a = "b"))

pi = 3.1415926535
print("Your pi is {0:2.2f}".format(pi))


stru = input("Enter your string you want to reverse : ")
print(stru[::-1])


countD = 0
countL = 0
someString = input("Enter your string : ")
for i in someString:
    if i.isdigit():
        countD+=1
    elif i.isalpha():
        countL+=1
print(f"Count of letters is {countL}")
print(f"Count of digits is {countD}")