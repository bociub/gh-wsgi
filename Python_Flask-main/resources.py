
import matplotlib.pyplot as plt
import numpy as np
from models.greenHouse import GreenHouse
from models.user import User
import json
def getplot(user): #needs the email address not the user.
    
    
    
    
    
    getbyemail = User.get_by_email(user)    
    
    user_id = getbyemail.data()["user_id"]
    
    
    
    
    
    

    
    getdata = GreenHouse.get_by_user_id(user_id)
        
    labels = []
    OutsideTemp = []
    InsideTemp  = []
    WaterTemp = []
    dayscount = 0
    dayslist = []
    
    for hour in getdata: #get the needed data lists only. dont fight to miracle
        currenthour = hour.data()
        labels.append(currenthour["recordDateTime"])
        OutsideTemp.append(currenthour["OutsideTemp"])
        InsideTemp.append(currenthour["InsideTemp"])
        WaterTemp.append(currenthour["WaterTemp"])
        dayslist.append(dayscount)
        dayscount += 1
    
    
    plt.plot(dayslist, OutsideTemp, color='r', label='Outside temperature')
    plt.plot(dayslist, InsideTemp, color='g', label='Inside temperature')
    plt.plot(dayslist, WaterTemp, color='b', label='Water temperature')
    plt.xlabel("hours")
    plt.ylabel("temperature")
    plt.title("Temperature data")
    plt.legend()
    plt.savefig("static/img/plot.png")
    plt.close()
    
    
"""
30/8 way more better if days are presented not hours. 3 data per day per recorded temperature data. the min, the max, and the avarage

"""    
 
"""    
test = {} 
x=0  
for time in labels:
    test[time] = [OutsideTemp[x],InsideTemp[x],WaterTemp[x]]
    
    x += 1
test = json.dumps(test)       
f = open("duckyquack.txt", "w")
f.write(test)  
f.close()  
"""
    
    
"""it works   
x = [1, 2, 3, 4, 5]
y = [4, 6, 3, 7, 2]
plt.plot(x, y)
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Matplotlib - Save plot but dont show")
plt.savefig("filename.png")
plt.close()
"""