#!/usr/bin/ipy

import clr

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Drawing import Size, Color, SolidBrush

class IForm(Form):

    def __init__(self):
        self.Text = 'Transparent rectangles'
        self.Size = Size(590, 110)

        self.Paint += self.OnPaint
        
        self.CenterToScreen()


    def OnPaint(self, event):

        g = event.Graphics

        for i in range(1, 11):
            color = Color.FromArgb(i*25, 0, 0, 255)
            brush = SolidBrush(color)
            g.FillRectangle(brush, 50*i, 20, 40, 40)
            

Application.Run(IForm())