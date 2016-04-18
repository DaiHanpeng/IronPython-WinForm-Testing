#!/usr/bin/ipy

import clr

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Drawing import Size, Color, SolidBrush, Pen

class IForm(Form):

    def __init__(self):
        self.Text = 'Donut'
        self.Size = Size(350, 300)

        self.Paint += self.OnPaint
        self.CenterToScreen()

    def OnPaint(self, event):

        g = event.Graphics
        pen = Pen(Color.Gray, 1)
        
        size = self.ClientSize
        g.TranslateTransform(size.Width/2, size.Height/2)
        g.DrawEllipse(pen, -125, -125, 250, 250)
        
        for i in range(0, 36):
            g.DrawEllipse(pen, 0, 0, 120, 50)
            g.RotateTransform(10)
            
        g.Dispose()

Application.Run(IForm())