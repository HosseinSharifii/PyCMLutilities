

from PyCMLutil.animation.pymyovent_ventricle import animate_pymyovent as ap
import pandas as pd
import numpy as np
#pandas_data = pd.read_excel(data_str)
#pandas_data.to_csv('data/pymyovent_sample.csv')
def test_animation():
	data_str = 'data/pymyovent_sample.csv'
	temps = ['templates/2D_vent_anim.json',
			'templates/multipanel_anim.json',
			'templates/combined_anim.json']
	temps = ['templates/combined_anim.json']

	pandas_data = pd.read_csv(data_str)
	for temp in temps:
		output_str = 'examples' + '/' + temp.split('/')[-1].split('.')[0] + '.mp4'

		ap(pandas_data = pandas_data,
			template_file_string = temp,
			output_image_file_string = output_str)

if __name__ == "__main__":
	test_animation()
