.. 2024_DC_WOC-ESA documentation master file, created by
   sphinx-quickstart on Fri Jul 21 14:53:11 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: figures/dc_2024_WOC-ESA_logo-rtd2.jpg
    :width: 1500
    :alt: alternate text
    :align: center 
     
.. raw:: html


    <embed> 
    
        <br /> 
        
        <br />

    </embed>

The WOC data challenges are comparison platforms that allow a sound and fair assessment of the WOC products between them and to other products. These platforms offer an input dataset (altimetric data, drifters, SST data ...) for anyone to create a surface current products as well as a reference dataset (independant from the input dataset) in order to evaluate the products. These data challenges are contained in a `github repository <https://github.com/ocean-data-challenges/2024_DC_WOC-ESA/tree/main>`_ and their documentation and results are presented on this readthedocs website. 
 
    
.. raw:: html


    <embed> 
    
        <br />
        
        <center>
        <div id="image_map"> <map name="map_example"> <area href="https://2024-dc-woc-esa.readthedocs.io/en/latest/2_regionaleval/index_Agulhas.html" target="_blank" alt="Agulhas Current" shape=poly coords="310,265, 310,220, 365,220, 365,265"> <area href="https://2024-dc-woc-esa.readthedocs.io/en/latest/2_regionaleval/index_GulfStream.html" target="_blank" alt="Gulf Stream" shape=poly coords="170,135, 170,70, 280,70, 280,135"> <area href="https://2024-dc-woc-esa.readthedocs.io/en/latest/2_regionaleval/index_MedSea.html" target="_blank" alt="Mediterranean Sea" shape=poly coords="290,110, 290,75, 335,75, 335,110">  <img src="_static/DC_2024_map_frontpage.jpg" title="Gulf Stream" alt="image map example" width=600 height=350 usemap="#map_example"></map> </div> </center>
        
        <br />
        
        <hr />
        
        <br />

    </embed>
    
     

 
Objectives and caveats   
======================

The goal of the data challenge is to evaluate the products ability to estimate the total surface current in three different regions during the year 2019 (evaluation period). 
The input observations used to generate the products are not resticted apart for the AOML drifter data during the evaluation period: 2019. A dataset of some input observations is also provided (see `Download the data <https://2024-dc-woc-esa.readthedocs.io/en/latest/0_getstarted/getstarted_data.html>`_), however any other data apart from the drifter data during the evaluation period can be used. 

Note that some products are intrinsically estimating only specific components of the total current (e.g., the geostrophic component) they are nonetheless evaluated like the other products, making their assumption on the surface currents an approximation of the total current. 

The caveats of the data challenge are: 
    
.. raw:: html

    <embed> 
        <ul>
            <li> not all products are using the same input observations,   
            </br>

            <li> some products' goal is not to estimate the total currents (i.e., geostrophic reconstruction).    
            </br>  

            <li> the one year evaluation period may not be enough for some diagnosis (Lagrangian cumulative distance) to be fully informative on the low frequency signals,   
            </br> 


        </ul>
        
        
        <br />
        
        <hr />
        
        <br />
        
        
    </embed>
    
     
    
Evaluated products   
==================

.. raw:: html

    <embed>  

        <table>
          <thead>
            <tr> 
              <th>Products</th>
              <th>Provider</th>
              <th>Reconstructed currents</th>
              <th>Input observations used</th> 
              <th>Available regions</th> 
            </tr>
          </thead>
          <tbody>   
            <tr> 
              <td style="text-align:left;"> <strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/1_products/products_woc.html">  BFN-QG </a></strong></td>
              <td> WOC-ESA </td>
              <td> Geostrophic </td> 
              <td> altimetry </td> 
              <td> Agulhas </td> 
            </tr> 
            <tr> 
              <td style="text-align:left;"><strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/1_products/products_woc.html"> dADR-SR</a></strong></td>
              <td> WOC-ESA </td>
              <td> Total currents </td> 
              <td> altimetry, SST</td> 
              <td> Mediterranean </td> 
            </tr> 
            <tr>  
              <td style="text-align:left;"><strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/1_products/products_woc.html"> Omega 3D</a></strong></td>
              <td> WOC-ESA </td>
              <td> Total currents </td> 
              <td> altimetry, SST</td> 
              <td> Gulf Stream </td> 
            </tr> 
            <tr> 
              <td style="text-align:left;"><strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/1_products/products_woc.html"> SSTSSH-NAtl2D</a></strong></td>
              <td> WOC-ESA </td>
              <td> Total currents </td> 
              <td> altimetry, SST</td> 
              <td> Gulf Stream </td> 
            </tr> 
            <tr> 
              <td style="text-align:left;"><strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/1_products/products_woc.html"> Global Inertial</a></strong></td>
              <td> WOC-ESA </td>
              <td> Geostrophic + Ekman + Induced Ekman (NIO) </td> 
              <td> Drifter currents, GlobCurrent geos.</td> 
              <td> Agulhas, Gulf Stream, Mediterranean </td> 
            </tr> 
            <tr> 
              <td style="text-align:left;"><strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/1_products/products_cmems.html">GlobCurrent</a></strong></td>
              <td> CMEMS </td>
              <td> Geostrophic + Ekman </td> 
              <td> altimetry, gravimetry, drifters </td> 
              <td> Agulhas, Gulf Stream, Mediterranean </td>
            </tr>
            <tr> 
              <td style="text-align:left;"><strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/1_products/products_cmems.html">GlobCurrent Geostrophic</a></strong></td>
              <td> CMEMS </td>
              <td> Geostrophic </td> 
              <td> altimetry </td> 
              <td> Agulhas, Gulf Stream, Mediterranean </td>
            </tr> 
          </tbody>
        </table> 
        </br>
    </embed>

