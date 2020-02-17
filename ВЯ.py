import os
import sys
import pygame
import requests
import requests
import json
from pygame.locals import *


#ИНОГДА НАДО НЕМНОГО ПОДОЖДАТЬ
def pgu():
    global razmer
    if (float(y) + float(str(float(razmer) / 0.4356)) / 2 > 88.7 or float(y) - float(str(float(razmer) / 0.4356)) / 2 < -88.7) or (float(x) + float(str(float(razmer) / 0.4356)) / 2 > 179.9 or float(x) - float(str(float(razmer) / 0.4356)) / 2 < -179.9):
        geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + x + ',' + y + '&format=json'
        response = requests.get(geocoder_request)
        a = response.json()
        b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[
            1] + '&spn=' + razmer + ',' + razmer + '&l=' + s + vse
        response = requests.get(map_request)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
    else:
        razmer = str(float(razmer) / 0.4356)
        geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + x + ',' + y + '&format=json'
        response = requests.get(geocoder_request)
        a = response.json()
        b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[1] + '&spn=' + razmer + ',' + razmer + '&l=' + s + vse
        response = requests.get(map_request)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)


def pgd():
    global razmer
    if (float(y) + float(str(float(razmer) * 0.4356)) / 2 > 88.7 or float(y) - float(str(float(razmer) * 0.4356)) / 2 < -88.7) or (
            float(x) + float(str(float(razmer) * 0.4356)) / 2 > 179.9 or float(x) - float(str(float(razmer) * 0.4356)) / 2 < -179.9):
        geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + x + ',' + y + '&format=json'
        response = requests.get(geocoder_request)
        a = response.json()
        b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[
            1] + '&spn=' + razmer + ',' + razmer + '&l=' + s + vse
        response = requests.get(map_request)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
    else:
        razmer = str(float(razmer) * 0.4356)
        geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + x + ',' + y + '&format=json'
        response = requests.get(geocoder_request)
        a = response.json()
        b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[1] + '&spn=' + razmer + ',' + razmer + '&l=' + s + vse
        response = requests.get(map_request)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)


def r():
    global x
    global y
    if (float(y) + float(razmer) / 2 > 88.7 or float(y) - float(razmer) / 2 < -88.7) or (
            float(str(float(x) - 0.5 * float(razmer))) + float(razmer) / 2 > 179.9 or float(str(float(x) - 0.5 * float(razmer))) - float(razmer) / 2 < -179.9):
        geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + x + ',' + y + '&format=json'
        response = requests.get(geocoder_request)
        a = response.json()
        b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[
            1] + '&spn=' + razmer + ',' + razmer + '&l=' + s + vse
        response = requests.get(map_request)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
    else:
        x = str(float(x) + 0.5 * float(razmer))
        geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + x + ',' + y + '&format=json'
        response = requests.get(geocoder_request)
        a = response.json()
        b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[1] + '&spn=' + razmer + ',' + razmer + '&l=' + s + vse
        response = requests.get(map_request)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)


def l1():
    global x
    global y
    if (float(y) + float(razmer) / 2 > 88.7 or float(y) - float(razmer) / 2 < -88.7) or (
            float(str(float(x) - 0.5 * float(razmer))) + float(razmer) / 2 > 179.9 or float(str(float(x) - 0.5 * float(razmer))) - float(razmer) / 2 < -179.9):
        geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + x + ',' + y + '&format=json'
        response = requests.get(geocoder_request)
        a = response.json()
        b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[
            1] + '&spn=' + razmer + ',' + razmer + '&l=' + s + vse
        response = requests.get(map_request)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
    else:
        x = str(float(x) - 0.5 * float(razmer))
        geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + x + ',' + y + '&format=json'
        response = requests.get(geocoder_request)
        a = response.json()
        b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[1] + '&spn=' + razmer + ',' + razmer + '&l=' + s + vse
        response = requests.get(map_request)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)


def u():
    global x
    global y
    if (float(str(float(y) + 0.5 * float(razmer))) + float(razmer) / 2 > 88.7 or float(str(float(y) + 0.5 * float(razmer))) - float(razmer) / 2 < -88.7) or (
            float(x) + float(razmer) / 2 > 179.9 or float(x) - float(razmer) / 2 < -179.9):
        geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + x + ',' + y + '&format=json'
        response = requests.get(geocoder_request)
        a = response.json()
        b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[
            1] + '&spn=' + razmer + ',' + razmer + '&l=' + s + vse
        response = requests.get(map_request)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
    else:
        y = str(float(y) + 0.5 * float(razmer))
        geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + x + ',' + y + '&format=json'
        response = requests.get(geocoder_request)
        a = response.json()
        b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[1] + '&spn=' + razmer + ',' + razmer + '&l=' + s + vse
        response = requests.get(map_request)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)


