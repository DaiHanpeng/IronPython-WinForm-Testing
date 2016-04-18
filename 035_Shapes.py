#!/usr/bin/ipy

import clr

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Drawing import Size, Rectangle, Brushes, Pens, Point
from System.Drawing.Drawing2D import SmoothingMode
from System import Array

class IForm(Form):

    def __init__(self):
        self.Text = 'Basic shapes'
        self.Size = Size(420, 280)
        
        self.Paint += self.OnPaint
        
        self.CenterToScreen()

    def OnPaint(self, event):

        g = event.Graphics
        g.SmoothingMode = SmoothingMode.AntiAlias
        
        g.FillRectangle(Brushes.Gray, 20, 20, 120, 80)
        g.FillRectangle(Brushes.Gray, 180, 20, 80, 80)
        
        g.FillEllipse(Brushes.Gray, 30, 120, 100, 100)
        g.FillEllipse(Brushes.Gray, 160, 130, 100, 70)
        
        p1 = Point(300, 40)
        p2 = Point(340, 15)
        p3 = Point(380, 40)
        p4 = Point(380, 80)
        p5 = Point(340, 105)
        p6 = Point(300, 80)
 
        g.FillPolygon(Brushes.Gray, Array[Point]([p1, p2, p3, p4, p5, p6]))
        g.FillPie(Brushes.Gray, Rectangle(290, 130, 90, 90), 0, 315)

        g.Dispose()

Application.Run(IForm())