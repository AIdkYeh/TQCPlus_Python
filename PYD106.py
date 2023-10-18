"""
TQC+ 程式語言Python 106 公里英哩換算

假設一賽跑選手在x分y秒的時間跑完z公里，請撰寫一程式，輸入x、y、z數值，
最後顯示此選手每小時的平均英哩速度（1英哩等於1.6公里）。
提示：輸出浮點數到小數點後第一位。

Input:
10
25
3

Output:
Speed = 10.8
"""

x = eval(input())
y = eval(input())
z = eval(input())

# TODO
print("Speed = {:.1f}".format(z/1.6/((60*x+y)/3600)))


x, y, z = eval(input("請輸入幾分x:")), \
          eval(input("請輸入幾秒y:")), \
          eval(input("請輸入幾公里Z:"))

print(f"Speed = {z/1.6/((60*x+y)/3600):.1f} 英哩/小時")