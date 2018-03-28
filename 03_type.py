print("--- 001 --------------------------------------------------")
print(type(1))
print(type(1.1))
print(type("a"))
print("--- 002 コピーと参照--------------------------------------------------")
list_1 = [1]
list_2 = [1] #コピー
print("value:" + str(list_1 == list_2))
print(list_1 is list_2)
list_2 = list_1 #参照
print(list_1 is list_2)
list_2 = list_1.copy() #コピー
print(list_1 is list_2)
list_2 = list_1[:] #コピー
print(list_1 is list_2)
list_2 = list(list_1) #コピー
print(list_1 is list_2)
