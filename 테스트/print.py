from selenium import webdriver #크롤링
import datetime #실행시각출력
import time #시간지연
import threading #주기적실행
import sys #프로그램종료
import shutil #파일복사
import os #파일삭제

i=0

def chromedriver(): 

    global i
    i = i + 1

    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://sada.gbshs.kr/today/timetable.php')

    driver.implicitly_wait(1)
    getid = driver.find_element_by_id('Grade')
    getid.clear()
    getid.send_keys('2')
    getpw = driver.find_element_by_id('Class')
    getpw.clear()
    getpw.send_keys('2')
    driver.find_element_by_class_name('setTimetableInfoButton').click()

    data_list2=[]

    os.remove('datacopy1.txt')
    #time.sleep(5)
    shutil.copy('datacopy2.txt', 'datacopy1.txt')

    id = driver.find_element_by_id('cell-0-0')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-0-1')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-0-2')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-0-3')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-0-4')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-0-5')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-0-6')
    data_list2.append(id.text)

    id = driver.find_element_by_id('cell-1-0')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-1-1')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-1-2')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-1-3')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-1-4')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-1-5')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-1-6')
    data_list2.append(id.text)


    id = driver.find_element_by_id('cell-2-0')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-2-1')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-2-2')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-2-3')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-2-4')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-2-5')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-2-6')
    data_list2.append(id.text)

    id = driver.find_element_by_id('cell-3-0')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-3-1')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-3-2')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-3-3')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-3-4')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-3-5')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-3-6')
    data_list2.append(id.text)

    id = driver.find_element_by_id('cell-4-0')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-4-1')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-4-2')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-4-3')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-4-4')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-4-5')
    data_list2.append(id.text)
    id = driver.find_element_by_id('cell-4-6')
    data_list2.append(id.text)

    file = open('datacopy2.txt', 'w', encoding = 'utf-8')
    for data in data_list2:
        file.write(data + '\n')
    file.close()

    if i == 1:
        file = open('datacopy1.txt', 'w', encoding = 'utf-8')
        for data in data_list2:
            file.write(data + '\n')
        file.close()

    driver.close()
        
    print(datetime.datetime.now())

    if i == 2: #크롤링 횟수
         sys.exit()

    #크롤링 주기(입력 숫자+7초)

    threading.Timer(3, chromedriver).start() #TEST
    #threading.Timer(3593, chromedriver).start()

chromedriver()