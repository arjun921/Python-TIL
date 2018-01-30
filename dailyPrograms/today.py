import os
from datetime import datetime as dt
from pathlib import Path

yy = str(dt.now().year)
mm = str(dt.now().month)
dd = str(dt.now().day)
a = yy+mm+dd
# print(a)
workingDir_root = Path('/Users/arjun921/working_directory/refactored-lamp/dailyPrograms/')

if not os.path.exists(workingDir_root / yy):
    os.makedirs(workingDir_root / yy)
if not os.path.exists(workingDir_root / yy / mm):
    os.makedirs(workingDir_root / yy / mm)
if not os.path.exists(workingDir_root / yy / mm / dd):
    os.makedirs(workingDir_root / yy / mm / dd)


os.system('cd {} && atom {}.py'.format(workingDir_root / yy / mm / dd,a))
a = str(workingDir_root / yy / mm / dd )
print(a + "/")
