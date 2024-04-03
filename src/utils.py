import pandas as pd
import xarray as xr
import numpy as np
import cartopy
import matplotlib.axes
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import cartopy.feature as cfeature 
import cartopy.crs as ccrs
import pickle

import os
import subprocess
from IPython.display import Video
 

    
class DictTable():
    """
    Overridden dict class which takes a list of dictionaries and renders an HTML Table in IPython Notebook.

    Parameters
    ----------
    list : list
        A list of dictionaries, where each dictionary contains 'path', 'type_stat', and 'name' keys.

    Attributes
    ----------
    html_table : str
        HTML representation of the table.

    Methods
    -------
    _repr_html_():
        Returns the HTML representation of the table.

    Example
    -------
    # Usage Example:
    table = DictTable(list_of_dicts)
    table_html = table._repr_html_()
    """
    
    def __init__(self,list):
        self.html_table = None
        self.list = list
        
    def _repr_html_(self):
        filehandler = open(self.list[0]['path'], 'rb') 
        object = pickle.load(filehandler)
        html = ["<table width=100%>"] 
        html.append("<tr>")
        html.append("<td><b>{0}</b></td>".format(self.list[0]['type_stat']))  
        for key, value in object.items():
            html.append("<td>{0}</td>".format(key)) 
        html.append("</tr>") 
        
        for dict in self.list: 
            
            filehandler = open(dict['path'], 'rb') 
            object = pickle.load(filehandler)
            html.append("<tr>") 
            html.append("<td><b>{0}</b></td>".format(dict['name']))  
            for key, value in object.items():
                html.append("<td>{0}</td>".format("{:.3f}".format(value)))
            html.append("</tr>")
            
        html.append("</table>")  
        
        self.html_table = '\n'.join(html)
            
        return self.html_table 

  
    
def movie_intercomp(ds_maps_list, methods=['DUACS'], name_var='uv', dir_output='../results/', region='Agulhas', framerate=24, colsize = 14):
    """
    Create and save an intercomparison movie from a list of xarray datasets.

    Parameters
    ----------
    ds_maps_list : list
        A list of xarray datasets, each containing map data.
    methods : list, optional
        List of method names. Default is ['DUACS'].
    name_var : str, optional
        Name of the variable to plot. Default is 'uv'.
    dir_output : str, optional
        Output directory to save frames and movie. Default is '../results/'. 
    region : str, optional
        Region name for the movie title. Default is 'Agulhas'.
    framerate : int, optional
        Frame rate of the movie. Default is 24.
    colsize : int, optional
        Width of the plot in inches. Default is 14.

    Returns
    -------
    Video: 
        IPython displayable video object. 
    """ 
    
    for tt in range(ds_maps_list[0]['time'].size): 

            nmet = np.size(methods)

            method = 'intercomp'
            ncol = 2 
            gridspec_kw={'width_ratios': [1, 1.25]}

            if nmet == 1: 
                ncol=1 
                gridspec_kw=None
                method = methods[0]

            fig, axs = plt.subplots(int(np.ceil(nmet/2)),ncol,figsize=(colsize,int(np.ceil(nmet/2))*4+2), gridspec_kw=gridspec_kw)

            date = str(ds_maps_list[0]['time'][tt].values)[:13]
            plt.suptitle(date)

            for i_met in range(nmet):

                if nmet==1:
                    ax0 = axs
                elif nmet>2: 
                    ax0 = axs[int(i_met/2),i_met%2]
                else:  
                    ax0 = axs[i_met]

                ids = ds_maps_list[i_met].isel(time=tt) 
                if i_met%2 == 0 and nmet!=1: 
                    ids[name_var].plot(ax=ax0,cmap='YlGnBu_r',vmin=0,vmax=0.6,add_colorbar=False)
                else: 
                    ids[name_var].plot(ax=ax0,cmap='YlGnBu_r',vmin=0,vmax=0.6,add_colorbar=True, extend='max')
                ax0.set_title(methods[i_met])  

            if nmet%2 !=0 and nmet!=1:
                i_met += 1
                axs[int(i_met/2),i_met%2].axis('off')

            fig.savefig(f'{dir_output}/frame_{method}_{region}_{name_var}_{str(tt).zfill(5)}.png',dpi=100)

            plt.close(fig) 
            
    moviename = f'movie_{method}_{region}_{name_var}.mp4'


    # Create movie
    sourcefolder = dir_output
    frame_pattern = f'frame_{method}_{region}_{name_var}_*.png'
    ffmpeg_options="-c:v libx264 -preset veryslow -crf 15 -pix_fmt yuv420p -loglevel quiet"

    command = 'ffmpeg -f image2 -r %i -pattern_type glob -i %s -y %s -r %i %s' % (
            framerate,
            os.path.join(sourcefolder, frame_pattern),
            ffmpeg_options,
            framerate,
            os.path.join(dir_output, moviename),
        )
    #print(command)

    _ = subprocess.run(command.split(' '),stdout=subprocess.DEVNULL)


    os.system(f'rm {os.path.join(sourcefolder, frame_pattern)}')

    return Video(os.path.join(dir_output, moviename),embed=True)
