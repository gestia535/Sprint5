import random
import string

first_names = ['aleksandr', 'ivan', 'mariya', 'anna', 'dmitriy',
               'ekaterina', 'nikolay', 'olga', 'vladimir', 'natalya']
last_names = ['ivanov', 'petrov', 'smirnov', 'kuznetsov', 'popov',
              'vasiliev', 'pavlov', 'sokolov', 'mikhailov', 'novikov']
group_numbers = list(range(1, 21))


def login_generator(domain='gmail.com'):
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    group_number = random.choice(group_numbers)
    number = random.randint(1, 999)
    email = f'{first_name}_{last_name}_{group_number}{number}@{domain}'
    return email, first_name


def password_generator():
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choices(characters, k=6))
    return password
