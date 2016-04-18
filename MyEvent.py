'''
It¡¯s important to realize that event handlers may not receive calls in the order in
which you add them to the event. Consequently, you should never create event
handlers that depend on a specific order of calling.

It¡¯s generally a good practice to keep the event, form, and operational code
separate. Doing so will make the application easier to debug later. This example
actually uses three separate files, even though it¡¯s a very simple example. Make
sure you follow this principle when creating events of your own.
'''
class MyEvent:
	# Create the initial HandlerList.
	def __init__(self):
		self.HandlerList = set()
		
	# Add new handlers to the list.
	def Add(self, NewHandler):
		self.HandlerList.add(NewHandler)
		
	# Remove existing handlers from the list.
	def Remove(self, OldHandler):
		try:
			self.HandlerList.remove(OldHandler)
		except KeyError:
			pass
			
	# Invoke the handler.
	def Fire(self, Msg):
		# Call each of the handlers in the list.
		for self.Handler in self.HandlerList:
		self.Handler(Msg)