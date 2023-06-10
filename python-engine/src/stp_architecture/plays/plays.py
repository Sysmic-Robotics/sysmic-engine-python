## Generic file for every play ##
import time

class Play(object):
	# this default time is in milliseconds
	TIMEOUT = 50 * 1e6

	def __init__(self, name, time_out=TIMEOUT):
		self.name       = name
		self.time_out   = time_out
		self.begin_time = time.time_ns() #tiempo en ns

    ## Indica si el tiempo se acabó o no ##
	def timed_out(self):
		if time.time_ns() - self.begin_time > self.time_out:
			return True
		else:
			return False