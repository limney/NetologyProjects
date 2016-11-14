#!/usr/bin/env python
# -*- coding: utf-8 -*-

residence_limit = 90  # 45, 60
schengen_constraint = 180

# ------------- Функции работы с витами --------------------

def date_difference(leave, arrive):
    """
    Количество дней между двумя датами
    :param leave:
    :param arrive:
    :return:
    """
    result = leave - arrive + 1
    return result


def visit_length(visit):
    """
    Количетсво дней в визите
    :param visit:
    :return:
    """
    return date_difference(visit[1], visit[0])


def get_days_for_visits(visits):
    """
    Количество проведенных дней в ЕС из списка визитов
    :param visits:
    :return:
    """
    days_for_visits = []
    for visit in visits:
        days_for_visit = 0
        for past_visit in visits:
            if visit[0] - schengen_constraint < past_visit[0] < visit[0]:
                days_for_visit += visit_length(past_visit)
        days_for_visit += visit_length(visit)
        days_for_visits.append(days_for_visit)
    return days_for_visits


def print_days_future_visit(visits, date_in_future):
    """
    Печатаем количество доступных дней в ЕС
    :param visits:
    :param date_in_future:
    :return:
    """
    visits_for_future = visits + [[date_in_future, date_in_future]]
    days_for_future_visits = get_days_for_visits([visit for visit in visits_for_future if visit[0] > date_in_future - schengen_constraint])
    days_in_es = residence_limit - days_for_future_visits[len(days_for_future_visits) - 1] + 1
    if date_in_future + days_in_es > 365:
        days_in_es = 365 - date_in_future
    print('Если въедем %s числа, сможем провести в шенгене %s дней' % (date_in_future, days_in_es))
    return days_in_es


def print_residence_limit_violation(visits, new_visit):
    """
    Печатает о превышении допустимого времени пребывания в ЕС
    :param visits:
    :return:
    """
    days_for_visits = get_days_for_visits([visit for visit in visits if visit[0] > new_visit[0] - schengen_constraint])
    for visit, total_days in zip(visits, days_for_visits):
        if total_days > residence_limit:
            overstay_time = total_days - residence_limit
            print('Во время визита', visit, 'количество время пребывания превышено на', overstay_time, 'дней')
            return False
    return True

def is_across(new_visit, visits):
    """
    Определяет пересечение нового визита со старыми визитами
    :param new_visit:
    :return:
    """
    for visit in visits:
        if (new_visit[0] >= visit[0] and new_visit[0] <= visit[1]) or (new_visit[1] >= visit[0] and new_visit[1] <= visit[1]):
            return visit
    return None

visits = [[1, 10], [61, 70], [101, 140], [141, 160], [171, 180], [300, 350]]

# ---------------------- Функции по работе с меню -------------------------------------------

def exit_to_main_menu():
    """
    Возвращение в главное меню
    :return:
    """
    input("Нажмите любую клавишу, чтобы вернуться в меню ...")

def visit_input():
    """
    Данные визита полученные от пользователя
    :return:
    """
    print('Дата начала:')
    start = int(input())
    print('Дата окончания:')
    end = int(input())
    return start, end

def add_new_visit():
    """
    Добавление визита
    :return:
    """
    start, end = visit_input()  # получаем данные о визите от пользователя
    new_visit = [start, end]
    result = is_across([start, end], visits)
    if result is not None:
        print("Пересечение с визитом: от %d до %d" % (result[0], result[1]))
    else:
        visits_temp = visits.copy()
        visits_temp.append(new_visit)
        visits_temp.sort(key=lambda v: v[1])
        if print_residence_limit_violation(visits_temp, new_visit):  # если ошибки нет то добавим новый визит
            visits.append(new_visit)
        visits.sort(key=lambda v: v[1])  # сортируем список визитов
    exit_to_main_menu()

def delete_visit():
    """
    Удаление визита
    :return:
    """
    print("Удаление визита")
    start, end = visit_input()  # получаем данные о визите от пользователя
    for visit in visits:
        if visit[0] == start and visit[1] == end:
            visits.remove(visit)
            print("Удалено")
            break
    exit_to_main_menu()

def get_count_free_days():
    """
    Вычислим количество доступных дней
    :return:
    """
    print('Введите дату начала визита:')
    date_in_future = int(input())
    date_valid = True
    for visit in visits:
        if date_in_future < visit[1]:
            print("Дата должа быть в будущем")
            date_valid = False
    if date_valid:
        print("Количество доступный дней для пребывания в ЕС")
        print_days_future_visit(visits, date_in_future)
    exit_to_main_menu()

def show_visits():
    """
    Печатаем все доступные визиты
    :return:
    """
    print("Все визиты:")
    days_for_visits = get_days_for_visits(visits)
    for days_for_visit, visit in zip(days_for_visits, visits):
        print("Дата начала: %d, дата окончания: %d, дней в визите %d" % (visit[0], visit[1], visit_length(visit)))
    exit_to_main_menu()

def select_menu(selected_menu):
    """
    Действия выбранные пользователем
    :param selected_menu:
    :return:
    """
    return {'s': show_visits,
            'v': add_new_visit,
            'r': delete_visit,
            'p': get_count_free_days,
            'e': exit
           }.get(selected_menu)

# ------------------ Меню программы --------------------------------------------------
while True:
    # Выбираю меню
    print('Меню:',
          's - показать существующие визиты',
          'v - добавить визит',
          'r - удаление визита',
          'p - получить количество дне от даты начала нового виза',
          'e - выход из программы',
          sep='\n')
    user_input = input()
    if select_menu(user_input) is not None:
        select_menu(user_input)()
    else:
        print('Некоректный ввод меню! Введите корректный символ меню.')


