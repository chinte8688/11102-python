# numbers = input("請輸入三個整數（以空格分隔）：")
# numbers = numbers.split()  # 將輸入以空格分隔成一個數字列表

# 將列表中的元素轉換為整數
#numbers = [int(num) for num in numbers]

# 使用內建的sorted函數將數字列表排序
# sorted_numbers = sorted(numbers)

# 輸出排序後的結果
# print("排序結果：", sorted_numbers)


a,b,c,d = eval(input("請輸入 4 個數字以,號分開："))
# d = int(a) + int(b) + int(c)
# print("d = %d " % (d))
i = 0
swap = 0
while True :
    #i = 0
    #swap = 0
    if a < b :
        if b > c :
            if c > d :
                print("第 %d 圈 %d %d %d %d 排序完畢01" % (i,a,b,c,d))
                break
    elif a > b :         
        swap = a
        a = b
        b = swap
        i = i + 1
        print("第 %d 圈 %d %d %d %d " % (i,a,b,c,d))
        continue
    elif b > c :         
        swap = b
        b = c
        c = swap
        i = i + 1
        print("第 %d 圈 %d %d %d %d " % (i,a,b,c,d))
        continue
    elif c > d :
        swap = c
        c = d
        d = swap
        i = i + 1
        print("第 %d 圈 %d %d %d %d " % (i,a,b,c,d))
        continue
    else:
        print("第 %d 圈 %d %d %d %d 排序完畢02" % (i,a,b,c,d))
        continue
        #break
        #while


    # print("%d %d %d" % (a,b,c))
        
    #    if a < b 
    #    print("%d %d %d 排序完畢" % (a,b,c))
    #   reak
    # print("第 %d 圈 %d %d %d" % (i,a,b,c))