import requests
from datetime import datetime

def load_data(url):
    """
    Функция получения списка со словарями в формате python из json файла
    :param url: ссылка на json файл
    :return: список со словарями
    """
    responce = requests.get(url)
    data = responce.json()
    return data


def actual_data(data):
    """
    Функция отфильтровывает данные по исполненным транзакциям и наличием данных отправителя
    :param data: список со словарями
    :return: список со словарями с данными отфильтрованными по наличию данных отправителя
    и исполненными транзакциям
    """
    actual_data = []
    for transaction in data:
        if 'state' in transaction and transaction['state'] == 'EXECUTED' and 'from' in transaction:
           actual_data.append(transaction)
    return actual_data


def sorted_data(data):
    """
    Функция сортирует данные о транзакциях по дате
    :param data: отфильрованный список со словарями
    :return: список со словарями содержащий 5 последних транзакций
    """
    sorted_data = sorted(data, key=lambda x: x['date'], reverse=True)
    return sorted_data[:5]



def print_data(data):
    """
    Функция выводит список транзакций в формате указанном в задании
    :param data: список последних 5 транзакций
    :return: список транзакций в формате указанном в задании
    """
    task_data=[]
    for transaction in data:
        date = datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
        description = transaction['description']
        source = transaction['from'].split()
        source_account = source.pop(-1)
        source_account = f'{source_account[:4]} {source_account[4:6]}** **** {source_account[-4:]}'
        source_info = ' '.join(source)
        payee = f'Счет **{transaction["to"][-4:]}'
        amount = f'{transaction["operationAmount"]["amount"]} {transaction["operationAmount"]["currency"]["name"]}'
        task_data.append(f"""\
{date} {description}
{source_info} {source_account} -> {payee}
{amount}
""")
    return task_data

