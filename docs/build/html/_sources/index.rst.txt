.. 2024_DC_WOC-ESA documentation master file, created by
   sphinx-quickstart on Fri Jul 21 14:53:11 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: figures/dc_2024_WOC-ESA_logo-rtd2.png
    :width: 1200
    :alt: alternate text
    :align: center
    
    
    
========== 
DC-WOC-ESA   
==========

.. role:: raw-html(raw)
    :format: html

:raw-html:`<br />`    
   
.. raw:: html  

   <embed> 
    <center> 
     <h1 style="color:rgb(28, 69, 135);font-size:40px;">Opening 31st of March 2024 !</h1> 
    </center> 
   </embed>
 

.. image:: ../../figures/dc_2024a_WOC-ESA_banner.jpg
    :width: 550 
    :align: center 

:raw-html:`<br />`

:raw-html:`<br />`
 

The WOC data challenges are comparison platforms that allow a sound and fair assessment of the WOC products between them and to other products. These platforms offer an input dataset (altimetric data, drifters, SST data ...) for anyone to create a current products as well as a reference dataset (independant from the input dataset) in order to evaluate the products. These data challenges are contained in a `github repository <https://github.com/ocean-data-challenges/2024_DC_WOC-ESA/tree/main>`_ and their documentation and results are presented on this readthedocs website. 

:raw-html:`<br />` 
    
.. raw:: html

    <embed> 
        <center>
        <div id="image_map"> <map name="map_example"> <area href="https://2024-dc-woc-esa.readthedocs.io/en/latest/4_dc_agulhas/dc_agulhas_details.html" target="_blank" alt="North Sea" shape=poly coords="335,295, 335,270, 370,270, 370,295"> <area href="https://2024-dc-woc-esa.readthedocs.io/en/latest/3_dc_gulfstream/dc_gulfstream_details.html" target="_blank" alt="Gulf Stream" shape=poly coords="160,175, 160,110, 290,110, 290,175"> <area href="https://2024-dc-woc-esa.readthedocs.io/en/latest/2_dc_medsea/dc_medsea_details.html" target="_blank" alt="Mediterranean Sea" shape=poly coords="300,155, 300,115, 345,115, 345,155">  <img src="_static/dc_2024_WOC-ESA_map2_regions.png" title="Gulf Stream" alt="image map example" width=600 height=350 usemap="#map_example"></map> </div> </center>

    </embed>
    
    

:raw-html:`<br />` 
     
:raw-html:`<hr />` 

:raw-html:`<br />` 

 
Objectives and caveats   
==========================

The goal of the data challenge is to evaluate the products ability to estimate the total surface current in three different regions during the year 2019 (evaluation period). 
The input observations used to generate the products are not resticted apart for the drifters data during the evaluation period. A dataset of some input observations is provided (see `Download the data <https://2024-dc-woc-esa.readthedocs.io/en/latest/1_getstarted/getstarted_data.html>`_), however any other data apart from the drifters data during the evaluation period can be used. 

Note that some products are intrinsically estimating only specific components of the total current (e.g., the geostrophic component) they are nonetheless evaluated like the other products, making their assumption on the currents as a total current approximation. 

The caveats of the data challenge are: 
    
.. raw:: html

    <embed> 
        <ul>
            <li> not all products are using the same input observations,   
            </br>

            <li> some products may use drifters which are also used for the evaluation <b> but never drifters data acquired during the evaluation period </b>,   
            </br> 

            <li> some products' goal is not to estimate the total currents,    
            </br> 

            <li> the summarized score in the scoreboards may not be representative of the methods' full performances, making it important to look at the detailed comparisons, 


        </ul>
    </embed>
    
    

:raw-html:`<br />` 
     
:raw-html:`<hr />` 

:raw-html:`<br />` 
    
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
            </tr>
          </thead>
          <tbody>  
            <tr> 
              <td><strong>BFN-QG</strong></td>
              <td> WOC-ESA </td>
              <td> Geostrophic </td> 
              <td> altimetry </td> 
            </tr> 
            <tr> 
              <td><strong>dADR-SR</strong></td>
              <td> WOC-ESA </td>
              <td> Total currents </td> 
              <td> altimetry, SST</td> 
            </tr> 
            <tr> 
              <td><strong>DDDcurr</strong></td>
              <td> WOC-ESA </td>
              <td> Total currents </td> 
              <td> Drifter currents, GlobCurrent geos.</td> 
            </tr> 
            <tr> 
              <td><strong>GC-combined</strong></td>
              <td> GlobCurrent </td>
              <td> Geostrophic + Ekman </td> 
              <td> altimetry, gravimetry, drifters </td> 
            </tr>
            <tr> 
              <td><strong>DUACS</strong></td>
              <td> CMEMS </td>
              <td> Geostrophic </td> 
              <td> altimetry </td> 
            </tr>
            <tr> 
              <td><strong>MIOST</strong></td>
              <td> CLS </td>
              <td> Geostrophic </td> 
              <td> altimetry </td> 
            </tr>
          </tbody>
        </table> 
        </br>
    </embed>

