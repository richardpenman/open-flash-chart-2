This module is based on the Python module included with [OpenFlashChart 2](http://teethgrinder.co.uk/open-flash-chart-2/). I found this module useful but quite buggy - for example values of zero could not be plotted because the module used `if value` rather than `if value is not None`. This module has fixes for what I needed to get it working.