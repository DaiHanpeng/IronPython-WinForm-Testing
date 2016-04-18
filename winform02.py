# Set up the path to the .NET Framework.
import sys
sys.path.append('C:\\WINDOWS\\Microsoft.NET\\Framework\\v4.0.30319')
# Make clr accessible.
import clr
# Add any required references.
clr.AddReference('System.Windows.Forms.DLL')
clr.AddReference('System.Drawing.DLL')
# Import the .NET assemblies.
import System
import System.Windows.Forms
import System.Drawing.Point

class frmMain(System.Windows.Forms.Form):
	# This function performs all of the required initialization.
	def InitializeComponent(self):
		# Configure the form.
		self.ClientSize = System.Drawing.Size(350, 200)
		self.Text = 'Using a Timer Example'
		# Configure btnStart
		self.btnStart = System.Windows.Forms.Button()
		self.btnStart.Text = '&Start'
		self.btnStart.Location = System.Drawing.Point(263, 13)
		# Configure btnQuit
		self.btnQuit = System.Windows.Forms.Button()
		self.btnQuit.Text = '&Quit'
		self.btnQuit.Location = System.Drawing.Point(263, 43)
		# Configure lblTime
		self.lblTime = System.Windows.Forms.Label()
		self.lblTime.Text = System.DateTime.Now.ToLongTimeString()
		self.lblTime.Location = System.Drawing.Point(13, 13)
		self.lblTime.Size = System.Drawing.Size(120, 13)
		# Configure objTimer
		self.objTimer = System.Windows.Forms.Timer()
		self.objTimer.Interval = 1000
		# Add the controls to the form.
		self.Controls.Add(self.btnStart)
		self.Controls.Add(self.btnQuit)
		self.Controls.Add(self.lblTime)
		
		# Always add event handlers after defining the Windows Form.
		self.btnStart.Click += self.btnStart_Click
		self.btnQuit.Click += self.btnQuit_Click
		self.objTimer.Tick += self.objTimer_Tick		
		
	# Define the event handlers.
	def btnStart_Click(self,Sender,MArgs):
		# Check the button status.
		if self.btnStart.Text == '&Start':
			# Start the timer.
			self.objTimer.Start()
			# Change the button text.
			self.btnStart.Text = '&Stop'
		else:
			# Start the timer.
			self.objTimer.Stop()
			# Change the button text.
			self.btnStart.Text = '&Start'
	
	def btnQuit_Click(self, *args):
		# Close the application.
		self.Close()		
		
	def objTimer_Tick(self,*args):
		# Handle the timer tick.
		self.lblTime.Text = System.DateTime.Now.ToLongTimeString()		
	
if __name__ == "__main__":
	
	winform = frmMain()
	winform.InitializeComponent()
	'''
	winform.ShowDialog()
	'''
	# Run the application.
	System.Windows.Forms.Application.Run(winform)

