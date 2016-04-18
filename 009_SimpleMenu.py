#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form
from System.Windows.Forms import Keys, MenuStrip, ToolStripMenuItem
from System.Drawing import Size

class IForm(Form):

    def __init__(self):
        self.Text = 'Simple Menu'
        self.Size = Size(250, 200)

        ms = MenuStrip()
        ms.Parent = self
        
        filem = ToolStripMenuItem("&File")         
        exit = ToolStripMenuItem("&Exit", None,
            self.OnExit)  
        exit.ShortcutKeys = Keys.Control | Keys.X
        filem.DropDownItems.Add(exit)

        ms.Items.Add(filem)
        self.MainMenuStrip = ms
        
        self.CenterToScreen()
    

    def OnExit(self, sender, event):
        self.Close()
    

Application.Run(IForm())