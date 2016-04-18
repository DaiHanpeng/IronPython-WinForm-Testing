#!/usr/bin/ipy

import clr

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, Button
from System.Drawing import Size, Point

class IForm(Form):

    def __init__(self):
        self.Text = 'Button'
        self.CenterToScreen()
        self.Size = Size(200, 150)

        btn = Button()
        btn.Parent = self
        btn.Text = "Quit"
        btn.Location = Point(50, 50)
        btn.Click += self.OnClick
        btn.MouseEnter += self.OnEnter


    def OnClick(self, sender, args):
        self.Close()

    def OnEnter(self, sender, args):
        print "button entered"


Application.Run(IForm())