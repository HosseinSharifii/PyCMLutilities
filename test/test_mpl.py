from PyCMLutil.plots.multi_panel import multi_panel_from_flat_data as mpl
import pandas as pd


def test_mpl():
    data_file_string = "demos/data/test_data.xlsx"
    temp_list = [None,
                "demos/templates/1X1_mpl.json",
                "demos/templates/1X1_wide.json",
                "demos/templates/1X1_x_display.json",
                "demos/templates/1X1_height.json",
                "demos/templates/1X1_x_ticks.json",
                "demos/templates/1X2_wide.json",
                "demos/templates/1X3_wide.json",
                "demos/templates/1X3_wide_scaling.json",
                "demos/templates/1X2_envelope.json",
                "demos/templates/2X2_partial.json",
                "demos/templates/2X2_full.json",
                "demos/templates/2X2_multi_series.json",
                "demos/templates/2X2_multi_series_labels.json",
                "demos/templates/2X2_envelope_partial.json",
                "demos/templates/2X2_mix.json",
                "demos/templates/5X2_mpl.json",
                "demos/templates/5X2_margins.json",
                "demos/templates/2X2_mix_annotate.json",
                "demos/templates/pymyovent.json"]

    for i,t in enumerate(temp_list):
        print(i)
        if t == None:
            output_image_str = 'demos/numerical/'+'no_temp'+'.png'
        elif t.split('/')[-1].split('.')[0] == 'pymyovent':
            data_file_string = "demos/data/pymyovent_test.csv"
            output_image_str = 'demos/numerical/'+t.split('.')[0].split('/')[-1]+'.png'
        else:
            output_image_str = 'demos/numerical/'+t.split('.')[0].split('/')[-1]+'.png'


        mpl(data_file_string = data_file_string,
            template_file_string = t,
            output_image_file_string = output_image_str)

if __name__ == "__main__":
    test_mpl()
        
