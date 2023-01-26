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
    driver.get('http://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount=0&orderBy=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&ccl_code=&inside_outside=&fric_yn=&image_yn=&gubun=&kdc=&ttsUseYn=&l_sub_code=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=1&resultKeyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=bib_t&colName=bib_t&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&clickKeyword=&relationKeyword=&query=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5')

    driver.implicitly_wait(1)

    data_list2=[]

    #time.sleep(5)
    shutil.copy('datacopy2.txt', 'datacopy1.txt')

    id = driver.find_element_by_id('divContent')
    #id = driver.find_element_by_class_name('cont')
    #id - driver.find_element_by_xpath('/html/body/div[1]/div[2]/div[4]/div[2]/div/div[3]/div[2]/ul/li[1]/div[2]/p[1]')
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