data = []
count = 0
with open ('reviews.txt', 'r') as f :
	for line in f :
		data.append(line)
		count = count + 1
		if count % 10000 == 0 : # % 求餘數
			print(len(data))
print(data[0])

sum_len = 0
for d in data:
	sum_len = sum_len + len(d) #計算總留言文字數量
	
print ('每筆留言平均長度為', sum_len/len(data))

new = []
for d in data:
	if len(d) < 100 :
		new.append(d)
print('一共有', len(new), '小於100個字的留言')
print(new[0])
print(new[1])

