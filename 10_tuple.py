print("--- 001 --------------------------------------------------")
tuple_n = (1,2)
print(tuple_n)

tuple_n = ((1,2),(1,2))
print(tuple_n)

tuple_n = (1,)
print(tuple_n)

tuple_n = 1,2
print(tuple_n)

print(tuple(range(3)))
print(tuple([1,2,3]))
print(tuple("abc"))

print("--- 002 アンパック--------------------------------------------------")
x,y = 1,2
print(x,y)

print("--- 003 zip --------------------------------------------------")
list_x = [1,2,3]
list_y = ["a001","a002","a003"]
zip_xy = zip(list_x, list_y)
print(list(zip_xy))
for x,y in zip(list_x, list_y):
	print(x,y)
