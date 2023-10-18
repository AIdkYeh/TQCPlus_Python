"""
TQC+ 程式語言Python 104 圓形面積計算

請撰寫一程式，輸入一圓的半徑，並加以計算此圓之面積和周長，
最後請印出此圓的半徑（Radius）、周長（Perimeter）和面積（Area）。
提示1：需import math模組，並使用math.pi。
提示2：輸出浮點數到小數點後第二位。

Input:
10

Output:
Radius = 10.00
Perimeter = 62.83
Area = 314.16
"""

# TODO
import math
radius = eval(input())

# TODO
print("Radius = {:.2f}".format(radius))
print("Perimeter = {:.2f}".format(2*radius*math.pi))
print("Area = {:.2f}".format(radius**2*math.pi))

"""
Radius = _
Perimeter = _
Area = _
"""

import math
r = eval(input("請輸入圓的半徑r:"))
# 圓面積 math.pi*r**2
Area = math.pi*r**2
# 圓周長 2*math.pi*r
Perimeter = 2 * math.pi * r

print(f"Radius = {r:.2f}")
print(f"Perimeter = {Perimeter:.2f}")
print(f"Area = {Area:.2f}")