Click on the products for more details. 
    
    
  
    
.. raw:: html

    <embed>  
        
        
        <br />
        
        <hr />
        
        <br />
        
        
    </embed>
  
  

Regions of interest      
===================
 
    
The WOC data challenges cover three geographical regions, with different dynamical characteristics. 

.. raw:: html   
 
    <div class="tab">
      <button class="tablinks" onclick="openCity(event, 'AgulhasCurrent')" id="defaultOpen"><b>Agulhas Current region</b></button>
      <button class="tablinks" onclick="openCity(event, 'GulfStream')"><b>Gulf Stream region</b></button>
      <button class="tablinks" onclick="openCity(event, 'MediterraneanSea')"><b>Mediterranean Sea region</b></button>
    </div>
    
    <div id="AgulhasCurrent" class="tabcontent">
      <br /> 
      
      </br>
      
      <p align="center">
          <img src="_static/illustration_agulhas_region.jpg" alt="Alt Text" width="400"/>
      </p> 
       
        
      <ul>
        <li>  Area: [14°E, 35°E, 45°S, 30°S]</li>
        <li>  Dynamical specificities: Strongly geostrophic region. </li> 
        <li>  Independant evaluation data: CMEMS drifters currents and trajectories.</li>
        <li>  Products: 
            <ul>  
                <li> WOC BFN-QG </li> 
                <li> WOC Global Inertial </li> 
                <li> GlobCurrent Geostrophic </li>
                <li> GlobCurrent Total </li>
              </ul>
      
      </ul>
      
       

        </br>
        
        <h3><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/4_dc_agulhas/dc_agulhas_details.html"> >  Agulhas Current setup </a></h3> 
       
 
        
        <h3><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/4_dc_agulhas/dc_agulhas_movies.html"> > Reconstruction movies </a></h3> 
       
 
        
        <h3><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/4_dc_agulhas/dc_agulhas_overalleval.html"> > Product comparison </a></h3> 
        
    </div>

    <div id="GulfStream" class="tabcontent">
      <br /> 
      
      </br>
      
      <p align="center">
  <img src="https://github.com/ocean-data-challenges/2024_DC_WOC-ESA/assets/33433820/3647745e-b2a8-480b-befd-8e90dd0a8b82" alt="Alt Text" width="400"/>
      </p> 
       
      <ul>
        <li>  Area: [80°W, 10°W, 25°N, 50°N]</li>
        <li>  Dynamical specificities: High variability region with mixed geostrophic and ageostrophic dynamics. </li> 
        <li>  Independant evaluation data: CMEMS drifters currents and trajectories.</li>
        <li>  Products: 
            <ul> 
                <li> WOC Omega 3D </li> 
                <li> WOC Global Inertial </li> 
                <li> GlobCurrent Geostrophic </li>
                <li> GlobCurrent Total </li>
              </ul>
      
      </ul>
       
        
        </br>
        
        <h3><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/3_dc_gulfstream/dc_gulfstream_details.html"> > Gulf Stream setup </a></h3>  
         
        <h3><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/3_dc_gulfstream/dc_gulfstream_movies.html"> > Reconstruction movies </a></h3>  
         
        <h3><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/3_dc_gulfstream/dc_gulfstream_overalleval.html"> > Overall comparison </a></h3>  
        
    </div>



    <div id="MediterraneanSea" class="tabcontent">
      <br /> 
      
      </br>
      
      <p align="center">
          <img src="_static/illustration_agulhas_region.jpg" alt="Alt Text" width="400"/>
      </p> 
       
      <ul>
        <li>  Area: [5°W, 25°E, 35°N, 47°N] </li>
        <li>  Dynamical specificities: A quasi-closed basin with strong ageostrophic dynamics and vertical shear. </li> 
        <li>  Independant evaluation data: CMEMS drifters currents and trajectories.</li>
        <li>  Products: 
            <ul> 
                <li> WOC dADR-SR </li> 
                <li> WOC Global Inertial </li> 
                <li> GlobCurrent Geostrophic </li>
                <li> GlobCurrent Total </li>
              </ul>
      
      </ul>   

        </br>
        
        <h3> <a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/2_dc_medsea/dc_medsea_details.html"> > Mediterranean Sea setup </a></h3>   
 
        <h3> <a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/2_dc_medsea/dc_medsea_movies.html"> > Reconstruction movies </a></h3>   
 
        <h3> <a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/2_dc_medsea/dc_medsea_overalleval.html"> > Overall comparison </a></h3>   

    </div>
    <script>
    function openCity(evt, cityName) {
      var i, tabcontent, tablinks;
      tabcontent = document.getElementsByClassName("tabcontent");
      for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
      }
      tablinks = document.getElementsByClassName("tablinks");
      for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
      }
      document.getElementById(cityName).style.display = "block";
      evt.currentTarget.className += " active";
    }

    // Get the element with id="defaultOpen" and click on it
    document.getElementById("defaultOpen").click();
    </script>  
    
    <br />
   
     
  
    
