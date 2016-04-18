#!/usr/bin/ipy

import sys
import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, PictureBox, PictureBoxSizeMode
from System.Windows.Forms import Cursors
from System.Drawing import Size, Point, Rectangle, Brushes, Bitmap

class IForm(Form):

    def __init__(self):

        self.ClientSize = Size(350, 250)
        self.Text = "Dragging Images"
        self.Paint += self.OnPaint
    
        self.isDragging = False
        self.dropRect = Rectangle(10, 10, 200, 160)
        self.brush = Brushes.Gray
        picBox = PictureBox()

        self.loadImage()

        self.isDragging = False
        self.CenterToScreen()

        picBox.Parent = self
        picBox.Location = Point(100, 50)
        picBox.Size = Size(self.image.Width, self.image.Height)
        picBox.Image = self.image
        picBox.MouseDown += self.OnMousDown
        picBox.MouseUp += self.OnMousUp
        picBox.MouseMove += self.OnMousMove
        picBox.Cursor = Cursors.Hand


    def loadImage(self):
        try:
            self.image = Bitmap("image.jpg")
        except Exception, e: 
            print "Error reading image"
            print e.msg
            sys.exit(1)


    def OnMousMove(self, sender, event): 
        if self.isDragging:
            sender.Top = sender.Top + (event.Y - self.oldY)
            sender.Left = sender.Left + (event.X - self.oldX)


    def OnMousUp(self, sender, event):
        self.isDragging = False

        if self.dropRect.Contains(sender.Bounds):
            self.brush = Brushes.Gold
        else: 
            self.brush = Brushes.Gray

        self.Refresh()


    def OnMousDown(self, sender, event):
        self.isDragging = True
        self.oldX = event.X
        self.oldY = event.Y
 

    def OnPaint(self, event): 
        g = event.Graphics
        g.FillRectangle(self.brush, self.dropRect)
 
  
Application.Run(IForm()) 