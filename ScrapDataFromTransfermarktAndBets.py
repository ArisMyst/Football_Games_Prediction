# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 17:14:08 2020

@author: User
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

def PL_ValueData():
    
    headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    
    #Process League Table
    page = "https://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB1"
    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
    
    TeamName = pageSoup.find_all("td", {"class": "hauptlink no-border-links hide-for-small hide-for-pad"})
    print(TeamName[2].text)
    TeamAvgAge = pageSoup.find_all("td", {"class": "zentriert hide-for-small hide-for-pad"})
    print(TeamAvgAge[2].text)
    #Values = pageSoup.find_all("td", {"class": "rechts hide-for-small hide-for-pad"})
    Values = pageSoup.find_all("td", {"class": "rechts show-for-small show-for-pad nowrap"})
    
    print(Values[2].text)
       
    AgeList = []
    ValuesList = []
    TeamList = []
    AvgValueList = []
    
    for i in range(2,42,2):
        ValuesList.append(Values[i].text)
    
    for i in range(3,43,2):
        AvgValueList.append(Values[i].text)
    
    for i in range(0,20):
        TeamList.append(TeamName[i].text)
         
    for i in range(1,21):
        AgeList.append(TeamAvgAge[i].text)
        
    df = pd.DataFrame({"Team":TeamList, "Age":AgeList,"Values":ValuesList, "AvgValues":AvgValueList})    
    print(df.head(30))
    print(TeamList[19])
    
def DE_ValueData():
    
    headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    
    #Process League Table
    page = "https://www.transfermarkt.com/bundesliga/startseite/wettbewerb/L1"
    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
    
    TeamName = pageSoup.find_all("td", {"class": "hauptlink no-border-links hide-for-small hide-for-pad"})
    print(TeamName[2].text)
    TeamAvgAge = pageSoup.find_all("td", {"class": "zentriert hide-for-small hide-for-pad"})
    print(TeamAvgAge[2].text)
    #Values = pageSoup.find_all("td", {"class": "rechts hide-for-small hide-for-pad"})
    Values = pageSoup.find_all("td", {"class": "rechts show-for-small show-for-pad nowrap"})
    
    print(Values[2].text)
       
    AgeList = []
    ValuesList = []
    TeamList = []
    AvgValueList = []
    
    for i in range(2,38,2):
        ValuesList.append(Values[i].text)
    
    for i in range(3,39,2):
        AvgValueList.append(Values[i].text)
    
    for i in range(0,18):
        TeamList.append(TeamName[i].text)
         
    for i in range(1,19):
        AgeList.append(TeamAvgAge[i].text)
        
    df = pd.DataFrame({"Team":TeamList, "Age":AgeList,"Values":ValuesList, "AvgValues":AvgValueList})    
    print(df.head(30))
    print(TeamList[17])
    
def GR_ValueData():
    
    headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    
    #Process League Table
    page = "https://www.transfermarkt.com/super-league-1/startseite/wettbewerb/GR1"
    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
    
    TeamName = pageSoup.find_all("td", {"class": "hauptlink no-border-links hide-for-small hide-for-pad"})
    print(TeamName[2].text)
    TeamAvgAge = pageSoup.find_all("td", {"class": "zentriert hide-for-small hide-for-pad"})
    print(TeamAvgAge[2].text)
    #Values = pageSoup.find_all("td", {"class": "rechts hide-for-small hide-for-pad"})
    Values = pageSoup.find_all("td", {"class": "rechts show-for-small show-for-pad nowrap"})
    
#    print(Values[2].text)
       
    AgeList = []
    ValuesList = []
    TeamList = []
    AvgValueList = []
    
    for i in range(2,30,2):
        ValuesList.append(Values[i].text)
        
    print(len(ValuesList))
    for i in range(3,31,2):
        AvgValueList.append(Values[i].text)
        
    print(len(AvgValueList))
    for i in range(0,14):
        TeamList.append(TeamName[i].text)
        
    print(len(TeamList))  
    for i in range(1,15):
        AgeList.append(TeamAvgAge[i].text)
        
    print(len(AgeList))
    df = pd.DataFrame({"Team":TeamList, "Age":AgeList,"Values":ValuesList, "AvgValues":AvgValueList})    
    print(df.head(14))
