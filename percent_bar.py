import sys
import redpitaya_scpi as scpi


#if __name__ == '__main__':
rp_s = scpi.scpi(sys.argv[1])
if len(sys.argv) > 2:
    percent = int(sys.argv[2])
else:
    percent = 60
print("Bar showing: {}%".format(percent))
for i in range(8):
    if int(0.125*i*10) < percent:
        rp_s.tx_txt("DIG:PIN LED{},{}".format(i, 1))
    else:
        rp_s.tx_txt("DIG:PIN LED{},{}".format(i, 0))
    