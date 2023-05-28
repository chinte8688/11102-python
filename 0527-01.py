#numbers = input("請輸入4個整數（以空格分隔）：")
#numbers = numbers.split()  # 將輸入以空格分隔成一個數字列表

a,b,c,d = eval(input("請輸入 4 個數字以,號分開："))
# d = int(a) + int(b) + int(c)
# print("d = %d " % (d))
print("輸入為：%d %d %d %d" % (a,b,c,d))
i = 0
swap = 0
while a > b or b > c or c > d :
    if a < b and b < c and c < d:
        print("第 %d 圈 %d %d %d %d 排序完畢02" % (i,a,b,c,d))
        break
    else:
        if a > b or b > c or c > d: 
           if c > d :     
              swap = c
              c = d
              d = swap
              i = i + 1
              print("第 %d 圈 %d %d %d %d " % (i,a,b,c,d))
        else:
            continue
        if a > b or b > c:      
            if b > c:
               swap = b
               b = c
               c = swap
               i = i + 1
               print("第 %d 圈 %d %d %d %d " % (i,a,b,c,d))
        else:    
            continue
        if a > b :          
            swap = a
            a = b
            b = swap
            i = i + 1
            print("第 %d 圈 %d %d %d %d " % (i,a,b,c,d))
        else:
            continue    
         
print("第 %d 圈 %d %d %d %d 排序完畢01" % (i,a,b,c,d))    
    
    
    