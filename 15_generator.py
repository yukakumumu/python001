print("--- 001 ジェネレータ-------------------------------------------------------")
def gene_abc():
	yield "A"
	yield "B"
	yield "C"
gene_abc001 = gene_abc()
print([x for x in gene_abc001])

print("--- 002 next -------------------------------------------------------------")
def gene_loop():
	n=0
	while True:
		yield n
		n += 1
gene_loop001 = gene_loop()
for x in range(3):
	print(next(gene_loop001))

print("--- 003  ジェネレータ式 ---------------------------------------------------")
gene_sk = (x*2 for x in range(10))
for x in range(3):
	print(next(gene_sk))
print(list(gene_sk))

print("--- 004  send ---------------------------------------------------")
def gene_send():
	n=0
	while True:
		r = yield n
		if r:
			n = r
gene_send001 = gene_send()
print(next(gene_send001))
print(next(gene_send001))
print(next(gene_send001))
print(gene_send001.send(100))
print(next(gene_send001))
print(next(gene_send001))

print("--- 005  sub ---------------------------------------------------")
def gene_main():
	yield from range(3)
	yield from "abc"
	yield from [10,20,30]
	yield "end"
gene_main001 = gene_main()
print(list(gene_main001))

def gene_sub():
	yield "A"
	yield "B"
	yield "C"
def gene_main2():
	yield from [10,20,30]
	yield from gene_sub()
gene_main2_001 = gene_main2()
print(list(gene_main2_001))
