from subprocess import Popen, PIPE
import logging

class Notifications:

	@staticmethod
	def display(title, message):
		script = 'display notification "{}" with title "{}" sound name "Purr"'.format(message, title)
		p = Popen(['osascript', '-'], stdin=PIPE, stdout=PIPE, stderr=PIPE)
		stdout, stderr = p.communicate(script.encode("utf-8"))
		logging.debug("Popen returncode: {}".format(p.returncode))