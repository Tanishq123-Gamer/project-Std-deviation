import csv 
import pandas as pd 
import plotly.express as px
import math 



with open("data.csv",newline='') as f: 
    reader=csv.reader(f)
    data=list(reader)


#data.pop(0)


print(len(data))
print(data)

total=0

for x in data:
    num=x[0]
    print(num)
    total=total+float(num)

mean=total/len(data)

print(mean)


sq_list=[]


for a in data:
    num=a[0]
    diff= float(num)-float(mean)
    sq=diff**2
    sq_list.append(sq)

total1=0
for y in sq_list: 
    total1=total1+y


result= total1/len(data)
std=math.sqrt(result)

print(std)
     