print("--- 001 set --------------------------------------------------")
set_1 = {1,2}
print(set_1)

set_empty = set()
print(set_empty)

set_1 = {1,1,2,2,3,3}
print(set_1)

set_1.add(4)
print(set_1)

set_1.remove(1) #無ければエラー
print(set_1)

set_1.discard(1) #無くてもエラーにならない
print(set_1)

set_1.clear()
print(set_1)

print("--- 002 frozenset --------------------------------------------------")
fset_1 = frozenset([1,2,3])
print(fset_1)

print("--- 003 集合演算 --------------------------------------------------")
set_A = {1,2}
set_B = {2,3}
print(set_A & set_B)
print(set_A | set_B)
print(set_A - set_B)
print(set_A ^ set_B)

print("--- 004 --------------------------------------------------")
set_A = {"a","b"}
set_B = {"b","c"}
print(set_A.intersection(set_B))

set_A = {"a","b"}
set_B = {"b","c"}
print(set_A.union(set_B))

set_A = {"a","b"}
set_B = {"b","c"}
print(set_A.difference(set_B))

set_A = {"a","b"}
set_B = {"b","c"}
print(set_A.symmetric_difference(set_B))

print("--- 005 --------------------------------------------------")
set_A = {"a","b"}
set_B = {"b","c"}
set_A.update(set_B)
print(set_A)

set_A = {"a","b"}
set_B = {"b","c"}
set_A |= set_B
print(set_A)

print("--- 006 --------------------------------------------------")
set_A = {"a","b"}
set_B = {"b","c"}
set_A.intersection_update(set_B)
print(set_A)

set_A = {"a","b"}
set_B = {"b","c"}
set_A &= set_B
print(set_A)

print("--- 007 --------------------------------------------------")
set_A = {"a","b"}
set_B = {"b","c"}
set_A.difference_update(set_B)
print(set_A)

set_A = {"a","b"}
set_B = {"b","c"}
set_A -= set_B
print(set_A)

print("--- 008 --------------------------------------------------")
set_A = {"a","b"}
set_B = {"b","c"}
set_A.symmetric_difference_update(set_B)
print(set_A)

set_A = {"a","b"}
set_B = {"b","c"}
set_A ^= set_B
print(set_A)

print("--- 009 比較 --------------------------------------------------")
set_A = {"a","b"}
set_B = {"b","a"}
print(set_A == set_B)
print(set_A != set_B)

set_A = {"a","b"}
set_B = {"b","c"}
print(set_A.isdisjoint(set_B)) #接点が無いときにtrueなので注意！

set_A = {"a"}
set_B = {"a","b"}
print(set_A.issubset(set_B)) #含まれる
print(set_A <= set_B) #含まれる
print(set_A.issuperset(set_B)) #含まれる
print(set_A >= set_B) #含まれる


