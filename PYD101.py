"""
TQC+ 程式語言Python 101 整數格式化輸出

請撰寫一程式，輸入四個整數，然後將這四個整數以欄寬為5、欄與欄間隔一個空白字元，
再以每列印兩個的方式，先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。
85 4 299 478

|   85     4|
|  299   478|
|85    4    |
|299   478  |
"""
#TODO
a=eval(input())
b=eval(input())
c=eval(input())
d=eval(input())

#向右靠齊
#TODO
print("|{:>5} {:>5}|".format(a,b))
print("|{:>5} {:>5}|".format(c,d))
#向左靠齊
#TODO
print("|{:<5} {:<5}|".format(a,b))
print("|{:<5} {:<5}|".format(c,d))


num = list(map(int,input().split(',')))

print("|{:>5d} {:>5d}|".format(num[0],num[1]))
print("|{:>5d} {:>5d}|".format(num[2],num[3]))
print("|{:<5d} {:<5d}|".format(num[0],num[1]))
print("|{:<5d} {:<5d}|".format(num[2],num[3]))

#F-string
print(f"|{num[0]:>5d} {num[1]:>5d}|")
print(f"|{num[2]:>5d} {num[3]:>5d}|")
print(f"|{num[0]:<5d} {num[1]:<5d}|")
print(f"|{num[2]:<5d} {num[3]:<5d}|")


