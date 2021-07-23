# -*- coding: utf-8 -*-
import os
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

def run_multi_panel_package():
    from PyCMLutil.plots.multi_panel import multi_panel_from_flat_data as mpl

    data_file_string = "./data/pymyovent_test.csv"
    template_file_string = "./json/pymyovent.json"
    image_file_string = "./output_file/multi_panel.png"

    output_dir = os.path.dirname(image_file_string)
    print('output_dir %s' % output_dir)
    if not os.path.isdir(output_dir):
        print('Making output dir')
        os.makedirs(output_dir)



    mpl(data_file_string=data_file_string,
        template_file_string=template_file_string,
        output_image_file_string=image_file_string)

if __name__ == "__main__":
    run_multi_panel_package()
    #pmc_util()
