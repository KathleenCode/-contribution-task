import pandas as pd
import requests

currentfile = pd.read_csv("Task 2 - Intern.csv", names = [ ], delimiter = " ")

# print(currentfile.index[0])

currentfile = currentfile.index[1:]

# print(currentfile)


def loopthroughurl(aurl):
    try:
        response = requests.get(aurl)
        # print(response.status_code)
        return response.status_code, aurl
    except Exception as e:
        print(str(e))

qaa = map(loopthroughurl, currentfile)

for singurl, au in qaa:
    print(f'({singurl}) {au}')
