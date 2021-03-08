import pandas as pd
import mplfinance as mpf
import requests

from urllib.request import urlopen
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt



# url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'
# with urlopen(url) as doc:
#     html = BeautifulSoup(requests.get(url, headers={'User-agent': 'Mozilla/5.0'}).text, "lxml")
#     pgrr = html.find('td', class_='pgRR')
#     s = str(pgrr.a['href']).split('=')
#     last_page = int(s[-1])

# df = pd.DataFrame()
# sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'

# for page in range(1, last_page + 1):
#     page_url = '{}&page={}'.format(sise_url, page)
#     df = df.append(pd.read_html(requests.get(page_url, headers={'User-agent': 'Mozilla/5.0'}).text)[0])


# df = df.dropna()
# df = df.iloc[0:30]
# df = df.rename(
#     columns = {
#         '날짜' : 'Date',
#         '시가' : 'Open',
#         '고가' : 'High',
#         '저가' : 'Low',
#         '종가' : 'Close',
#         '거래량' : 'Volume'
#     })
# df = df.sort_values(by='Date')
# df.index = pd.to_datetime(df.Date)
# df = df[['Open', 'High', 'Low', 'Close', 'Volume']]

# mpf.plot(df, title='Celltrion candle chart', type='candle')



#  def read_naver(self, code, company, pages_to_fetch):
#         """네이버에서 주식 시세를 읽어서 데이터프레임으로 반환"""
#         try:
#             url = f"http://finance.naver.com/item/sise_day.nhn?code={code}"
#             html = BeautifulSoup(requests.get(url,
#                 headers={'User-agent': 'Mozilla/5.0'}).text, "lxml")
#             pgrr = html.find("td", class_="pgRR")
#             if pgrr is None:
#                 return None
#             s = str(pgrr.a["href"]).split('=')
#             lastpage = s[-1] 
#             df = pd.DataFrame()
#             pages = min(int(lastpage), pages_to_fetch)
#             for page in range(1, pages + 1):
#                 pg_url = '{}&page={}'.format(url, page)
#                 df = df.append(pd.read_html(requests.get(pg_url,
#                     headers={'User-agent': 'Mozilla/5.0'}).text)[0])                                          
#                 tmnow = datetime.now().strftime('%Y-%m-%d %H:%M')
#                 print('[{}] {} ({}) : {:04d}/{:04d} pages are downloading...'.
#                     format(tmnow, company, code, page, pages), end="\r")
#             df = df.rename(columns={'날짜':'date','종가':'close','전일비':'diff'
#                 ,'시가':'open','고가':'high','저가':'low','거래량':'volume'})
#             df['date'] = df['date'].replace('.', '-')
#             df = df.dropna()
#             df[['close', 'diff', 'open', 'high', 'low', 'volume']] = df[['close',
#                 'diff', 'open', 'high', 'low', 'volume']].astype(int)
#             df = df[['date', 'open', 'high', 'low', 'close', 'diff', 'volume']]
#         except Exception as e:
#             print('Exception occured :', str(e))
#             return None
#         return df


# url = 'https://finance.naver.com/item/sise_day.nhn?code=068270&page=1'
# with urlopen(url) as doc:
#     html = BeautifulSoup(doc, 'lxml') 
#     pgrr = html.find('td', class_='pgRR')
#     s = str(pgrr.a['href']).split('=')
#     last_page = s[-1]  

# df = pd.DataFrame()
# sise_url = 'https://finance.naver.com/item/sise_day.nhn?code=068270'  
# for page in range(1, int(last_page)+1):
#     page_url = '{}&page={}'.format(sise_url, page)  
#     df = df.append(pd.read_html(page_url, header=0)[0])

# df = df.dropna()
# df = df.iloc[0:30] 
# df = df.sort_values(by='날짜') 

# plt.title('Celltrion (close)')
# plt.xticks(rotation=45) 
# plt.plot(df['날짜'], df['종가'], 'co-')
# plt.grid(color='gray', linestyle='--')
# plt.show()

from Investar import Analyzer 

mk = Analyzer.MarketDB()  
df = mk.get_daily_price('005930', '2017-07-10', '2018-06-30')  # â‘¢

plt.figure(figsize=(9, 6))
plt.subplot(2, 1, 1)
plt.title('Samsung Electronics (Investar Data)')
plt.plot(df.index, df['close'], 'c', label='Close')  # â‘£
plt.legend(loc='best')
plt.subplot(2, 1, 2)
plt.bar(df.index, df['volume'], color='g', label='Volume')
plt.legend(loc='best')
plt.show()