For more details on the products, check the `Products description <https://2024-dc-woc-esa.readthedocs.io/en/latest/1_getstarted/getstarted_products.html>`_ page.
    
    

:raw-html:`<br />` 
     
:raw-html:`<hr />` 

:raw-html:`<br />` 

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
      <h3><a href='https://2024-dc-woc-esa.readthedocs.io/en/latest/4_dc_agulhas/dc_agulhas_details.html'>Agulhas Current</a></h3>
      <ul>
        <li>  Area: [14°E, 35°E, 45°S, 30°S]</li>
        <li>  Dynamical specificities: Strongly geostrophic region. </li>
        <li>  Observations available for mapping currents: conventional nadir altimeters</li>
        <li>  WOC products: Drifter data-driven currents, BFN-QG geostrophic currents</li>
        <li>  Independant evaluation data: CMEMS drifters currents and trajectories.</li>
      
      </ul>
      
      
      <h3> Scoreboard</h3>  
 
      <h5> RMS error to drifter currents</h5> 
        <table>
          <thead>
            <tr> 
              <th></th>
              <th>RMSE(u)</th>
              <th>RMSE score(u)</th>
              <th>RMSE(v)</th>
              <th>RMSE score(v)</th>
            </tr>
          </thead>
          <tbody>  
            <tr> 
              <td><strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/4_dc_agulhas/dc_agulhas_duacs.html">DUACS</a></strong></td>
              <td>21.06 cm/s</td>
              <td>47.76 %</td> 
              <td>21.33 cm/s</td>
              <td>42.91 %</td> 
            </tr>
            <tr> 
              <td><strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/4_dc_agulhas/dc_agulhas_miost.html">MIOST</a></strong></td>
              <td>20.91 cm/s</td>
              <td>47.92 %</td> 
              <td>21.49 cm/s</td>
              <td>42.30 %</td> 
            </tr>
            <tr> 
              <td><strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/4_dc_agulhas/dc_agulhas_bfnqgproduct.html">BFN-QG</a></strong></td>
              <td><span style="color:blue">20.19 cm/s</span></td>
              <td><span style="color:blue">49.90 %</span></td> 
              <td><span style="color:blue">20.01 cm/s</span></td>
              <td><span style="color:blue">46.26 %</span></td> 
            </tr> 
          </tbody>
        </table> 

        </br>
        
        <h4>You can <a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/4_dc_agulhas/dc_agulhas_overalleval.html"><i> check the detailed comparison</i></a> or click on a method to see its specific performances.</h4> 
        
    </div>

    <div id="GulfStream" class="tabcontent">
      <br />
      <h3><a href='https://2024-dc-woc-esa.readthedocs.io/en/latest/3_dc_gulfstream/dc_gulfstream_details.html'>Gulf Stream</a></h3>
      <ul>
        <li>  Area: [80°W, 10°W, 25°N, 50°N]</li>
        <li>  Dynamical specificities: High variability region with mixed geostrophic and ageostrophic dynamics. </li>
        <li>  Observations available for mapping currents: conventional nadir altimeters, satellite SST data</li>
        <li>  WOC products: Merged SSH/SST currents, Drifter data-driven currents, BFN-QG geostrophic currents</li>
        <li>  Independant evaluation data: CMEMS drifters currents and trajectories.</li>
      
      </ul>
      

      <h3> Scoreboard</h3>  

        <table>
          <thead>
            <tr> 
              <th></th>
              <th>RMSE(u)</th>
              <th>RMSE score(u)</th>
              <th>RMSE(v)</th>
              <th>RMSE score(v)</th>
            </tr>
          </thead>
          <tbody>  
            <tr> 
              <td><strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/3_dc_gulfstream/dc_gulfstream_duacs.html">DUACS</a></strong></td>
              <td>15.57 cm/s</td>
              <td>34.82 %</td> 
              <td>14.89 cm/s</td>
              <td>33.73 %</td> 
            </tr>
            <tr> 
              <td><strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/3_dc_gulfstream/dc_gulfstream_miost.html">MIOST</a></strong></td>
              <td>15.43 cm/s</td>
              <td>35.44 %</td> 
              <td>14.83 cm/s</td>
              <td>33.96 %</td> 
            </tr>
            <tr> 
              <td><strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/3_dc_gulfstream/dc_gulfstream_drifterproduct.html">DDDcurr</a></strong></td>
              <td>15.06 cm/s</td>
              <td>37.05 %</td> 
              <td>14.71 cm/s</td>
              <td>34.33 %</td> 
            </tr> 
            <tr> 
              <td><strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/3_dc_gulfstream/dc_gulfstream_sshsstproduct.html">dADR-SR</a></strong></td>
              <td><span style="color:blue">13.79 cm/s</span></td>
              <td><span style="color:blue">41.53 %</span></td> 
              <td><span style="color:blue">14.10 cm/s</span></td>
              <td><span style="color:blue">35.10 %</span></td> 
            </tr> 
          </tbody>
        </table>
        
        
        </br>
        
        <h4>You can <a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/3_dc_gulfstream/dc_gulfstream_overalleval.html"><i> check the detailed comparison</i></a> or click on a method to see its specific performances.</h4>  
        
    </div>



    <div id="MediterraneanSea" class="tabcontent">
      <br />
      <h3><a href='https://2024-dc-woc-esa.readthedocs.io/en/latest/2_dc_medsea/dc_medsea_details.html'>Mediterranean Sea</a></h3>
      <ul>
        <li>  Area: [5°W, 25°E, 35°N, 47°N] </li>
        <li>  Dynamical specificities: A quasi-closed basin with strong ageostrophic dynamics and vertical shear. </li>
        <li>  Observations available for mapping currents: conventional nadir altimeters</li>
        <li>  WOC products: Merged SSH/SST currents, Drifter data-driven currents, BFN-QG geostrophic currents </li>
        <li>  Independant evaluation data: CMEMS drifters currents and trajectories.</li>
      
      </ul>  

      <h3> Scoreboard</h3> 
      
      <h5> Variance error score (best is 100%)</h5> 
      
        <table>
          <thead>
            <tr> 
              <th></th>
              <th>RMSE(u)</th>
              <th>RMSE score(u)</th>
              <th>RMSE(v)</th>
              <th>RMSE score(v)</th>
            </tr>
          </thead>
          <tbody>  
            <tr> 
              <td><strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/2_dc_medsea/dc_medsea_duacs.html">DUACS</a></strong></td>
              <td>16.45 cm/s</td>
              <td>30.10 %</td> 
              <td>14.89 cm/s</td>
              <td>27.48 %</td> 
            </tr>
            <tr> 
              <td><strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/2_dc_medsea/dc_medsea_miost.html">MIOST</a></strong></td>
              <td> <span style="color:blue">11.99 cm/s</span></td>
              <td> <span style="color:blue">37.87 %</span></td> 
              <td> <span style="color:blue">11.88 cm/s</span></td>
              <td> <span style="color:blue">30.17 %</span></td> 
            </tr> 
            <tr> 
              <td><strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/2_dc_medsea/dc_medsea_sshsstprod.html">dADR-SR</a></strong></td>
              <td> 17.35 cm/s </td>
              <td> 28.56 % </td> 
              <td> 15.06 cm/s </td>
              <td> 26.75 % </td> 
            </tr> 
            <tr> 
              <td><strong><a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/2_dc_medsea/dc_medsea_bfnqg.html">BFN-QG</a></strong></td>
              <td> 15.94 cm/s </td>
              <td> 31.04 % </td> 
              <td> 14.82 cm/s </td>
              <td> 27.92 % </td> 
            </tr> 
          </tbody>
        </table>  

        </br>
        
        <h4>You can <a href="https://2024-dc-woc-esa.readthedocs.io/en/latest/2_dc_medsea/dc_medsea_overalleval.html"><i> check the detailed comparison</i></a> or click on a method to see its specific performances.</h4>   

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
   
     
     

