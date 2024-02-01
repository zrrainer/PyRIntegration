import rpy2
import rpy2.robjects as robjects
from rpy2.robjects import rl
import tkinter as tk
from PIL import Image, ImageTk
import math
import time
import numpy
import scipy
from scipy import constants
from module.pythonScript import obj


r = robjects.r
r.source("./module/Rscript.R")


obj001 = obj("001",-10,0,0,0,0,0)
obj002 = obj("002",10,0,0,0,0,0)
obj003 = obj("003",0,17,0,0,0,0)


obj.updateRdf()

RmakePlot = robjects.globalenv['makePlot']    #make plot from df stored in R session
RmakePlot(saveplot = True)





# #------------something here is profoundly wrong-----------------
def updateWindow(): #update window loop
    #visualize data stored in df   
    RmakePlot(saveplot = True)
    image = Image.open("images/plot.jpeg")
    image = ImageTk.PhotoImage(image)
    
    

    
    # #calculate next step & update df
    for i in obj.existing_objs:
        i.updateObjA()
        i.updateObjVP()

    obj.updateRdf() ###########something wrong with rpy2? 



    #label.config(image = "images/devil-may-cry-devil-may-cry3.gif")
    # root.update()
    # root.after(10, updateWindow)




root = tk.Tk()
root.geometry("1000x1000")
image = Image.open("images/plot.jpeg")
image = ImageTk.PhotoImage(image)
label = tk.Label(root, image = image)
label.place(anchor="center", relx=0.5, rely = 0.5)
print(type(label))

root.after(1000,updateWindow)
root.mainloop()
    