print("--- 001 関数オブジェクト --------------------------------------------------")
def func001():
    print("func001")
    return
x = func001
x()

def func002(f,x):
    f(x)
def f001(x):
    print(x)
func002(f001,4)

print("--- 002 クロージャ --------------------------------------------------")
def main(x):
    def sub(y):
        return x*y
    return sub
main5 = main(5)
print(main5(100))

print("--- 003 ラムダ式 --------------------------------------------------")
lambda003 = lambda x:print(x)
lambda003(100)

(lambda x:print(x))(100)

lambda004 = lambda x,y:print(x,y)
lambda004(10,100)

lambda005 = lambda x=500:print(x)
lambda005()

print("--- 004 ソート --------------------------------------------------")
input_list=["L","M","S","M","L","S","M","L","S"]
input_list.sort(key=(lambda x:["S","M","L"].index(x)))
print(input_list)

print("--- 005 マップ --------------------------------------------------")
input_list=[1,2,3]
print(list(map(lambda x:x*2, input_list)))

print("--- 006 フィルター --------------------------------------------------")
input_list=[1,4,-3,-2,0,6]
print(list(filter(lambda x:x>0, input_list)))
