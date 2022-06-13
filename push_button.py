import sys
import redpitaya_scpi as scpi

IP = '192.168.0.20'
rp_s = scpi.scpi(IP)

for i in range(8):
    rp_s.tx_txt('DIG:PIN:DIR IN,DIO'+str(i)+'_N')

for i in range(8):
    rp_s.tx_txt('DIG:PIN LED{},0'.format(i))

while 1:
    i = 5
    rp_s.tx_txt('DIG:PIN? DIO'+str(i)+'_N')
    state = rp_s.rx_txt()
    rp_s.tx_txt('DIG:PIN LED'+str(i)+','+str(state))