import time
from datetime import date
dateNow = str(date.today())+'-'+str(int(time.time()))
inp = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
print(dateNow)
print(inp)

"""
备注：更新推送
"""
