# 导入时间包
import datetime
# 导入Tushare 开源python财经数据接口包
import tushare as tsimport

time = datetime.date
# 打印当前时间
print(time.today())


print(tsimport.get_hist_data());
