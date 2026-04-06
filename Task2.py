# import pandas as pd
# import requests

# currentfile = pd.read_csv("Task 2 - Intern.csv", delimiter = " ")

# f = open("Task 2 - Intern.csv")
# f = f.read()

# print(f[0:7])

# currentfile = currentfile[0:]

# print(currentfile)

# print(f)

# def loopthroughurl(aurl):
#     url = str(aurl).strip()
        
#     if not url.startswith(('http://', 'https://')):
#         url = 'http://' + url
#     response = requests.get(aurl)
#     print(response.status_code)
#     return response.status_code

# qaa = map(loopthroughurl, f)

# for singurl in qaa:
#     print(singurl)
#     print(f'(singurl.status_code) singurl')

import requests


f = open("Task 2 - Intern.csv")
f = f.read()
urls = [line.strip() for line in f if line.strip()]

print(f"Loaded {len(urls)} URLs")

for url in urls:
    try:
        if not url.startswith(('http://', 'https://')):
            url = "https://" + url
        response = requests.get(url, timeout=10)
        print(f"{response.status_code} {url}")
    except Exception as e:
        print(f"Error with {url}: {e}")