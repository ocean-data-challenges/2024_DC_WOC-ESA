# Overall comparison

<br>
 
    
## Metric boards

<details>
<summary>Variance error [m²/s²] ⤵️  </summary>
    
<br> 


| Region| Method| Variance error u [m²/s²] | Variance error v [m²/s²]  | 
|---|---|---|---| 
|**coastal**         |**DUACS**      | 0.026835     |  <span style="color:blue">0.027367</span>    |  
|                    |**MIOST**      | 0.026970     | 0.028193     |  
|                    |**DDDcurr**    | 0.025531     | 0.027564     | 
|                    |**SSHSSTprod** | <span style="color:blue">0.017744</span>     | 0.028912     |  
|||| 
|**offshore_highvar**|**DUACS**      | 0.049405     | 0.048346     |  
|                    |**MIOST**      | 0.048746     | 0.049801     | 
|                    |**DDDcurr**    | 0.053595     | 0.051306     |  
|                    |**SSHSSTprod** | <span style="color:blue">0.047787</span>     | <span style="color:blue">0.047780</span>     | 
|||| 
|**offshore_lowvar** |**DUACS**      | 0.018048     | 0.015990     |  
|                    |**MIOST**      | 0.017930     | 0.015888     | 
|                    |**DDDcurr**    | 0.016065     | 0.015166     | 
|                    |**SSHSSTprod** | <span style="color:blue">0.013400</span>     | <span style="color:blue">0.013444</span>     | 

</details>
 
<br>

<details>
<summary>Error scores ⤵️  </summary>
    
<br> 


| Region| Method  | Error score u | Error score v |
|---|---|---|---| 
|**coastal**         |**DUACS**      | 54.2 %     | <span style="color:blue">66.2 %</span> |  
|                    |**MIOST**      | 54.0 %     | 65.2     |  
|                    |**DDDcurr**    | 56.9 %     | 64.9     | 
|                    |**SSHSSTprod** | <span style="color:blue">60.4 %</span> | 43.4     |  
|||| 
|**offshore_highvar**|**DUACS**      | 72.7 %     | 67.7 %     |  
|                    |**MIOST**      | 73.1 %     | 66.7 %     | 
|                    |**DDDcurr**    | 70.4 %     | 65.7 %     |  
|                    |**SSHSSTprod** | <span style="color:blue">73.6 %</span> | <span style="color:blue">68.1 %</span> | 
|||| 
|**offshore_lowvar** |**DUACS**      | 39.9 %     | 41.7 %     |  
|                    |**MIOST**      | 40.4 %     | 42.1 %     | 
|                    |**DDDcurr**    | 46.6 %     | 44.7 %     | 
|                    |**SSHSSTprod** | <span style="color:blue">54.6 %</span> | <span style="color:blue">50.1 %</span> | 

  
</details>
 

<br>

## Current magnitud movie 
 
<details>
<summary>Current movies ⤵️  </summary>

<br> 

<center>
<video controls width="1000">
  <source src="https://github.com/ocean-data-challenges/2024_DC_WOC-ESA/assets/33433820/0dd433a6-f98d-46bd-b44f-0a0f5662164a" type="video/mp4" />  
</video>
</center>
 
</details>
 

<br>

## Current errors  
 
<details>
<summary>Zonal and Meridional current error variances ⤵️  </summary>

<br> 

|![Maps_DUACS_errvar_Gulfstream_uv](../_static/Maps_DUACS_errvar_Gulfstream_uv.png)  |![Maps_MIOST_errvar_Gulfstream_uv](../_static/Maps_MIOST_errvar_Gulfstream_uv.png)  | 
|----|----| 
![Maps_DDDcurr_errvar_Gulfstream_uv](../_static/Maps_DDDcurr_errvar_Gulfstream_uv.png)  |![Maps_SSHSSTprod_errvar_Gulfstream_uv](../_static/Maps_SSHSSTprod_errvar_Gulfstream_uv.png)  |  

</details>
 

<br>

## Current explained variances
  
<details>
<summary>Zonal and Meridional current explained variances ⤵️  </summary>

<br> 

