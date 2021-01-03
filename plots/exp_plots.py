# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:20:25 2020

@author: kscamp3
"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

def exp_plot(t, y, draw_fit=False, ax=[], sym='ro', output_image_file_string = []):
    """ Draws exponential recovery plot with optional fit """
    
    # Make axes if requried
    if not ax:
        fig = plt.figure(constrained_layout=True)
        fig.set_size_inches([5,5])
        spec = gridspec.GridSpec(nrows=1, ncols=1, figure=fig)
        ax = fig.add_subplot(spec[0,0])
        
    ax.plot(t, y, 'b-')
    
    if draw_fit:
        from curve_fitting.curve_fitting import fit_exponential_recovery
        
        fit_data = fit_exponential_recovery(t, y)
        
        ax.plot(fit_data['x_fit'], fit_data['y_fit'], "y-",
                label='offset = %g\namp = %g\nk = %g' %
                    (fit_data['offset'], fit_data['amp'], fit_data['k']))
        
        
    # Add labels
    ax.set_xlabel('Time')
    ax.set_ylabel('Tension')
    ax.legend()
    
    # Save if required
    if output_image_file_string:
        print('Saving figure to %s' % output_image_file_string)
        plt.savefig(output_image_file_string, dpi=300)
    
    # Show figure in matplotlib window
    plt.show()
    
    

    

