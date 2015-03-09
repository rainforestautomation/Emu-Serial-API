# Emu-Serial-API


# Getting Started
### Installation

Installation is pretty simple in Linux/OS X.  To install the EMU serial api tools, simply type the following commands:

    git clone https://github.com/rainforestautomation/Emu-Serial-API.git
    cd ./Emu-Serial-API
    pip install -r ./requirements.txt

You can now easily get access to your EMU device through the serial port.
    > python
    > from emu import *
    > emu('/tty/USBACM0')
    > emu.start_serial()

# API Commands
