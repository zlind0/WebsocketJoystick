import pyvjoy, json, sys
import math

j = pyvjoy.VJoyDevice(1)
retval=j.set_axis(pyvjoy.HID_USAGE_X, 1)
print(retval)

def regulary(y):
    y/=60
    # if y>90: y=180-y
    # if y<-90: y=-180-y
    # if y>60: y=60
    # if y<-60: y=-60
    # y/=50
    return -y*abs(y)

def regularz(z):
    z-=90
    z/=60
    # if z<0: z+=180
    # z-=120
    # if z<-90: z+=180
    # if z>60: z=60
    # if z<-60: z=-60
    # z/=50
    return -z*abs(z)

while True:
    jsinput=sys.stdin.readline()
    # print(jsinput)
    data=json.loads(jsinput)
    if "y" in data:
        y=regulary(data["y"])
        z=regularz(data["z"])
        print("[Y %.4f][Z %.4f]"%(y,z))
        j.set_axis(pyvjoy.HID_USAGE_X, int(0x4000*(y)+0x4000))
        j.set_axis(pyvjoy.HID_USAGE_Y, int(0x4000*(-z)+0x4000))
    if "t" in data:
        print("[Z %.4f]"%(data["t"]))
        j.set_axis(pyvjoy.HID_USAGE_RZ, int(0x8000*(data["t"])))
    if "btn" in data:
        j.set_button(int(data["btn"][1]), data["val"])
        print("[%s %d]"%(data["btn"], data["val"]))