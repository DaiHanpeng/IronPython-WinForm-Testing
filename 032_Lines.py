#!/usr/bin/ipy

import clr

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Drawing import Size, Pen, Color
from System.Drawing.Drawing2D import DashStyle

class IForm(Form):

    def __init__(self):
        self.Text = 'Lines'
        self.Size = Size(280, 270)
        self.Paint += self.OnPaint

        self.CenterToScreen()


    def OnPaint(self, event):

        g = event.Graphics

        pen = Pen(Color.Black, 1)
        pen.DashStyle = DashStyle.Dot
        
        g.DrawLine(pen, 20, 40, 250, 40)

        pen.DashStyle = DashStyle.DashDot
        g.DrawLine(pen, 20, 80, 250, 80)

        pen.DashStyle = DashStyle.Dash
        g.DrawLine(pen, 20, 120, 250, 120)

        pen.DashStyle = DashStyle.DashDotDot
        g.DrawLine(pen, 20, 160, 250, 160)

        pen.DashPattern = (6, 8, 1, 1, 1, 1, 1, 1)
        g.DrawLine(pen, 20, 200, 250, 200)
        
        pen.Dispose()
        g.Dispose()


Application.Run(IForm())