#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, MenuStrip
from System.Windows.Forms import ToolStripMenuItem, ToolStripSeparator
from System.Drawing import Size, Image

class IForm(Form):

    def __init__(self):
        self.Text = 'MenuStrip'
        self.Size = Size(250, 200)

        menuStrip = MenuStrip()
   
        titem1 = ToolStripMenuItem("File")
        menuStrip.Items.Add(titem1)
  
        titem2 = ToolStripMenuItem("Tools")
        menuStrip.Items.Add(titem2)
  
        subm1 = ToolStripMenuItem("New")
        subm1.Image = Image.FromFile("new.png")
        titem1.DropDownItems.Add(subm1)
   
        subm2 = ToolStripMenuItem("Open") 
        subm2.Image = Image.FromFile("open.png")
        titem1.DropDownItems.Add(subm2)
  
        titem1.DropDownItems.Add(ToolStripSeparator())

        subm3 = ToolStripMenuItem("Exit")
        subm3.Image = Image.FromFile("exit.png")
        titem1.DropDownItems.Add(subm3)  
  
        subm3.Click += self.OnExit
        self.Controls.Add(menuStrip)
        self.MainMenuStrip = menuStrip 
        
        self.CenterToScreen()
    

    def OnExit(self, sender, event):
        self.Close()
    

Application.Run(IForm())