#!/usr/bin/ipy

import clr

clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Windows.Forms import Button, ToolTip
from System.Drawing import Point, Size

class IForm(Form):

    def __init__(self):
        self.Text = 'Tooltips'
        self.CenterToScreen()
        self.Size = Size(200, 150)

        tooltip = ToolTip()
        tooltip.SetToolTip(self, "This is a Form")

        button = Button()
        button.Parent = self
        button.Text = "Button"
        button.Location = Point(50, 70)

        tooltip.SetToolTip(button, "This is a Button")


Application.Run(IForm())