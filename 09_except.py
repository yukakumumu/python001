print("--- 001 -------------------------------------------------")
try:
	print(a)
except:
	print("except")


print("--- 002 -------------------------------------------------")
try:
	print(1/0)
except (ValueError, ZeroDivisionError):
	print("except_ValueError or except_ZeroDivisionError")
finally:
	print("finally")


print("--- 003 -------------------------------------------------")
try:
	print(1/0)
except ValueError:
	print("except_ValueError")
except ZeroDivisionError:
	print("except_ZeroDivisionError")
else:
	print("else")
finally:
	print("finally")

print("--- 004 -------------------------------------------------")
try:
	print(1/0)
except Exception as x:
	print(x)
