import os
import sys
import pygame
import requests
import requests
import json


spisok_gorodov = []
spisok_gorodov2 = []
spisok_koordinat = []
a = ''
while a != 'выход':
    a = input()
    if a != '':
        spisok_gorodov = a.strip().split(', ')
        for i in range(len(spisok_gorodov)):
            geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + spisok_gorodov[i] + '&format=json'
            response = requests.get(geocoder_request)
            a = response.json()
            spisok_koordinat.append(a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()[1])
        for i in range(len(spisok_gorodov)):
            if spisok_koordinat[i] == min(spisok_koordinat):
                spisok_gorodov2.append(i)
        print('Самые южный(е) город(а): ', sep='', end='')
        for i in range(len(spisok_gorodov2) - 1):
            print(spisok_gorodov[spisok_gorodov2[i]], sep='', end=', ')
        print(spisok_gorodov[spisok_gorodov2[-1]])
        spisok_gorodov2 = []
        spisok_gorodov = []
        spisok_koordinat = []
    else:
        print('Вы ничего не ввели')
