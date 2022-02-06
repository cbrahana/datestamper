import sublime
import sublime_plugin
from datetime import datetime


class DatestamperCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		currentdatetime = str(datetime.now())[0:19]
		self.view.insert(edit, self.view.sel()[0].begin(), currentdatetime)
