
 #!/usr/bin/python
 # -*- coding: utf-8 -*-
 import sys
 import requests
 import json
 import time
 import urllib
 import os

 class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   HEADER = '\033[95m'
   OKBLUE = '\033[94m'
   OKGREEN = '\033[92m'
   WARNING = '\033[93m'
   FAIL = '\033[91m'

 class config:
	key = "" #go to https://numverify.com/

 def banner():
	os.system('clear')
	print  color.YELLOW + """
   _____  __  __  ___ 
  |_   _||  \/  || __|
    | |  | |\/| || _| 
    |_|  |_|  |_||_|  

	Editör - KenanTMF - MertTMF Sürüm - 1.0                 
	""" + color.END

 def main():
	banner()
	if len(sys.argv) == 2:
		number = sys.argv[1]
		api = "http://apilayer.net/api/validate?access_key=" + config.key + "&number=" + number + "&country_code=&format=1"
		output = requests.get(api)
		content = output.text
		obj = json.loads(content)
		country_code = obj['country_code']
		country_name = obj['country_name']
		location = obj['location']
		carrier = obj['carrier']
		line_type = obj['line_type']

		print color.YELLOW + "[+] " + color.END + "Telefon Bilgisi Alınıyot..."
		print "--------------------------------------"
		time.sleep(0.2)

		if country_code == "":
			print " - Ülke   		[ " + color.RED + "Başarısız " + color.END + "]"
		else:
			print " - Ülke	         	[ " + color.GREEN + "Başarılı " + color.END + "]"

		time.sleep(0.2)
		if country_name == "":
			print " - Ülke Adı Alma 	[ " + color.RED + "Başarısız " + color.END + "]"
		else:
			print " - Ülke Adı Alma		[ " + color.GREEN + "Başarılı " + color.END + "]"

		time.sleep(0.2)
		if location == "":
			print " - Konum Alma		[ " + color.RED + "Başarısız " + color.END + "]"
		else:
			print " - Konum Alma		[ " + color.GREEN + "Başarılı " + color.END + "]"

		time.sleep(0.2)
		if carrier == "":
			print " - Taşıyıcı Alma		[ " + color.RED + "Başarısız " + color.END + "]"
		else:
			print " - Taşıyıcı Alma		[ " + color.GREEN + "Başarılı " + color.END + "]"

		time.sleep(0.2)
		if line_type == None:
			print " - Cihaz Alma		[ " + color.RED + "Başarısız " + color.END + "]"
		else:
			print " - Cihaz Alma		[ " + color.GREEN + "Başarılı " + color.END + "]"

		print ""
		print color.YELLOW + "[+] " + color.END + "Bilgilerin Sonucu"
		print "--------------------------------------"
		print " - Telefon Numarası: " + str(number)
		print " - Ülke: " + str(country_code)
		print " - Ülke Adı: " + str(country_name)
		print " - Konum: " + str(location)
		print " - Taşıyıcı: " + str(carrier)
		print " - Cihaz: " + str(line_type)
	else:
		print "[?] Kullanım:"
		print "	./%s <Telefon-Numarası>" % (sys.argv[0])
		print "	./%s +13213707446" % (sys.argv[0])

 main()
