# 4 Assessment of the position of the dynamical structures

<br>
 

<br> 
 
## 4.1 Current direction using Fronts

This section describes how the positions of front and eddies derived from high resolution SST are used to diagnose velocity fields. It relies on the hypothesis that fronts are aligned with the direction of currents at mesoscale and are in geostrophic balance, and assuming that the advection of frontal structure is small enough. This could be checked by looking at the displacement of a front through time.


For each data point $P_i=\begin{bmatrix}lon_i\\ lat_i\end{bmatrix}$ that belongs to a frontal structure one can compute the flow crossing the fronts using the velocity product.  

$$Flow[P_i] = \left| \frac{{\vec{v}[P_i]}\cdot\vec{\delta_i}}{\lVert\vec{v}\left[P_i\right]\rVert \lVert\vec{\delta_i}\rVert} \right| = \left|cos\left(\angle(\vec{v}[P_i],\vec{\delta_i})\right) \right| $$

where $\vec{\delta_i}=\begin{bmatrix}lat_{i+1} - lat_{i-1}\\ -(lon_{i+1} - lon_{i-1}) cos(lat_i)\end{bmatrix}$ is the normal vector of the front at point $P_i$. The values of the flow range from 0 to 1. 

Assuming that the fronts are aligned with the true currents, the smaller the flow, the more consistent the current estimation is to the SST. 

