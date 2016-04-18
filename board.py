import clr
clr.AddReference("System.Drawing")
clr.AddReference("System")


from System.Windows.Forms import UserControl, Keys, Timer
from System.Drawing import Size, Color, Bitmap, Brushes, RectangleF
from System.Drawing import Font, StringAlignment, StringFormat, PointF
from System import Random
from System.ComponentModel import Container

WIDTH = 300
HEIGHT = 300
DOT_SIZE = 10
ALL_DOTS = 900
RAND_POS = 27

x = [0] * ALL_DOTS
y = [0] * ALL_DOTS


class Board(UserControl):

    def __init__(self):
        self.Text = 'Snake'

        self.components = Container()
        self.BackColor = Color.Black
        self.DoubleBuffered = True
        self.ClientSize = Size(WIDTH, HEIGHT)

        self.left = False
        self.right = True
        self.up = False
        self.down = False
        self.inGame = True

        try: 
            self.dot = Bitmap("dot.png")
            self.apple = Bitmap("apple.png")
            self.head = Bitmap("head.png")

        except Exception, e:
            print e.Message
        

        self.initGame()


    def OnTick(self, sender, event):

        if self.inGame:
            self.checkApple()
            self.checkCollision()
            self.move()
        
        self.Refresh()
    
    def initGame(self):

        self.dots = 3

        for i in range(self.dots):
            x[i] = 50 - i * 10
            y[i] = 50
        

        self.locateApple()
        self.KeyUp += self.OnKeyUp


        self.timer = Timer(self.components)
        self.timer.Enabled = True
        self.timer.Interval = 100
        self.timer.Tick += self.OnTick

        self.Paint += self.OnPaint


    def OnPaint(self, event):

        g = event.Graphics
 
        if (self.inGame):
            g.DrawImage(self.apple, self.apple_x, self.apple_y)

            for i in range(self.dots):
                if i == 0:
                    g.DrawImage(self.head, x[i], y[i])
                else:
                    g.DrawImage(self.dot, x[i], y[i])     
               
        else:
           self.gameOver(g)
        
    

    def gameOver(self, g):

        msg = "Game Over"
        format = StringFormat()
        format.Alignment = StringAlignment.Center
        format.LineAlignment = StringAlignment.Center

        width = float(self.ClientSize.Width)
        height = float(self.ClientSize.Height)
        rectf = RectangleF(0.0, 0.0, width, height)

        g.DrawString(msg, self.Font, Brushes.White, rectf, format)    
        self.timer.Stop()
    

    def checkApple(self):

        if x[0] == self.apple_x and y[0] == self.apple_y: 
            self.dots = self.dots + 1
            self.locateApple()
        
    
    def move(self):

        z = self.dots

        while z > 0:
            x[z] = x[(z - 1)]
            y[z] = y[(z - 1)]
            z = z - 1

        if self.left:
            x[0] -= DOT_SIZE

        if self.right: 
            x[0] += DOT_SIZE

        if self.up:
            y[0] -= DOT_SIZE

        if self.down:
            y[0] += DOT_SIZE
        
    

    def checkCollision(self):

        z = self.dots
       
        while z > 0:
            if z > 4 and x[0] == x[z] and y[0] == y[z]:
                self.inGame = False
            z = z - 1

        if y[0] >= HEIGHT - DOT_SIZE - self.TITLEBAR_HEIGHT:
            self.inGame = False
        
        if y[0] < 0:
            self.inGame = False
        
        if x[0] >= WIDTH - DOT_SIZE - self.BORDER_WIDTH:
            self.inGame = False

        if x[0] < 0:
            self.inGame = False
        

    def locateApple(self):
        rand = Random()
        r = rand.Next(RAND_POS)
        self.apple_x = r * DOT_SIZE
        r = rand.Next(RAND_POS)
        self.apple_y = r * DOT_SIZE
    

    def OnKeyUp(self, event): 

        key = event.KeyCode

        if key == Keys.Left and not self.right: 
            self.left = True
            self.up = False
            self.down = False
        

        if key == Keys.Right and not self.left:
            self.right = True
            self.up = False
            self.down = False
        

        if key == Keys.Up and not self.down:
            self.up = True
            self.right = False
            self.left = False
        

        if key == Keys.Down and not self.up: 
            self.down = True
            self.right = False
            self.left = False