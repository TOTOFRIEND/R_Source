import os
import pandas as pd

# '~' user home directory
home_folder = os.path.expanduser("~")

# C:\Users\front\Documents\Python\data\NBA_2014_15
# 데이터 폴더 위치 지정
data_folder = os.path.join(home_folder, "Documents", "python", "data", "NBA_2014_15")
print(data_folder)

dat_files = ["nba_2014_10_dat.csv", "nba_2014_11_dat.csv", "nba_2014_12_dat.csv",
                 "nba_2015_01_dat.csv", "nba_2015_02_dat.csv", "nba_2015_03_dat.csv",
                "nba_2015_04_dat.csv", "nba_2015_05_dat.csv", "nba_2015_06_dat.csv"]

# 파일을 하나씩 읽어와 이 데이터를 cvs_objs에 추가한다.
cvs_dat = [ ]
for f in dat_files:
   month_data =  os.path.join(data_folder, f)
   cvs_dat.append(pd.read_csv(month_data))

s_result = pd.concat(cvs_dat, ignore_index=True)
s_result.cols = ["Date", "StartTime", "VisitorTeam", "VisitorPts",
                 "HomeTeam", "HomePts", "ScoreType", "Overtime",
                 "Notes"]

print(s_result['HomePts'])

print(len(s_result))


