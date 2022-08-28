
import matplotlib.pyplot as plt
import numpy as np
from models.greenHouse import GreenHouse
from models.user import User
import json

getdata = GreenHouse.get_by_user_id(1)
"""
tow = duck[0]
toto = tow.data() #THIS IS AN HUOR's DICTIONARY'
tutu = json.dumps(toto)
f = open("duckyquack.txt", "w")
f.write(tutu)
f.close()
"""
thedata = {}
for hour in getdata: 
    currenthour = hour.data()
    currenttime = currenthour["recordDateTime"]
    currenttime = currenttime.split(',')
    thehour = int(currenttime[1])
    theday = int(currenttime[0])
    
    
    
    #thedata[theday][thehour] = currenthour.copy()  
    f = open("duckyquack.txt", "a")
    f.write(str(thehour) + "-" + str(theday) + "#")
    f.close()
    
    
    
    


  
x = np.array([1, 2, 3, 4]) #x axis b
y = x*2 #y axxis

# first plot with X and Y data
plt.plot(x, y) #draw the empty chart



  
x1 = [2, 4, 6, 34]
y1 = [3, 5, 7, 4]
  
# second plot with x1 and y1 data
plt.plot(x1, y1)
  
plt.xlabel("X-axis data")
plt.ylabel("Y-axis data")
plt.title('multiple plots')


plt.show()