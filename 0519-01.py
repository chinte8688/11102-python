a,b,c = eval(input("請輸入3個數字以,號分開："))
# d = int(a) + int(b) + int(c)
# print("d = %d " % (d))

if a < b and b < c :
        print("%d %d %d 排序完畢" % (a,b,c))
else : 
    i = 0
    swap = 0 
    print("第 %d 圈 %d %d %d" % (i,a,b,c))
    while a > b or b > c:
        swap = a
        a = b
        b = swap
        i = i + 1
        print("第 %d 圈 %d %d %d" % (i,a,b,c))
        break
        #while


    # print("%d %d %d" % (a,b,c))
        
    #    if a < b 
    #    print("%d %d %d 排序完畢" % (a,b,c))
    #   reak
    