#!/usr/bin/ipy

import clr

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Drawing import Size, Font, SolidBrush
from System.Drawing import PointF, Color

class IForm(Form):

    def __init__(self):
        self.Text = "You know I'm No Good"
        self.Size = Size(380, 450)
        
        self.Paint += self.OnPaint
        
        self.CenterToScreen()


    def OnPaint(self, event):

        g = event.Graphics

        ft = Font("Purisa", 10)
        br = SolidBrush(Color.Black)

        pt = PointF(20.0, 20.0)
        g.DrawString("Meet you downstairs in the bar and heard", ft, br, pt)

        pt = PointF(20.0, 50.0)
        g.DrawString("Your rolled up sleeves and your skull t-shirt", ft, br, pt)

        pt = PointF(20.0, 80.0)
        g.DrawString("You say why did you do it with him today?", ft, br, pt)

        pt = PointF(20.0, 110.0)
        g.DrawString("And sniffed me out like I was tanqueray", ft, br, pt)

        pt = PointF(20.0, 160.0)
        g.DrawString("Cause you're my fella, my guy", ft, br, pt)

        pt = PointF(20.0, 190.0)
        g.DrawString("Hand me your stella and fly", ft, br, pt)

        pt = PointF(20.0, 220.0)
        g.DrawString("By the time I'm out the door", ft, br, pt)

        pt = PointF(20.0, 250.0)
        g.DrawString("You tear me down like roger moore", ft, br, pt)

        pt = PointF(20.0, 300.0)       
        g.DrawString("I cheated myself", ft, br, pt)

        pt = PointF(20.0, 330.0)   
        g.DrawString("Like I knew I would", ft, br, pt)

        pt = PointF(20.0, 360.0)        
        g.DrawString("I told ya, I was trouble", ft, br, pt)

        pt = PointF(20.0, 390.0)       
        g.DrawString("You know that I'm no good", ft, br, pt)
        
        g.Dispose()


Application.Run(IForm())