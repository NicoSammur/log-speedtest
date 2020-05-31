import os
import re
import subprocess
import time
import csv
from datetime import datetime

response = subprocess.Popen('/usr/local/bin/speedtest-cli --simple', shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

ping = re.findall('Ping:\s(.*?)\s', response, re.MULTILINE)
download = re.findall('Download:\s(.*?)\s', response, re.MULTILINE)
upload = re.findall('Upload:\s(.*?)\s', response, re.MULTILINE)

fecha = datetime.now().date()
hora = datetime.now().time()

download = download[0].replace(',', '.')
upload = upload[0].replace(',', '.')
ping = ping[0].replace(',', '.')

fields=[fecha, hora, download , upload, ping]
with open(r'/home/nicolas/speedtest/movistar.csv', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)

'''print(fecha)
print(hora)
print(ping)
print(download)
print(upload)


0 */2 * * * python3 /home/nicolas/speedtest/logBWtest.py

'''
