import pandas as pd
import requests

currentfile = pd.read_csv("Task 2 - Intern.csv", names = [ ], delimiter = " ")

currentfile = currentfile.index[1:]

def loopthroughurl(aurl):
    try:
        response = requests.get(aurl)
        # print(response.status_code)
        print((response.status_code), aurl)
        # return response.status_code, aurl
    except Exception as e:
        print((str(e)), aurl)    

qaa = map(loopthroughurl, currentfile)

for singurl in qaa:
    print(f'{singurl}')
