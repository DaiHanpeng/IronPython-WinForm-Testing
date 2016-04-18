#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, CheckBox
from System.Drawing import Size, Point



class IForm(Form):

    def __init__(self):

        self.Text = "CheckBox"
        self.Size = Size(220, 170)

        cb = CheckBox()
        cb.Parent = self
        cb.Location = Point(30, 30)
        cb.Text = "Show Title"
        cb.Checked = True

        cb.CheckedChanged += self.OnChanged


        self.CenterToScreen()

    def OnChanged(self, sender, event):
        if sender.Checked:
            self.Text = "CheckBox"
        else:
            self.Text = ""
        
    
Application.Run(IForm())