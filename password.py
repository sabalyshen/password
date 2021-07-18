#這是密碼驗證程式
password = 'a123456'
t = 3
while t >= 1:
	t = t - 1
	pwd = input('請輸入密碼 :')
	if pwd == password:
		print('welcome')
		break
	else:
		print('密碼錯誤')
		if t > 0:
			print('剩餘', t, '次機會')
		else:
			print('沒機會了')
