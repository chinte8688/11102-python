
n1,n2,n3,n4,n5 = eval(input("請輸入 5 個數字以[,]號分開："))

print("您輸入的數字為 %d %d %d %d %d" % (n1,n2,n3,n4,n5))
i = 0                                                # 圈數  
j = 0                                                # 交換數  
swn1p = 0                                            # 交換空間

if n1 <= n2 and n2 <= n3 and n3 <= n4 and n4 <= n5:  # if 一開始就由小排到大
        print("第%02d圈%02d次交換 %d %d %d %d %d 排序完畢01" % (i,j,n1,n2,n3,n4,n5)) #排序完成

while n1 >= n2 or n2 >= n3 or n3 >= n4 or n4 >= n5:  # 排序未完成，進入迴圈 
    i += 1                                           # 圈數計算
    if n1 >= n2 or n2 >= n3 or n3 >= n4 or n4 >= n5: # 如果有前數 > 後數的狀況
        if n4 >= n5 :                                # 如果 n4 >= n5    
            swn1p = n4                               #  
            n4 = n5                                  #   n4,n5 對調
            n5 = swn1p                               #   
            j += 1                                   # 交換次數 +1   
              
            if n1 <= n2 and n2 <= n3 and n3 <= n4 and n4 <= n5:
                print("第%02d圈%02d次交換 %d %d %d %d %d 排序完畢02" % (i,j,n1,n2,n3,n4,n5))
                break
            else:
                print("第%02d圈%02d次交換 %d %d %d %d %d" % (i,j,n1,n2,n3,n4,n5))
    else:
        continue

    if n1 >= n2 or n2 >= n3 or n3 >= n4: 
        if n3 >= n4 :     
            swn1p = n3
            n3 = n4
            n4 = swn1p
            j += 1

            if n1 <= n2 and n2 <= n3 and n3 <= n4 and n4 <= n5:
                print("第%02d圈%02d次交換 %d %d %d %d %d 排序完畢03" % (i,j,n1,n2,n3,n4,n5))
                break
            else:
                print("第%02d圈%02d次交換 %d %d %d %d %d" % (i,j,n1,n2,n3,n4,n5))
              
    else:
            continue
    
    if n1 >= n2 or n2 >= n3:      
        if n2 >= n3:
           swn1p = n2
           n2 = n3
           n3 = swn1p
           j += 1

           if n1 <= n2 and n2 <= n3 and n3 <= n4 and n4 <= n5:
                print("第%02d圈%02d次交換 %d %d %d %d %d 排序完畢04" % (i,j,n1,n2,n3,n4,n5))
                break
           else:
                print("第%02d圈%02d次交換 %d %d %d %d %d" % (i,j,n1,n2,n3,n4,n5))
               
    else:    
            continue
    
    if n1 >= n2 :          
            swn1p = n1
            n1 = n2
            n2 = swn1p
            j += 1

            if n1 <= n2 and n2 <= n3 and n3 <= n4 and n4 <= n5:
                print("第%02d圈%02d次交換 %d %d %d %d %d 排序完畢05" % (i,j,n1,n2,n3,n4,n5))
                break
            else:
                print("第%02d圈%02d次交換 %d %d %d %d %d" % (i,j,n1,n2,n3,n4,n5))    

    else:
            continue 