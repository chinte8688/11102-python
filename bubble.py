
a,b,c,d = eval(input("請輸入 4 個數字以,號分開："))
# d = int(a) + int(b) + int(c)
# print("d = %d " % (d))
print("您輸入的數字是：%d %d %d %d" % (a,b,c,d))
i = 0
swap = 0

while True :
    if a < b and b < c and c < d :
        print("第 %d 圈 %d %d %d %d 排序完畢01" % (i,a,b,c,d))
        break
    elif c > d :         
        swap = c
        c = d
        c = swap
        i = i + 1
        print("第 %d 圈 %d %d %d %d " % (i,a,b,c,d))
        #continue
    elif b > c :         
        swap = b
        b = c
        c = swap
        i = i + 1
        print("第 %d 圈 %d %d %d %d " % (i,a,b,c,d))
        #continue
    elif a > d :         
        swap = a
        a = b
        a = swap
        i = i + 1
        print("第 %d 圈 %d %d %d %d " % (i,a,b,c,d))
        #continue
    else:
        print("第 %d 圈 %d %d %d %d 排序完畢02" % (i,a,b,c,d))
        #continue
    #else:
    #    print("第 %d 圈 %d %d %d %d 排序完畢02" % (i,a,b,c,d))
        #continue
        #break