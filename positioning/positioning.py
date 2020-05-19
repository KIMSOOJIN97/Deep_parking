import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

car_position = []
car_number = []

fp = open('car_position.txt', mode='rt', encoding="utf8")
fn = open('car_number.txt', mode='rt')
number = 0

for line in fp:
    data = line.split(' ')
    data_area = data[0]
    data_x = data[1]
    data_y = data[2]
    number += 1
    car_position.append({
        'area': data_area,
        'x': data_x,
        'y': data_y[:-1],
    })

for line in fn:
    car_number.append(line[:-1])

print(car_number)
print(car_position)

car_info = []
car_info = input('차량번호를 입력하세요 : ')

cnt = 0
find_num = 0
for j in range(0, number):
    for i in range(0, 7):
        if car_number[j][i] == car_info[i]:
            if cnt >= 6:
                continue
            cnt += 1
            find_num = j

result = cv2.imread('exPIC.jpg')
if cnt >= 5:
    if car_position[find_num]['area'] == 'A':
        x = 40
        y = 40
    elif car_position[find_num]['area'] == 'B':
        x = 550
        y = 40
    elif car_position[find_num]['area'] == 'C':
        x = 40
        y = 360
    else:
        x = 550
        y = 360
else:
    print('없는 차량입니다\n')

cv2.circle(result, (40, 40), 20, (0, 0, 255), -1)
cv2.circle(result, (550, 40), 20, (0, 255, 0), -1)
cv2.circle(result, (40, 360), 20, (255, 0, 0), -1)
cv2.circle(result, (550, 360), 20, (255, 0, 255), -1)
cv2.imshow('output', result)
cv2.waitKey()

a = cv2.imread('a.jpg')
red = (0, 0, 255)

if cnt >= 5:
    if car_position[find_num]['area']=='A':
        sum_y=(int(car_position[0]['y'])+int(car_position[1]['y'])+int(car_position[2]['y']))/3
        int(sum_y)
    elif car_position[find_num]['area']=='B':
        sum_y = (int(car_position[0]['y']) + int(car_position[1]['y']) + int(car_position[2]['y'])) / 3
        int(sum_y)
    elif car_position[find_num]['area']=='C':
        sum_y = (int(car_position[0]['y']) + int(car_position[1]['y']) + int(car_position[2]['y'])) / 3
        int(sum_y)
    else:
        sum_y = (int(car_position[0]['y']) + int(car_position[1]['y']) + int(car_position[2]['y'])) / 3
        int(sum_y)

if cnt >=5:
    if car_number[find_num]==car_number[0]:
        #print(car_info + "1")
        x1 = int(int(car_position[find_num]['x'])/4)
        y1 = int(sum_y/4)

        if 0 <= x1 <= 320 and 360 < y1 <= 720 :
            cv2.circle(a, (185, 530), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 0 <= x1 <= 320 and 0 <= y1 <= 360 :
            cv2.circle(a, (185, 200), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 320 < x1 <= 640 and 0 <= y1 <= 360 :
            cv2.circle(a, (485, 200), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 320 < x1 <= 640 and 360 < y1 <= 720 :
            cv2.circle(a, (485, 530), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 640 < x1 <= 960 and 0 <= y1 <= 360:
            cv2.circle(a, (785, 200), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 640 < x1 <= 960 and 360 < y1 <= 720:
            cv2.circle(a, (785, 530), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 960 < x1 <= 1280 and 0 <= y1 <= 360:
            cv2.circle(a, (1085, 200), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 960 < x1 <= 1280 and 360 < y1 <= 720:
            cv2.circle(a, (1085, 530), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()

    elif car_number[find_num]==car_number[1]:
        #print(car_info+"2")
        x2 = int(int(car_position[find_num]['x'])/4)
        y2 = int(sum_y/4)

        if 0 <= x2 <= 320 and 360 < y2 <= 720:
            cv2.circle(a, (185, 530), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 0 <= x2 <= 320 and 0 <= y2 <= 360:
            cv2.circle(a, (185, 200), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 320 < x2 <= 640 and 0 <= y2 <= 360:
            cv2.circle(a, (485, 200), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 320 < x2 <= 640 and 360 < y2 <= 720:
            cv2.circle(a, (485, 530), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 640 < x2 <= 960 and 0 <= y2 <= 360:
            cv2.circle(a, (785, 200), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 640 < x2 <= 960 and 360 < y2 <= 720:
            cv2.circle(a, (785, 530), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 960 < x2 <= 1280 and 0 <= y2 <= 360:
            cv2.circle(a, (1085, 200), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 960 < x2 <= 1280 and 360 < y2 <= 720:
            cv2.circle(a, (1085, 530), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()

    elif car_number[find_num]==car_number[2]:
        #print(car_info+"2")
        x3 = int(int(car_position[find_num]['x'])/4)
        y3 = int(sum_y/4)

        if 0 <= x3 <= 320 and 360 < y3 <= 720:
            cv2.circle(a, (185, 530), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 0 <= x3 <= 320 and 0 <= y3 <= 360:
            cv2.circle(a, (185, 200), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 320 < x3 <= 640 and 0 <= y3 <= 360:
            cv2.circle(a, (485, 200), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 320 < x3 <= 640 and 360 < y3 <= 720:
            cv2.circle(a, (485, 530), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 640 < x3 <= 960 and 0 <= y3 <= 360:
            cv2.circle(a, (785, 200), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 640 < x3 <= 960 and 360 < y3 <= 720:
            cv2.circle(a, (785, 530), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 960 < x3 <= 1280 and 0 <= y3 <= 360:
            cv2.circle(a, (1085, 200), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
        elif 960 < x3 <= 1280 and 360 < y3 <= 720:
            cv2.circle(a, (1085, 530), 20, red, -1)
            cv2.imshow('output', a)
            cv2.waitKey()
