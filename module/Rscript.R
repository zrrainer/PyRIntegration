library(tidyverse)
library(tidymodels)
library(dplyr)



makePlot = function(){
    localdf = get("df", envir = .GlobalEnv) 
    localdf = drop_na(localdf)
    p = ggplot(data = localdf, mapping = aes(x = posx, y = posy)) +
    geom_point() +
    xlim(-50,50) +
    ylim(-50,50) +
    theme_classic() +
    theme(axis.title.x=element_blank(),
        axis.text.x=element_blank(),
        axis.ticks.x=element_blank(),
        axis.line.x=element_blank(),
        axis.title.y=element_blank(),
        axis.text.y=element_blank(),
        axis.ticks.y=element_blank(),
        axis.line.y=element_blank(),)

    return(p)
}

#create the df in R envirnment. works
createDf = function(){
    localdf = data.frame(id = c(NA), 
                 posx = c(NA),
                 posy = c(NA))
    assign("df",localdf, envir = .GlobalEnv)
}



getDf = function(){
    localdf = get("df", envir = .GlobalEnv) 
    return(localdf)
}

#clear df. then add info from every existing obj insatnce
updateDf = function(){
    createDf()
    for (i in obj$existing_objs){
      row = list(i$id, i$posx, i$posy)
      df <<- rbind(.GlobalEnv$df, row)
    }
}

