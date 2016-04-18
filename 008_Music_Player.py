#!/usr/bin/ipy

import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")


from System.Windows.Forms import Application, Form, Button, Panel
from System.Windows.Forms import DockStyle, AnchorStyles, StatusBar
from System.Windows.Forms import TrackBar, MainMenu, MenuItem
from System.Windows.Forms import FlatStyle, TickStyle, Shortcut
from System.Drawing import Size, Point, Bitmap, Color


class IForm(Form):

    def __init__(self):

        self.Text = 'Player'        
        self.Size = Size(350, 280)

        mainMenu = MainMenu()
        filem = mainMenu.MenuItems.Add("&File")
        playm = mainMenu.MenuItems.Add("&Play")
        view = mainMenu.MenuItems.Add("&View")

        tools = mainMenu.MenuItems.Add("&Tools")
        favourites = mainMenu.MenuItems.Add("&Favourites")
        help = mainMenu.MenuItems.Add("&Help")
        filem.MenuItems.Add(MenuItem("E&xit",
                 self.OnExit, Shortcut.CtrlX))

        self.Menu = mainMenu

        panel = Panel()
        panel.Parent = self
        panel.BackColor = Color.Black
        panel.Dock = DockStyle.Fill
       
        buttonPanel = Panel()
        buttonPanel.Parent = self
        buttonPanel.Height = 40
        buttonPanel.Dock = DockStyle.Bottom

        pause = Button()
        pause.FlatStyle = FlatStyle.Popup
        pause.Parent = buttonPanel
        pause.Location = Point(5, 10)
        pause.Size = Size(25, 25)
        pause.Image = Bitmap("pause.png")

        play = Button()
        play.FlatStyle = FlatStyle.Popup
        play.Parent = buttonPanel
        play.Location = Point(35, 10)
        play.Size = Size(25, 25)
        play.Image = Bitmap("play.png")

        forward = Button()
        forward.FlatStyle = FlatStyle.Popup
        forward.Parent = buttonPanel
        forward.Location = Point(80, 10)
        forward.Size = Size(25, 25)
        forward.Image = Bitmap("forward.png")

        backward = Button()
        backward.FlatStyle = FlatStyle.Popup
        backward.Parent = buttonPanel
        backward.Location = Point(110, 10)
        backward.Size = Size(25, 25)
        backward.Image = Bitmap("backward.png")

        tb = TrackBar()
        tb.Parent = buttonPanel
        tb.TickStyle = TickStyle.None
        tb.Size = Size(150, 25)
        tb.Location = Point(200, 10)
        tb.Anchor = AnchorStyles.Right

        audio = Button()
        audio.FlatStyle = FlatStyle.Popup
        audio.Parent = buttonPanel
        audio.Size = Size(25, 25)
        audio.Image = Bitmap("audio.png")
        audio.Location = Point(170, 10)
        audio.Anchor = AnchorStyles.Right

        sb = StatusBar()
        sb.Parent = self
        sb.Text = "Ready"

        self.CenterToScreen()
    
    def OnExit(self, sender, event):
        self.Close()


Application.Run(IForm())