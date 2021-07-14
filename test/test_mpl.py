from PyCMLutil.plots.multi_panel import multi_panel_from_flat_data as mpl
import pandas as pd


def test_mpl():
    data_file_string = "data/pymyovent_test.csv"
    temp_list = ['templates/pymyovent.json']
    for i,t in enumerate(temp_list):
        print(i)
        output_image_str = 'examples/'+'test_'+t.split('.')[0].split('/')[-1]+'.png'


        mpl(data_file_string = data_file_string,
            template_file_string = t,
            output_image_file_string = output_image_str,dpi=100)

if __name__ == "__main__":
    test_mpl()
        
