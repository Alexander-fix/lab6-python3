#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Вариант: ((N+5)^2 mod 19) + 1 = 8
# Задание:  Использовать словарь, содержащий следующие ключи: название пункта
# назначения; номер поезда; время отправления. Написать программу, выполняющую
# следующие действия: ввод с клавиатуры данных в список, состоящий из словарей
# заданной структуры; записи должны быть упорядочены по номерам поездов;
# вывод на экран информации о поезде, номер которого введен с клавиатуры;
# если таких поездов нет, выдать на дисплей соответствующее сообщение.

import sys


if __name__ == '__main__':
    # Список поездов.
    trains = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о поезде.
            name = input("Пункт назначения? ")
            number = input("Номер поезда? ")
            time = input("Время отправления? ")

            # Создать словарь
            train = {
                'name': name,
                'number': number,
                'time': time,
            }

            # Добавить словарь в список.
            trains.append(train)
            # Отсортировать список в случае необходимости.
            if len(trains) > 1:
                trains.sort(key=lambda item: item.get('number', ''))

        elif command == 'list':
            # Заголовок таблицы.
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 17
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
                    "№",
                    "Название пункта назначения",
                    "Номер поезда",
                    "Время отправления",
                )
            )
            print(line)

            # Вывести данные о всех поездах.
            for idx, train in enumerate(trains, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                        idx,
                        train.get('name', ''),
                        train.get('number', ''),
                        train.get('time', '')
                    )
                )

            print(line)

        elif command.startswith('select '):

            # Разбить команду на части для выделения номера поезда.
            parts = command.split(' ', maxsplit=1)

            # Инициализировать счетчик.
            count = 0
            # Проверить сведения поездов из списка.
            for train in trains:
                if train.get('number', '') == parts[1]:
                    count += 1
                    print(
                        '{:>4}: {}, {}, {}'.format(
                            count,
                            train.get('name', ' '),
                            train.get('number', ' '),
                            train.get('time', ' '))
                    )

            # Если счетчик равен 0, то поезд не найден.
            if count == 0:
                print("Поезд с данным номером не найден.")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <стаж> - запросить номер поезда;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
