#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, StatusBar
from System.Windows.Forms import Button, TreeView, TreeNode
from System.Windows.Forms import DockStyle, AnchorStyles
from System.Drawing import Size, Point
from System.IO import Directory, DirectoryInfo


HOME_DIR = 'D:\\'

class IForm(Form):

    def __init__(self):
        self.Text = 'Directories'
        self.Size = Size(400, 400)
        
        self.tv = TreeView()

        self.SuspendLayout()

        self.tv.Parent = self
        self.tv.Location = Point(10,10)
        self.tv.Size = Size(self.ClientSize.Width - 20, self.Height - 200)
        self.tv.Anchor = AnchorStyles.Top | AnchorStyles.Left | AnchorStyles.Right 


        self.tv.FullRowSelect = False
        self.tv.ShowLines = True
        self.tv.ShowPlusMinus = True
        self.tv.Scrollable = True  
        self.tv.AfterSelect += self.AfterSelect

        expand = Button()
        expand.Parent = self
        expand.Location = Point(20, self.tv.Bottom + 20)
        expand.Text = 'Expand'
        expand.Anchor = AnchorStyles.Left | AnchorStyles.Top
        expand.Click += self.OnExpand

        expandAll = Button()
        expandAll.Parent = self
        expandAll.Location = Point(20, expand.Bottom + 5)
        expandAll.Text = 'Expand All'
        expandAll.Anchor = AnchorStyles.Left | AnchorStyles.Top
        expandAll.Click += self.OnExpandAll

        collapse = Button()
        collapse.Parent = self
        collapse.Location = Point(expandAll.Right + 5, expand.Top)
        collapse.Text = 'Collapse'
        collapse.Anchor = AnchorStyles.Left | AnchorStyles.Top
        collapse.Click += self.OnCollapse

        collapseAll = Button()
        collapseAll.Parent = self
        collapseAll.Location = Point(collapse.Left, collapse.Bottom + 5)
        collapseAll.Text = 'Collapse All'
        collapseAll.Anchor = AnchorStyles.Left | AnchorStyles.Top
        collapseAll.Click += self.OnCollapseAll

        self.sb = StatusBar()
        self.sb.Parent = self

        self.ShowDirectories(self.tv.Nodes, HOME_DIR)

        self.ResumeLayout()

        self.CenterToScreen()
    
    def AfterSelect(self, sender, event):
  
        self.sb.Text = event.Node.Text
        
    def ShowDirectories(self, trvNode, path):
    
        dirInfo = DirectoryInfo(path)
        if (dirInfo != None):
      
          subDirs = dirInfo.GetDirectories()
          tr = TreeNode(dirInfo.Name)

          if (subDirs.Length > 0):
          
              for dr in subDirs: 
                  if not dr.Name.StartsWith("."):
                      self.ShowDirectories(tr.Nodes, dr.FullName)
                        
          trvNode.Add(tr)    

      
    def OnExpand(self, sender, event):
        self.tv.SelectedNode.Expand()
  

    def OnExpandAll(self, sender, event):
        self.tv.ExpandAll()
  

    def OnCollapse(self, sender, event):
        self.tv.SelectedNode.Collapse()
  

    def OnCollapseAll(self, sender, event):
        self.tv.CollapseAll()


Application.Run(IForm())