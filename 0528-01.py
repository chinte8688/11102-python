a,b,c,d = eval(input("請輸入 4 個數字以,號分開："))

print("您輸入的數字是：%d %d %d %d" % (a,b,c,d))
i = 0
swap = 0
while a > b or b > c or c > d :
    if a < b and b < c and c < d:
        print("第 %d 圈 %d %d %d %d 排序完畢02" % (i,a,b,c,d))
        break
    elif a > b or b > c and c > d: 
            #c > d     
         swap = c
         c = d
         d = swap
         i = i + 1
         print("第 %d 圈 %d %d %d %d " % (i,a,b,c,d))
         #continue
    elif a > b or b > c:    
            #b > c 
        #if a < b :
        #     continue 

          
         swap = b
         b = c
         c = swap
         i = i + 1
         print("第 %d 圈 %d %d %d %d " % (i,a,b,c,d))  
         #continue
    elif a > b :
            #a > b           
         swap = a
         a = b
         b = swap
         i = i + 1
         print("第 %d 圈 %d %d %d %d " % (i,a,b,c,d))
         #continue    
    else:     
        print("第 %d 圈 %d %d %d %d 排序完畢01" % (i,a,b,c,d))    
