print("--- 001 --------------------------------------------------")
print(1,2,3)
print(1,2,3,sep="/",end="@")
print()
print("--- 002 配列の取り出し(スライス)--------------------------------------------------")
str_abc = "0123456789"
print(str_abc[0])
print(str_abc[-1])
print(str_abc[:2])
print(str_abc[2:])
print(str_abc[2:4])
print(str_abc[0:5:2])
print(str_abc[::-1])
print([1,2,3,4,5][2:])
print([1,2,3,4,5][2:])
print("--- 003 --------------------------------------------------")
print(1,2,3)
print([1,2,3])
print(range(3))
print("--- 004 リスト作成 --------------------------------------------------")
print([1,2,3])
print([3,"a",True])
print([5]*10)
print(["A","B"]*5)
print(list(range(0,3))) # range -> list
print(list(range(-6,6,2))) # range -> list
print(list("abc")) # str -> list
print(list())
print("aaa/bbb/ccc".split("/"))
print("/".join(["a","b","c"]))
print(["a","b","c"] + ["x","y"])
print("--- 005 リスト要素 --------------------------------------------------")
list_x=["A","B","C"]
print(list_x[0])
print(list_x[-1])
list_x[0]="X" # リストはミュータブル（変更可能）
print(list_x)
print("--- 006 多重要素 --------------------------------------------------")
list_y = [["0-0","0-1","0-2"],["1-0","1-1","1-2"]]
print(list_y[1][1])
print("--- 007 要素の追加・削除 --------------------------------------------------")
list_z = []
list_z.append("a0")
list_z.append("a1")
list_z.append("a2")
list_z.append("a3")
list_z.append("a4")
list_z.append("a5")
list_z.append("ax")
list_z.append("a6")
list_z.append("a7")
list_z.append("a8")
list_z.append("a9")
list_z.append("a10")
list_z.insert(0,"i0")
list_z.pop(1)
list_z.pop()
list_z.remove("ax")
del list_z[5]
print(list_z)

del list_z
list_empty = []
if not list_empty:
	print("空です")

print("--- 008 ソート --------------------------------------------------")
list_x = [3,1,2]
list_x.sort()
print(list_x)

list_x.sort(reverse = True)
print(list_x)

list_y = [3,1,2]
print(sorted(list_y))

list_x = ["aaa","a","aa"]
list_x.sort(key = len)
print(list_x)

print("--- 009 逆 --------------------------------------------------")
list_x = [1,2,3]
list_x.reverse()
print(list_x)

print("--- 010 ループ --------------------------------------------------")
list_x = ["a","b","c","d"]
for x,y in enumerate(list_x,1):
	print(f"{x}/{y}")

list_x = ["a","b","c"]
for x in list_x:
	print(f"{x}")

print("--- 011 検索 --------------------------------------------------")
print("c" in ["a","b","c","d","e"])
print("c" not in ["a","b","c","d","e"])
print(["a","b","c","d","e"].index("c"))
print(["a","b","c","d","e"].count("c"))

print("--- 012 組み込み関数 --------------------------------------------------")
list_n = [1,2,3,4,5]
print(sum(list_n))
print(max(list_n))
print(min(list_n))
