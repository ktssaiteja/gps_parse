import pynmea2

def print_detail(mode, msg):
    print(mode)
    if(mode=='GGA'):
        print("Latitude : " + str(msg.latitude) + " " + msg.lat_dir + "\nLongitude : " + str(msg.longitude) + " " + msg.lon_dir + "\nTimestamp : " + str(msg.timestamp) + "\nNumber of Satellites used : " + msg.num_sats + "\n")
    elif(mode=="RMC"):
        print("Latitude : " + str(msg.latitude) + " " + msg.lat_dir + "\nLongitude : " + str(msg.longitude) + " " + msg.lon_dir + "\nTimestamp : " + str(msg.timestamp) + "\nDate : " + str(msg.datestamp) + "\n")
    elif(mode=="GLL"):
        print("Latitude : " + str(msg.latitude) + " " + msg.lat_dir + "\nLongitude : " + str(msg.longitude) + " " + msg.lon_dir + "\nTimestamp : " + str(msg.timestamp) + "\n")
    elif (mode=="VTG"):
        print("Speed : " + str(msg.spd_over_grnd_kts) + " Knots or " + str(msg.spd_over_grnd_kmph) + " kmph\n")
    else:
        print("\n")

myfile=open("gpsdata.txt", "r")

for line in myfile:
    msg=pynmea2.parse(line)
    mode=''
    for i in range(3,6):
        mode+=line[i]
    print_detail(mode, msg)

myfile.close()
