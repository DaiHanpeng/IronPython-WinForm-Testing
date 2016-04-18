#!/usr/bin/ipy

import sys
import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, PictureBox
from System.Windows.Forms import TrackBar, TickStyle
from System.Drawing import Size, Point, Bitmap


class IForm(Form):

    def __init__(self):
        self.Text = 'TrackBar'
        self.Size = Size(260, 190)
      

        tb = TrackBar()
        tb.Parent = self
        tb.Size = Size(150, 30)
        tb.Location = Point(30, 50)
        tb.TickStyle = TickStyle.None
        tb.SetRange(0, 100)

        tb.ValueChanged += self.OnChanged

        self.LoadImages()

        self.pb = PictureBox()
        self.pb.Parent = self
        self.pb.Location = Point(210, 50)
        self.pb.Image = self.mutep
        
        self.CenterToScreen()


    def LoadImages(self):
        try:
            self.mutep = Bitmap("mute.png")
            self.minp = Bitmap("min.png")
            self.medp = Bitmap("med.png")
            self.maxp = Bitmap("max.png")
        except Exception, e:
            print "Error reading images"
            print e.msg
            sys.exit(1)
    


    def OnChanged(self, sender, event): 
        val = sender.Value

        if val == 0: 
            self.pb.Image = self.mutep
        elif val > 0 and val <= 30:
            self.pb.Image = self.minp
        elif val > 30 and val < 80:
            self.pb.Image = self.medp
        else: self.pb.Image = self.maxp



Application.Run(IForm())