"""
TQC+ 程式語言Python 105 矩形面積計算

請撰寫一程式，輸入兩個正數，代表一矩形之寬和高，
計算並輸出此矩形之高（Height）、寬（Width）、周長（Perimeter）及面積（Area）。
提示：輸出浮點數到小數點後第二位。

Input:
23.5
19

Output:
Height = 23.50
Width = 19.00
Perimeter = 85.00
Area = 446.50
"""

# TODO

h = eval(input())
w = eval(input())

# TODO

print("Height = {:.2f}".format(h))
print("Width = {:.2f}".format(w))
print("Perimeter = {:.2f}".format(2*(h+w)))
print("Area = {:.2f}".format(h*w))



h, w = eval(input("請輸入矩形的高H:")),eval(input("請輸入矩形的寬W:"))

print(f"Height = {h:.2f}")
print(f"Weight = {w:.2f}")
print(f"Perimeter = {(h+w)*2:.2f}")
print(f"Area = {h*w:.2f}")