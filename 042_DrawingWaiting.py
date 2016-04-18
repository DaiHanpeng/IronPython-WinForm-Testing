#!/usr/bin/ipy

import clr

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, Timer
from System.Drawing import Size, Color, SolidBrush, Pen
from System.Drawing.Drawing2D import SmoothingMode, LineCap
from System.ComponentModel import Container


trs =  (
    ( 0, 35, 70, 100, 150, 180, 210, 250 ),
    ( 250, 0, 35, 70, 100, 150, 180, 210  ),
    ( 210, 250, 0, 35, 70, 100, 150, 180  ),
    ( 180, 210, 250, 0, 35, 70, 100, 150 ),
    ( 150, 180, 210, 250, 0, 35, 70, 100 ),
    ( 100, 150, 180, 210, 250, 0, 35, 70 ),
    ( 70, 100, 150, 180, 210, 250, 0, 35 ),
    ( 35, 70, 100, 150, 180, 210, 250, 0 )
)


class IForm(Form):

    def __init__(self):
        self.Text = 'Waiting'
        self.Size = Size(250, 150)

        self.Paint += self.OnPaint

        self.count = 0
        
        self.timer = Timer(Container())
        self.timer.Enabled = True
        self.timer.Interval = 80
        self.timer.Tick += self.OnTick

        self.CenterToScreen()

    
    def OnTick(self, sender, event):
        self.count = self.count + 1
        self.Refresh()

    def OnPaint(self, event):

        g = event.Graphics
        g.SmoothingMode = SmoothingMode.AntiAlias
        
        size = self.ClientSize
        g.TranslateTransform(size.Width/2, size.Height/2)
        
        for i in range(0, 8):
            color = Color.FromArgb(trs[self.count%8][i], 30, 30, 30)
            pen = Pen(color, 3)
            pen.StartCap = LineCap.Round
            pen.EndCap = LineCap.Round
            g.DrawLine(pen, 0, -10, 0, -40)
            g.RotateTransform(45)
            
        pen.Dispose()    
        g.Dispose()
        

Application.Run(IForm())