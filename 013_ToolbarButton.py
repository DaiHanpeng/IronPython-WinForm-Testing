#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")
clr.AddReference("System")

from System.Windows.Forms import Application, Form
from System.Windows.Forms import ToolBar, ToolBarButton, ImageList
from System.Drawing import Size, Icon



class IForm(Form):

    def __init__(self):
        self.Text = 'Simple ToolBar'
        self.Size = Size(250, 200)

        toolBar = ToolBar()
        toolBarIcons = ImageList()
        save = ToolBarButton()
        exit = ToolBarButton()

        save.ImageIndex = 0
        save.Tag = "Save"
        exit.ImageIndex = 1
        exit.Tag = "Exit"

        toolBar.ImageList = toolBarIcons
        toolBar.ShowToolTips = True
        toolBar.Buttons.AddRange((save, exit))
        toolBar.ButtonClick += self.OnClicked
    
        #toolBarIcons.ImageSize = Size(16, 16)
        #toolBarIcons.Images.Add(Icon("new.png"))
        #toolBarIcons.Images.Add(Icon("exit.png"))

        self.Controls.Add(toolBar)
        self.CenterToScreen()
    
    def OnClicked(self, sender, event):
        if event.Button.Tag == "Exit":
            self.Close()
    

Application.Run(IForm())