
  # Check out the data challenge [website](https://2023a-ssh-mapping-ose.readthedocs.io) for more infos !

<p align="center">
  <img src="figures/dc_2023_ose_global_banner.jpg" alt="Alt Text" width="900"/>
</p>

# WOC ESA Data Challenges

This repository contains codes and sample notebooks for downloading and processing the 2024a WOC-ESA data challenges.
Note that this data challenge is part of the extended effort to improve oceanographic algorithms using data challenges: [ocean-data-challenges](https://ocean-data-challenges.github.io/index.html).

So far, the github page visits amount to: 

[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Focean-data-challenges%2F2024_DC_WOC-ESA&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=PAGE+VIEWS&edge_flat=false)](https://hits.seeyoufarm.com)



# 1. Context & Motivation
 

# 2. DC: Mediterranean Sea


### Observations
 

### Experimental setup


### Evaluation


# 3. DC: Gulf Stream


### Observations
 

### Experimental setup


### Evaluation


# 4. DC: North Sea


### Observations
 

### Experimental setup


### Evaluation
 

  

# 5. Get started


## Installation
:computer: _**How to get started ?**_

Clone the data challenge repo: 
```
git clone https://github.com/ocean-data-challenges/2024_DC_WOC-ESA.git
```
or using SSH: 
```
git clone git@github.com:ocean-data-challenges/2024_DC_WOC-ESA.git
```

create the data challenge conda environment, named env-dc-swot-filtering, by running the following command:
```
conda env create --file=dc_environment.yml 
```
and activate it with:

```
conda activate env-dc-woc-esa
```
then add it to the available kernels for jupyter to see: 
```
ipython kernel install --name "env-dc-woc-esa" --user
```
finally, select the "env-dc-woc-esa" kernel in your notebook with Kernel > Change Kernel.

You're now good to go ! 


## Download the data

The data are hosted and can be accessed on the MEOM server opendap [here](https://ige-meom-opendap.univ-grenoble-alpes.fr/thredds/catalog/meomopendap/extract/MEOM/OCEAN_DATA_CHALLENGES/2023a_SSH_mapping_OSE/catalog.html). The disk space needed to locally download the full dataset (for the reconstruction experiment, the independant evaluation and the comparison) is approximately 33Go. The comparison data is by far the heaviest with approximately 26Go. 




### 2. DC: Mediterranean Sea

#### Data structure

#### Example notebook

  
### 3. DC: Gulf Stream
 
#### Data structure

#### Example notebook


###  DC: North Sea

#### Data structure

#### Example notebook

  
  

# Acknowledgement

