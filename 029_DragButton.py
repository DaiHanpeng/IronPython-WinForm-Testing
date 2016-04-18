#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, Button
from System.Drawing import Size, Point

class IForm(Form):

    def __init__(self):
        self.Text = 'Drag & Drop'

        button = Button()
        button.Parent = self
        button.Text = 'Button'
        button.MouseDown += self.OnMousDown
        button.MouseUp += self.OnMousUp
        button.MouseMove += self.OnMousMove

        button.Location = Point(20, 20)

        self.isDragging = False
        self.CenterToScreen()

    def OnMousDown(self, sender,  event):
  
        self.isDragging = True
        self.oldX = event.X
        self.oldY = event.Y

    def OnMousMove(self, sender, event):
  
        if self.isDragging: 
            sender.Top = sender.Top + (event.Y - self.oldY)
            sender.Left = sender.Left + (event.X - self.oldX)
    

    def OnMousUp(self, sender,  event):
        self.isDragging = False
  

Application.Run(IForm())