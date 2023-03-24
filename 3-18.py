dist = 384400   # 地球到月球距離 384,400 公里
speed = 1225    # 馬赫 1 小時距離 1,225 公里
total_hours = dist // speed
days = total_hours //24
hours = total_hours % 24
print("總供需要多少天:")
print(days)
print("小時數:")
print(hours)
