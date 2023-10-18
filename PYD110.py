"""
TQC+ 程式語言Python 110 正n邊形面積計算

請撰寫一程式，讓使用者輸入兩個正數n、s，代表正n邊形之邊長為s，
計算並輸出此正n邊形之面積（Area）。
提示1：建議使用import math模組的math.pow及math.tan
提示2：正n邊形面積的公式如下：Area=(n∗s^2)/(4∗tan(pi/n)) 
提示3：輸出浮點數到小數點後第四位

Input:
8
6

Output:
Area = 173.8234
"""

# TODO
import math
# n = eval(input())
# s = eval(input())
n,s = eval(input("請輸入正n邊形:")),eval(input("請輸入邊長s:"))
area = (n*s**2)/(4*math.tan(math.pi/n))
# TODO
print("Area = {:.4f}".format(area))
print(f"Area = {area:.4f}")

#Area = _
