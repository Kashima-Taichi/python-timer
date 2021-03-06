from datetime import datetime
import sys

# タスクの変数宣言
task1 = ['english study', '15m', 900]
task2 = ['register cost', '5m', 300]
task3 = ['programming study', 0.55]
task4 = ['reading book', 0.05]
task5 = 'side business'

# 現在の時間とそのunixタイムを取得
now = datetime.now()
now_ts = now.timestamp()

# 本日の入浴時間とそのunixタイムを取得
bath = datetime(year=now.year, month=now.month,
                day=now.day, hour=23, minute=15)
bath_ts = bath.timestamp()

# 現在から風呂に入るまでの時間を算出する
free_ts = bath_ts - now_ts

# 風呂に入るまでの時間が1時間に満たない場合は、下記のメッセージを表示
if free_ts < 3600:
    print('You should study programming until you take bath.')
    sys.exit()

# 各タスクに割り当てる時間を計算
free_ts = free_ts - task1[2]
free_ts = free_ts - task2[2]
task3_ts = free_ts * task3[1]
free_ts = free_ts - task3_ts
task4_ts = free_ts * task4[1]
free_ts = free_ts - task4_ts

# 計算した時間をターミナルに出力
print('#############################')
print('The current time is... ' + str(now.hour) + ':' + str(now.minute))
print('belows are tasks list!')
print(task1[0] + ' : ' + task1[1])
print(task2[0] + ' : ' + task2[1])
print(task3[0] + ' : ' + str(round(task3_ts / 60)) + 'm')
print(task4[0] + ' : ' + str(round(task4_ts / 60)) + 'm')
print(task5 + ' : ' + str(round(free_ts / 60)) + 'm')
print('#############################')
