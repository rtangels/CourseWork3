import json

from pprint import pprint

from datetime import datetime
def born_list(path):
    """формирует список с операциями из файла json"""
    with open(path, 'r', encoding='utf-8') as file:
         data=json.load (file)
    return data
def filter_by_state (new_list):
    """фильтрует списко с операциями"""
    data = [d for d in new_list if 'state' in d if d['state'] == 'EXECUTED']
    # я решил добавить фильтр по пункту от кого - from
    data = [x for x in data if 'from' in x]
    return data
def get_date(dictionary):
    """Получение даты из словаря"""
    return dictionary['date']
def sort_by_date(new_list):
    """Cортирует список по дате начиная с последней
    возвращает последние 5"""
    data= sorted(new_list, key=get_date, reverse=True)
    return data[:5]

def formated_output (new_list):
    """Формирует вывод информации"""
    formated_invoice = []
    for line in new_list:
        date = datetime.strptime(line['date'],"%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = line ['description']
        sender = line['from'].split()
        from_bill = sender.pop(-1)
        from_bill = f'{from_bill[:4]} {from_bill[4:6]}** **** {from_bill[-4:]}'
        sender_info =' '.join(sender)
        recepient = line['to'].split()
        to_bill = recepient.pop(-1)
        to_bill = f' **{from_bill[-4:]}'
        recepient_info =' '.join(recepient)
        amount = line['operationAmount']['amount']
        currency = line['operationAmount']['currency']['name']
        formated_invoice.append(f""" {date} {description}
 {sender_info} {from_bill} -> {recepient_info} {to_bill}
 {amount} {currency}""")
    return formated_invoice





