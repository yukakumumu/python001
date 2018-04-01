# モジュールを読み込む(モジュール名を省略)
# from モジュール import 関数
# from モジュール import 関数 as エイリアス
# 関数()

from math import floor
print(floor(10.3))

from pac003 import mod004
AAA = mod004.ClsAAA(100)
print(AAA.x)
