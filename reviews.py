data = []
count = 0
with open ('reviews.txt', 'r') as f :
	for line in f :
		data.append(line)
		count = count + 1
		if count % 10000 == 0 : # % 求餘數
			print(len(data))
print(data[0])


wc = {}
for d in data :
	words = d.split()
	for word in words :
		if word in wc:
			wc[word] += 1
		else :
			wc[word] = 1 #新增新的key

for word in wc:
	if wc[word] > 1000000 :
		print(word , wc[word]) 

while True:
	word = input('請問你要查什麼字')
	if word == 'q':
		break
	if word in wc:
		print(word,'出現過次數',wc[word])
	else: 
		print('沒出現這個字')
	



















#sum_len = 0
#for d in data:
#	sum_len = sum_len + len(d) #計算總留言文字數量
#	
#print ('每筆留言平均長度為', sum_len/len(data))

#new = []
#for d in data:
#	if len(d) < 100 :
#		new.append(d)
#print('一共有', len(new), '小於100個字的留言')
#print(new[0])
#print(new[1])

#good = []
#for d in data :
#	if 'good' in d :
#		good.append(d) # a in abc -> true
#print('一共有',len(good),'筆留言')
#print(good[0])

#快寫篩選 good in data 
#good = [d for d in data if 'good' in d]
#print('一共有',len(good),'筆留言')
#bad = [d for d in data if 'bad' in d]
#print('一共有',len(bad),'筆留言')
#nice = [d for d in data if 'nice' in d]
#print('一共有',len(nice),'筆留言')


#快寫＆一般差異

#bad = ['bad' in d for d in data] # true or false in d
#print(bad)

#bad = []
#for d in data 
#	bad.append('bad' in d )
