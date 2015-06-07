# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import json

from neopixel import *


# LED strip configuration:
LED_COUNT      = 64      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

class LEDMatrix(object):

	def __init__(self, json):

		self.id = None

		self.row0 = json["row0"]
		self.row1 = json["row1"]
		self.row2 = json["row2"]
		self.row3 = [0, 0, 0] * 9
		self.row4 = [0, 0, 0] * 9
		self.row5 = [0, 0, 0] * 9
		self.row6 = [0, 0, 0] * 9
		self.row7 = [0, 0, 0] * 9
		self.row8 = [0, 0, 0] * 9
		self.row9 = [0, 0, 0] * 9
		self.row10 = [0, 0, 0] * 9
		self.row11 = [0, 0, 0] * 9
		self.row12 = [0, 0, 0] * 9
		self.row13 = [0, 0, 0] * 9
		self.row14 = [0, 0, 0] * 9
		self.row15 = [0, 0, 0] * 9
		self.row16 = [0, 0, 0] * 9
		self.row17 = [0, 0, 0] * 9
		self.row18 = [0, 0, 0] * 9
		self.row19 = [0, 0, 0] * 9
		self.row20 = [0, 0, 0] * 9
		self.row21 = [0, 0, 0] * 9
		self.row22 = [0, 0, 0] * 9
		self.row23 = [0, 0, 0] * 9

def loadDisplay(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""

	# for each row in the display
	for i in range(24):
		print 
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	# intialize currentId value
	current_id = None

	print 'Press Ctrl-C to quit.'
	while True:

		data = json.loads(open("example2.json").read())
		new_id = data["id"]


		if not new_id == current_id:
			current_id = new_id
			print "New Display"

			display = LEDMatrix(data)
			print display.row0

			# display LEDs



		# else do nothing

		#strip.setPixelColor(2, Color(0, 255, 0))
		#strip.setPixelColor(1, Color(255, 0, 0))
		#strip.show()
		#time.sleep(1000)