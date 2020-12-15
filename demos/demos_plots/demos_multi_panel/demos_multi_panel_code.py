# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 23:40:08 2020

@author: ken
"""
import os
import matplotlib.pyplot as plt

from plots import multi_panel as mp

def demo():
    
    data_file_string = 'data/test_data.xlsx'
    image_dir = 'temp'
    json_dir = 'json'
   
    # Get files in json dir
    current_dir = os.path.dirname(os.path.realpath(__file__))
    json_dir = os.path.join(current_dir, json_dir)
    json_files = [f for f in os.listdir(json_dir) 
                  if os.path.isfile(os.path.join(json_dir,f))]
    json_files.append('')
    
    data_file_string = os.path.join(
            current_dir,'data','test_data.xlsx')
    
    for js in json_files:
        if (js == ''):
            image_name = 'blank_json'
            json_file_string = ''
        else:
            image_name = js.split('.')[0]
            json_file_string = os.path.join(
                current_dir, json_dir, js)
            
        print(json_file_string)
        # continue
        
        image_file_string = os.path.join(
                current_dir,image_dir,('%s.png' % image_name))
                
        fig, ax = mp.multi_panel_from_flat_data(
            data_file_string=data_file_string,
            template_file_string=json_file_string,
            output_image_file_string=image_file_string)
    
        plt.close(fig)
        
    print('ken was here')