:raw-html:`<br />` 
     
:raw-html:`<hr />` 

:raw-html:`<br />` 
     

A word on the WOC project 
------------------------- 

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
        
    </embed>
     
 
  

:raw-html:`<br />` 

:raw-html:`<br />` 

.. raw:: html

    <embed>    
        So far, the github page visits amount to: <br> <br> <a href="https://github.com/ocean-data-challenges/2024_DC_WOC-ESA"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Focean-data-challenges%2F2024_DC_WOC-ESA&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=PAGE+VIEWS&edge_flat=false"/></a> 
        
    </embed>
    
----------------- 

:raw-html:`<br />`
 
    
.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Get started 

   1_getstarted/getstarted_install.md
   1_getstarted/getstarted_data.md 
   1_getstarted/getstarted_eval.md
   1_getstarted/getstarted_products.md

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: DC - Agulhas Current
 
   4_dc_agulhas/dc_agulhas_details.md
   4_dc_agulhas/dc_agulhas_overalleval.md  
     

.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: DC - Gulf Stream
 
   3_dc_gulfstream/dc_gulfstream_details.md
   3_dc_gulfstream/dc_gulfstream_overalleval.md   
   
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: DC - Mediterranean Sea

   2_dc_medsea/dc_medsea_details.md
   2_dc_medsea/dc_medsea_overalleval.md  
 

   
.. toctree::
   :hidden:
   :maxdepth: 1
   :caption: Metrics details

   5_metrics_det/metrics_0-introduction.md
   5_metrics_det/metrics_EulerianRMS.md
   5_metrics_det/metrics_spectrum.md
   5_metrics_det/metrics_LagrangianCumulativeDistance.md
   5_metrics_det/metrics_structure_evaluation.md  

.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Scripts

   6_scripts/modules.rst
