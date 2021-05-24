
# -*- coding: utf-8 -*-
"""
Created on Sat April 16 2021

@author: Hossein_Sharifi
"""

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib import patches as pat
from matplotlib import animation

import seaborn as sns

def default_formatting():
    """
    Sets default formatting (fontname, axis linewidth, ...)

    Returns
    -------
    formatting : dict
        dictionnary containing the default formatting.

    """
    formatting = dict()
    formatting['data_linewidth'] = 1.5
    formatting['fontname'] = 'Arial'
    formatting['axis_linewidth'] = 1.5
    formatting['x_label_fontsize'] = 12
    formatting['x_label_pad'] = 0
    formatting['y_label_rotation'] = 0
    formatting['y_label_fontsize'] = 12
    formatting['y_label_pad'] = 30
    formatting['legend_location'] = 'upper left'
    formatting['legend_bbox_to_anchor'] = [1.05, 1]
    formatting['legend_fontsize'] = 9
    formatting['legend_handlelength'] = 1
    formatting['tick_fontsize'] = 11
    formatting['patch_alpha'] = 0.3
    formatting['max_rows_per_legend'] = 4
    formatting['palette'] = None

    return formatting

def default_layout():
    """
    Sets default layout (figure size, margin size, grid space)

    Returns
    -------
    layout : dict
        dictionnary containing the default layout.

    """
    layout = dict()
    layout['fig_width'] = 5
    layout['fig_height'] = 5
    layout['panel_height'] = 1
    layout['top_margin'] = 0.1
    layout['bottom_margin'] = 0.1
    layout['left_margin'] = 0.1
    layout['right_margin'] = 0.1
    layout['grid_wspace'] = 0.1
    layout['grid_hspace'] = 0.1

    return layout


def animate_ventricle(pandas_data = [],
                    r1_name = "internal_radius",
                    r2_name = "external_radius",
                    template_data = dict(),
                    output_image_file_string="",
                    dpi = 300):

    import imageio

    # Pull default formatting, then overwite any values from the template

    skip_frames = 10
    temp_image_file_string = 'temp.png'
    with imageio.get_writer(output_image_file_string, mode='I') as writer:
        for i in np.arange(0, 2000,skip_frames):
                print(('Frame: %.0f' % i), end=' ', flush=True)

                r1 = pandas_data[r1_name].iloc[i].round(2)
                r2 = pandas_data[r2_name].iloc[i].round(2)
                t = pandas_data['time'].iloc[i]
                print(('time: %.0f' % t), end=' ', flush=True)
                display_vent(r1=r1,r2=r2,
                            output_image_file_string = temp_image_file_string,
                            t=t)

                image = imageio.imread(temp_image_file_string, format='png')
                writer.append_data(image)
        print('Animation built')
        print('Animation written to %s' % output_image_file_string)
    os.remove(temp_image_file_string)

