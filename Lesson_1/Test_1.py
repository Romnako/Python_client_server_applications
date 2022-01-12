# 1. Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
# проверить тип и содержание соответствующих переменных. Затем с помощью онлайн-конвертера
# преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных.

a = str('разработка')
print(a)
print(type(a))
enc_a_bytes = a.encode('utf-8')
print(enc_a_bytes)
test_a = b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
print(test_a.decode())
print(type(test_a))

b = str('сокет')
print(b)
enc_b_bytes = b.encode('utf-8')
print(enc_b_bytes)
test_b = b'\xd1\x81\xd0\xbe\xd0\xba\xd0\xb5\xd1\x82'
print(test_b.decode())
print(type(test_b))


c = str('декоратор')
print(c)
enc_c_bytes = c.encode('utf-8')
print(enc_c_bytes)
test_c = b'\xd0\xb4\xd0\xb5\xd0\xba\xd0\xbe\xd1\x80\xd0\xb0\xd1\x82\xd0\xbe\xd1\x80'
print(test_c.decode())
print(type(test_c))

var = ['разработка', 'сокет', 'декоратор']

for line in var:
    print('тип переменной: {}\n'.format(type(line)))
    print('содержание переменной - {}\n'.format(line))
    print('длинна строки: {}\n'.format(len(line)))