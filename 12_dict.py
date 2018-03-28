print("--- 001 --------------------------------------------------")

dict_1 = {
	"key1":1,
	"key2":2,
	"key3":3
	}
print(dict_1)

list_1 = [
	("key1",1),
	("key2",2),
	("key3",3)
	]
dict_1 = dict(list_1)
print(dict_1)

tuple_1 = (
	("key1",1),
	("key2",2),
	("key3",3)
	)
dict_1 = dict(tuple_1)
print(dict_1)

list_1 = [
	["key1",1],
	["key2",2],
	["key3",3]
	]
dict_1 = dict(list_1)
print(dict_1)

print("--- 002 zip --------------------------------------------------")

keys = ["key1", "key2", "key3"]
vals = [1,2,3]
dict_1 = dict(zip(keys,vals))
print(dict_1)

keys = ("key1", "key2", "key3")
vals = (1,2,3)
dict_1 = dict(zip(keys,vals))
print(dict_1)

keys = ["key1", "key2", "key3"]
vals = [1,2,3]
dict_1 = dict(zip(keys,vals))
print(dict_1)

print("--- 003 キーワード引数 --------------------------------------------------")

dict_1 = dict(
	key1=1,
	key2=2,
	key3=3
	)
print(dict_1)

print("--- 004 fromkeys --------------------------------------------------")

dict_1 = dict.fromkeys(
	[
		"key1",
		"key2",
		"key3"
	],
	0
	)
print(dict_1)

print("--- 005 内包表現 --------------------------------------------------")

dict_1 = {i:0 for i in ["key1","key2","key3"]}
print(dict_1)

print("--- 006 更新/追加 --------------------------------------------------")

dict_1 = {"key1":1, "key2":2, "key3":3}
dict_1["key4"]=100 #あれば更新、なければ追加
print(dict_1)

dict_1 = {"key1":1, "key2":2, "key3":3}
dict_1.setdefault("key4", 100) #あれば更新、なければ追加
print(dict_1)

dict_1 = {"key1":1, "key2":2}
dict_2 = {"key2":200, "key3":300}
dict_1.update(dict_2)
print(dict_1)

print("--- 007 削除 --------------------------------------------------")
dict_1 = {"key1":1, "key2":2, "key3":3}
del dict_1["key2"]
print(dict_1)

dict_1 = {"key1":1, "key2":2, "key3":3}
dict_1.clear()
print(dict_1)

print("--- 008 複製 --------------------------------------------------")
dict_1 = {"key1":1, "key2":2, "key3":3}
dict_2 = dict_1.copy()
print(dict_1 is dict_2)
print(dict_2)

dict_1 = {"key1":1, "key2":2, "key3":3}
dict_2 = dict_1.fromkeys(dict_1, 0)
print(dict_1 is dict_2)
print(dict_2)

print("--- 009 取得 --------------------------------------------------")
dict_1 = {"key1":1, "key2":2, "key3":3}
print(dict_1["key2"]) # なければexception

dict_1 = {"key1":1, "key2":2, "key3":3}
print(dict_1.get("key2")) # なくてもexceptionにならない
print(dict_1.get("key4")) # なくてもexceptionにならない

dict_1 = {"key1":1, "key2":2, "key3":3}
print("key1" in dict_1)

for key in dict_1:
	print(key)

for key,value in dict_1.items():
	print(key,value)

print(list(dict_1.keys()))
print(list(dict_1.values()))
print(list(dict_1.items()))

print([key for key in dict_1])
print([dict_1[key] for key in dict_1])
print([(key,dict_1[key]) for key in dict_1])

print("--- 010 取り出して削除 --------------------------------------------------")
dict_1 = {"key1":1, "key2":2, "key3":3}
dict_1.pop("key2")
print(dict_1)

dict_1 = {"key1":1, "key2":2, "key3":3}
while dict_1:
	print(dict_1.popitem())

