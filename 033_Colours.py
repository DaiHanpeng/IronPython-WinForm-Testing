#!/usr/bin/ipy

import clr

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, ControlStyles
from System.Drawing import Size, Brushes

class IForm(Form):

    def __init__(self):
        self.Text = 'Colors'       
        self.Size = Size(360, 300)
        self.Paint += self.OnPaint
        
        self.CenterToScreen()


    def OnPaint(self, event):

        g = event.Graphics

        g.FillRectangle(Brushes.Sienna, 10, 15, 90, 60)
        g.FillRectangle(Brushes.Green, 130, 15, 90, 60)
        g.FillRectangle(Brushes.Maroon, 250, 15, 90, 60)
        g.FillRectangle(Brushes.Chocolate, 10, 105, 90, 60)
        g.FillRectangle(Brushes.Gray, 130, 105, 90, 60)
        g.FillRectangle(Brushes.Coral, 250, 105, 90, 60)
        g.FillRectangle(Brushes.Brown, 10, 195, 90, 60)
        g.FillRectangle(Brushes.Teal, 130, 195, 90, 60)
        g.FillRectangle(Brushes.Goldenrod, 250, 195, 90, 60)
        
        g.Dispose()


Application.Run(IForm())