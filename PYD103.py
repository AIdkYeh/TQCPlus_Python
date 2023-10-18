"""
TQC+ 程式語言Python 103 字串格式化輸出

請撰寫一程式，輸入四個單字，然後將這四個單字以欄寬為10、
欄與欄間隔一個空白字元、每列印兩個的方式，先列印向右靠齊，
再列印向左靠齊，左右皆以直線 |（Vertical bar）作為邊界。

Input:
I
enjoy
learning
Python

Output:
|         I      enjoy|
|  learning     Python|
|I          enjoy     |
|learning   Python    |
"""

#TODO
a=str(input())
b=str(input())
c=str(input())
d=str(input())

#向右靠齊
#TODO
print("|{:>10} {:>10}|".format(a,b))
print("|{:>10} {:>10}|".format(c,d))
#向左靠齊
#TODO
print("|{:<10} {:<10}|".format(a,b))
print("|{:<10} {:<10}|".format(c,d))



snum = list(map(str, input().split(',')))

print("|{:>10} {:>10}|".format(snum[0],snum[1]))
print("|{:>10} {:>10}|".format(snum[2],snum[3]))
print("|{:<10} {:<10}|".format(snum[0],snum[1]))
print("|{:<10} {:<10}|".format(snum[2],snum[3]))

#F-string
print(f"|{snum[0]:>10} {snum[1]:>10}|")
print(f"|{snum[2]:>10} {snum[3]:>10}|")
print(f"|{snum[0]:<10} {snum[1]:<10}|")
print(f"|{snum[2]:<10} {snum[3]:<10}|")