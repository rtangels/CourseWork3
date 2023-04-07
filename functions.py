import json

from datetime import datetime


def born_list(path):
    """
    Функция формирует список с операциями из файла json
    """
    with open(path, 'r', encoding='utf-8') as file:
        data_temp = json.load(file)
    return data_temp


def filter_by_state(new_list):
    """
          Функция выделяет из списка опираций
только те, что имеют пометку EXECUTED(т.е. операция выполнена)
          и выводит список из этих операций
    """
    # использование спискового включения для формирования нового списка
    data = [d for d in new_list if 'state' in d if d['state'] == 'EXECUTED']
    return data


def get_date(dictionary):
    """
     Функция получает дату из словаря
     """
    return dictionary['date']


def sort_by_date(new_list):
    """
    Cортирует список по значению date
    начиная с последней даты возвращает
    5 последних по времени операций
    """
    data = sorted(new_list, key=get_date, reverse=True)
    return data[:5]


def formated_output(new_list):
    """
    Функция формирует вывод информации
    в требуемом формате
    """
    # новый список для данных в необходимом формате
    formated_invoice = []
    # цикл по списку с операциями для получения необходимых значений
    for line in new_list:
        # изменение формата даты
        date = datetime.strptime(line['date'], "%Y-%m-%dT%H:%M:%S.%f")
        date = date.strftime("%d.%m.%Y")
        # описание операции из списка операций остаётся без имзенений
        description = line['description']
        # проверка условия наличия данных отправителя и запись данных
        # в соответвтующую переменную
        if 'from' in line:
            sender = line['from'].split()
            from_bill = sender.pop(-1)
            bill_part_1 = f"""{from_bill[:4]} {from_bill[4:6]}** """
            bill_part_2 = f"""**** {from_bill[-4:]}"""
            from_bill = bill_part_1+bill_part_2
            sender_info = ' '.join(sender)
            recepient = line['to'].split()
            to_bill = recepient.pop(-1)
            to_bill = f' **{to_bill[-4:]}'
            recepient_info = ' '.join(recepient)
            amount = line['operationAmount']['amount']
            currency = line['operationAmount']['currency']['name']
            formated_invoice.append(f"""{date} {description}
{sender_info} {from_bill} -> {recepient_info} {to_bill}
{amount} {currency}"""
                                    )
        else:
            recepient = line['to'].split()
            to_bill = recepient.pop(-1)
            to_bill = f' **{to_bill[-4:]}'
            recepient_info = ' '.join(recepient)
            amount = line['operationAmount']['amount']
            currency = line['operationAmount']['currency']['name']
            formated_invoice.append(f"""{date} {description}
Счёт неизвестен -> {recepient_info} {to_bill}
{amount} {currency}
"""
                                    )
    return formated_invoice
new_list = [
      {
            "id": 716496732,
            "state": "EXECUTED",
            "date": "2018-04-04T17:33:34.701093",
            "operationAmount": {
                "amount": "40701.91",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Gold 5999414228426353",
            "to": "Счет 72731966109147704472"
        }]
new_list = formated_output(new_list)
print(new_list)