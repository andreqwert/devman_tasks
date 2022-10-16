import random
import time
from datetime import date, timedelta
from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from datacenter.models import Schoolkid, Teacher, Subject, Lesson, Mark, Chastisement, Commendation



def get_days_between_dates(date1, date2):
     """Получить все даты между указанными"""

     y1, m1, d1 = date1.split('-')
     y2, m2, d2 = date2.split('-')
     start_date = date(int(y1), int(m1), int(d1))
     end_date = date(int(y2), int(m2), int(d2))
     delta = end_date - start_date

     days = []
     for deltaday in range(delta.days + 1):
          curr_date = start_date + timedelta(days=deltaday)
          days.append('{}-{}-{}'.format(curr_date.year, curr_date.month, curr_date.day))
     return days


def get_commendation_expressions(fp_to_expressions):
     """Читаем файл с разными вариациями похвалы"""

     with open(fp_to_expressions) as f:
          experssions = f.read().splitlines()
     return experssions


def remove_chastisements(schoolkid):
     """Удалить все жалобы учителей"""

     try:
          child_name = Schoolkid.objects.filter(full_name__contains=schoolkid).get()
          child_chastisements= Chastisement.objects.filter(schoolkid=child_name)
          child_chastisements.delete()
          print('Жалобы удалены!')
     except ObjectDoesNotExist:
          print('Такого ученика не существует.')
     except MultipleObjectsReturned:
          print(f'Введите более конкретное ФИО ученика. Например, с отчеством.')


def remove_commendations(schoolkid):
     """Удалить всю похвалу ученика"""

     try:
          child_name = Schoolkid.objects.filter(full_name__contains=schoolkid).get()
          child_commendations= Commendation.objects.filter(schoolkid=child_name)
          child_commendations.delete()
          print('Похвала стёрта!')
     except ObjectDoesNotExist:
          print('Такого ученика не существует.')
     except MultipleObjectsReturned:
          print(f'Введите более конкретное ФИО ученика. Например, с отчеством.')


def fix_marks(schoolkid):
     """Исправляем все оценки ниже либо равные тройке - на пятёрки"""

     try:
          child_name = Schoolkid.objects.filter(full_name__contains=schoolkid).get()
          bad_marks = Mark.objects.filter(schoolkid=child_name, points__lte=3)
          for mark in bad_marks:
               mark.points = 5
               mark.save()
          print('Оценки исправлены!')
     except ObjectDoesNotExist:
          print('Такого ученика не существует.')
     except MultipleObjectsReturned:
          print(f'Введите более конкретное ФИО ученика. Например, с отчеством.')


def create_commendations(schoolkid, subject):
     """Создать похвалу для ученика"""

     try:
          child_name = Schoolkid.objects.filter(full_name__contains=schoolkid).get()
          lesson = Lesson.objects.filter(year_of_study=6, group_letter='А', subject__title=subject).first()
          teacher_name = Teacher.objects.filter(lesson=lesson).first()
          subject_name = Subject.objects.filter(title__contains=subject).first()
          Commendation.objects.create(text=random.choice(get_commendation_expressions('./datacenter/commendation_expressions.txt')),
                                      created=random.choice(get_days_between_dates('2018-10-02', '2018-12-03')), 
                                      teacher=teacher_name, schoolkid=child_name, subject=subject_name)
          print('Похвала добавлена!')
     except ObjectDoesNotExist:
          print('Такого ученика не существует.')
     except MultipleObjectsReturned:
          print(f'Введите более конкретное ФИО ученика. Например, с отчеством.')
     except IntegrityError:
          print('Неверно указано название предмета. Укажите корректное название предмета.')





