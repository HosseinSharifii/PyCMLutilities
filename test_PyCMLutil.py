# -*- coding: utf-8 -*-
import os
import sys 
"""
Created on Mon July 13 11:34:38 2021

@author: Hossein
"""


def test_pycmlutil():

    # Get the number of arguments
    no_of_arguments = len(sys.argv)

    # Switch depending on number of arguments
    if (no_of_arguments == 1):
        print('No argument has been called!')
        print('Call the right "test_name" to test PyCMLutil')

    elif (no_of_arguments == 2):
        if sys.argv[1] == "test_mpl_num":
            print("Testing multi_panel_plots for numerical data")
            from test.test_mpl import test_mpl 
            test_mpl()

        elif sys.argv[1] == "test_mpl_cat":
            print("Testing multi_panel_plots for categorical data")
            from test.test_cat import test_cat
            test_cat()

        elif sys.argv[1] == "test_animation":
            print("Testing animation feature")
            from test.test_animation import test_animation
            test_animation()

        elif sys.argv[1] == "test_pv":
            print("Testing pressure-volume loop plots")
            from test.test_pv import test_pv
            test_pv()

if __name__ == "__main__":
    test_pycmlutil()
    #pmc_util()
