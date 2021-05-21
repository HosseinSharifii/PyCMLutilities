# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 10:33:36 2021

@author: Hossein_Sharifi
"""

import json
import pandas as pd
import numpy as np
import math

from scipy.signal import find_peaks

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.lines import Line2D
from matplotlib import patches as pat
from matplotlib.patches import Patch
from matplotlib.patches import Rectangle
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
    formatting['color_theme_category'] = 'Set2'
    formatting['palette_list'] = ['pastel','Set2','flare','deep']
    formatting['color_saturation'] = 1
    formatting['box_width'] = 0.75
    formatting['dodge'] = True
    formatting['jitter_bool'] = True
    formatting['scatter_marker'] = '.'
    formatting['markers_size'] = 8
    formatting['scatter_edgecolor'] = None
    formatting['scatter_edge_linewidth'] = 0.5
    # pointplot
    formatting['join'] = True

    return formatting
def default_strip_formatting():
    """
    Sets default formatting for strip plot (marker_type, marker_size, jitter, ...)

    Returns
    -------
    strip_formatting : dict
        dictionnary containing the default formatting for strip plot.

    """
    strip_formatting = dict()
    strip_formatting['marker_list'] = ['o','^','s','x','*']
    strip_formatting['jitter'] = True
    strip_formatting['dodge'] = True
    strip_formatting['marker_ec'] = None
    strip_formatting['marker_elw'] = 0.5
    strip_formatting['marker_size'] = 8

    return strip_formatting

def default_box_formatting():
    """
    Sets default formatting for box plot (marker_type, marker_size, jitter, ...)

    Returns
    -------
    box_formatting : dict
        dictionnary containing the default formatting for strip plot.

    """
    box_formatting = dict()
    box_formatting['color_saturation'] = 1
    box_formatting['box_width'] = 0.75
    box_formatting['dodge'] = True
    box_formatting['linewidth'] = 1


    return box_formatting

def default_layout():
    """
    Sets default layout (figure size, margin size, grid space)

    Returns
    -------
    layout : dict
        dictionnary containing the default layout.

    """
    layout = dict()
    layout['fig_width'] = 3.5
    layout['panel_height'] = 1
    layout['top_margin'] = 0.1
    layout['bottom_margin'] = 0.1
    layout['left_margin'] = 0.1
    layout['right_margin'] = 0.1
    layout['grid_wspace'] = 0.1
    layout['grid_hspace'] = 0.1

    return layout

def default_processing():
    processing = dict()
    processing['envelope_n'] = 300

    return processing

def multi_panel_cat_from_flat_data(
        data_file_string = [],
        excel_sheet = 'Sheet1',
        pandas_data = [],
        template_file_string=[],
        output_image_file_string = [],
        dpi = 300):
    """
    Plot a multi-panel figure

    Parameters
    ----------
    data_file_string : str, optional
        Path to the data file. The default is [].
    excel_sheet : str, optional
        Excel sheet where the data are stored. The default is 'Sheet1'.
    pandas_data : DataFrame, optional
        DataFrame containing the data. The default is [].
    template_file_string : str, optional
        Path to the .json structure file. The default is [].
    output_image_file_string : str, optional
        Path where the output plot is saved. The default is [].
    dpi : int, optional
        Image resolution. The default is 300.

    Returns
    -------
    fig : figure
        Handle to the produced pyplot figure.
    ax : axes
        Handle to an array of the pyplot axes.

    """

    # Check for template file, make an empty dict if absent
    if (template_file_string):
        with open(template_file_string, 'r') as f:
            template_data = json.load(f)
    else:
        template_data=dict()

    # Pull default formatting, then overwite any values from the template
    formatting = default_formatting()
    if ('formatting' in template_data):
        for entry in template_data['formatting']:
            formatting[entry] = template_data['formatting'][entry]
    # Pull default formatting for strip plot, then overwite any values from the template
    strip_formatting = default_strip_formatting()
    if ('strip_formatting' in template_data):
        for entry in template_data['strip_formatting']:
            strip_formatting[entry] = template_data['strip_formatting'][entry]

      # Pull default formatting for box plot, then overwite any values from the template
    box_formatting = default_box_formatting()
    if ('box_formatting' in template_data):
        for entry in template_data['box_formatting']:
            box_formatting[entry] = template_data['box_formatting'][entry]

    # Pull default processing
    processing = default_processing()
    if 'processing' in template_data:
        for entry in template_data['processing']:
            processing[entry] = template_data['processing'][entry]

    # Read in the data
    if (not data_file_string==[]):
        file_type = data_file_string.split('.')[-1]
        if file_type == 'xlsx':
            pandas_data = pd.read_excel(data_file_string,
                                        sheet_name=excel_sheet)
        if file_type == 'csv':
            pandas_data = pd.read_csv(data_file_string)

    # Try to work out x data
    if 'x_display' in template_data:
        x_display = template_data['x_display']
    else:
        x_display = dict()

    # Set plausible values if fields are missing
    """ Need to think a bit more how to deal with missing fields for categorical data"""
    ####
    if 'global_x_field' not in x_display:
        x_display['global_x_field'] = pandas_data.columns[0]
    """if 'global_x_ticks' not in x_display:
        x_lim = (pandas_data[x_display['global_x_field']].iloc[0],
                 pandas_data[x_display['global_x_field']].iloc[-1])
        x_display['global_x_ticks'] = \
            np.asarray(deduce_axis_limits(x_lim, 'autoscaling'))
        x_ticks_defined=False
    else:
        x_ticks_defined=True"""
    if 'label' not in x_display:
        x_display['label'] = x_display['global_x_field']
    if 'order' not in x_display:
        x_display['order'] = \
            pandas_data[x_display['global_x_field']].unique()
    # setup hue 

    if 'global_hue' not in x_display:
        x_display['global_hue'] = None
        x_display['global_hue_order'] = None
    else:
        if 'global_hue_order' not in x_display: 
            x_display['global_hue_order'] = \
                pandas_data[x_display['global_hue']].unique()

    ####
    # Try to pull off the panel data and cycle through the panels one by one to
    # get the number of columns

    """ Need to think a bit more how to deal with missing fields for categorical data"""
    # Check for panels tag. If it doesn't exist
    # make up panel data
    if 'panels' in template_data:
        panel_data = template_data['panels']
    ####
    else:
        panel_data=dict()
        panel_data['column'] = 1
        panel_data['y_info'] = dict()
        panel_data['y_info']['label'] = pandas_data.columns[0]
        y_data = dict()
        y_data['field'] = pandas_data.columns[0]
        panel_data['y_info']['series'] = [y_data]
        panel_data = [panel_data]
    ####


    no_of_columns = 0
    for p_data in panel_data:
        test_column = p_data['column']
        if (test_column > no_of_columns):
            no_of_columns = test_column

    # Now scan through panels working out how many panel rows to create
    row_counters = np.zeros(no_of_columns, dtype=int)

    for i,p_data in enumerate(panel_data):
        # Update row counters
        row_counters[p_data['column']-1] += 1
    rows_per_column = row_counters
    ax=[]
    no_of_rows = np.amax(row_counters)


    # Now you know how many panels, create a figure of the right size
    layout = default_layout()
    if 'layout' in template_data:
        for entry in template_data['layout']:
            layout[entry] = template_data['layout'][entry]

    fig_height = layout['top_margin'] + \
                (no_of_rows * layout['panel_height']) + \
                 layout['bottom_margin']

    # Now create figure
    fig = plt.figure(constrained_layout=False)

    fig.set_size_inches([layout['fig_width'], fig_height])
    spec = gridspec.GridSpec(nrows=no_of_rows,
                             ncols=no_of_columns,
                             figure=fig,
                             wspace=layout['grid_wspace'],
                             hspace=layout['grid_hspace'])


    # Now return to panel data, scan through adding plots as you go
    row_counters = np.zeros(no_of_columns, dtype=int)
    for i,p_data in enumerate(panel_data):

        # Update row counters and add axis
        row_counters[p_data['column']-1] += 1
        c = p_data['column']-1
        r = row_counters[c]-1
        ax.append(fig.add_subplot(spec[r,c]))

        # setup x axis
        if 'x_field' not in p_data:
            p_data['x_field'] = x_display['global_x_field']
            p_data['x_order'] = x_display['order']
        # setup hue
        if 'hue' not in p_data:
            #check global field
            p_data['hue'] = x_display['global_hue']
            p_data['hue_order'] = x_display['global_hue_order']
        else:
            if 'hue_order' not in p_data:
                p_data['hue_order'] = \
                    pandas_data[p_data['hue']].unique()

        legend_symbols = []
        legend_strings = []

        # Set up your colors
        colors = sns.color_palette(formatting['color_theme_category'])
        line_counter = 0
        patch_counter = 0
        data_counter =0

        # Cycle through the y_data
        for j,y_d in enumerate(p_data['y_info']['series']):
            # Set the plot style to strip if it is missing
            if 'style' not in y_d:
                y_d['style'] = 'strip'
            # Fill in a blank label if it is missing
            if 'field_label' not in y_d:
                y_d['field_label'] = []

            # setup marker
            if 'marker' not in y_d:
                y_d['marker'] = strip_formatting['marker_list'][j]
            # setup palette
            if 'field_palette' not in y_d:
                y_d['field_palette'] = formatting['palette_list'][j]
            print(y_d['field_palette'], f'panel {i}',f'for y_data {j}')


            x = pandas_data[p_data['x_field']]
            y = pandas_data[y_d['field']]
            if p_data['hue'] == None:
                hue = None
            else: 
                hue = pandas_data[p_data['hue']]
            

            if 'scaling_factor' in y_d:
                y = y * y_d['scaling_factor']

            if 'log_display' in y_d:
                if y_d['log_display']=='on':
                    y = np.log10(y)

            # Track min and max y
            if (j==0):
                min_y = y.min()
                max_y = y.max()

            min_y = np.amin([min_y, np.amin(y)])
            max_y = np.amax([max_y, np.amax(y)])

            # handle next categorical variable if it is called


            # plot striplot depending on setyle
            if y_d['style'] == 'strip':
                sns.stripplot(x = x, y = y, hue = hue,
                                ax = ax[i],
                                marker = y_d['marker'],
                                jitter = strip_formatting['jitter'],
                                dodge = strip_formatting['dodge'],
                                palette = y_d['field_palette'],
                                edgecolor = strip_formatting['marker_ec'],
                                linewidth = strip_formatting['marker_elw'],
                                size = strip_formatting['marker_size'],
                                order = p_data['x_order'],
                                hue_order = p_data['hue_order'],
                                clip_on = False)


                # handle legend 
                if hue is not None:
                    for k,h in enumerate(p_data['hue_order']):
                        print(k)
                        legend_symbols.append(Line2D([],[],
                                                color = sns.color_palette(palette =y_d['field_palette'])[k],
                                                marker = y_d['marker'],
                                                markersize = strip_formatting['marker_size'],
                                                linestyle = 'None'))
                        field_label = ''
                        if y_d['field_label']:
                            field_label  = f'({y_d["field_label"]})'
                        
                        str = f'{h} {field_label}'
                        legend_strings.append(str)

                else:
                    if y_d['field_label']:
                        for l,o in enumerate(p_data['x_order']):
                            legend_symbols.append(Line2D([],[],
                                                color = sns.color_palette(palette =y_d['field_palette'])[l],
                                                marker = y_d['marker'],
                                                markersize = strip_formatting['marker_size'],
                                                linestyle = 'None'))
                            legend_strings.append(y_d["field_label"])

            if y_d['style'] == 'box':
                sns.boxplot(x = x, y = y, hue=hue,
                            ax = ax[i],
                            saturation = box_formatting['color_saturation'],
                            width = box_formatting['box_width'],
                            dodge = box_formatting['dodge'],
                            linewidth = box_formatting['linewidth'],
                            palette = y_d['field_palette'])

            # handle legend 
                if hue is not None:
                    for k,h in enumerate(p_data['hue_order']):
                        print(k)
                        legend_symbols.append(Patch(facecolor=sns.color_palette(palette =y_d['field_palette'])[k],
                                                    alpha=box_formatting['color_saturation']))
                        field_label = ''
                        if y_d['field_label']:
                            field_label  = f'({y_d["field_label"]})'
                        
                        str = f'{h} {field_label}'
                        legend_strings.append(str)

                else:
                    if y_d['field_label']:
                        for l,o in enumerate(p_data['x_order']):
                            legend_symbols.append(Patch(facecolor=sns.color_palette(palette =y_d['field_palette'])[l],
                                                    alpha=box_formatting['color_saturation']))
                            legend_strings.append(y_d["field_label"])

            if y_d['style'] == 'point':
                sns.pointplot(x = x, y = y, hue=hue,
                                ax = ax[i],
                                join = formatting['join'],
                                palette = formatting['color_theme_category'])
            # Plot line depending on style
            if (y_d['style'] == 'line'):
                if 'field_color' in y_d:
                    col = y_d['field_color']
                else:
                    col = colors[line_counter]
                ax[i].plot(x, y,
                        linewidth = formatting['data_linewidth'],
                        color = col,
                        clip_on = True)
                line_counter +=1
                if y_d['field_label']:
                    legend_symbols.append(
                        Line2D([0], [0],
                               color = ax[i].lines[-1].get_color(),
                               lw = formatting['data_linewidth']))
                    legend_strings.append(y_d['field_label'])

            if (y_d['style'] == 'envelope'):
                # Hold the maximum and minimum values
                y_top = pd.Series(y).rolling(processing['envelope_n'],
                                             min_periods=1).max().to_numpy()
                y_bot = pd.Series(y).rolling(processing['envelope_n'],
                                             min_periods=1).min().to_numpy()
                yp = np.hstack((y_top, y_bot[::-1], y_top[0]))
                xp = np.hstack((x, x[::-1], x[0]))
                xy = np.vstack((xp,yp))
                xy = np.array(np.array(xy).transpose());
                if 'field_color' in y_d:
                    col = y_d['field_color']
                else:
                    col = colors[patch_counter]
                polygon = pat.Polygon(xy = xy,
                                      closed = True,
                                      clip_on = True,
                                      fc = col,
                                      alpha = formatting['patch_alpha'])
                ax[i].add_patch(polygon)

                if y_d['field_label']:
                    legend_symbols.append(
                            Patch(facecolor = col,
                                  alpha =formatting['patch_alpha']))
                    legend_strings.append(y_d['field_label'])

                patch_counter = patch_counter+1

        # Tidy up axes and legends

        # Set y limits
        min_y = math.floor(min_y)
        max_y = math.ceil(max_y)
        ylim=([min_y, max_y])
        if ('ticks' in p_data['y_info']):
            ylim=tuple(p_data['y_info']['ticks'])

        ax[i].set_ylim(ylim)
        ax[i].set_yticks(ylim)

        # Update axes, tick font and size
        for a in ['left','bottom']:
            ax[i].spines[a].set_linewidth(formatting['axis_linewidth'])
        ax[i].tick_params('both',
                width = formatting['axis_linewidth'])

        for tick_label in ax[i].get_xticklabels():
            tick_label.set_fontname(formatting['fontname'])
            tick_label.set_fontsize(formatting['tick_fontsize'])
        for tick_label in ax[i].get_yticklabels():
            tick_label.set_fontname(formatting['fontname'])
            tick_label.set_fontsize(formatting['tick_fontsize'])

        # Remove top and right-hand size of box
        ax[i].spines['top'].set_visible(False)
        ax[i].spines['right'].set_visible(False)

        # Display x axis if bottom
        if (r==(rows_per_column[c]-1)):
            ax[i].set_xlabel(x_display['label'],
                          labelpad = formatting['x_label_pad'],
                          fontfamily = formatting['fontname'],
                          fontsize = formatting['x_label_fontsize'])
        else:
            ax[i].set_xlabel('')
            #ax[i].spines['bottom'].set_visible(False)
            #ax[i].tick_params(labelbottom=False, bottom=False)

        # Set y label
        ax[i].set_ylabel(p_data['y_info']['label'],
                      loc='center',
                      verticalalignment='center',
                      labelpad = formatting['y_label_pad'],
                      fontfamily = formatting['fontname'],
                      fontsize = formatting['y_label_fontsize'],
                      rotation = formatting['y_label_rotation'])

        # Add legend if it exists
        if legend_symbols:
            leg = ax[i].legend(legend_symbols, legend_strings,
                         loc = formatting['legend_location'],
                         handlelength = formatting['legend_handlelength'],
                         bbox_to_anchor=(formatting['legend_bbox_to_anchor'][0],
                                         formatting['legend_bbox_to_anchor'][1]),
                         prop={'family': formatting['fontname'],
                               'size': formatting['legend_fontsize']},
                         ncol = int(np.ceil(len(legend_symbols)/
                                            formatting['max_rows_per_legend'])))
            leg.get_frame().set_linewidth(formatting['axis_linewidth'])
            leg.get_frame().set_edgecolor("black")
        handle_annotations(template_data, ax[i], i, formatting)

    # Tidy overall figure
    # Move plots inside margins
    lhs = layout['left_margin']/layout['fig_width']
    bot = layout['bottom_margin']/fig_height
    wid = (layout['fig_width']-0*layout['left_margin']-layout['right_margin'])/layout['fig_width']
    hei = (fig_height-0*layout['bottom_margin']-layout['top_margin'])/fig_height
    r = [lhs, bot, wid, hei]
    spec.tight_layout(fig, rect=r)

    fig.align_labels()

    # Save if required
    if output_image_file_string:
        print('Saving figure to %s' % output_image_file_string)
        fig.savefig(output_image_file_string, dpi=dpi)

    return ax, fig


def handle_annotations(template_data, ax, panel_index, formatting):
    if not ('annotations' in template_data):
        return
    annotation_data = template_data['annotations']
    for an in annotation_data:
        if ((an['panel'] == 'all') or (an['panel'] == panel_index)):
            # check for vertical lines
            if (an['type'] == 'v_line'):
                # define default formats for v_line,
                # if they are not alrady defined
                if not('linestyle' in an):
                    an['linestyle'] = '--'
                if not('linewidth' in an):
                    an['linewidth'] = formatting['data_linewidth']
                if not('color' in an):
                    an['color'] = 'black'
                # now draw the v_line
                ax.axvline(x = an['x_value'],
                            linestyle = an['linestyle'],
                            linewidth = an['linewidth'],
                            color = an['color'])

            # check for horizontal lines
            elif (an['type'] == 'h_line'):
                # define default formats for v_line,
                # if they are not alrady defined
                if not('linestyle' in an):
                    an['linestyle'] = '--'
                if not('linewidth' in an):
                    an['linewidth'] = formatting['data_linewidth']
                if not('color' in an):
                    an['color'] = 'black'
                # now draw the v_line
                ax.axhline(y = an['y_value'],
                            linestyle = an['linestyle'],
                            linewidth = an['linewidth'],
                            color = an['color'])

            elif (an['type'] == 'box'):
                # drawing box
                x_start = an['x_coord']
                y_lim = ax.get_ylim()
                y_start = y_lim[0] + \
                        (y_lim[1]-y_lim[0]) * an['y_rel_coord']
                h_box = (y_lim[1]-y_lim[0]) * an['rel_height']
                xy_start = [x_start,y_start]
                if not('linestyle' in an):
                    an['linestyle'] = '-'
                if not('linewidth' in an):
                    an['linewidth'] = formatting['data_linewidth']
                if not('face_color' in an):
                    an['face_color'] = 'none'
                if not('edge_color' in an):
                    an['edge_color'] = 'black'
                box = Rectangle(xy = xy_start,
                            width = an['width'],
                            height = h_box,
                            facecolor = an['face_color'],
                            edgecolor = an['edge_color'],
                            linestyle = an['linestyle'],
                            linewidth = an['linewidth'],
                            clip_on = False)
                ax.add_patch(box)

            elif (an['type'] == 'text'):
                # writing text
                y_lim = ax.get_ylim()
                if not('label_fontsize' in an):
                    an['label_fontsize'] = formatting['y_label_fontsize']
                if not('label_color' in an):
                    an['label_color'] = 'black'
                ax.text(x = an['x_coord'],
                        y = y_lim[0] + (y_lim[1]-y_lim[0]) * an['y_rel_coord'],
                        s = an['label'],
                        fontsize = an['label_fontsize'],
                        fontfamily = formatting['fontname'],
                        horizontalalignment='center',
                        verticalalignment='center',
                        color = an['label_color'])

def deduce_axis_limits(lim, mode_string=[]):

    """
    Sets the x limits

    Parameters
    ----------
    lim : tuple
        tuple containing the first and last x-value from the data.
    mode_string : str, optional
        If set to "close_fit", the x limits are the closest to the lim input. The default is [].

    Returns
    -------
    Tuple containing the x limits

    """

    # Start simply
    lim = np.asarray(lim)
    lim[0] = multiple_less_than(lim[0])
    lim[1] = multiple_greater_than(lim[1])

    if (mode_string != 'close_fit'):
        if (lim[0]>0):
            lim[0]=0
        else:
            if (lim[1]<0):
                lim[1]=0

    return ((lim[0],lim[1]))

def multiple_greater_than(v, multiple=0.2):
    if (v>0):
        n = np.floor(np.log10(v))
        m = multiple*np.power(10,n)
        v = m*np.ceil(v/m)
    if (v<0):
        n = np.floor(np.log10(-v))
        m = multiple*np.power(10,n)
        v = m*np.ceil(v/m)

    return v

def multiple_less_than(v, multiple=0.2):
    if (v>0):
        n = np.floor(np.log10(v))
        m = multiple*np.power(10,n)
        v = m*np.floor(v/m)
    if (v<0):
        n = np.floor(np.log10(-v))
        m = multiple*np.power(10,n)
        v = m*np.floor(v/m)

    return v

def transfer_ax(ax,new_figure,spec = 111):

    old_fig = ax.figure
    #ax.remove()
    ax.figure = new_figure



    dummy_ax = new_figure.add_subplot(spec)
    pos = dummy_ax.get_position()

    ax.set_position(pos)
    print(f'dum_pos = {pos}',f'ax_pos = {ax.get_position()}')
    dummy_ax.remove()
    new_figure.axes.append(ax)
    new_figure.add_axes(ax)
    plt.close(old_fig)

if __name__ == "__main__":
    (fig,ax) = multi_panel_from_flat_data()
    plt.close(fig)
