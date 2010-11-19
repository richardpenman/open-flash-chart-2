# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 of the License.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# Author: Emanuel Fonseca
# Email:  emdfonseca<at>gmail<dot>com
# Date:   25 August 2008
#
# Author: Eugene Kin Chee Yip
# Date:   7 Nov 2008
#
# Author: Richard Penman
# Date:   12 Nov 2009



class varieties(dict):
    def __init__(self, type=None, alpha=None, colour=None, text=None, fontsize=None, values=None):
        if type is not None: self.set_type(type)
        if alpha is not None: self.set_alpha(alpha)
        if colour is not None: self.set_colour(colour)
        if text is not None: self.set_text(text)
        if fontsize is not None: self.set_fontsize(fontsize)
        if values is not None: self.set_values(values)

    def set_type(self, type):
        self['type'] = type

    def set_alpha(self, alpha):
        self['alpha'] = alpha

    def set_colour(self, colour):
        self['colour'] = colour

    def set_gradient_fill(self, gradient_fill):
        self['gradient-fill'] = gradient_fill
  
    def set_halo_size(self, size):
        self['halo-size'] = size
        
    def set_width(self, width):
        self['width'] = width
        
    def set_dot_size(self, size):
        self['dot-size'] = size
        
    def set_text(self, text):
        self['text'] = text

    def set_fontsize(self, fontsize):
        self['font-size'] = fontsize

    def set_values(self, values):
        self['values'] = values
            
    def append_keys(self, colour=None, text=None, fontsize=None):
        try:
            self['keys'].append(bar_stack_key(colour, text, fontsize))
        except:
            self['keys'] = [bar_stack_key(colour, text, fontsize)]
    
    def append_values(self, values):
        try:
            self['values'].append(values)
        except:
            self['values'] = [values]
            
    def append_stack(self, values):
        self.append_values(values)
       
    def set_line_style(self, on, off):
        self['line-style'] = line_style(on, off)
        
    def set_tooltip(self, text):
        self['tip'] = text
        
    def set_no_labels(self, no_labels):
        self['no-labels'] = no_labels
        
    def set_loop(self):
        self['loop'] = True
        
    def set_on_click(self, javascript_call):
        self['on-click'] = javascript_call




##########################################
# key class for bar stack
class bar_stack_key(dict):
    def __init__(self, colour=None, text=None, fontsize=None):
        if colour is not None: self.set_colour(colour)
        if text is not None: self.set_text(text)
        if fontsize is not None: self.set_fontsize(fontsize)
        
    def set_colour(self, colour):
        self['colour'] = colour
            
    def set_text(self, text):
        self['text'] = text
            
    def set_fontsize(self, fontsize):
        self['font-size'] = fontsize


##########################################
# value class for custom data points
class value(dict):
    def __init__(self, val=None, colour=None, tooltip=None):
        if val is not None: self.set_val(val)
        if colour is not None: self.set_colour(colour)
        if tooltip is not None: self.set_tooltip(tooltip)
        
    def set_val(self, val):
        self['value'] = val
        
    def set_colour(self, colour):
        self['colour'] = colour
        
    def set_tooltip(self, tooltip):
        self['tip'] = tooltip
            
class dot_value(value):
    pass

class bar_value(value):
    def __init__(self, (top, bottom), colour=None, tooltip=None):
        value.__init__(self, colour = colour, tooltip = tooltip)
        self.set_top_value(top)
        self.set_bottom_value(bottom)
        
    def set_top_value(self, top):
        self['top'] = top
    
    def set_bottom_value(self, bottom):
        self['bottom'] = bottom
        
class bar_3d_value(bar_value):
    def __init__(self, top, colour=None, tooltip=None):
        value.__init__(self, colour = colour, tooltip = tooltip)
        self.set_top_value(top)
        
    def set_top_value(self, top):
        self['top'] = top
        
        
class bar_glass_value(bar_3d_value):
    pass
        
class bar_sketch_value(bar_3d_value):
    pass        

class hbar_value(value):
    def __init__(self, (left, right), colour=None, tooltip=None):    
        value.__init__(self, colour = colour, tooltip = tooltip)
        self.set_left_value(left)
        self.set_right_value(right)
        
    def set_left_value(self, left):
        self['left'] = left
    
    def set_right_value(self, right):
        self['right'] = right

class bar_stack_value(value):
    def __init__(self, val, colour=None, tooltip=None):
        value.__init__(self, colour = colour, tooltip = tooltip)
        self.set_value(val)
        
    def set_value(self, val):
        if val:
            self['val'] = val
        
class pie_value(value):
    def __init__(self, val, label=None, colour=None, tooltip=None):
        value.__init__(self, val, colour, tooltip)
        if label is not None: self.set_label(label)
        
    def set_label(self, (label, colour, fontsize)):
        self['label'] = label
        self['label-colour'] = colour
        self['font-size'] = fontsize
            

            
class scatter_value(value):
    def __init__(self, (x, y), colour=None, tooltip=None):
        value.__init__(self, colour = colour, tooltip = tooltip)
        self.set_x_value(x)
        self.set_y_value(y)
        
    def set_x_value(self, x):
        self['x'] = x
    
    def set_y_value(self, y):
        self['y'] = y


##########################################
# line style class for charts with lines
class line_style(dict):
    def __init__(self, on=None, off=None, style='dash'):
        self.set_style(style)
        if on is not None: self.set_on(on)
        if off is not None: self.set_off(off)
        
    def set_style(self, style):
        self['style'] = style
        
    def set_on(self, on):
        self['on'] = on
    
    def set_off(self, off):
        self['off'] = off
 
