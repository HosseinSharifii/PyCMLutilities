# -*- coding: utf-8 -*-
"""
Demos.md
"""

import os
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from plots import pCa_plots as p
from plots import fv_plots as fv
from plots import exp_plots as exp
#from plots import power_plot as pp

# plots import pCa_plots as p
# import PyCMLutilities.plots.fv_plots as fv
# import PyCMLutilities.curve_fitting.curve_fitting as cf

def demos(demo_group):
    """
    Parameters
    ----------
    demo_group : string

    Returns
    -------
    None.

    """        
    
    if (demo_group == 'tension_pCa'):
        
        pCa = np.array([9, 6, 5.5, 5, 4])
        f = np.array([1, 2, 5, 8, 10])
        
        image_file_string = 'demos_plots/demos_fit/temp/tension_pCa.png'
        
        # Adjust input files for current path
        current_dir = os.path.dirname(os.path.realpath(__file__))
        image_file_string = os.path.join(current_dir, image_file_string)
        
        p.y_pCa_plot(pCa, f, draw_fit=True, output_image_file_string=image_file_string)

    if (demo_group == 'force_velocity'):
        
        f = np.array([100, 500, 1000, 2000, 5000, 8000])
        v = np.array([2, 1.5, 1, 0.5, 0.1, 0.01])
        
        image_file_string = 'demos_plots/demos_fit/temp/force_velocity.png'
        
        # Adjust input files for current path
        current_dir = os.path.dirname(os.path.realpath(__file__))
        image_file_string = os.path.join(current_dir, image_file_string)        
        
        fv.fv_plot(f, v, draw_fit=True, output_image_file_string=image_file_string)
        
    if (demo_group == 'force_power'):
        
        f = np.array([100, 500, 1000, 2000, 5000, 8000])
        v = np.array([2, 1.5, 1, 0.5, 0.1, 0.01])
        fv_power = f*v
        
        image_file_string = 'demos_plots/demos_fit/temp/force_power.png'
        
        # Adjust input files for current path
        current_dir = os.path.dirname(os.path.realpath(__file__))
        image_file_string = os.path.join(current_dir, image_file_string)        
        
        fv.power_plot(f, fv_power, draw_fit=True, output_image_file_string=image_file_string)
        
    if (demo_group == 'exp_recovery'):
        
        n = 500
        t = np.linspace(0,1,n)
        noise = 0.1*np.random.normal(0,1,n)
        y = noise + 0.5 + 3.0 * (1 - np.exp(-4*t))
        
        image_file_string = 'demos_plots/demos_fit/temp/exp_recovery.png'
        
        # Adjust input files for current path
        current_dir = os.path.dirname(os.path.realpath(__file__))
        image_file_string = os.path.join(current_dir, image_file_string)        
        
        exp.exp_plot(t, y, draw_fit=True, output_image_file_string=image_file_string)
        
    if (demo_group == "plots_multi_panel"):
        from .demos_plots.demos_multi_panel import demos_multi_panel_code as dmp
        dmp.run_demos()
      
        
if __name__ == "__main__":
    demos()  
