

from PyCMLutil.animation.pymyovent_ventricle import animate_pymyovent as ap
import pandas as pd
import numpy as np
#pandas_data = pd.read_excel(data_str)
#pandas_data.to_csv('data/pymyovent_sample.csv')
def test_animation():
	data_str = 'demos/data/test_data.xlsx'
	
	temps = ['demos/templates/mpl_anim.json']

	for temp in temps:
		output_str = 'demos' + '/' +'animation/' + temp.split('/')[-1].split('.')[0] + '.mp4'

		ap(data_file_string = data_str,
			template_file_string = temp,
			output_image_file_string = output_str)

if __name__ == "__main__":
	test_animation()