##########################################
# label classes
class x_axis_labels(dict):
    def __init__(self, labels=None, steps=None, colour=None, size=None, rotate=None):
        if labels is not None: self.set_labels(labels)
        if steps is not None: self.set_steps(steps)
        if colour is not None: self.set_colour(colour)
        if size is not None: self.set_size(size)
        if rotate is not None: self.set_rotate(rotate)
        
    def set_labels(self, labels):
        self['labels'] = labels
    
    def set_steps(self, steps):
        self['steps'] = steps
            
    def set_colour(self, colour):
        self['colour'] = colour
            
    def set_size(self, size):
        self['size'] = size
    
    def set_rotate(self, rotate):
        self['rotate'] = rotate
    
class x_axis_label(dict):
    def __init__(self, text=None, colour=None, size=None, rotate=None):
        self.set_text(text)
        self.set_colour(colour)
        self.set_size(size)
        self.set_rotate(rotate)
        
    def set_text(self, text):
        self['text'] = text
            
    def set_colour(self, colour):
        self['colour'] = colour
            
    def set_size(self, size):
        self['size'] = size
            
    def set_rotate(self, rotate):
        self['rotate'] = rotate
        
        
        
##########################################
# Chart classes

# Line Charts
class Line(varieties):
    def __init__(self, alpha=None, colour=None, text=None, fontsize=None, values=None):
        varieties.__init__(self, 'line', alpha, colour, text, fontsize, values)
        
class Line_Dot(varieties):
    def __init__(self, alpha=None, colour=None, text=None, fontsize=None, values=None):
        varieties.__init__(self, 'line_dot', alpha, colour, text, fontsize, values)
        
class Line_Hollow(varieties):
    def __init__(self, alpha=None, colour=None, text=None, fontsize=None, values=None):
        varieties.__init__(self, 'line_hollow', alpha, colour, text, fontsize, values)



# Bar Charts
class Bar(varieties):
    def __init__(self, alpha=None, colour=None, text=None, fontsize=None, values=None):
        varieties.__init__(self, 'bar', alpha, colour, text, fontsize, values)

class Bar_Filled(varieties):
    def __init__(self, alpha=None, colour=None, text=None, fontsize=None, values=None, outline=None):
        varieties.__init__(self, 'bar_filled', alpha, colour, text, fontsize, values)
        if outline is not None:
            self['outline-colour'] = outline

class Bar_Glass(varieties):
    def __init__(self, alpha=None, colour=None, text=None, fontsize=None, values=None):
        varieties.__init__(self, 'bar_glass', alpha, colour, text, fontsize, values)

class Bar_3d(varieties):
    def __init__(self, alpha=None, colour=None, text=None, fontsize=None, values=None):
        varieties.__init__(self, 'bar_3d', alpha, colour, text, fontsize, values)

class Bar_Sketch(varieties):
    def __init__(self, alpha=None, colour=None, text=None, fontsize=None, values=None, outline=None):
        varieties.__init__(self, 'bar_sketch', alpha, colour, text, fontsize, values)
        if outline is not None:
            self['outline-colour'] = outline

class HBar(varieties):
    def __init__(self, alpha=None, colour=None, text=None, fontsize=None, values=None):
        varieties.__init__(self, 'hbar', alpha, colour, text, fontsize, values)


class Bar_Stack(varieties):
    def __init__(self, alpha=None, colour=None, text=None, fontsize=None, values=None, colours=None):
        varieties.__init__(self, 'bar_stack', alpha, colour, text, fontsize, values)
        if colours is not None:
            self['colours'] = colours
            
# Area Charts
class Area_Line(varieties):
    def __init__(self, alpha=None, colour=None, text=None, fontsize=None, values=None, fill=None, fill_alpha=None):
        varieties.__init__(self, 'area', alpha, colour, text, fontsize, values)
        if fill_alpha is not None:
            self['fill-alpha'] = fill_alpha
        if fill is not None:
            self['fill'] = fill

class Area_Hollow(varieties):
    def __init__(self, alpha=None, colour=None, text=None, fontsize=None, values=None, fill=None, fill_alpha=None):
        varieties.__init__(self, 'area_hollow', alpha, colour, text, fontsize, values)
        if fill_alpha is not None:
            self['fill-alpha'] = fill_alpha
        if fill is not None:
            self['fill'] = fill

# Pie Chart
class Pie(varieties):
    def __init__(self, alpha=None, colour=None, text=None, fontsize=None, values=None, start_angle=None, animate=None, colours=None, label_colour=None):
        varieties.__init__(self, 'pie', alpha, colour, text, fontsize, values)
        if start_angle is not None:
            self['start-angle'] = start_angle
        if animate is not None:
            self['animate'] = animate
        if colours is not None:
            self['colours'] = colours
        if label_colour is not None:
            self['label-colour'] = label_colour
            
# Scatter Charts
class Scatter(varieties):
	def __init__(self, alpha=None, colour=None, text=None, fontsize=None, values=None, colours=None):
		varieties.__init__(self, 'scatter', alpha, colour, text, fontsize, values)

class Scatter_Line(varieties):
    def __init__(self, alpha=None, colour=None, text=None, fontsize=None, values=None, colours=None):
           varieties.__init__(self, 'scatter_line', alpha, colour, text, fontsize, values)


# other classes
class Shape(varieties):
	def __init__(self, alpha=None, colour=None, text=None, fontsize=None, values=None, colours=None):
		varieties.__init__(self, 'shape', alpha, colour, text, fontsize, values)
