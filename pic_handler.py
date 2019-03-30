import os
import re


regexes = []

#YYYY-MM-DD
#will not recognize days at the end of the month properly, particularly february
#regexes.add('([0-2]{1}\d{3})-(0{1}[1-9]{1}|1{1}[0-2]{1})-([0-2]{1}[1-9]{1}|3{1}[0-1]{1})\..*')


#YYYYMMDD_HHMMSS | YYYYMMDD_HHMMSS_Pano | YYYYMMDD_HHMMSS_HDR | YYYYMMDD_HHMMSS_Burst | IMG_YYYYMMDD_HHMMSS | PANO_YYYYMMDD_HHMMSS | VID_YYYYMMDD_HHMMSS | video-YYYYMMDD_HHMMSS | YYYYMMDD_HHMMSSnopm | YYYYMMDD_HHMMSS_nopm
#baseline regex: ([1-2]{1}[\d]{3})(0{1}[1-9]{1}|1{1}[0-2]{1})(0{1}\d{1}|1|[1-2]{1}[0-9]{1}|3{1}[0-1]{1})_([0-1]\d{1}|2{1}[0-3]{1})([0-5]{1}\d{1})([0-5]{1}\d{1})
#(?:IMG_|PANO_|VID_|video-)*([1-2]{1}[\d]{3})(0{1}[1-9]{1}|1{1}[0-2]{1})(0{1}\d{1}|1|[1-2]{1}[0-9]{1}|3{1}[0-1]{1})_([0-1]\d{1}|2{1}[0-3]{1})([0-5]{1}\d{1})([0-5]{1}\d{1})(?:\.|_Pano\.|_HDR\.|_Burst\d*|[_]?nopm).*







def handle_pic(pic):
	pass




def main():
	print('holla')
	test_pics_dir = "./test_pics/"
	test_pics = os.listdir(test_pics_dir)
	for pic in test_pics:
		print(pic)
		handle_pic(pic)
	
	
if __name__ == "__main__":
	main()
	

"""
potential file naming scheme:
YYYY-MM-DD
YYYYMMDD_6[0-9]((1-2))
YYYYMMDD_6[0-9]_HDR((1-2))
IMG_YYYYMMDD_6[0-9]
4371237753670073950_account_id=1 //wtf
PANO_YYYYMMDD_6[0-9]
VID_YYYYMMDD_6[0-9]
"""