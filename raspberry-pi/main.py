# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.
import time
import json

from neopixel import *


# LED strip configuration:
LED_COUNT      = 237      # Number of LED pixels.
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
		self.row3 = json["row3"]
		self.row4 = json["row4"]
		self.row5 = json["row5"]
		self.row6 = json["row6"]
		self.row7 = json["row7"]
		self.row8 = json["row8"]
		self.row9 = json["row9"]
		self.row10 = json["row10"]
		self.row11 = json["row11"]
		self.row12 = json["row12"]
		self.row13 = json["row13"]
		self.row14 = json["row14"]
		self.row15 = json["row15"]
		self.row16 = json["row16"]
		self.row17 = json["row17"]
		self.row18 = json["row18"]
		self.row19 = json["row19"]
		self.row20 = json["row20"]
		self.row21 = json["row21"]
		self.row22 = json["row22"]
		self.row23 = json["row23"]

	def loadRow(self, strip, row_index, start_pixel, row):

		# for each row in the display
		# even index
		if row_index % 2 == 0:
			for i in range( len(row) ):
				r = row[i][0]
				g = row[i][1]
				b = row[i][2]
				strip.setPixelColor( start_pixel+i, Color(r, g, b))
		
		if not row_index % 2 == 0:
			for i in range( len(row) ):
				r = row[i][0]
				g = row[i][1]
				b = row[i][2]
				strip.setPixelColor( start_pixel+len(row)-i-1, Color(r, g, b))


# Main program logic follows:
if __name__ == '__main__':
	# Create NeoPixel object with appropriate configuration.
	strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
	# Intialize the library (must be called once before other functions).
	strip.begin()

	# intialize values
	app_url = "http://172.16.100.11:3000/foo"
	current_id = None

	print 'Press Ctrl-C to quit.'

	# main program loop
	while True:

		import urllib2
		data = urllib2.urlopen(app_url).read()

		data = json.loads(data)
		new_id = data["id"]
		print new_id


		if not new_id == current_id:
			current_id = new_id
			print "New Display"

			led_matrix = LEDMatrix(data)
			
			led_matrix.loadRow(strip, 0, 0, data["row0"])
			led_matrix.loadRow(strip, 1, 9, data["row1"])
			led_matrix.loadRow(strip, 2, 18, data["row2"])
			led_matrix.loadRow(strip, 3, 27, data["row3"])
			led_matrix.loadRow(strip, 4, 37, data["row4"])
			led_matrix.loadRow(strip, 5, 46, data["row5"])
			led_matrix.loadRow(strip, 6, 55, data["row6"])
			led_matrix.loadRow(strip, 7, 64, data["row7"])
			led_matrix.loadRow(strip, 8, 72, data["row8"])
			led_matrix.loadRow(strip, 9, 81, data["row9"])
			led_matrix.loadRow(strip, 10, 90, data["row10"])
			led_matrix.loadRow(strip, 11, 99, data["row11"])
			led_matrix.loadRow(strip, 12, 109, data["row12"])
			led_matrix.loadRow(strip, 13, 120, data["row13"])
			led_matrix.loadRow(strip, 14, 132, data["row14"])
			led_matrix.loadRow(strip, 15, 144, data["row15"])
			led_matrix.loadRow(strip, 16, 157, data["row16"])
			led_matrix.loadRow(strip, 17, 170, data["row17"])
			led_matrix.loadRow(strip, 18, 183, data["row18"])
			led_matrix.loadRow(strip, 19, 197, data["row19"])
			led_matrix.loadRow(strip, 20, 208, data["row20"])
			led_matrix.loadRow(strip, 21, 217, data["row21"])
			led_matrix.loadRow(strip, 22, 225, data["row22"])
			led_matrix.loadRow(strip, 23, 231, data["row23"])

			strip.setBrightness(255)

			strip.show()

		# sleep before querying the server again
		time.sleep(2000.0/1000.0)