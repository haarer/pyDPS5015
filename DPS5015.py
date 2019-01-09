
#modbus registers of DPS5015 according to DPS5015 CNC Communication Protocol V1.2.pdf
U_SET = 0	#r/w 2 Bytes
I_SET = 1	#r/w 2 Bytes
UOUT = 2	#r   2 Bytes
IOUT = 3	#r   2 Bytes
POWER = 4	#r   2 Bytes
UIN = 5		#r   2 Bytes
LOCK = 6	#r/w 2 Bytes : Key lock function reading and writing value are 0 and 1, 0 represents not lock, 1 represents lock
PROTECT = 7	#r   2 Bytes : Protection status reading value are 0-3, 0 represents good running, 1 represents OVP, 2 represents OCP, 3 represents OPP.
CV_CC = 8	#r   2 Bytes : Constant voltage and constant current reading value are 0-1, 0 represents CV, 1 represents CV.
ONOFF = 9	#r/w 2 Bytes : Control output function reading and writing value are 0-1, 0 represents close, 1 represents open.
B_LED = 10	#r/w 2 Bytes : Level of backlight rank reading and writing value is 0-5, 0 represents the darkest, 5 represents the brightest.
MODEL = 11	#r   2 Bytes
VERSION = 12	#r   2 Bytes
EXTRACT_M = 35	#r/w 2 Bytes : shortcut bringing up data groups function writing value are 0-9, after writing, all corresponding data group are extracted.

# DPS5015 hass user programmable ‘Data Groups’ which each store preset user values. The groups are
# named M0-M9 giving a total of 10 ‘Data Groups’. Each data group has a subset of 8 parameters at number 10-17.
#
# The ‘M0’ Data Group is the power-on default data group.
# M1 and M2 are the shortcut bring up data group.
# M3-M9 are ordinary storage data groups.
#
# Each Data Group (M0-M9) start address is calculated by the following formula: 
#  0050H + ( Data group number * 0010H).
# For example, M3 Data Group has the starting address as follows: 0050H + (3 * 0010H) = 0080H.

DG_U_SET = 0x50	#r/w 2 Bytes
DG_I_SET = 0x51	#r/w 2 Bytes
DG_S_OVP = 0x52	#r/w 2 Bytes
DG_S_OCP = 0x53	#r/w 2 Bytes
DG_S_OPP = 0x54	#r/w 2 Bytes
DG_B_LED = 0x55	#r/w 2 Bytes
DG_M_PRE = 0x56	#r/w 2 Bytes
DG_S-INI = 0x57	#r/w 2 Bytes
