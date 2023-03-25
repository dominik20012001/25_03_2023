# import math
# # wynik = math.sqrt(49)
# # print(type(wynik))
# # print(int(wynik))
# # print(type(y))

# # wynik = math.sqrt(99)

# wynik = abs(-1)
# print(wynik)
# x = {'truskawka', 
# 'kiwi',
# 'malina',
# 'pomrańcza',
# 'japko',
# }
# print(x[-3:])

# x.pop()
# x.remove('Kabanos')


# q = requests.get(
#     url='https://2p66nmmycsj3.statuspage.io/api/v2/status.json'
# ).json()
# print(q.keys())
# qqq = q.get('page').get('url')
# print(qqq)

x = 10
y = int(input("podaj liczbe całkowitą: "))
print(y)
if y < x :
    print(f'{y} jest mniejsze od {x}')
else: 
    print('warunek nie spełnił się')