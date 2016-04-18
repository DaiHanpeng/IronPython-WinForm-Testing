#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, StatusBar
from System.Windows.Forms import ListBox, DockStyle
from System.Drawing import Size


class IForm(Form):

    def __init__(self):
        self.Text = "ListBox"
        
        lb = ListBox()
        lb.Parent = self

        lb.Items.Add("Jessica")
        lb.Items.Add("Rachel")
        lb.Items.Add("Angelina")
        lb.Items.Add("Amy")
        lb.Items.Add("Jennifer")
        lb.Items.Add("Scarlett")

        lb.Dock = DockStyle.Fill
        lb.SelectedIndexChanged += self.OnChanged

        self.sb = StatusBar()
        self.sb.Parent = self

        self.Size = Size(220, 220)
        self.CenterToScreen()
    

    def OnChanged(self, sender, event):
        self.sb.Text = sender.SelectedItem


Application.Run(IForm())