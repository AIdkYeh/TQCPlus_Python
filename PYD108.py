"""
TQC+ 程式語言Python 108 座標距離計算

請撰寫一程式，讓使用者輸入四個數字x1、y1、x2、y2，
分別代表兩個點的座標(x1, y1)、(x2, y2)。計算並輸出這兩點的座標與其歐式距離。
提示1：歐式距離=√((x1−x2)^2+(y1−y2)^2)
提示2：兩座標的歐式距離，輸出到小數點後第4位

Input:
2
1
5.5
8

Output:
( 2 , 1 )
( 5.5 , 8 )
Distance = 7.8262
"""

# TODO
x1=eval(input())
y1=eval(input())
x2=eval(input())
y2=eval(input())
d= ((x1-x2)**2+(y1-y2)**2)**0.5
print("( {} , {} )".format(x1,y1))
print("( {} , {} )".format(x2,y2))
print("Distance = {:.4f}".format(d))

#Distance = _

num = list(map(eval, input("請輸入座標x1,y1,x2,y2:").split(',')))
d = ((num[0]-num[2])**2+(num[1]-num[3])**2)**(0.5)

print(f"( {num[0]} , {num[1]} )")
print(f"( {num[2]} , {num[3]} )")
print(f"Distance = {d:.4f}")

