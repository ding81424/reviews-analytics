data = []
#count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
#		count += 1
#		if count % 1000 == 0:
#			print(len(data))
print('檔案讀取完畢，總共有', len(data), '筆留言')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
print('留言平均長度為', sum_len/len(data))


new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆資料長度小於100')


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆資料提到good')


# 單字計數
wc = {}
for d in data:
	words = d.split(' ')
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1
	
for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

while True:
	word = input('輸入你想查詢的字：')
	if word == 'q':
		print('感謝使用！')
		break
	elif word not in wc:
		print('這個字不在留言中')
	else:
		print(word, '出現過的次數為', wc[word],'次')

