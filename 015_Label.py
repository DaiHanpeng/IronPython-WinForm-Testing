#!/usr/bin/ipy

import sys
import clr
clr.AddReference("System.Windows.Forms")
clr.AddReference("System.Drawing")

from System.Windows.Forms import Application, Form, Label
from System.Drawing import Size, Point, Font


text = """Meet you downstairs in the bar and heard
Your rolled up sleeves and your skull t-shirt
You say why did you do it with him today?
And sniffed me out like I was tanqueray

Cause you're my fella, my guy
Hand me your stella and fly
By the time I'm out the door
You tear me down like roger moore

I cheated myself
Like I knew I would
I told ya, I was trouble
You know that I'm no good

Upstairs in bed, with my ex boy
He's in a place, but I cant get joy
Thinking of you in the final throws, this is when my buzzer goes"""


class IForm(Form):

    def __init__(self):

        self.Text = "You know I'm No Good"

        font = Font("Serif", 10)

        lyrics = Label()
        lyrics.Parent = self
        lyrics.Text = text
        lyrics.Font = font
        lyrics.Location = Point(10, 10)
        lyrics.Size = Size(390, 390)
        
        self.Size = Size(400,400)
        self.CenterToScreen()


Application.Run(IForm())