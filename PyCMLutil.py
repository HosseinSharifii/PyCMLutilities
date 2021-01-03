# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 23:30:38 2020

@author: ken
"""

import sys

def pmc_util():
    """
    Calls the demo_code to run different demo plots
    
    Returns
    -------
    None.

    """      
    from demos import demos_code as d
    
    d.demos(sys.argv[1])
    
    #d.demos("plots_multi_panel")
    
    
if __name__ == "__main__":
    pmc_util()
    