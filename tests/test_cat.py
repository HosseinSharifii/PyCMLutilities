from PyCMLutil.plots.multi_panel_cat import multi_panel_cat_from_flat_data as mplc
import pandas as pd


def test_cat():
    data_file_string = "demos/data/valvular_disease.xlsx"
    temp_list = ['demos/templates/1X1_strip_valvular.json',
                'demos/templates/1X1_strip_valvular_markers.json',
                'demos/templates/1X1_strip_valvular_no_jitter.json',
                'demos/templates/1X1_strip_valvular_hue.json',
                'demos/templates/1X1_point_valvular.json',
                'demos/templates/1X1_point_valvular_markers.json',
                'demos/templates/1X1_point_valvular_hue.json',
                'demos/templates/1X1_box_valvular.json',
                'demos/templates/1X1_box_valvular_hue.json',
                'demos/templates/1X1_box_valvular_modified_style.json',
                'demos/templates/1X1_box_strip_valvular.json',
                'demos/templates/1X2_box_point_strip_valvular.json',
                'demos/templates/4X4_multiple_valvular.json']
    for i,t in enumerate(temp_list):
        print(i)
        output_image_str = 'demos/categorical/'+t.split('.')[0].split('/')[-1]+'.png'


        mplc(data_file_string = data_file_string,
            template_file_string = t,
            output_image_file_string = output_image_str,dpi=100)

if __name__ == "__main__":
    test_cat()
        
