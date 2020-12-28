# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 23:30:38 2020

@author: ken
"""

def pmc_util():
    """
    Calls the demo_code to run a multi-panel plot 
    
    Returns
    -------
    None.

    """    
    
    from demos import demos_code as d
    
    d.demos('plots_multi_panel')
    
    
if __name__ == "__main__":
    pmc_util()
