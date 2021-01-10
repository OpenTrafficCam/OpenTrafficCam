# OTCamera: LEDs and their functions.
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
import config

from helpers import log


if config.USE_LED:

    log.write("Initalizing LEDs")

    POWERPIN = 13
    WIFIPIN = 12
    RECPIN = 5

    power = PWMLED(POWERPIN)
    wifi = PWMLED(WIFIPIN)
    rec = PWMLED(RECPIN)

    log.write("LEDs initalized")


def off():
    """[summary]"""
    if config.USE_LED:
        power.on()
        wifi.on()
        rec.on()
    else:
        pass


def rec_on():
    if config.USE_LED:
        rec.blink(on_time=0.1, off_time=4.9, n=None, background=True)
    else:
        pass


def rec_off():
    if config.USE_LED:
        rec.off()
        rec.pulse(fade_in_time=0.25, fade_out_time=0.25, n=4, background=True)
    else:
        pass


def power_on():
    if config.USE_LED:
        power.blink(on_time=0.1, off_time=0, n=1, background=True)
    else:
        pass
