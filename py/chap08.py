#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import urllib.request

url = 'https://blog.python.org/'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    body = str(res.read())

if 'security' in body or 'vulnerability' in body:
    print('セキュリティに関する記述があります')
    print('https://blog.python.org/を確認してください')
else:
    print('調査対象のセキュリティ用語はありませんでした')


# In[ ]:


import sqlite3
with sqlite3.connect('sample.db') as conn:
    cursor = conn.cursor()
    cursor.execute('SELECT ID, NAME FROM EMPLOYEES')
    for row in cursor.fetchall():
        print(row[0])
        print(row[1])


# In[ ]:


import tkinter as tk
root = tk.Tk()
root.geometry('240x240')
root.title('GUI Sample')
button = tk.Button(root, text='Hello, World')
button.pack()
root.mainloop()


# In[ ]:


from flask import Flask
import datetime
app = Flask(__name__)
@app.route('/')
def hello():
    dt = datetime.datetime.now()
    html = '<!DOCTYPE html>'
    html += '<html>'
    html += '<head><title>Flask Sapmle</title></head>'
    html += '<body>'
    html += '{}年{}月{}日 {}時{}分{}秒です'.format(dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)
    html += '</body></html>'
    return html
if __name__ == '__main__':
    app.run()


# In[ ]:


import RPi.GPIO as GPIO
import dht11
import time
import datetime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
instance = dht11.DHT11(pin=14)
while True:
    result = instance.read()
    if result.is_valid():
        temperature = result.temperature
        humidity = result.humidity
        print('温度:{}'.format(temperature))
        print('湿度:{}'.format(humidity))
    time.sleep(1)


# In[ ]:


import pandas as pd
df = pd.read_csv('curry.csv', encoding='Shift_JIS')
df['month'] = pd.to_datetime(df['時間軸(月次)'], format='%Y年%m月').dt.month
df = df.groupby('month').mean()
df.mean(axis=1)
get_ipython().run_line_magic('matplotlib', 'inline')
df.mean(axis=1).plot() # Pandasがmatplotlibを使って可視化する

