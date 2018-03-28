x=100
if x<50:
	y= "val001"
elif x<120:
	y = "val002"
elif (x>=120) and (x<500):
	y = "val003"
elif 600<x<700:
	y = "val004"
elif x<800:
	y = "val005"
else:
	y = "val006"
print(y)

x = ""
if not x:
	y = True
else:
	y = False
print(y)

x = 10
y = 100 if x<20 else 200 #3項演算子のかわり
print(y)

