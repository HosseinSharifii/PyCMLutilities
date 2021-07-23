---
title: Multipanel Categorical
has_children: False
parent: Plots
nav_order: 2
---

# Multipanel Categorical
{:.no_toc}

* TOC
{:toc}
## Overview
This python function is useful for plotting multipanel plots when one variable is categorical.  

## Function
````python
PyCMLutil.plots.multi_panel_cat.multi_panel_cat_from_flat_data(
        data_file_string = [],
        excel_sheet = 'Sheet1',
        pandas_data = [],
        template_file_string=[],
        output_image_file_string = [],
        dpi = 300)
````
**Parameters:**

| **Key** | **Type** | **Comment** |
| ------ | ------- | ---------- |
| data_file_string | str, optional | Path to the data file (either in format of csv or xlsx). The default is []. |
| excel_sheet | str, optional | Excel sheet where the data are stored. The default is *Sheet1*. |
| pandas_data | Pandas DataFrame, optional | DataFrame containing the data. The default is []. |
| template_file_string | str, optional | Path to the .json structure file. The default is []. |
| output_image_file_string | str, optional | Path where the output plot is saved. The default is []. |
| dpi | int, optional | Image resolution. The default is 300. |


**Returns:**

| **Key** | **Comment** |
| ------ | ---------- |
| figure | Handle to the produced pyplot figure |
| ax | Handle to an array of the pyplot axes. |

### Data spreadsheet

Similar to multipanel plot function for [numerical](num_mpl.html), multipanel categorical plot reads data in two-dimensional tabular structure stored either in excel spreadsheets or Pandas [DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html). The only difference in this function is that one of the variables must be categorical.

### Template files

