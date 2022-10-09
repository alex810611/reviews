date = []
count = 0
with open ('reviews.txt', 'r') as f :
	for line in f :
		date.append(line)
		count = count + 1
		if count % 10000 == 0 : # % 求餘數
			print(len(date))
print(date[0])

