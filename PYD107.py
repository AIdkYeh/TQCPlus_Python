"""
TQC+ 程式語言Python 107 數值計算

請撰寫一程式，讓使用者輸入五個數字，計算並輸出這五個數字之數值、總和及平均數。
提示：總和與平均數皆輸出到小數點後第1位。

Input:
88.7
12
56
132.55
3

Output:
88.7 12 56 132.55 3
Sum = 292.2
Average = 58.5
"""
num1 = eval(input())
num2 = eval(input())
num3 = eval(input())
num4 = eval(input())
num5 = eval(input())

# TODO
print("{} {} {} {} {}".format(num1,num2,num3,num4,num5))
print("Sum = {:.1f}".format(num1+num2+num3+num4+num5))
print("Average = {:.1f}".format((num1+num2+num3+num4+num5)/5))
# Sum = _
# Average = _


num = list(map(eval, input().split(',')))

# for i in num:
#     print(i, end = '')
print(" ".join(str(i) for i in num))
print(f"Sum = {sum(num):.1f}")
print(f"Average = {sum(num)/len(num):.1f}")