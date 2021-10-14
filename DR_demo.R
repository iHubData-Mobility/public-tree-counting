### A demo for "DR.R"
### The GPS dataset is from UCI repository:
###     https://archive.ics.uci.edu/ml/datasets/GPS+Trajectories
### Please download the dataset using the above link.
# install.packages("raster")
# install.packages("Rcpp")
# install.packages("MASS")
# install.packages("rgdal")
# install.packages()

library(leaflet)
library(osmdata)
library(MASS)
library(ggmap)
library(ggplot2)
library(rgdal)
library(raster)
source("DR.R")

# Reading and plotting the street tree GPS points
D0 = read.csv("tree_density.csv")
D1 = D0[,3:2]
print(D1)
plot(D1)

### start analysis
# smoothing bandwidth
h0 = 0.0001
 
# Calling the DR function
D_DR = DR(data = D1,h = h0)

### density ranking contour
colP = colorRampPalette(c("white","tan","brown"))
test_list = list(D_DR$x_grid, D_DR$y_grid, matrix(D_DR$gr_alpha, nrow=201))
names(test_list) = c("x", "y", "z")
r1 <- raster(test_list)

# Showcase the actual street tree GPS points on a map
leaflet(D1) %>% 
  addTiles() %>%
  addCircleMarkers(lng = D1$longitude, lat = D1$latitude, radius = 0.0001)

# Showcase the KDR results for street trees on a map
r1@data@values[which(r1@data@values < 0.001)] <- NA
palRaster <- colorNumeric("Spectral", domain = r1@data@values, na.color = "transparent")
leaflet() %>% 
  addProviderTiles(providers$CartoDB.Positron) %>% 
  addRasterImage(r1, colors = palRaster, opacity = .9) %>%
  addLegend(pal = palRaster, values = r1@data@values, title = "Tree Density")

### mass-volume curve
plot(x=rev(D_DR$clevel),y=log(D_DR$Mcurve,base = 10), 
     type="l",lwd=3, ylab="log volume",  xlab=expression(gamma), 
     main="Mass-Volume Curve")

### Betti number curve
plot(x=rev(D_DR$clevel),y=D_DR$Bcurve, type="l",lwd=3,
     main="Betti Number Curve", ylab="# of connceted component",
     xlab=expression(gamma))

### Persistence curve
plot(D_DR$Pcurve, pch=20, lwd=2, 
     main="Persistence Curve",xlim=c(0,1))

