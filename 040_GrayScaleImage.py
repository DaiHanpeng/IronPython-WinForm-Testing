#!/usr/bin/ipy

import clr
import sys

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Drawing import Size, Rectangle
from System.Drawing import Bitmap, Color

class IForm(Form):

    def __init__(self):
        self.Text = 'Grayscale'
        self.Size = Size(290, 150)

        self.Paint += self.OnPaint

        self.rotunda = self.loadImage()
        self.gs = self.grayScale(self.rotunda.Clone())

        self.CenterToScreen()

    def loadImage(self):
        try:
            rotunda = Bitmap("image.jpg")
            return rotunda
        except Exception, e:
            print e.msg
            sys.exit(1)

    def grayScale(self, image):
        
        w = image.Width
        h = image.Height

        for i in range(w):
            for j in range(h):
                c = image.GetPixel(i, j)
                lum = 0.299*c.R + 0.587*c.G + 0.114*c.B
                image.SetPixel(i, j, Color.FromArgb(lum, lum, lum))
          
        return image


    def OnPaint(self, event):

        g = event.Graphics

        r1 = Rectangle(15, 15, self.rotunda.Width, self.rotunda.Height)
        g.DrawImage(self.rotunda, r1)

        r2 = Rectangle(150, 15, self.gs.Width, self.gs.Height)
        g.DrawImage(self.gs, r2)
        
        g.Dispose()

Application.Run(IForm())