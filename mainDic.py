# myDict = dict()
# print(type(myDict))
# myDict2 = {"Developer":"Dmitro"}
# print(type(myDict2))


# myDict3 = {"Macbook":"Pro", "Developer":"Olexandr", "Iphone":"15 Pro", 1: "Hello world", "1":"Hello to you"}
# print(myDict3)

# myDict3["Key"] = "Castle"
# # value = input("Enter value you want to add : ")
# # key = input("Enter key for your value")

# # myDict3[key] = value
# myDict3.update(myDict2)

# print(myDict3)


# mydict4 = dict.fromkeys(("One", "Two", "Three", "Four"),1)
# print(mydict4)

# print(myDict3.keys())
# print(myDict3.values())
# print(myDict3.items())
# print(myDict3.get("Developer"))
# print(myDict3.setdefault("Developer2"))
# print(myDict3)

# print(myDict3.pop("Developer"))
# print(myDict3)
# print(myDict3.popitem())
# print(myDict3)

my_dict = {"Mark": {"Phone":"0973421423""Hello", "Instagram":"@mark228","tiktok":"@mark777"}, 
           "Andrii":{"Phone":"0634411214", "Instagram":"@andrii228","tiktok":"@andrii777"}, 
           "Sasha": {"Phone":"0973689295", "Instagram":"@sasha228","tiktok":"@sasha777"}}

user = my_dict[input("Enter name : ")][input("Enter data you wanna know : ")]
print(user)