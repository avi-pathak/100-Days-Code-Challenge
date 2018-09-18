import csv

with open("data.csv","r") as f:
     r=csv.reader(f)
     list_of_data = list(r)
     for i in list_of_data:
          for j in i:
               print(j,"\t",end='')
          print()
