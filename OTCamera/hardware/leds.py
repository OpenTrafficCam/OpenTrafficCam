# OTCamera: buttons config file to be imported.
# Copyright (C) 2020 OpenTrafficCam Contributors
# <https://github.com/OpenTrafficCam
# <team@opentrafficcam.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from gpiozero import PWMLED

POWERLEDPIN = 13
WIFILEDPIN = 12
RECLEDPIN = 5

powerled = PWMLED(POWERLEDPIN)
wifiled = PWMLED(WIFILEDPIN)
recled = PWMLED(RECLEDPIN)


def init():
    """[summary]
    """
    powerled.on()
    wifiled.on()
    recled.on()

