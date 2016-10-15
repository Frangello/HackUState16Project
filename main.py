import serial, json, urllib, struct, time
ser = serial.Serial('/dev/cu.usbmodemFA131')  #open serial port connected to the arduino
                                              #to find serial port go on the arduino.app

APIKey = "*INSERT API KEY HERE*" #for legal reasons I cannot publish the API Key,
                                 #to get one go to https://sandbox.amadeus.com/travel-innovation-sandbox/apis/get/flights/low-fare-search


def getData(airport, url):
	response = urllib.urlopen(url)
	data = json.loads(response.read())
	fare = float(data['results'][0]['fare']['total_price'])
	print '{0}: ${1:.2f}'.format(airport, fare)
	return fare

def ledControl(fare, ledPin):
	if fare <= 1000:
		print "Fare is under budget"
		ser.write(struct.pack('>B', ledPin))
	elif fare > 1000:
		print "Fare is over budget"
		ser.write(struct.pack('>B',ledPin + 1))
	

while True:
	print "-----Searching for flights-----"
	ser.write(struct.pack('>B',1))
	#GREEN
	LONurl = "https://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=" + APIKey + "&origin=SLC&destination=LON&departure_date=2016-11-25&currency=USD&number_of_results=1"
	LONFare = getData("LON", LONurl)
	ledControl(LONFare, 2)
	#YELLOW
	LAXurl = "https://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=" + APIKey + "&origin=SLC&destination=LAX&departure_date=2016-11-25&currency=USD&number_of_results=1"
	LAXFare = getData("LAX", LAXurl)
	ledControl(LAXFare, 4)
	#ORANGE
	GRUurl = "https://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=" + APIKey + "&origin=SLC&destination=GRU&departure_date=2016-11-25&currency=USD&number_of_results=1"
	GRUFare = getData("GRU", GRUurl)
	ledControl(GRUFare, 6)
	#BLUE
	BJSurl = "https://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=" + APIKey + "&origin=SLC&destination=BJS&departure_date=2016-11-25&currency=USD&number_of_results=1"
	BJSFare = getData("BJS", BJSurl)
	ledControl(BJSFare, 8)
	#RED
	CPTurl = "https://api.sandbox.amadeus.com/v1.2/flights/low-fare-search?apikey=" + APIKey + "&origin=SLC&destination=CPT&departure_date=2016-11-25&currency=USD&number_of_results=1"
	CPTFare = getData("CPT", CPTurl)
	ledControl(CPTFare, 10)
	ser.write(struct.pack('>B',1))
	print "-----Finished searching-----"
	time.sleep(15)

ser.close()

