#/*--
#
# Copyright (c) 2025  Frêney Studios
#
# Module Name:
#
#	 customex.py
#
# Abstract:
#
#	 Custom exceptions/Vector IDT
#
# Author:
#
#	 Marco Panseri (Marx) 18-02-2025
#
# Revision History:
#
#--*/


class SpeedLimitPass(BaseException):
    self.message = "SPEED > MAXSPEED \
                    please increase the MAXSPEED value) \
                    or: set RAISE to False"
    print(self.message)
