import json
from pandas import DataFrame
import pandas as pd
import requests
import emails

file_name = 'teste.csv'


def getJson():
    r = requests.get('https://api.biscoint.io/v1/ticker?base=BTC&quote=BRL')

    df_new = pd.DataFrame()
    df = pd.DataFrame(json.loads(r.text))
    date = pd.Timestamp.date(pd.Timestamp(
        df['data']['timestamp'], tz='America/Fortaleza'))
    time = pd.Timestamp.time(pd.Timestamp(
        df['data']['timestamp'], tz='America/Fortaleza')).strftime('%H:%M:%S')

    df_new['ask'] = [df['data']['ask']]
    df_new['bid'] = [df['data']['bid']]
    df_new['high'] = [df['data']['high']]
    df_new['last'] = [df['data']['last']]
    df_new['low'] = [df['data']['low']]
    df_new['vol'] = [df['data']['vol']]
    df_new['date'] = [date]
    df_new['time'] = [time]

    last = df_new['last'][0]
    low = df_new['low'][0]
    diff = (1-(last / low))

    if diff > 0.04:
        high = df_new['high'][0]
        emails.send_email(last, low, diff, high)

    with open(file_name, 'a') as f:
        df_new.to_csv(f, header=f.tell() == 0)


if __name__ == '__main__':
    # testar()
    getJson()
