# Python-R integration


--An experiment on integrating Python into R, and vice versa. 

I have written some simple code that runs a physics simulation, calculated via python and visualized via the R package ggplot2. This repo documents me playing with (losing sanity over) rpy2, the most popular python package for integrating R code into python, and reticulate, themost popular R package for integrating python code into R.  



some reflections on rpy2:

rpy2 has very obvious weak points: its syntax are arduous and, frankly, very ugly. Every function in the R script needs to be imported into a python object individually, on top of sourcing the R script itself, leading to ridiculous code such as

RcreateDf = robjects.globalenv['createDf']
RcreateDf()

Oh, rpy2 also does not have windows binaries. So.  





reflections on reticulate:

direct access to the methods in the python script. cool. awesome. 10/10. the trouble is displaying the ggplot objects.

while using rpy2 I took the easy way out and wrote all the code in a ipynb file, and displayed the outputs using, uh, display(). R markdown do not have the same behavior. the main loop for the animation never ends, and the ggplot objects are never actually printed out.  




2024.1.31

display() was more of an easy way out than I thought. without using the IPython.display module, it is nigh impossible to convert the ggplot object into a useful python object... i am temporarily resorting to doing it the heathen way - saving the ggplot object as a local file and reading it with PIL. which works. for now. (i am deeply exasperated)

additionally, ktinker....... every time i call update on a tk window it flashes for a second. which would be fine if i werent updating every 10 ms. 

![](https://github.com/zrrainer/RPyIntegration/blob/main/images/devil-may-cry-devil-may-cry3.gif)

ah. maybe the lesson here is that dont bother integrating other languages if not necessary. i have a feeling i can get matplotlib working within a couple hours.... 

