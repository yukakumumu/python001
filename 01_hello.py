print("aaa")

a=100
print(a)

b=a+100
print(b)

#セミコロン
c=10;d=10;e=c+d
print(e)

#改行
f= 10 + 10 + 10 + \
   10 + 10 + 10 
print(f)

"""
ブロックコメント
"""
print("---------------------------------------------------")
print(round(1.66666666,3))
print(0b11111111)
print(bin(8))
print(0xff)
print(hex(16))
print("---------------------------------------------------")
print(10 / 3)
print(10 // 3)
print(10 % 6)
print(2 ** 3)
print("---------------------------------------------------")
print('aaa"bbb"aaa')
print("aaa'bbb'aaa")
print("aaa\taaa\naaaaaaaaaaaaaaaaaa")
print("aaa\"aaa\aaaaaaaaaaaaaaaaa")
print("---------------------------------------------------")
print("aaa"+str(1000))
print("abc" * 10)

str_abc = "abc"
print(str_abc[2])
print("文字列はイミュータブル")

print("-------------------------------------------------------------")
print(1==1)
print(True and True)
print(True and False)
print(True or False)
print(not True)
print(not False)
print(not 1)
print(not 0)
print(1 or 2)
print("-------------------------------------------------------------")
print(bin(0b11 & 0b110))
print(bin(0b11 | 0b110))
print(bin(0b11 ^ 0b110))
print(bin(~ 0b1111))
print(bin(0b1 << 3))
print("-------------------------------------------------------------")
print(chr(97))
print(ord("a"))
print("-------------------------------------------------------------")
print("aaa{}aaa{}aaa{}aaa".format(1,2,3))
print("aaa{2}aaa{1}aaa{0}aaa".format(1,2,3))
format_x = 10
format_y = 20
format_z = 30
print(f"aaa{format_x}aaa{format_y}aaa{format_z}aaa") #Fフォーマット
print("{:,}".format(1000000)) #3桁位取り
print(f"{2000000:,}") #3桁位取り
print("{:.2f}".format(10.0000)) #小数点以下２桁
print("{:>10}".format(1000)) #右寄せ10文字
print("%s%s%s"%("aaa","bbb","ccc")) #%形式
x="{:>3}" #3桁右詰め
print(x.format(5))
print("-------------------------------------------------------------")
numx=1000
print(isinstance(numx, (int,float))) #対象がintかfloatか？ → 数値チェック
strx="a"
print(isinstance(strx, (str)))
