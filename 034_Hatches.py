#!/usr/bin/ipy

import clr

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Drawing import Size, Color
from System.Drawing.Drawing2D import HatchBrush, HatchStyle

class IForm(Form):

    def __init__(self):
        self.Text = 'Hatches'
        self.Size = Size(360, 300)
        
        self.Paint += self.OnPaint
        
        self.CenterToScreen()


    def OnPaint(self, event):

        g = event.Graphics

        hb = HatchBrush(HatchStyle.Cross, Color.Black, self.BackColor)
        g.FillRectangle(hb, 10, 15, 90, 60)

        hb = HatchBrush(HatchStyle.Percent05, Color.Black, self.BackColor)
        g.FillRectangle(hb, 130, 15, 90, 60)

        hb = HatchBrush(HatchStyle.SolidDiamond, Color.Black, self.BackColor)
        g.FillRectangle(hb, 250, 15, 90, 60)

        hb = HatchBrush(HatchStyle.DiagonalBrick, Color.Black, self.BackColor)
        g.FillRectangle(hb, 10, 105, 90, 60)

        hb = HatchBrush(HatchStyle.Divot, Color.Black, self.BackColor)
        g.FillRectangle(hb, 130, 105, 90, 60)

        hb = HatchBrush(HatchStyle.Wave, Color.Black, self.BackColor)
        g.FillRectangle(hb, 250, 105, 90, 60)

        hb = HatchBrush(HatchStyle.ZigZag, Color.Black, self.BackColor)
        g.FillRectangle(hb, 10, 195, 90, 60)

        hb = HatchBrush(HatchStyle.Sphere, Color.Black, self.BackColor)
        g.FillRectangle(hb, 130, 195, 90, 60)

        hb = HatchBrush(HatchStyle.Shingle, Color.Black, self.BackColor)
        g.FillRectangle(hb, 250, 195, 90, 60)

        hb.Dispose()
        g.Dispose()


Application.Run(IForm())