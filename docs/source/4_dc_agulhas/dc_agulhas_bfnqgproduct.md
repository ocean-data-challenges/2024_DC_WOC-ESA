# WOC - BFN-QG geostrophic currents  

<br>

For over 25 years, satellite altimetry has provided invaluable information about the ocean dynamics at many scales. Gridded Sea Surface Height (SSH) maps allow to estimate the mesoscale geostrophic circulation in the ocean. However, conventional interpolation techniques rely on static optimal interpolation schemes, hence limiting the estimation of non-linear dynamics at scales not well sampled by altimetry (i.e., below 150-200km at mid latitudes). To overcome this limitation in the resolution of small-scale SSH structures (and thus small-scale geostrophic currents), a Back-and-Forth Nudging algorithm combined with a Quasi-Geostrophic model, a technique called BFN-QG, has been implemented within the theme 1 of the ESA World Ocean Circulation (WOC) project. The performances have been evaluated within Observing System Experiments (OSEs) that use independent data (such as independent SSH, Sea Surface Temperature and drifter data) as ground-truth. By comparing the mapping performances to the ones obtained by operational products, the BFN-QG improves the mapping of short, energetic mesoscale structures and associated geostrophic currents both in space and time. In particular, the BFN-QG improves (i) the spatial effective resolution of the SSH maps by a factor of 20%, (ii) the zonal and (especially) the meridional geostrophic currents and (iii) the prediction of Lagrangian transport for lead times up to 10 days.
 
**More information on the BFN-QG products [here](https://www.worldoceancirculation.org/Products#/metadata/7fe77c80-798a-42d4-a69c-2b5f0ba81a43) !**

<br>  

## Current magnitud movie 
 
<center>
<video controls width="600">
  <source src="https://github.com/ocean-data-challenges/2024_DC_WOC-ESA/assets/33433820/1b609f81-bf4a-4641-a146-556cce3c332b" type="video/mp4" />   
</video>
</center> 



<br>

## Zonal and Meridional current error variance
 

|![Maps_BFNQG_errvar_Agulhas_uv](../figures/Maps_BFNQG_errvar_Agulhas_uv.png)  | ![Maps_BFNQG_explvar_Agulhas_uv](../figures/Maps_BFNQG_explvar_Agulhas_uv.png) |
|----|----|

<br> 

<br>

## Lagrangian cumulative distance 

| ![BFN-QG LDC h1](../figures/deviation_maps_BFN-QG_h1.png) | ![BFN-QG LDC h2](../figures/deviation_maps_BFN-QG_h2.png) | ![BFN-QG LDC h3](../figures/deviation_maps_BFN-QG_h3.png) | ![BFN-QG LDC h4](../figures/deviation_maps_BFN-QG_h4.png) | ![BFN-QG LDC h5](../figures/deviation_maps_BFN-QG_h5.png) |
|--|--|--|--|--|

<br>  
  