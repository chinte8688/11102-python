a,b,c,d,e = eval(input("請輸入 5 個數字以[,]號分開："))

print("您輸入的數字為 %d %d %d %d %d" % (a,b,c,d,e))
i = 0
j = 0
swap = 0

while True:    
    if a < b and b < c and c < d and d < e:
        print("第%02d圈%02d次交換 %d %d %d %d %d 排序完畢01" % (i,j,a,b,c,d,e))
        break
    else : 
        i += 1
        if a > b or b > c or c > d or d > e: 
           if d > e :     
              swap = d
              d = e
              e = swap
              j += 1
              
              if a < b and b < c and c < d and d < e:
                print("第%02d圈%02d次交換 %d %d %d %d %d 排序完畢02" % (i,j,a,b,c,d,e))
                break
              else:
                print("第%02d圈%02d次交換 %d %d %d %d %d" % (i,j,a,b,c,d,e))
        else:
            continue
        if a > b or b > c or c > d: 
           if c > d :     
              swap = c
              c = d
              d = swap
              j += 1
              print("第%02d圈%02d次交換 %d %d %d %d %d" % (i,j,a,b,c,d,e))
        else:
            continue
        if a > b or b > c:      
            if b > c:
               swap = b
               b = c
               c = swap
               j += 1
               print("第%02d圈%02d次交換 %d %d %d %d %d" % (i,j,a,b,c,d,e))
        else:    
            continue
        if a > b :          
            swap = a
            a = b
            b = swap
            j += 1
            print("第%02d圈%02d次交換 %d %d %d %d %d" % (i,j,a,b,c,d,e))
        else:
            continue 