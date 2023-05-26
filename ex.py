numbers = input("請輸入六個整數（以空格分隔）：")
numbers = numbers.split()  # 將輸入以空格分隔成一個數字列表

a,b,c,d = eval(input("請輸入 4 個數字以,號分開："))
# d = int(a) + int(b) + int(c)
# print("d = %d " % (d))
print("您輸入的數字是：%d %d %d %d" % (a,b,c,d))
i = 0
swap = 0
while True :
    if a < b and b < c and c < d:
        print("第 %d 圈 %d %d %d %d 排序完畢01" % (i,a,b,c,d))
        break
    elif a > b :         
        swap = a
        a = b
        b = swap
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
    else:
        swap = c
        c = d
        d = swap
        i = i + 1
        print("第 %d 圈 %d %d %d %d " % (i,a,b,c,d))
        #continue
    #else:
    #    print("第 %d 圈 %d %d %d %d 排序完畢02" % (i,a,b,c,d))
        #continue
        #break


# 使用迴圈和判斷式進行排序
for i in range(len(numbers)):
    print("i 第 %d 圈" % (i), end=(' '))
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]
        print("j 第 %d 圈" % (j), end=(' '))    
        print(numbers)  # 印出每一次交換後的排序結果

# 輸出最終排序結果
print("最終排序結果：", numbers)