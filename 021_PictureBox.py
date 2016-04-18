#!/usr/bin/ipy

import sys
import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, PictureBox
from System.Drawing import Size, Point, Bitmap


class IForm(Form):

    def __init__(self):
        self.Text = 'PictureBox'
        
        try:
            castle = Bitmap('image.jpg') 
        except Exception, e:
            print 'Cannot read image file'
            print e.msg
            sys.exit(1)
 
        pb = PictureBox()
        pb.Parent = self
        pb.Size = Size(castle.Width, castle.Height)
        pb.Location = Point(2, 2)
        pb.Image = castle

        self.Size = Size(castle.Width, castle.Height)
        self.CenterToScreen()


Application.Run(IForm())