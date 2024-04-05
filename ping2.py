import os
def check_ping(hostname):
	# hostname = "taylor"
	response = os.system("ping -c 1 " + hostname)
	# and then check the response...
	if response == 0:
		pingstatus = "Network Active"
	else:
		pingstatus = "Network Error"

	return pingstatus
# print(check_ping("raspberrypi"))
# print(check_ping("RASPBERRYPI"))
print(check_ping("192.168.1.6"))