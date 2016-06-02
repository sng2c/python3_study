from urllib import request

with request.urlopen('http://www.mabook.com/') as f:
    print(f.read().decode('utf-8'))