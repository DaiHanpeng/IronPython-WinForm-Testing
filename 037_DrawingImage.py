#!/usr/bin/ipy

import sys
import clr

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Drawing import Size, Bitmap, Rectangle


class IForm(Form):

    def __init__(self):
        self.Text = 'Red Rock'
        self.Size = Size(200, 150)

        self.loadImage()
        self.Size = Size(self.castle.Width, self.castle.Height)

        self.Paint += self.OnPaint
        self.CenterToScreen()

    def loadImage(self):
        try:
            self.castle = Bitmap("image.jpg")
        except Exception, e:
            print e.msg
            sys.exit(1)
    

    def OnPaint(self, event):
    
        g = event.Graphics
        r = Rectangle(1, 1, self.castle.Width, self.castle.Height)
        g.DrawImage(self.castle, r)
        
        g.Dispose()
        


Application.Run(IForm())