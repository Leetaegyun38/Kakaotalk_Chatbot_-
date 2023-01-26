from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/timetable2', methods=['POST'])

def timetable2():

    f = open("/workspace/kakaochatbot/datacopy1.txt", 'r')
    table1 = f.readlines()
    f.close()
    f = open("/workspace/kakaochatbot/datacopy2.txt", 'r')
    table2 = f.readlines()
    f.close()

    req = request.get_json()

    date = req["action"]["detailParams"]["sys_date"]["value"]

    print(date)

    answervar = '\0'
    
    if(date == '{"date": "2020-11-09", "dateTag": "Monday", "dateHeadword": null, "year": null, "month": null, "day": null}'):
        answer1 = '<월요일>' + '\n\n' + '1교시: ' + table2[0] + ' ' + table2[1]
        answer2 = '2교시: ' + table2[2] + ' ' + table2[3]
        answer3 = '3교시: ' + table2[4] + ' ' + table2[5]
        answer4 = '4교시: ' + table2[6] + ' ' + table2[7]
        answer5 = '5교시: ' + table2[8] + ' ' + table2[9]
        answer6 = '6교시: ' + table2[10] + ' ' + table2[11]
        answer7 = '7교시: ' + table2[12] + ' ' + table2[13]
        i = 0
        while(i<=13):
            if(table1[i] != table2[i]):
                answervar = '\n' + '!! 최근 1시간 이내에 바뀐 시간표가 있습니다 !!' + '\n' + '<' + str(i/2+1) + '교시>' + '\n' + table1[i] + ' ' + table1[i+1] + ' -> ' + table2[i] + ' -> ' + table2[i+1]
            i = i+2
    elif(date == '{"date": "2020-11-10", "dateTag": "Tuesday", "dateHeadword": null, "year": null, "month": null, "day": null}'):
        answer1 = '<화요일>' + '\n\n' + '1교시: ' + table2[14] + ' ' + table2[15]
        answer2 = '2교시: ' + table2[16] + ' ' + table2[17]
        answer3 = '3교시: ' + table2[18] + ' ' + table2[19]
        answer4 = '4교시: ' + table2[20] + ' ' + table2[21]
        answer5 = '5교시: ' + table2[22] + ' ' + table2[23]
        answer6 = '6교시: ' + table2[24] + ' ' + table2[25]
        answer7 = '7교시: ' + table2[26] + ' ' + table2[27]
        i = 14
        while(i<=27):
            if(table1[i] != table2[i]):
                answervar = '\n' + '!! 최근 1시간 이내에 바뀐 시간표가 있습니다 !!' + '\n' + '<' + str(i/2+1) + '교시>' + '\n' + table1[i] + ' ' + table1[i+1] + ' -> ' + table2[i] + ' -> ' + table2[i+1]
            i = i+2
    elif(date == '{"date": "2020-11-11", "dateTag": "Wednesday", "dateHeadword": null, "year": null, "month": null, "day": null}'):
        answer1 = '<수요일>' + '\n\n' + '1교시: ' + table2[28] + ' ' + table2[29]
        answer2 = '2교시: ' + table2[30] + ' ' + table2[31]
        answer3 = '3교시: ' + table2[32] + ' ' + table2[33]
        answer4 = '4교시: ' + table2[34] + ' ' + table2[35]
        answer5 = '5교시: ' + table2[36] + ' ' + table2[37]
        answer6 = '6교시: ' + table2[38] + ' ' + table2[39]
        answer7 = '7교시: ' + table2[40] + ' ' + table2[41]
        i = 28
        while(i<=41):
            if(table1[i] != table2[i]):
                answervar = '\n' + '!! 최근 1시간 이내에 바뀐 시간표가 있습니다 !!' + '\n' + '<' + str(i/2+1) + '교시>' + '\n' + table1[i] + ' ' + table1[i+1] + ' -> ' + table2[i] + ' -> ' + table2[i+1]
            i = i+2
    elif(date == '{"date": "2020-11-12", "dateTag": "Thursday", "dateHeadword": null, "year": null, "month": null, "day": null}'):
        answer1 = '<목요일>' + '\n\n' + '1교시: ' + table2[42] + ' ' + table2[43]
        answer2 = '2교시: ' + table2[44] + ' ' + table2[45]
        answer3 = '3교시: ' + table2[46] + ' ' + table2[47]
        answer4 = '4교시: ' + table2[48] + ' ' + table2[49]
        answer5 = '5교시: ' + table2[50] + ' ' + table2[51]
        answer6 = '6교시: ' + table2[52] + ' ' + table2[53]
        answer7 = '7교시: ' + table2[54] + ' ' + table2[55]
        i = 42
        while(i<=55):
            if(table1[i] != table2[i]):
                answervar = '\n' + '!! 최근 1시간 이내에 바뀐 시간표가 있습니다 !!' + '\n' + '<' + str(i/2+1) + '교시>' + '\n' + table1[i] + ' ' + table1[i+1] + ' -> ' + table2[i] + ' -> ' + table2[i+1]
            i = i+2
    elif(date == '{"date": "2020-11-13", "dateTag": "Friday", "dateHeadword": null, "year": null, "month": null, "day": null}'):
        answer1 = '<금요일>' + '\n\n' + '1교시: ' + table2[56] + ' ' + table2[57]
        answer2 = '2교시: ' + table2[58] + ' ' + table2[59]
        answer3 = '3교시: ' + table2[60] + ' ' + table2[61]
        answer4 = '4교시: ' + table2[62] + ' ' + table2[63]
        answer5 = '5교시: ' + table2[64] + ' ' + table2[65]
        answer6 = '6교시: ' + table2[66] + ' ' + table2[67]
        answer7 = '7교시: ' + table2[68] + ' ' + table2[69]
        i = 56
        while(i<=69):
            if(table1[i] != table2[i]):
                answervar = '\n' + '!! 최근 1시간 이내에 바뀐 시간표가 있습니다 !!' + '\n' + '<' + str(i/2+1) + '교시>' + '\n' + table1[i] + ' ' + table1[i+1] + ' -> ' + table2[i] + ' -> ' + table2[i+1]
            i = i+2
    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer1 + '\n' + answer2 + '\n' + answer3 + '\n' + answer4+ '\n' + answer5+ '\n' + answer6+ '\n' + answer7 + answervar
                    }
                }
            ]
        }
    }

    return jsonify(res)

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=4998, threaded=True)