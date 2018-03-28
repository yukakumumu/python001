print("--- 001 --------------------------------------------------")
list_x = ["aaa","bbb","ccc"]
for i in list_x:
	print(i)

for i in range(5):
	print(i)

for i in range(500,550,10):
	print(i)

for i in range(3):
	print(i)
else:
	print("end")

for x,y in enumerate(list_x,1):
	print(f"{x}/{y}")

list_x = [10,20,30]
list_y = [40,50,60]
for x,y in zip(list_x, list_y):
	print(x,y)

print("--- 002 イテラブルの内包表記 --------------------------------------------------")
print([i*2 for i in [1,2,3]])
print([i*2 for i in "ABC"])
print([x+y for x,y in zip("ABC","XYZ")])
print([i for i in range(5)])
print([i for i in [1,2,3] if i>1])

z = [[1,2],[1,2],[1,2]]
print([x for y in z for x in y])
result = []
for y in z:
	for x in y:
		result.append(x)
print(result)

print([[x for x in y] for y in z])
result_z = []
for y in z:
	result_y = []
	for x in y:
		result_y.append(x)
	result_z.append(result_y)
print(result_z)
