import os 


def read_file(filename):
    products = []
    with open(filename,'r', encoding = 'utf-8') as f:
        for line in f:
            if 'name, price' in line:
                continue
            name, price = line.strip().split(',')
            products.append([name, price])
    return products


#let user input some data
def user_input(products):
    while True:
        name = input('請輸入商品名稱：')
        if name == 'q':
            break
        price = input('請輸入商品價格：')
        # price = int(price)
        products.append([name, price])
    print(products)
    return products


#printout the record of data
def print_products(products):
    for p in products:
        print(p[0], '拉麵的價格為', p[1])



#write data into files
def write_file(filename, products):
    with open(filename, 'w', encoding = 'utf-8') as f:
        f.write('name, price\n')
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n')


def main():
    filename ='products.csv'
    if os.path.isfile(filename):
        print('yeah! found it')
        products = read_file(filename)
    else:
        print('can not find the file')
    products = user_input(products)
    print_products(products)
    write_file('products.csv', products)


main()
