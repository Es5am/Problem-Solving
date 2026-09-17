import requests
import csv
import os
from bs4 import BeautifulSoup
from itertools import zip_longest

title,skill,company_name,location = [],[],[],[]
page_number = 0

session = requests.Session()
while True:
    
    result = session.get(f"https://wuzzuf.net/search/jobs?q=python&start={page_number}&a=hpb")
    scr = result.content

    soup = BeautifulSoup(scr,"lxml")
    page_limit = int(soup.find('p', {'class': 'css-17yjama'}).strong.text)
    job_titles = soup.find_all('h2',{'class':'css-193uk2c'})
    job_skills = soup.find_all('div',{'class':'css-1rhj4yg'})
    company_names = soup.find_all("a",{"class": "css-ipsyv7"})
    locations = soup.find_all("span",{'class':'css-16x61xq'})

    for i in range(len(job_titles)):
        title.append(job_titles[i].text)
        skill.append(job_skills[i].select_one('div:nth-of-type(2)').text)
        company_name.append(company_names[i].text)
        location.append(locations[i].text)

    print(page_number+1)
    page_number+=1
    if page_number > (page_limit//15) :
        print('Page Ends')
        break


data = [title,company_name,location,skill]
ex_data = zip_longest(*data)
with open(r'D:\Work\Elzero\Python\Lib\Beautiful_Soup\Jobs.csv', "w", encoding="utf-8", newline='') as myfile:
    wr = csv.writer(myfile)
    wr.writerow(['Job Title','Location','Company Name','Job Skills'])
    wr.writerows(ex_data)

file_name = r"D:\Work\Elzero\Python\Lib\Beautiful_Soup\1\Jobs.csv" #File Path 
os.startfile(file_name)





