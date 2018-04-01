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
