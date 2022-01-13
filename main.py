import pickle
from os import system

_ = system('python Back.py')

with open ('file1.bin', 'rb') as fp:
    x = pickle.load(fp)

count=0
print('Would you Like to enter')
print('1. Sl.No from 1 to 120')
print("OR")
print("2. Name of spacecraft")
print("Enter Option 1 OR 2")
n=int(input("Enter option: "))
try:
    if n==1:
        w=input("Enter serial number: ")
        for i in range(0,len(x)):
            if x[i][0]==w:
                print("Sl.No: ",x[i][0])
                print("Name: ",x[i][1])
                print("Launch Date: ",x[i][2])
                print("Launch Vehicle: ",x[i][3])
                print("orbit type: ",x[i][4])
                print("Application: ",x[i][5])
                if x[i][6]=='no info':
                    print("Remarks: Successful")
                else:
                    print("Remarks: ",x[i][6])
except:
    print("Wrong input, try again")

if n==2:
    wm=input("Enter Name: ")
    for i in range(0,len(x)):
        if wm.lower() in x[i][1].lower():
            print("Sl.No: ",x[i][0],"Name: ",x[i][1])
            count = 1
    if count!=1:
        print("Not found, please try entering serial number")

    w=input("Enter serial number for more details: ")
    for i in range(0,len(x)):
        if x[i][0]==w:
            print("Sl.No: ",x[i][0])
            print("Name: ",x[i][1])
            print("Launch Date: ",x[i][2])
            print("Launch Vehicle: ",x[i][3])
            print("orbit type: ",x[i][4])
            print("Application: ",x[i][5])
            if x[i][6]=='no info':
                print("Remarks: Successful")
            else:
                print("Remarks: ",x[i][6])
    
     
        
            
                
                
                
                
                
                
                
                    
                
                    

            
                   
                



                
               
        
        
        



            
        
    