Again, multipanel categorical plot function uses similar [JSON](https://www.json.org/json-en.html) format for the template file. The only differences are explaind in below. 


At the moment, this function only supports three type of [seaborn](https://seaborn.pydata.org/index.html) plots for categorical data as follows. The following optional formatting parameters for each type of categorical plots can be set by the user. Otherwise, <u>default values will be used</u>. 


1. [stripplot()](https://seaborn.pydata.org/generated/seaborn.stripplot.html#seaborn.stripplot): 
   
    Following parameteres can be set by the user based on the desription provided by [seaborn](https://seaborn.pydata.org/index.html):


    | **Parameters** | **Type** | **Comment** |
    | ------ | ------- | ---------- |
    | marker | str, optional | Marker shape based on the markers [list](https://matplotlib.org/stable/api/markers_api.html). |
    | jitter | float, optional | Amount of jitter (only along the categorical axis) to apply. This can be useful when you have many points and they overlap, so that it is easier to see the distribution. You can specify the amount of jitter (half the width of the uniform random variable support), or just use True for a good default. |
    | dodge | bool, optional | When using hue nesting, setting this to True will separate the strips for different hue levels along the categorical axis. Otherwise, the points for each level will be plotted on top of each other. |
    | field_palette | palette name, optional | Colors to use for the different levels of the hue variable. Should be something that can be interpreted by [color_palette()](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette), or a dictionary mapping hue levels to matplotlib colors. We highly recommend to pick one of the qualitative colormaps offered by [matplotlib](https://matplotlib.org/stable/gallery/color/colormap_reference.html).|
    | marker_ec | str, optional | edge color of markers. |
    | marker_elw | str, optional | edge line width of markers. |
    | marker_size | str, optional | marker size. |
    
    1. To change the default values for any of these parameters, user can do that within the `series` sub-section under `panels` section in the **template** file as is explained for multipanel [numerical](num_mpl.html) plots.  
    For instance, in below example, `jitter` and `dodge` are manually set by the user. Wherease, for the second plot, deafult values are being used by not defining a new value.  
    ````javascript
    "series":
                [
                    {
                        "field": "LVESVi",
                        "style": "strip",
                        "field_label": "ESVi",
                        "jitter":0.5,
                        "dodge":true        
                    },
                    {
                        "field" : "LVEDVi",
                        "style" : "strip",
                        "field_label": "EDVi"
                    }
                ]
    ````
    2. Previous method might be tough when a large number of **stripplots** are difined within a multipanel categorical figure. Alternatively, user can globally change some of the parameteres described in above by defining a section called `strip_formatting` in the **template** file. In this way, all defined changes would be applied to all **stripplot** within the figure. 

    Default values for `strip_formatting` are:

    ````javascript
    "strip_formatting":
        {
            "jitter": true,
            "dodge": true,
            "marker_ec": None,
            "marker_elw": 0.5,
            "marker_size": 8,
            "marker_list": ['o','^','s','x','*']
        }
    ````
    
2. [boxplot()](https://seaborn.pydata.org/generated/seaborn.boxplot.html#seaborn.boxplot):

    Following parameteres can be set by the user based on the desription provided by [seaborn](https://seaborn.pydata.org/index.html):


    | **Parameters** | **Type** | **Comment** |
    | ------ | ------- | ---------- |
    | color_saturation | float, optional | Proportion of the original saturation to draw colors at. Large patches often look better with slightly desaturated colors, but set this to 1 if you want the plot colors to perfectly match the input color spec. |
    | dodge | bool, optional | When using hue nesting, setting this to True will shift the **boxplot** along the categorical axis. Otherwise, the points for each level will be plotted on top of each other. |
    | field_palette | palette name, optional | Colors to use for the different levels of the hue variable. Should be something that can be interpreted by [color_palette()](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette), or a dictionary mapping hue levels to matplotlib colors. We highly recommend to pick one of the qualitative colormaps offered by [matplotlib](https://matplotlib.org/stable/gallery/color/colormap_reference.html).|
    | linewidth | float, optional | Width of the gray lines that frame the plot elements. |
    | box_width | float, optional | Width of a full element when not using hue nesting, or width of all the elements for one level of the major grouping variable. |
    
    1. Similar to **stripplot**, the default values of these parameters can be changed by the user where the **boxplot** is being defined under `series` sub-section in the **template** file. 
    For instance, in below example, `field_palette` is manually set by the user. 
    ````javascript

    "series":
                [
                    {
                        "field": "SVi",
                        "style": "box",
                        "field_palette": "pastel"
                    }
                ]
    ````

    2. Again, this might be complicated when you are dealing with a large number of **boxplots**. Alternatively, user can globally change some of the parameteres described in above by defining a section called `box_formatting` in the **template** file. In this way, all defined changes in these parameteres would be applied to all **boxplots** within the figure. 

    Default values for `box_formatting` are:

    ````javascript

    "box_formatting":
        {
            "color_saturation": 1,
            "dodge": true,
            "box_width": 0.75,
            "linewidth": 1
        }
    ````

3. [pointplot()](https://seaborn.pydata.org/generated/seaborn.pointplot.html#seaborn.pointplot):

    Following parameteres can be set by the user based on the desription provided by [seaborn](https://seaborn.pydata.org/index.html):

    | **Parameters** | **Type** | **Comment** |
    | ------ | ------- | ---------- |
    | confidence_int | float or “sd” or None, optional | Size of confidence intervals to draw around estimated values. If “sd”, skip bootstrapping and draw the standard deviation of the observations. If None, no bootstrapping will be performed, and error bars will not be drawn. |
    | estimator | str, optional | Name of statistical function to estimate within each categorical bin, e.g., `"mean"` implies [numpy.mean](https://numpy.org/doc/stable/reference/generated/numpy.mean.html) |
    | field_palette | palette name, optional | Colors to use for the different levels of the hue variable. Should be something that can be interpreted by [color_palette()](https://seaborn.pydata.org/generated/seaborn.color_palette.html#seaborn.color_palette), or a dictionary mapping hue levels to matplotlib colors. We highly recommend to pick one of the qualitative colormaps offered by [matplotlib](https://matplotlib.org/stable/gallery/color/colormap_reference.html).|
    | dodge | bool, optional | When using hue nesting, setting this to True will shift the **pointplot** along the categorical axis. Otherwise, the points for each level will be plotted on top of each other. |
    | linestyle | str, optional | Line styles to use for each of the hue levels. |
    | errwidth | float, optional | Thickness of error bar lines (and caps). |
    | capsize | float, optional | Width of the “caps” on error bars. |
    | markers | str, optional | Marker shape based on the markers [list](https://matplotlib.org/stable/api/markers_api.html). |
    | join | bool, optional | If True, lines will be drawn between point estimates at the same hue level. |


    1. The default values of these parameteres can be altered for each **pointplot** within a subplot/ panel by specify them in `series` sub-section. For example, in the following panel, first **pointplot** uses statistical function of *mean* as the estimator, while the second one uses *median*.  

    ````javascript
    "series":
                [
                    {
                        "field": "SVi",
                        "style": "point",
                        "estimator": "mean"
                    },
                    {
                        "field": "SVi",
                        "style": "point",
                        "estimator": "median"
                    }
                ]
    ````

    2. To globally adjust these parameters, user needs to define a section called `point_formatting` and assign the new values in there. 

    Default values for `point_formatting` are:

    ````javascript
    "point_formatting":
        {
            "confidence_int": "sd",
            "estimator": "mean",
            "linestyle": "-",
            "dodge": true,
            "join": true,
            "errwidth": None,
            "capsize": None
        }
    ````

## Note
- **hue**, **hue_order**, and **order** of categorical data can be defined in two manners: 
1. They can be assigned globally to all subplots/panels via defining `global_hue`, `global_hue_order`, and `order`, respectively in the `x_display` section of the **template** file as follows:
    ````javascript
        "x_display":
        {
            "global_x_field": "global x-axis variable",
            "label": "global x-axis label",
            "order": ["value_1","value_2"],
            "global_hue": "global hue variable",
            "global_hue_order": ["hue_value_1","hue_value_2"]
        }
    ````
2. Or they can be defined defined for each subplot independent of other panels via defining `hue`, `hue_oreder`, and `x_order` at each panel data in the **template** file. For instance:
    ````javascript
        {
            "column": 2,
            "hue": "valvular_disorder",
            "hue_order": ["AS","MR"],
            "x_order": ["control","patients"],
            "y_info":
            {
                "label":"Ejection\nfraction",
                "scaling_type": "close_fit",
                "series":
                [
                    {
                        "field": "EF",
                        "style": "box",
                        "field_palette": "Set2"
                    }
                ]
            }
        }
    ````
Now try [demos](../demos/multipanel_categorical/categorical.html) to ger more familiar.


