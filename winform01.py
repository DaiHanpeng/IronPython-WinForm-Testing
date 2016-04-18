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
		# Configure btnOK
		self.btnOK = System.Windows.Forms.Button()
		self.btnOK.Text = '&OK'
		self.btnOK.Location = System.Drawing.Point(263, 13)
		# Configure btnCancel
		self.btnCancel = System.Windows.Forms.Button()
		self.btnCancel.Text = '&Cancel'
		self.btnCancel.Location = System.Drawing.Point(263, 43)
		# Configure lblMessage
		self.lblMessage = System.Windows.Forms.Label()
		self.lblMessage.Text = 'This is a sample label.'
		self.lblMessage.Location = System.Drawing.Point(13, 13)
		self.lblMessage.Size = System.Drawing.Size(120, 13)
		# Configure the form.
		self.Text = 'Simple Python Windows Forms Example'
		self.ClientSize = System.Drawing.Size(350, 200)
		# Add the controls to the form.
		self.Controls.Add(self.btnOK)
		self.Controls.Add(self.btnCancel)
		self.Controls.Add(self.lblMessage)
		
		self.Tips = System.Windows.Forms.ToolTip()
		self.Tips.SetToolTip(self.btnOK, 'Displays an interesting message.')
		
		self.btnOK.Click += self.btnOK_Click
		self.btnCancel.Click += self.btnCancel_Click
		
		self.AcceptButton = self.btnOK
		self.CancelButton = self.btnCancel
		
	# Define the event handlers.
	def btnOK_Click(self,Sender,MArgs):
		# Display a message showing we arrived.
		SenderText = 'Text: ' + Sender.Text
		MouseText = '\nButton: ' + MArgs.Button.ToString()
		MousePosit = '\nX/Y: ' + MArgs.X.ToString() + '/' + MArgs.Y.ToString()
		System.Windows.Forms.MessageBox.Show(SenderText + MouseText + MousePosit)
	
	def btnCancel_Click(self, *args):
		# Close the application.
		self.Close()		
	
if __name__ == "__main__":
	
	winform = frmMain()
	winform.InitializeComponent()
	'''
	winform.ShowDialog()
	'''
	# Run the application.
	System.Windows.Forms.Application.Run(winform)