.. raw:: html

    <embed>  
        
        
        <br />
        
        <hr />
        
        <br />
        
        
    </embed>
     

A word on the WOC project      
=========================

The World Ocean Circulation (WOC) consortium is composed partners from France, Norway, Italy, Spain, Netherlands. It gathers experts in the Earth Observation  and ocean processes and sea state interactions. 

The WOC project developed synergetic products optimizing the capacy offered by Earth Observations as well as in-situ and numerical models by focusing on four domains of applications: 

* Sea-state current interactions for Safe Navigation, 
* 3D currents and vertical motion for Sustainable Fisheries, 
* Surface Lagrangian drift for a Clean Ocean, 
* High Resolution wave and current model assessment for a Productive Ocean and ocean processes and sea state interactions.
  

.. raw:: html

    <embed> 
        <center>
        <a href="https://www.worldoceancirculation.org/Products#/search?from=1&to=30"> <b>Check out the WOC products</b> </a>  <br> <br> <a href="https://www.worldoceancirculation.org/Products#/search?from=1&to=30"><img src="https://github.com/ocean-data-challenges/2024_DC_WOC-ESA/assets/33433820/8434082f-ad1d-494a-9325-e6668fc85e1a" width="200"></a> 
        </center>
         
        
        
        <br />
        
        <hr />
        
        <br />
        
         
        
    </embed>
     
     
More data challenges   
====================

If you are interested in more data challenges relating to ocean data, you can visit the ocean-data-challenges website. 
  
  
    
.. raw:: html  


    <embed>  
        
        <br />
        
        <center><a  href="https://ocean-data-challenges.github.io"/> <img src="_static/odc_webpage.jpg" alt="Alt Text" width="500"/></a></center>
        
        <center><a  href="https://ocean-data-challenges.github.io" alt="Alt Text"/> ocean-data-challenges.github.io </a></center>
        
        <br /> 
        
        <br />
        
          
        <br />
        
        <hr />
        
        <br />
        
        <center> <img src="_static/logos_partenaires_DC_WOC-ESA.jpg" alt="Alt Text" width="1200"/></center>
        
        
        
        <br />
        
        <hr />
        
        <br />
        
         
        So far, the github page visits amount to: <br> <br> <a href="https://github.com/ocean-data-challenges/2024_DC_WOC-ESA"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Focean-data-challenges%2F2024_DC_WOC-ESA&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=PAGE+VIEWS&edge_flat=false"/></a> 
        
    </embed>
    
-----------------  

  
    
.. raw:: html

    <embed>  
    
        
        <br /> 
        
    </embed>
 
    
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Participate 

   0_getstarted/index.md
   
    
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Products description 

   1_products/index.md 

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Regional Evaluations
 
   2_regionaleval/index.md 
      
   
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Metrics details 
 
   5_metrics_det/index.md 
    

.. toctree::  
    :caption: Illustration notebooks
    :hidden:
    :maxdepth: 0 
    
    gallery/index.md
    

.. toctree::  
    :caption: Contact us
    :hidden:
    :maxdepth: 0 
    
    contactus.md  

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Scripts

   6_scripts/modules.rst
   
    
