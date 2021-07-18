#這是密碼驗證程式
t = 0
while True:
	password = input('請輸入密碼 :')
	if password == 'a123456':
		print('welcome')
		break
	else:
		print('密碼錯誤')
		t = int(t)
		t = t + 1
		if t == 3:
			print('已經失敗3次了')
			break
		elif t == 1:
			print('已經失敗1次了')
		elif t == 2:
			print('已經失敗2次了')
