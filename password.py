#這是密碼驗證程式
password = 'a123456'
t = 3
while True:
	pwd = input('請輸入密碼 :')
	if pwd == password:
		print('welcome')
		break
	else:
		t = t - 1
		print('剩餘', t,'次')
		if t == 0:
			break
