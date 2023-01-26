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
    driver.get('http://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=ac054d819b29292cffe0bdc3ef48d419&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5')

    driver.implicitly_wait(1)

    data_list2=[]

    #time.sleep(5)
    shutil.copy('datacopy2.txt', 'datacopy1.txt')

    id = driver.find_element_by_id('thesisInfoDiv')
    data_list2.append(id.text)

    file = open('datacopy2.txt', 'w', encoding = 'utf-8')
    for data in data_list2:
        file.write(data + '\n')
    file.close()



    driver.close()
        
    print(datetime.datetime.now())

    if i == 1: #크롤링 횟수
         sys.exit()

    #크롤링 주기(입력 숫자+7초)

    threading.Timer(3, chromedriver).start() #TEST
    #threading.Timer(3593, chromedriver).start()

chromedriver()