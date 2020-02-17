import os
import sys
import pygame
import requests
import requests
import json

def job():
    global c
    c += 1
    if c == 3:
        c = 0
    if c == 1:
        geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Мадагаскар&format=json"
        response = requests.get(geocoder_request)
        a = response.json()
        b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[1] + '&spn=12.00,12.00&l=map'
        response = requests.get(map_request)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
    elif c == 2:
        geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Аляска&format=json"
        response = requests.get(geocoder_request)
        a = response.json()
        b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[1] + '&spn=15.00,15.00&l=map'
        response = requests.get(map_request)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
    else:
        geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Санкт Петербург&format=json"
        response = requests.get(geocoder_request)
        a = response.json()
        b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[1] + '&spn=2.00,2.00&l=map'
        response = requests.get(map_request)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)


geocoder_request = "http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=Санкт Петербург&format=json"
response = requests.get(geocoder_request)
a = response.json()
b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[1] + '&spn=2.00,2.00&l=map'
response = requests.get(map_request)
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)

# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
c = 0
running = True
fps = 60
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            job()
    screen.fill((255, 255, 255))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.display.flip()
    clock.tick(fps)

# Удаляем за собой файл с изображением.
os.remove(map_file)
