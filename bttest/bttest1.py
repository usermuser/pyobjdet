# https://stackoverflow.com/questions/11770594/using-sl4a-python-and-bluetooth

# import this

# sample code from previous project (read gyro data)
# from androidhelper import Android
# import time

# d = Android()
# for i in range (200):
# 	d.startSensingTimed(1, 250)
# 	s = d.sensorsReadOrientation().result
# 	d.stopSensing()
# 	print(i, '=', int(s[0]), int(s[1]), int(s[2]))
# 	time.sleep(0.5)

from androidhelper import Android
import time

d = Android()




