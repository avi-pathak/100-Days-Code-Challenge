import csv

with open("data.csv","w",newline="") as f:
     w=csv.writer(f)
     w.writerow(["Employee","Age","Sallery"])
     for i in range(int(input("enter the no of emplooyee"))):
          name=input("Enter the name of employee ")
          Age = input("Enter the Age of employee ")
          Sallery = input("Enter the Sallery of employee ")
          w.writerow([name,Age,Sallery])
print("Data Written in csv fuile successfully")
