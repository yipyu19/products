products = []
while True:
    name = input('請輸入商品名稱：')
    if name == 'q':
        break
    price = input('請輸入商品價格：')
    price = int(price)
    products.append([name, price])
print(products)

for p in products:
	print(p[0], '拉麵的價格為', p[1])

with open('products.csv', 'w') as f:
	f.write('products, price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')