#    print(TeamList[19])

def getTeamValueDataTransfermarkt(url, TeamNo):
    
    headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    
    #Process League Table
    page = url
    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
    
    TeamName = pageSoup.find_all("td", {"class": "hauptlink no-border-links hide-for-small hide-for-pad"})
    print(TeamName[2].text)
    TeamAvgAge = pageSoup.find_all("td", {"class": "zentriert hide-for-small hide-for-pad"})
    print(TeamAvgAge[2].text)
    #Values = pageSoup.find_all("td", {"class": "rechts hide-for-small hide-for-pad"})
    Values = pageSoup.find_all("td", {"class": "rechts show-for-small show-for-pad nowrap"})
    
    print(Values[2].text)
       
    AgeList = []
    ValuesList = []
    TeamList = []
    AvgValueList = []
    
    for i in range(2,(TeamNo*2) + 2,2):
        ValuesList.append(Values[i].text)
    
    for i in range(3, (TeamNo*2) + 3,2):
        AvgValueList.append(Values[i].text)
    
    for i in range(0,TeamNo):
        TeamList.append(TeamName[i].text)
         
    for i in range(1,TeamNo + 1):
        AgeList.append(TeamAvgAge[i].text)
        
    df = pd.DataFrame({"Team":TeamList, "Age":AgeList,"Values":ValuesList, "AvgValues":AvgValueList})    
    print(df.head(30))
    print(TeamList[17])
    
def Bet365_Data(url):
    
    headers = {'User-Agent': 
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    
    #Process League Table
#    page = "https://www.stoiximan.gr/match-odds/Asteras-Tripolis-Aris-Thessaloniki-4782369"
    page = url
    pageTree = requests.get(page, headers=headers)
    pageSoup = BeautifulSoup(pageTree.content, 'html.parser')
    
    TeamNameOdd = pageSoup.find_all("div", {"class": "pull-right text-right price-selection"})
    TeamName = pageSoup.find_all("div", {"class": "pull-left title-selection"})
#    print(pageSoup.find_all("span", {"class": "gl-Participant_Name"}))
    print(len(TeamName))  
    for i in range(8,19):
        print(TeamName[i-1].text +"---" +TeamNameOdd[i].text) 
    
    urls = []
    urls= url.split('/')    
    print(urls[4])


def Bet365_Data2():
    from selenium import webdriver
    from bs4 import BeautifulSoup
    
    url = "https://www.bet365.gr/#/AC/B1/C1/D8/E85788381/F3/G0/H0/I1/P^13/Q^37628398"
#    driver = webdriver.Chrome()
    driver = webdriver.Chrome("C:/Users/Mangekyo/Downloads/chromedriver_win32/chromedriver.exe")

    driver.get(url)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    containers = soup.findAll("div", {"class": "gl-MarketGroup sc-MarketGroupSoccer"})
    resultAndOdds = []    
    for container in containers:
        divs = container.findAll('div')
        texts = [div.text for div in divs]
        it = iter(texts)
        resultAndOdds.append(list(zip(it, it)))
        
    print(resultAndOdds[0])
    
#Bet365_Data("https://www.stoiximan.gr/match-odds/Panaitolikos-Volos-Nps-4782373")
#Bet365_Data("https://www.stoiximan.gr/match-odds/Sheffield-Utd-Brighton-Hove-Albion-4007985")
#Bet365_Data("https://www.stoiximan.gr/match-odds/Leicester-Aston-Villa-4013482")
#Bet365_Data2()
#PL_ValueData()
#GR_ValueData()
#DE_ValueData()
getTeamValueDataTransfermarkt("https://www.transfermarkt.com/super-lig/startseite/wettbewerb/TR1" , 18)
