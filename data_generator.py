# Файл генерации данных для заполнения форм
from time import time, sleep
from datetime import datetime
import json


def get_right_login_data():
    case = {'mail': 'mail@mail.com', 'password': '1234'}
    current_date = str(datetime.now().date()).replace('-', '')
    current_time = str(datetime.now().time()).replace(':', '')[:6]
    file_name = f'{current_date}{current_time}_right_login.json'
    with open(file_name, 'w') as file:
        file.write(json.dumps(case))
    return case


def generate_wrong_login_data():
    case = [{"mail": '', 'password': ''},
            {'mail': 'mail@mail.com', 'password': ''},
            {'mail': '12345@mail.com', 'password': 'Qwerty1@'}]
    current_date = str(datetime.now().date()).replace('-', '')
    current_time = str(datetime.now().time()).replace(':', '')[:6]
    file_name = f'{current_date}{current_time}_wrong_login.json'
    with open(file_name, 'w') as file:
        file.write(json.dumps(case))
    return case


def generate_right_registration_data():
    case = {'case': {'mail': f'{round(time() * 10000)}@test.com',
                     'phone': f'38{str(round(time() * 10000))[-10:]}',
                     'password': 'Qwerty1@',
                     'confirm': 'Qwerty1@',
                     'first_name': 'TestUser',
                     'last_name': 'TestUser'}}

    result = json.dumps(case)
    current_date = str(datetime.now().date()).replace('-', '')
    current_time = str(datetime.now().time()).replace(':', '')[:6]
    file_name = f'{current_date}{current_time}_right_reg.json'
    with open(file_name, 'w') as file:
        file.write(result)
    return case


def generate_wrong_registration_data():
    wrong_data_for_register = []
    case1 = {'mail': '',
             'phone': '',
             'password': '',
             'confirm': '',
             'first_name': '',
             'last_name': ''}
    wrong_data_for_register.append({'case': case1})
    sleep(0.2)

    case2 = {'mail': f'{round(time() * 10000)}@test.com',
             'phone': f'38{str(round(time() * 10000))[-10:]}',
             'password': '1234',
             'confirm': '1234',
             'first_name': 'TestUser',
             'last_name': 'TestUser'}
    wrong_data_for_register.append({'case': case2})
    sleep(0.2)

    case3 = {'mail': f'{round(time() * 10000)}@test.com',
             'phone': f'38{str(round(time() * 10000))[-10:]}',
             'password': 'qwertyui',
             'confirm': 'qwertyui',
             'first_name': 'TestUser',
             'last_name': 'TestUser'}
    wrong_data_for_register.append({'case': case3})
    sleep(0.2)

    case4 = {'mail': f'{round(time() * 10000)}@test.com',
             'phone': f'38{str(round(time() * 10000))[-10:]}',
             'password': 'qwerty12',
             'confirm': 'qwerty12',
             'first_name': 'TestUser',
             'last_name': 'TestUser'}
    wrong_data_for_register.append({'case': case4})
    sleep(0.2)

    case5 = {'mail': f'{round(time() * 10000)}@test.com',
             'phone': f'38{str(round(time() * 10000))[-10:]}',
             'password': 'qwerty1@',
             'confirm': 'qwerty1@',
             'first_name': 'TestUser',
             'last_name': 'TestUser'}
    wrong_data_for_register.append({'case': case5})
    sleep(0.2)

    case6 = {'mail': f'{round(time() * 10000)}@test.com',
             'phone': f'38{str(round(time() * 10000))[-10:]}',
             'password': 'Qwerty1@',
             'confirm': '12345678',
             'first_name': 'TestUser',
             'last_name': 'TestUser'}
    wrong_data_for_register.append({'case': case6})
    sleep(0.2)

    case7 = {'mail': 'mail@test.com',
             'phone': f'38{str(round(time() * 10000))[-10:]}',
             'password': 'Qwerty1@',
             'confirm': 'Qwerty1@',
             'first_name': 'TestUser',
             'last_name': 'TestUser'}
    wrong_data_for_register.append({'case': case7})
    sleep(0.2)

    case8 = {'mail': 'mail@test',
             'phone': f'38{str(round(time() * 10000))[-10:]}',
             'password': 'Qwerty1@',
             'confirm': 'Qwerty1@',
             'first_name': 'TestUser',
             'last_name': 'TestUser'}
    wrong_data_for_register.append({'case': case8})
    sleep(0.2)

    case9 = {'mail': 'mail',
             'phone': f'38{str(round(time() * 10000))[-10:]}',
             'password': 'Qwerty1@',
             'confirm': 'Qwerty1@',
             'first_name': 'TestUser',
             'last_name': 'TestUser'}
    wrong_data_for_register.append({'case': case9})
    sleep(0.2)

    case10 = {'mail': 'mail@mail.com',
              'phone': f'38{str(round(time() * 10000))[-10:]}',
              'password': 'Qwerty1@',
              'confirm': 'Qwerty1@',
              'first_name': 'TestUser',
              'last_name': 'TestUser'}
    wrong_data_for_register.append({'case': case10})
    sleep(0.2)

    case11 = {'mail': f'{round(time() * 10000)}@test.com',
              'phone': f'380501111111',
              'password': 'Qwerty1@',
              'confirm': 'Qwerty1@',
              'first_name': 'TestUser',
              'last_name': 'TestUser'}
    wrong_data_for_register.append({'case': case11})
    sleep(0.2)

    case12 = {'mail': f'{round(time() * 10000)}@test.com',
              'phone': f'12345',
              'password': 'Qwerty1@',
              'confirm': 'Qwerty1@',
              'first_name': 'TestUser',
              'last_name': 'TestUser'}
    wrong_data_for_register.append({'case': case12})
    sleep(0.2)

    case13 = {'mail': f'{round(time() * 10000)}@test.com',
              'phone': f'38{str(round(time() * 10000))[-10:]}',
              'password': 'Qwerty1@',
              'confirm': 'Qwerty1@',
              'first_name': '1',
              'last_name': 'TestUser'}
    wrong_data_for_register.append({'case': case13})
    sleep(0.2)

    case14 = {'mail': f'{round(time() * 10000)}@test.com',
              'phone': f'38{str(round(time() * 10000))[-10:]}',
              'password': 'Qwerty1@',
              'confirm': 'Qwerty1@',
              'first_name': 'TestUser',
              'last_name': '1'}
    wrong_data_for_register.append({'case': case14})

    result = json.dumps(wrong_data_for_register)
    current_date = str(datetime.now().date()).replace('-', '')
    current_time = str(datetime.now().time()).replace(':', '')[:6]
    file_name = f'{current_date}{current_time}_wrong_reg.json'
    with open(file_name, 'w') as file:
        file.write(result)
    return wrong_data_for_register


if __name__ == '__main__':
    generate_wrong_registration_data()
