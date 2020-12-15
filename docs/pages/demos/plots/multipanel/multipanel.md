---
title: Multipanel
has_children: false
grand_parent: Demos
parent: Plots
nav_order: 1
---
# Multipanel

## Overview

The [multipanel module](https://github.com/Campbell-Muscle-Lab/PyCMLutilities/blob/main/plots/multi_panel.py) creates figures with panels showing 1 or more columns from a flat data file.

The code takes 3 inputs:
+ an Excel file
+ a structure file written in JSON format
+ an output image file

For example

````
multi_panel_from_flat_data(
    excel_file_string = 'test.xlsx',
    template_file_string = 'template.json',
    output_image_file_string = 'image.png')
````

The images below were generated from the same excel file by passing in the templates stored in `<repo>/demos/demos_plots/demos_multi_panel/json`.

## Demo

+ Open a python prompt
+ Change directory to the repo base directory
+ `python PyCMLutil.py

The images below should be written to `<repo>/demos/demos_plots/demos_multi_panel/temp`

## Output

### Default - no layout
![blank](images/blank_json.png)

### 1 x 1
![Simple 1 x 1](images/1_1.png)

### 1 x 1 wide
![1 x 1 wide](images/1_1_wide.png)

### 1 x 1 height
![1 x 1 height](images/1_1_height.png)

### 1 x 1 x-display
![1 x 1 x-display](images/1_1_x_display.png)

### 1 x 1 x-ticks
![1 x 1 x-ticks](images/1_1_x_ticks.png)

### 1 x 2 wide
![1 x 2 wide](images/1_2_wide.png)

### 1 x 3 wide
![1 x 3 wide](images/1_3_wide.png)

### 1 x 2 wide
![1 x 2 envelope](images/1_2_envelope.png)

### 1 x 3 wide scaling
![1 x 3 wide scaling](images/1_3_wide_scaling.png)

### 2-2 partial
![2 x 2 partial](images/2_2_partial.png)

### 2 x 2
![2 x 2](images/2_2.png)

### 2 x 2 multi-series
![2 x 2 multi-series labels](images/2_2_multi_series.png)

### 2 x 2 multi-series labels
![2 x 2 multi-series with labels](images/2_2_multi_series_labels.png)

### 5 x 2
![5 x 2](images/5_2.png)

### 5 x 2 margins
![5 x 2 margins](images/5_2_margins.png)
