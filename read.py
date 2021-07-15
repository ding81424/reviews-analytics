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
print(good[0])
#清單快寫法
#good = [d for d in data if 'good' in d]
# 第一個d 表示要裝進去清單的東西
# 後面接著for迴圈: for d in data
# 在接著if條件句: if 'good' in d
#說明output = [(number-1) for number in reference if number % 2 == 0]
#                運算          變數        清單       篩選條件
