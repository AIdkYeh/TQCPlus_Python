"""
TQC+ 程式語言Python 102 浮點數格式化輸出

請撰寫一程式，輸入四個分別含有小數1到4位的浮點數，
然後將這四個浮點數以欄寬為7、欄與欄間隔一個空白字元、每列印兩個的方式，
先列印向右靠齊，再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。
提示：輸出浮點數到小數點後第二位。

23.12
395.3
100.4617
564.329

|  23.12  395.30|
| 100.46  564.33|
|23.12   395.30 |
|100.46  564.33 |

"""
#TODO
a=eval(input())
b=eval(input())
c=eval(input())
d=eval(input())

#向右靠齊
#TODO
print("|{:>7.2f} {:>7.2f}|".format(a,b))
print("|{:>7.2f} {:>7.2f}|".format(c,d))
#向左靠齊
#TODO
print("|{:<7.2f} {:<7.2f}|".format(a,b))
print("|{:<7.2f} {:<7.2f}|".format(c,d))


fnum = list(map(float, input().split(',')))

print("|{:>7.2f} {:>7.2f}|".format(fnum[0],fnum[1]))
print("|{:>7.2f} {:>7.2f}|".format(fnum[2],fnum[3]))
print("|{:<7.2f} {:<7.2f}|".format(fnum[0],fnum[1]))
print("|{:<7.2f} {:<7.2f}|".format(fnum[2],fnum[3]))

#F-string
print(f"|{fnum[0]:>7.2f} {fnum[1]:>7.2f}|")
print(f"|{fnum[2]:>7.2f} {fnum[3]:>7.2f}|")
print(f"|{fnum[0]:<7.2f} {fnum[1]:<7.2f}|")
print(f"|{fnum[2]:<7.2f} {fnum[3]:<7.2f}|")