|![Maps_DUACS_explvar_Gulfstream_uv](../_static/Maps_DUACS_explvar_Gulfstream_uv.png)   |![Maps_MIOST_explvar_Gulfstream_uv](../_static/Maps_MIOST_explvar_Gulfstream_uv.png)     |
|----|----| 
![Maps_DDDcurr_explvar_Gulfstream_uv](../_static/Maps_DDDcurr_explvar_Gulfstream_uv.png)     |![Maps_SSHSSTprod_explvar_Gulfstream_uv](../_static/Maps_SSHSSTprod_explvar_Gulfstream_uv.png)   |


</details>
 

<br>

## Current comparison

<details>
<summary>Zonal and Meridional current error and explained variance comparison ⤵️  </summary>

<br> 

<center>
    <div id="Maps_DUACSvsMIOST_errexplvarcomp_Gulfstream_uv">
        <img src="../_static/Maps_DUACSvsMIOST_errexplvarcomp_Gulfstream_uv.png" width="400">
        <img src="../_static/Maps_DUACSvsSSHSSTprod_errexplvarcomp_Gulfstream_uv.png" width="400">
    </div> 
</center>
 
  
<br> 

<center> 
    <div id="Maps_DUACSvsDDDcurr_errexplvarcomp_Gulfstream_uv">
        <img src="../_static/Maps_DUACSvsDDDcurr_errexplvarcomp_Gulfstream_uv.png" width="400">
        <img src="../_static/Maps_DDDcurrvsSSHSSTprod_errexplvarcomp_Gulfstream_uv.png" width="400">  
    </div>
</center>

</details>
 

<br>

## Lagrangian cumulative distance comparison

<details>
<summary>LCD maps ⤵️  </summary>

<br> 
 
| ![DUACS LDC Gulfstream h1](../_static/deviation_maps_DUACS_Gulfstream_h1.png) | ![DUACS LDC Gulfstream h2](../_static/deviation_maps_DUACS_Gulfstream_h2.png) | ![DUACS LDC Gulfstream h3](../_static/deviation_maps_DUACS_Gulfstream_h3.png) | ![DUACS LDC Gulfstream h4](../_static/deviation_maps_DUACS_Gulfstream_h4.png) | ![DUACS LDC Gulfstream h5](../_static/deviation_maps_DUACS_Gulfstream_h5.png) |
|--|--|--|--|--| 
| ![MIOST LDC Gulfstream h1](../_static/deviation_maps_MIOST_Gulfstream_h1.png) | ![MIOST LDC Gulfstream h2](../_static/deviation_maps_MIOST_Gulfstream_h2.png) | ![MIOST LDC Gulfstream h3](../_static/deviation_maps_MIOST_Gulfstream_h3.png) | ![MIOST LDC Gulfstream h4](../_static/deviation_maps_MIOST_Gulfstream_h4.png) | ![MIOST LDC Gulfstream h5](../_static/deviation_maps_MIOST_Gulfstream_h5.png) |
| ![DDDcurr LDC Gulfstream h1](../_static/deviation_maps_DDDcurr_Gulfstream_h1.png) | ![DDDcurr LDC Gulfstream h2](../_static/deviation_maps_DDDcurr_Gulfstream_h2.png) | ![DDDcurr LDC Gulfstream h3](../_static/deviation_maps_DDDcurr_Gulfstream_h3.png) | ![DDDcurr LDC Gulfstream h4](../_static/deviation_maps_DDDcurr_Gulfstream_h4.png) | ![DDDcurr LDC Gulfstream h5](../_static/deviation_maps_DDDcurr_Gulfstream_h5.png) | 
| ![SSHSSTprod LDC Gulfstream h1](../_static/deviation_maps_SSHSSTprod_Gulfstream_h1.png) | ![SSHSSTprod LDC Gulfstream h2](../_static/deviation_maps_SSHSSTprod_Gulfstream_h2.png) | ![SSHSSTprod LDC Gulfstream h3](../_static/deviation_maps_SSHSSTprod_Gulfstream_h3.png) | ![SSHSSTprod LDC Gulfstream h4](../_static/deviation_maps_SSHSSTprod_Gulfstream_h4.png) | ![SSHSSTprod LDC Gulfstream h5](../_static/deviation_maps_SSHSSTprod_Gulfstream_h5.png) | 
 
</details>
 
<br> 

<details>
<summary>LCD temporal horizon series ⤵️  </summary>

<br> 

![deviation_horizon_Agulhas](../_static/deviation_horizon_Gulfstream.png)  
 

<br>  
  