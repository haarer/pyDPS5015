#!/usr/bin/env python
# -*- coding: utf_8 -*-
"""
 Testing modbus control of DPS5015

 (C)2018 - Alexander Haarer

 This is distributed under GNU LGPL license, see license.txt
"""

import serial

import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu

import DPS5015

#PORT = 1
PORT = '/dev/ttyUSB1'

def main():
    """main"""
    logger = modbus_tk.utils.create_logger("console")

    try:
        #Connect to the slave
        master = modbus_rtu.RtuMaster(
            serial.Serial(port=PORT, baudrate=9600, bytesize=8, parity='N', stopbits=1, xonxoff=0)
        )
        master.set_timeout(5.0)
        master.set_verbose(False)
        logger.info("connected")

	res = master.execute(1, cst.READ_HOLDING_REGISTERS, DPS5015.U_SET, 1)
	print("U_SET = %2.2f V" %  ( res[0] / 100.0 ) )
	res = master.execute(1, cst.READ_HOLDING_REGISTERS, DPS5015.UOUT, 1)
	print("UOUT = %2.2f V" %  ( res[0] / 100.0 ) )
        res = master.execute(1, cst.READ_HOLDING_REGISTERS, DPS5015.IOUT, 1)
	print("IOUT = %2.2f A" %  ( res[0] / 100.0 ) )

        logger.info("Setting U_SET")
	print(master.execute(1, cst.WRITE_SINGLE_REGISTER, DPS5015.U_SET, output_value=1000))
        logger.info("Setting I_SET")
	print(master.execute(1, cst.WRITE_SINGLE_REGISTER, DPS5015.I_SET, output_value=100))
        logger.info("Powering on")
	print(master.execute(1, cst.WRITE_SINGLE_REGISTER, DPS5015.ONOFF, output_value=1))


	res = master.execute(1, cst.READ_HOLDING_REGISTERS, DPS5015.U_SET, 1)
	print("U_SET = %2.2f V" %  ( res[0] / 100.0 ) )
	res = master.execute(1, cst.READ_HOLDING_REGISTERS, DPS5015.UOUT, 1)
	print("UOUT = %2.2f V" %  ( res[0] / 100.0 ) )
        res = master.execute(1, cst.READ_HOLDING_REGISTERS, DPS5015.IOUT, 1)
	print("IOUT = %2.2f A" %  ( res[0] / 100.0 ) )

        logger.info("Setting U_SET")
	master.execute(1, cst.WRITE_SINGLE_REGISTER, DPS5015.U_SET, output_value=500)
        logger.info("Setting I_SET")
	master.execute(1, cst.WRITE_SINGLE_REGISTER, DPS5015.I_SET, output_value=10)
        logger.info("Powering off")
	print(master.execute(1, cst.WRITE_SINGLE_REGISTER, DPS5015.ONOFF, output_value=0))


    except modbus_tk.modbus.ModbusError as exc:
        logger.error("%s- Code=%d", exc, exc.get_exception_code())

if __name__ == "__main__":
    main()
