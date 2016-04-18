#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Windows.Forms import ComboBox, Label
from System.Drawing import Size, Point


class IForm(Form):

    def __init__(self):

        self.Text = "ComboBox"
        self.Size = Size(240, 240)

        cb = ComboBox()
        cb.Parent = self
        cb.Location = Point(50, 30)

        cb.Items.AddRange(("Ubuntu",
            "Mandriva",
            "Red Hat",
            "Fedora",
            "Gentoo"))

        cb.SelectionChangeCommitted += self.OnChanged

        self.label = Label()
        self.label.Location = Point(50, 140)
        self.label.Parent = self
        self.label.Text = "..."


        self.CenterToScreen()

    def OnChanged(self, sender, event):
         self.label.Text = sender.Text
    
    
Application.Run(IForm())