def s1():
    global s
    s = 'map'
    geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + x + ',' + y + '&format=json'
    response = requests.get(geocoder_request)
    a = response.json()
    b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
    map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[
        1] + '&spn=' + razmer + ',' + razmer + '&l=' + s + vse
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)


def s2():
    global s
    s = 'sat'
    geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + x + ',' + y + '&format=json'
    response = requests.get(geocoder_request)
    a = response.json()
    b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
    map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[
        1] + '&spn=' + razmer + ',' + razmer + '&l=' + s + vse
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)


def s3():
    global s
    s = 'sat,skl'
    geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + x + ',' + y + '&format=json'
    response = requests.get(geocoder_request)
    a = response.json()
    b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
    map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[
        1] + '&spn=' + razmer + ',' + razmer + '&l=' + s + vse
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)


def d():
    global x
    global y
    if (float(str(float(y) + 0.5 * float(razmer))) + float(razmer) / 2 > 88.7 or float(str(float(y) + 0.5 * float(razmer))) - float(razmer) / 2 < -88.7) or (
            float(x) + float(razmer) / 2 > 179.9 or float(x) - float(razmer) / 2 < -179.9):
        geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + x + ',' + y + '&format=json'
        response = requests.get(geocoder_request)
        a = response.json()
        b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[
            1] + '&spn=' + razmer + ',' + razmer + '&l=' + s + vse
        response = requests.get(map_request)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)
    else:
        y = str(float(y) - 0.5 * float(razmer))
        geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + x + ',' + y + '&format=json'
        response = requests.get(geocoder_request)
        a = response.json()
        b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
        map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[1] + '&spn=' + razmer + ',' + razmer + '&l=' + s + vse
        response = requests.get(map_request)
        map_file = "map.png"
        with open(map_file, "wb") as file:
            file.write(response.content)


def e():
    global x
    global y
    global vse
    geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + z + '&format=json'
    response = requests.get(geocoder_request)
    if response:
        a2 = response.json()
        x = a2['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()[0]
        y = a2['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()[1]
        if len(vse) == 4:
            vse += x + ',' + y + ',' + 'ya_ru'
        else:
            vse += '~' + x + ',' + y + ',' + 'ya_ru'
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
    geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + x + ',' + y + '&format=json'
    response = requests.get(geocoder_request)
    a = response.json()
    b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
    map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[
        1] + '&spn=' + razmer + ',' + razmer + '&l=' + s + vse
    response = requests.get(map_request)
    map_file = "map.png"
    with open(map_file, "wb") as file:
        file.write(response.content)

razmer = '0.002'
s = 'map'
x = '37.796157'
y = '55.790413'
z = ''
vse = '&pt='
white = (255, 255, 255)   # белый
yellow = (255, 255, 0)
blue = (0, 0, 255)
geocoder_request = 'http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode=' + x + ',' + y + '&format=json'
response = requests.get(geocoder_request)
a = response.json()
b = a['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos'].split()
map_request = 'http://static-maps.yandex.ru/1.x/?ll=' + b[0] + ',' + b[1] + '&spn=' + razmer + ',' + razmer + '&l=map'
response = requests.get(map_request)
map_file = "map.png"
with open(map_file, "wb") as file:
    file.write(response.content)
pygame.init()
screen = pygame.display.set_mode((600, 450))
running = True
fps = 60
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_PAGEUP:
                pgu()
            elif event.key == pygame.K_PAGEDOWN:
                pgd()
            elif event.key == pygame.K_RIGHT:
                r()
            elif event.key == pygame.K_LEFT:
                l1()
            elif event.key == pygame.K_UP:
                u()
            elif event.key == pygame.K_DOWN:
                d()
            elif event.key == pygame.K_F9:
                s1()
            elif event.key == pygame.K_F10:
                s2()
            elif event.key == pygame.K_F11:
                s3()
            elif event.key == pygame.K_RETURN:
                e()
                z = ''
            elif event.key == 8:
                z = z[:-1]
            else:
                z += str(event.unicode)
                print(z)
    screen.fill((255, 255, 255))
    screen.blit(pygame.image.load(map_file), (0, 0))
    pygame.draw.rect(screen, (0, 0, 0), (0, 420, 600, 450), 3)
    fontObj = pygame.font.Font('freesansbold.ttf', 20)
    textSurfaceObj = fontObj.render(z, True, (0, 0, 0), None)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj = (0, 425)
    screen.blit(textSurfaceObj, textRectObj)
    pygame.display.flip()
    clock.tick(fps)
os.remove(map_file)
