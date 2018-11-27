# encoding: utf-8
from matplotlib import rcParams
import matplotlib.pyplot as plt
import numpy as np
np.seterr(all='ignore')
rcParams['figure.figsize'] = (14, 6)
from funcat import * #FUNCAT的同花顺/通达信指标模块：和：&，或：|，其他基本相同。可以使用指标选股！！！
from tushare import * #TUSHARE数据连接更新。
from rqalpha import * #RQALPHA本地数据连接，通过 rqalpha update_bundle 8点后更新全部数据库
from funcat.data.tushare_backend import TushareDataBackend
from funcat.data.rqalpha_data_backend import RQAlphaDataBackend
backend = "rqalpha"
if backend == "rqalpha":
    set_data_backend(RQAlphaDataBackend("~/.rqalpha/bundle"))
elif backend == "tushare":
    set_data_backend(TushareDataBackend())
set_start_date(20170101)
#S("000001.XSHG")  # 设置当前关注股票
#T("20080202")   # 设置当前观察日期    

def callback(date, order_book_id,symbol):
    print(date,order_book_id,symbol) 
select(
    lambda : O / H[1] - 1 >= 0.0995,
    start_date=("20180205"),
    end_date=("20180206"),
    callback=callback,
)

