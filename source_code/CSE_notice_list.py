import requests
import webbrowser
import os
page_num = 2700
page_list_num = 50

def go(page_num):
    URL = "http://computer.knu.ac.kr/06_sub/02_sub.html?no="+str(page_num)+"&bbs_cmd=view"
    webbrowser.open(URL)

print('ver.19.09.26')
print('< 경북대학교 컴퓨터학부 공지사항 리스트 >\n')

while(True):    # find last page_num
    URL = "http://computer.knu.ac.kr/06_sub/02_sub.html?no="+str(page_num)+"&bbs_cmd=view"
    if (requests.get(URL).status_code == 200):
        page_num +=1
    else:
        page_num -=1
        break

for pg_num in range(page_num, page_num-page_list_num, -1):
    URL = "http://computer.knu.ac.kr/06_sub/02_sub.html?no="+str(pg_num)+"&bbs_cmd=view"
    response = requests.get(URL)
    str1 = response.text
    str2 = str1.split("kboard-title")[1]
    str3 = str2.split("</p>")[0]
    str4 = str3[10:]
    print(pg_num,' | ', str4, end='\n', sep = '')

input_page_num = input("\n보려는 페이지의 번호(4자리 정수)를 입력하세요\n")

if(not input_page_num.isdecimal()):
    print("오류입니다")
    os.system("pause")
elif(not(page_num-page_list_num+1 <= int(input_page_num) <= page_num)):
    print("오류입니다")
    os.system("pause")
else:
    print("이동합니다")
    go(int(input_page_num))


