#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Windows.Forms import MenuStrip, ToolStripMenuItem
from System.Drawing import Size

class IForm(Form):

    def __init__(self):
        self.Text = 'Simple Menu'
        self.Size = Size(380, 200)

        ms = MenuStrip()
        ms.Parent = self

        filem = ToolStripMenuItem("&File")
        exit = ToolStripMenuItem("&Exit", None,
            self.OnExit)

        importm = ToolStripMenuItem()
        importm.Text = "Import"

        filem.DropDownItems.Add(importm)

        temp = ToolStripMenuItem()
        temp.Text = "Import newsfeed list..."
        importm.DropDownItems.Add(temp)

        temp = ToolStripMenuItem()
        temp.Text = "Import bookmarks..."
        importm.DropDownItems.Add(temp)

        temp = ToolStripMenuItem()
        temp.Text = "Import mail..."
        importm.DropDownItems.Add(temp)

        filem.DropDownItems.Add(exit)

        ms.Items.Add(filem)
        self.MainMenuStrip = ms
        
        self.CenterToScreen()
    

    def OnExit(self, sender, event):
        self.Close()
    

Application.Run(IForm())