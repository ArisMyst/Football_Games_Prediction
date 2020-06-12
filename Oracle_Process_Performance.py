# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:31:12 2020

@author: Mangekyo
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 17:52:48 2019

@author: Mangekyo
"""




import urllib.request, json 
import cx_Oracle
import os, json
import pandas as pd
from glob import glob
import time
from datetime import datetime, timedelta

 
def ParseDB():
    dsn_tns = cx_Oracle.makedsn('localhost', '1521', service_name='orcl3') #if needed, place an 'r' before any parameter in order to address any special character such as '\'.
    conn = cx_Oracle.connect(user='system', password='26282628', dsn=dsn_tns) #if needed, place an 'r' before any parameter in order to address any special character such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'
    
    c = conn.cursor()
    c.execute('select TEAM_NAME from FTB_EN_PREMIERLEAGUE_VALUES') # use triple quotes if you want to spread your query across multiple lines
    TEAM_NAME = []
    for row in c:
        TEAM_NAME.append(row[0])
                
    print('TEAM_NAME IS ', len(TEAM_NAME))
    
    for x in range(0, len(TEAM_NAME)):
        print(str(TEAM_NAME[x]))
        teamName = str(TEAM_NAME[x])
        c.execute('''SELECT TEAM_NAME TEAM_NAME,
                        FTR FTR,
                        MATCH_DATE MATCH_DATE,
                        LOCATION LOCATION,
                        CASE
                        WHEN FTR = LOCATION THEN '3'
                        WHEN FTR = 'D' THEN '1'
                        ELSE '0'
                        END AS POINTS
                        FROM 
                        ((SELECT T1.TEAM_NAME, T2.FTR, T2.MATCH_DATE, 'H' AS LOCATION FROM FTB_EN_PREMIERLEAGUE_VALUES T1
                        INNER JOIN FTB_EN_PREMIERLEAGUE_GAMES T2 ON T1.TEAM_NAME = T2.HOMETEAM
                        WHERE T1.TEAM_NAME IN (:1))
                        UNION ALL
                        (SELECT T1.TEAM_NAME, T2.FTR, T2.MATCH_DATE, 'A' AS LOCATION FROM FTB_EN_PREMIERLEAGUE_VALUES T1
                        INNER JOIN FTB_EN_PREMIERLEAGUE_GAMES T2 ON T1.TEAM_NAME = T2.AWAYTEAM
                        WHERE T1.TEAM_NAME IN (:1))
                        ORDER BY MATCH_DATE)''',{"1" : teamName})
        
        TeamName = []
        Date = []
        Points = []
        Performance = []                
        for row in c:
            print(row[0] + '-' + row[4])
#            int(row[4])
            TeamName.append(row[0])
            Date.append(row[2])
            Points.append(row[4])
        
        for i in range(0, len(TeamName)): 
            performance = None
            if i == 0:
                performance = 0.5
                Performance.append(performance)                
            elif i == 1:
                performance = int(Points[0])/3
                Performance.append(performance)  
            elif i == 2:
                performance = (int(Points[0]) + int(Points[1]))/6
                Performance.append(performance)               
            elif i == 3:
                performance = (int(Points[0]) + int(Points[1]) + int(Points[2]) )/9
                Performance.append(performance)
            else:
                performance = (int(Points[i-4]) + int(Points[i-3]) + int(Points[i-2]) +int(Points[i-1]) )/12
                Performance.append(performance)
                
            print(TeamName[i] + '-' +str(Date[i]) + '-' +str(performance))
            c.execute('''INSERT INTO FTB_EN_PL_TEAM_PERFORMANCE 
                  (PERFORMANCE, MATCH_DATE, TEAMNAME) 
                  VALUES  
                  (:1, :2, :3)''',
                  {"1" : performance, "2" : Date[i], "3" : TeamName[i]})
#            c.execute('''INSERT INTO FTB_EN_PREMIERLEAGUE_GAMES 
#                              (PERFORMANCE) 
#                              VALUES  
#                              (:1)
#                              WHERE MATCH_DATE = (:2) AND (HOMETEAM = (:3) OR AWAYTEAM = (:3))''',
#                              {"1" : performance, "2" : Date[i], "3" : TeamName[i]})
           
            c.execute('COMMIT')
  
        print(row)      
#            print(row)

ParseDB() 
    
  
            
print('done2')   

