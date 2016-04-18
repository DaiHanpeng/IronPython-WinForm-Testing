#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, StatusBar
from System.Windows.Forms import TreeView, TreeNode, DockStyle
from System.Drawing import Size


class IForm(Form):

    def __init__(self):
        self.Text = 'TreeView'
        
        tv = TreeView()

        root = TreeNode()
        root.Text = 'Languages'

        child1 = TreeNode()
        child1.Text = 'Python'

        child2 = TreeNode()
        child2.Text = 'Ruby'

        child3 = TreeNode()
        child3.Text = 'Java'

        root.Nodes.AddRange((child1, child2, child3))

        tv.Parent = self
        tv.Nodes.Add(root)
        tv.Dock = DockStyle.Fill
        tv.AfterSelect += self.AfterSelect

        self.sb = StatusBar()
        self.sb.Parent = self

        self.Size = Size(220, 220)
        self.CenterToScreen()
    

    def AfterSelect(self, sender, event):    
        self.sb.Text = event.Node.Text
    

Application.Run(IForm())