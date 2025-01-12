import time

timeArray = time.localtime(
    1692576000)
# 秒数
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
print(otherStyleTime)

#日期转为秒数

import datetime
t = datetime.datetime(2013, 12, 31, 0,0, 0, 0)
print((t-datetime.datetime(1970,1,1)).total_seconds())