import pandas
import html5lib
import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

def getpartyvotes(url):
    site = url
    dfs = pandas.read_html(site)
    votes = dfs[3]
    votes.columns = votes.loc[0]
    votes = votes.drop([0,20])
    votes.reset_index(drop=True, inplace=True)
    areacode = site.split('/')[6].split('.')[0]
    areaname = dfs[1].iloc[0,0][17:-6]
    countryname = areaname[:3]
    districtname = areaname[3:]
    if site[-9:-5] == '0000':
        voteplace = countryname + districtname + '總票數'
    else:
        voteplace = countryname + '第 ' + site[-9:-5] + ' 號投開票所'
    votes['投開票所縣市'] = countryname
    votes['投開票所鄉鎮市區'] = districtname
    votes['投開票所'] = voteplace
    votes['投開票所代號'] = areacode[1:]
    return votes

main_website_url = 'https://www.cec.gov.tw/pc/zh_TW/L4/n00000000000000000.html'
domain_prefix = 'https://www.cec.gov.tw/pc/zh_TW/'
driver = webdriver.Chrome('C:\selenium_driver_chrome\chromedriver.exe')
driver.get(main_website_url)
driver.find_element_by_id('folder1260').click()
# 政黨得票數 (不分區及僑居國外國民立法委員)

soup = BeautifulSoup(driver.page_source, 'lxml')
links = soup.select('div[id^=folder] a')[5:-10][::2]
country_code = []
districts_website_url = []

for ele in links:
    # print(ele.get('href')[-6:-2])
    country_code.append(ele.get('href')[-6:-2])

for ele in range(len(country_code)):
    driver.get(main_website_url)
    # print('folder' + country_code[ele])  
    driver.find_element_by_id('folder' + country_code[ele]).click()
    soup = BeautifulSoup(driver.page_source, 'lxml')
    links = soup.select('div[id^=item] a')
    for i in links:
        districts_website_url.append(domain_prefix + i.get('href')[3:])

votes_result = []
print('')
print('******************************************')
print('*                                        *')
print('*  2020_Taiwan_Election_Results_Crawler  *')
print('* Party-list proportional representation *')
print('*            不分區立委政黨票             *')
print('*                                        *')
print('******************************************')
print('')
print('There are total ', len(districts_website_url), 'districts during 2020 Taiwan election.')
print('')

for ct in range(len(districts_website_url)):
# for ct in range(2): # for test only
    driver.get(districts_website_url[ct])
    soup = BeautifulSoup(driver.page_source, 'lxml')
    links = soup.select('option[value]')
    for ele in links:
        try:
            votes_result.append(getpartyvotes(domain_prefix + 'L4/' + ele.get('value')))
        except:
            continue
            # 以下除錯用，如果想知道有哪些網站沒抓好就print出來。
            # print(domain_prefix + 'L4/' + ele.get('value'))
    print(ct+1, ' / ', len(districts_website_url), ' is DONE.')
votes_result = pandas.concat(votes_result)
votes_result.reset_index(drop = True, inplace = True)
votes_result = pandas.DataFrame(votes_result)     

#print(votes_result)
print('')
print('SUCCESS, ready to output as a .csv file')
father_path = os.getcwd()
file_name = input("input the file name you wish: ")
path_csv = father_path + '\\' + file_name + '.csv'
votes_result.to_csv(path_csv, encoding = 'utf-8') # 編碼可以自行設定
print('')
print('Ouput Success, the file is in ' + path_csv)
print('')
print('Repository: https://github.com/rutopio/2020_Taiwan_Election_Results_Crawler')
