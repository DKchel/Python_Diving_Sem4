"""
Возьмите задачу о банкомате из семинара 2. 
Разбейте её на отдельные операции — функции. 
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""

import decimal as d

RICHNESS_SUM = d.Decimal(5_000_000)
RICHNESS_TAX = d.Decimal(10) / d.Decimal(100)
WITHDROW_PERCENT = d.Decimal(15) / d.Decimal(1000)
ADD_PERCENT = d.Decimal(3) / d.Decimal(100)
MULTIPLICITY = 50
MIN_REMOVAL = 30
MAX_REMOVAL = 600
COUNT_OPER = 3

def print_data():
    """Показ транзакций"""
    print('Выполненные транзакции:')
    for k, v in transaction_dict.items():
        print(f'{k}: {v}', sep='')

def deposit_money(account: int, count: int) -> int:
    """Внесение денег на счёт"""
    if count and count % COUNT_OPER == 0:
        bonus_percent = account * ADD_PERCENT
        account += bonus_percent
        print(f'\nНа счёт начислено {ADD_PERCENT * 100}%, составляющие {bonus_percent} у.е.\nНа карте: {account} у.е.')
    amount = 1
    while amount % 50 != 0:
        amount = int(input(f'\nВведите сумму, кратную {MULTIPLICITY}: '))
    account += amount
    print(f'\nПополнение карты на {amount} у.е. \nНа карте: {account} у.е.')
    transaction_dict[count + 1] = f'Транзакция пополнения счёта: + {amount} у.е.'
    return account

def take_money(account, count):
    """Снятие денег со счёта"""
    if count and count % COUNT_OPER == 0:
        bonus_percent = account * ADD_PERCENT
        account += bonus_percent
        print(f'\nНа счёт начислено {ADD_PERCENT * 100}%, составляющие {bonus_percent} у.е.\nНа карте: {account} у.е.')
    amount = 1
    while amount % 50 != 0:
        amount = int(input(f'\nВведите сумму, кратную {MULTIPLICITY}: '))
    withdrow_tax = amount * WITHDROW_PERCENT
    withdrow_tax = (MIN_REMOVAL if withdrow_tax < MIN_REMOVAL else 
                    MAX_REMOVAL if withdrow_tax > MAX_REMOVAL else withdrow_tax)
    if  account >= amount + withdrow_tax:
        print(f'{account=} + {withdrow_tax=} - {amount} = {account + withdrow_tax - amount}')          
        account -= (amount + withdrow_tax)
        print(f'\nСнятие с карты {amount} у.е.\nКомиссия за снятие: {withdrow_tax} у.е.\nНа карте: {account} у.е.')
        transaction_dict[count + 1] = f'Транзакция снятия со счёта: - {amount} у.е.'
    else:
        print(f'\nНа карте {account} у.е. Не достаточно для операции снятия {amount} у.е. с учётом комиссии за снятие: {withdrow_tax} у.е.')
        transaction_dict[count + 1] = f'Не успешная транзакция снятия: {amount} у.е - не достаточно средств.'
    return account

def exit_data(account):
    """Выход"""
    if account > RICHNESS_SUM:
        percent = account * RICHNESS_TAX
        account -= percent
        print(f'\nУдержан налог на богатство {RICHNESS_TAX}% в размере {percent} у.е.')
    print(f'Возьмите карту. На карте: {account} у.е.')
    

account = d.Decimal(0)
transaction_dict = {}
count = 0    
command = ''

while command != '0':
    print('Меню пользователя: \n'
        '1. Пополнить счёт \n'
        '2. Снять со счёта \n'
        '3. Список транзакций \n'
        '0. Выход \n')
    command = input('Выберите пункт меню: ')

    while command not in ('1', '2', '3', '0'):
        print('Не корректный ввод, поворите запрос')
        command = input('Выберите пункт меню: ')

    match command:
        case '1':
            account = deposit_money(account, count)
            count += 1
        case '2':
            account = take_money(account, count)
            count += 1
        case '3':
            print_data()
        case '0':
            exit_data(account)
    print()

