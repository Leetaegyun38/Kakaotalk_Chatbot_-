from selenium import webdriver #크롤링
import datetime #실행시각출력
import time #시간지연
import threading #주기적실행
import sys #프로그램종료
import shutil #파일복사
import os #파일삭제
from bs4 import BeautifulSoup as bs
import urllib.request
import re
import pandas as pd
import getpass

i=0

def chromedriver(): 

    global i
    i = i + 1

    driver = webdriver.Chrome('./chromedriver')
    driver.get('http://www.riss.kr/search/detail/DetailView.do?p_mat_type=be54d9b8bc7cdb09&control_no=ac054d819b29292cffe0bdc3ef48d419&keyword=%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5')

    driver.implicitly_wait(1)
    
    html = driver.page_source
    soup = bs(html, "html.parser")

    title = soup.find("h3", "title")
    title_txt = title.get_text("", strip=True).split("=")
    title_kor = re.sub("\n\b", "", str(title_txt[0]).strip())
    title_eng = str(title_txt[1]).strip()

    txt_box = []
    for text in soup.find_all("div", "text")
        txt = text.get_text("", strip=True)
        txt_box.append(txt)
    
    txt_kor = txt_box[1]
    txt_eng = txt_box[3]

    detail_box = []
    detail_info = soup.select(
        "#soptionview>div>div.thesisinfo>div.infoDetail.on>div.infoDetaiL>ul>li>div>p"
    )

    for detail in detail_info:
        detail_content = detail.get_text("", strip=True)
        detail_wrap = []
        detail_wrap.append(detail_content)

        detail_box.append(detail_Wrap)

    author = ",".join(detail_box[0])
    book = (
        "".joi(detail_box[2] + detail_box[3]).replace("\n", "").replace("\t", "").replace("", "")
        + "p."
        + "".join(detail_box[-2])
    )
    keyword = ",".join(detail_box[6])

    reference_data = pd.DataFrame(
        {
            "저자": [author],
            "국문 제목": [title_kor],
            "영문 제목": [title_eng],
            "수록지": [book],
            "핵심어": [keyword],
            "국문 요약": [txt_kor],
            "영문 요약": [txt_eng],
        }
    )

    driver.close()

    return reference_data


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