def display_vent(r1 = None,
                r2 = None,
                template_data = dict(),
                output_image_file_string="",
                t = 0,
                dpi = 300):

    formatting = default_formatting()
    if ('formatting' in template_data):
        for entry in template_data['formatting']:
            formatting[entry] = template_data['formatting'][entry]

    # Pull default layout, then overwite any values from the template
    layout = default_layout()
    if 'layout' in template_data:
        for entry in template_data['layout']:
            layout[entry] = template_data['layout'][entry]

    fig = plt.figure(constrained_layout = False)
    fig.set_size_inches([layout['fig_width'], layout['fig_height']])
    spec = gridspec.GridSpec(nrows = 1,
                             ncols = 1,
                             figure = fig,
                             wspace = layout['grid_wspace'],
                             hspace = layout['grid_hspace'])
    ax = fig.add_subplot(spec[0,0])
    #r1 = pandas_data[r1_name].iloc[0].round(2)

    #r2 = pandas_data[r2_name].iloc[0].round(2)
    fc = '#EE938C'
    outer_circle = plt.Circle((0,0),r2,fill=True, fc = fc, ec=fc)
    ax.add_patch(outer_circle)

    fc = '#D76F67'
    inner_circle = plt.Circle((0,0),r1,fill=True, fc = fc, ec=fc)
    ax.add_patch(inner_circle)

    """for r in [r2,r1]:
        fc = '#D76F67'
        if r == np.amax([r2,r1]):

            fc = '#EE938C'
        patch = plt.Circle((0,0),r,fill=True, fc = fc, ec=fc)
        ax.add_patch(patch)"""

    """points_1 ,points_2= develop_basal_view(r1 = r1.iloc[100],
                                           r2 = r2.iloc[100],
                                           resolution = 1e-3)

    XY = [points_1,points_2]
    #XY = np.concatenate(develop_basal_view(r1 = pandas_data[r1_name].iloc[100],
    #                                       r2 = pandas_data[r2_name].iloc[100],
    #                                       resolution = 0.001),axis = 0)
    #print(XY)
    for xy in XY:
        #print(xy)
        polygon = pat.Polygon(xy = xy,
                          closed = True,
                          clip_on = True,
                          fc = None,
                          alpha = formatting['patch_alpha'])

        ax.add_patch(polygon)"""
    ax.set_ylim(-1.1*r2,1.1*r2)
    ax.set_ylim(-100,100)
    ax.set_xlim(-100,100)
    ax.text(0, 90, ('Time %.3f s' % t),
                   verticalalignment='top')
    """anim = animation.FuncAnimation(fig, animate,
                               init_func=init,
                               frames=10000,
                               interval=100,
                               blit=True)"""
    #anim = animation.FuncAnimation(fig,)
    # Tidy overall figure
    # Move plots inside margins
    lhs = layout['left_margin']/layout['fig_width']
    bot = layout['bottom_margin']/layout['fig_height']
    wid = (layout['fig_width']-layout['left_margin']-layout['right_margin'])/layout['fig_width']
    hei = (layout['fig_height']-layout['bottom_margin']-layout['top_margin'])/layout['fig_height']
    r = [lhs, bot, wid, hei]
    spec.tight_layout(fig, rect=r)

 
    # Save if required
    if output_image_file_string:
        print('Saving figure to %s' % output_image_file_string)
        output_dir = os.path.dirname(output_image_file_string)
        if not os.path.isdir(output_dir):
            print('Making output dir')
            os.makedirs(output_dir)
        fig.savefig(output_image_file_string, dpi=dpi)
    plt.close()

def init():
    r1 = pandas_data['internal_radius'].iloc[0]
    inner_circle.radius = r1
    r2 = pandas_data['external_radius'].iloc[0]
    outer_circle.radius = r2
    return inner_circle, outer_circle

def animate(i):
    r1 = pandas_data['internal_radius'].iloc[i]
    inner_circle.radius = r1
    r2 = pandas_data['external_radius'].iloc[i]
    outer_circle.radius = r2
    return inner_circle, outer_circle

    """polygon = pat.Polygon(xy = xy,
                          closed = False,
                          clip_on = True,
                          fc = col,
                          alpha = formatting['patch_alpha'])"""



def develop_basal_view(r1 = 1, r2 = 1, resolution = 0.01):

    points_1 = return_points(r1, resolution)
    points_2 = return_points(r2, resolution)

    return (points_1, points_2)

def return_points(r=1, resolution= 0.01):
    x = np.arange(-r,r,resolution)
    #print('x',x)
    y_pos = np.power(r**2 - np.power(x,2),1/2)
    #print('y_pos',y_pos)
    y_neg = - y_pos

    xy_pos = np.stack([x,y_pos],axis=-1)
    print('xy_pos',xy_pos)
    xy_neg = np.stack([x,y_neg],axis=-1)
    #print('xy_neg',xy_neg)
    xy = np.concatenate((xy_pos,xy_neg),axis = 0)

    return xy
