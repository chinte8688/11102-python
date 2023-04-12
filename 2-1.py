# 1年可存多少錢
hourly_salary = 125     # 時薪
annual_salary = hourly_salary * 8 * 300 # 年薪
monthly_fee = 9000      # 月支出    
annual_fee = monthly_fee *12    
annual_savings = annual_salary - annual_fee # 年度存款
print(annual_savings)
print("年度收入 %d 年度支出 %d 年度結餘 %d" % (annual_salary,annual_fee,annual_savings))
print("年度收入 {0:d} 年度支出 {1:d} 年度結餘 {2:d}".format(annual_salary,annual_fee,annual_savings))
print("朱晉德")