#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, StatusBar
from System.Windows.Forms import RadioButton, GroupBox
from System.Drawing import Size, Point


class IForm(Form):

    def __init__(self):

        self.Text = "RadioButton"
        self.Size = Size(240, 240)

        gb = GroupBox()
        gb.Text = "Sex"
        gb.Size = Size(120, 110)
        gb.Location = Point(20, 20)
        gb.Parent = self

        male = RadioButton()
        male.Text = "Male"
        male.Parent = gb
        male.Location = Point(10, 30)
        male.CheckedChanged += self.OnChanged


        female = RadioButton()
        female.Text = "Female"
        female.Parent = gb
        female.Location = Point(10, 60)
        female.CheckedChanged += self.OnChanged

        self.statusbar = StatusBar()
        self.statusbar.Parent = self

        self.CenterToScreen()

    def OnChanged(self, sender, event):
        if sender.Checked:
            self.statusbar.Text = sender.Text
    
    
Application.Run(IForm())