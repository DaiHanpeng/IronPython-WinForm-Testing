#!/usr/bin/ipy

import clr

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Drawing import Size, Color, Point
from System.Drawing.Drawing2D import LinearGradientBrush

class IForm(Form):

    def __init__(self):
        self.Text = 'Gradients'
        self.Size = Size(350, 350)
        self.Paint += self.OnPaint

        self.CenterToScreen()

    def OnPaint(self, event):

        g = event.Graphics

        pt1 = Point(5, 5)
        pt2 = Point(25, 25)
        lg =  LinearGradientBrush(pt1, pt2, Color.Red, Color.Black)
        g.FillRectangle(lg, 20, 20, 300, 40)

        pt1 = Point(5, 25)
        pt2 = Point(20, 2)
        lg = LinearGradientBrush(pt1, pt2, Color.Yellow, Color.Black)
        g.FillRectangle(lg, 20, 80, 300, 40)

        pt1 = Point(5, 25)
        pt2 = Point(2, 2)
        lg = LinearGradientBrush(pt1, pt2, Color.Green, Color.Black)
        g.FillRectangle(lg, 20, 140, 300, 40)

        pt1 = Point(25, 25)
        pt2 = Point(15, 25)
        lg =  LinearGradientBrush(pt1, pt2, Color.Blue, Color.Black)
        g.FillRectangle(lg, 20, 200, 300, 40)

        pt1 = Point(0, 10)
        pt2 = Point(0, 20)
        lg = LinearGradientBrush(pt1, pt2, Color.Orange, Color.Black)
        g.FillRectangle(lg, 20, 260, 300, 40)

        lg.Dispose()
        g.Dispose()


Application.Run(IForm())