import os
from datetime import datetime as dt
from pathlib import Path

yy = str(dt.now().year)
mm = str(dt.now().month)
dd = str(dt.now().day)
a = yy+mm+dd

work_dir_root = Path('/home/arjun921/working_directory/Python-TIL/algorithms/')

todays_path = work_dir_root / yy / mm / dd

if not os.path.exists(todays_path):
    todays_path.mkdir(parents=True, exist_ok=True)
 

os.system('cd {} && code {}.py'.format(todays_path,a))
print(todays_path)

# Opens unsolved algorithms page from hackerrank
# os.system('google-chrome https://www.hackerrank.com/domains/algorithms?filters%5Bdifficulty%5D%5B%5D=medium&filters%5Bdifficulty%5D%5B%5D=hard')
# os.system('google-chrome https://www.hackerrank.com/interview/interview-preparation-kit')

# Opens unsolved problems from leetcode
print('Opening https://leetcode.com/problemset/algorithms/?status=Todo&listId=79h8rn6')
os.system('google-chrome "https://leetcode.com/problemset/algorithms/?status=Todo&listId=79h8rn6"')


