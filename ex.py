numbers = input("請輸入三個整數（以空格分隔）：")
numbers = numbers.split()  # 將輸入以空格分隔成一個數字列表

# 將列表中的元素轉換為整數
numbers = [int(num) for num in numbers]

# 使用內建的sorted函數將數字列表排序
sorted_numbers = sorted(numbers)

# 輸出排序後的結果
print("排序結果：", sorted_numbers)