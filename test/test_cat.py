from PyCMLutil.plots.multi_panel_cat import multi_panel_cat_from_flat_data as mplc
import pandas as pd


def test_cat():
    data_file_string = "data/valvular_disease.xlsx"
    temp_list = ['json/1X1_strip_valvular.json',
                'json/1X1_strip_hue_valvular.json',
                'json/1X1_point_valvular.json',
                'json/1X1_point_strip_valvular.json',
                'json/1X1_point_hue_valvular.json',
                'json/1X1_box_valvular.json',
                'json/1X1_box_strip_valvular.json',
                'json/1X1_box_hue_valvular.json',
                'json/4X4_multiple_valvular.json']
    temp_list = ['json/1X1_point_valvular.json']
    for i,t in enumerate(temp_list):
        print(i)
        output_image_str = 'examples/'+'test_'+t.split('.')[0].split('/')[-1]+'.png'


        mplc(data_file_string = data_file_string,
            template_file_string = t,
            output_image_file_string = output_image_str,dpi=100)

if __name__ == "__main__":
    test_cat()
        
