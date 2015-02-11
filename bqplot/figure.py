# Copyright 2015 Bloomberg Finance L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

r"""

======
Figure
======

.. currentmodule:: bqplot.figure

.. autosummary::
   :toctree: generate/

   Figure
"""

from IPython.html.widgets import DOMWidget, register
from IPython.utils.traitlets import (Unicode, Instance, List, Dict,
                                     CFloat, Bool, Enum, Float)

from .scales import Scale, LinearScale
from .interacts import Interaction


@register('bqplot.Figure')
class Figure(DOMWidget):

    """Main canvas for drawing a chart.

    The Figure object holds the list of Marks and Axes. It also holds an
    optional Interaction object that is responsible for figure-level mouse
    interactions, the "interaction layer".

    Besides, the Figure object has two reference scales, for positioning items
    in an absolute fashion in the figure canvas.

    Data Attributes
    ---------------
    Data attributes are decorated with the following values:

    title: string (default: "")
        title of the figure
    axes: List (default: [])
        list containing the instances of the axes for the figure
    marks: List (default: [])
        list containing the marks which are to be appended to the figure
    interaction: any (default: )
        optional interaction layer for the figure
    scale_x: Scale
        Scale representing the x values of the figure
    scale_y: Scale
        Scale representing the y values of the figure

    Layout Attributes
    -----------------
    min_width: CFloat (default: 800.0)
        minimum width of the figure including the figure margins
    min_height: CFloat (default: 600.0)
        minimum height of the figure including the figure margins
    preserve_aspect: bool (default: False)
        Determines whether the aspect ratio for the figure specified by
        min_width and min_height is preserved during resizing. This does not
        guarantee that the data coordinates will have any specific aspect ratio.
    fig_margin: dict (default: {top=60, bottom=60, left=60, right=60})
        Dictionary containing the top, bottom, left and right margins. The user
        is responsible for making sure that the width and height are greater
        than the sum of the margins.
    padding_x: float (default: 0.0)
        Padding to be applied in pixels in the horizontal direction of the
        figure around the data points
    padding_y: float (default: 0.025)
        Padding to be applied in pixels in the vertical direction of the figure
        around the data points
    legend_location:  {'top-right', 'top', 'top-left', 'left',
                       'bottom-left', 'bottom', 'bottom-right', 'right'}
        location of the legend relative to the center of the figure
    """
    _view_name = Unicode('bqplot.Figure', sync=True)

    title = Unicode(sync=True,
                    exposed=True, display_index=1, display_name='Title')
    axes = List(allow_none=False, sync=True)
    marks = List(allow_none=False, sync=True)
    interaction = Instance(Interaction, allow_none=True, sync=True)
    scale_x = Instance(Scale, sync=True)
    scale_y = Instance(Scale, sync=True)

    min_width = CFloat(800.0, sync=True)
    min_height = CFloat(600.0, sync=True)
    preserve_aspect = Bool(False, sync=True, exposed=True, display_index=3,
                           display_name='Preserve aspect ratio')

    fig_margin = Dict(dict(top=60, bottom=60, left=60, right=60),
                      sync=True)
    padding_x = Float(0.0, sync=True)
    padding_y = Float(0.025, sync=True)
    legend_location = Enum(['top-right', 'top', 'top-left', 'left',
                           'bottom-left', 'bottom', 'bottom-right', 'right'],
                           default_value='top-right', allow_none=False,
                           sync=True, exposed=True, display_index=2,
                           display_name='Legend position')

    def _scale_x_default(self):
        return LinearScale(min=0, max=1)

    def _scale_y_default(self):
        return LinearScale(min=0, max=1)
