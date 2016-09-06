# Emu-Serial-API

The Emu - 2 is a Energy Monitoring Unit (EMU) that wirelessly connects to your home smart meter and allows you to monitor your power consumption and costs visually. 
This API-Library allows you to connect to the EMU-2 through the USB-serial port on the device, issue querying commands and easily readback the emus response like so:

    > python
    > from emu import *
    > instance = emu('/tty/usbACM0')
    > instance.start_serial()
    > instance.get_network_info()
    > instance.NetworkInfo
    <NetworkInfo>
      <DeviceMacId>0xd8d5b900000041d7</DeviceMacId>
      <CoordMacId>0x000781000081fd17</CoordMacId>
      <Status>Connected</Status>
      <Description>Successfully Joined</Description>
      <ExtPanId>0x000781000081fd17</ExtPanId>
      <Channel>18</Channel>
      <ShortAddr>0x2776</ShortAddr>
      <LinkStrength>0x64</LinkStrength>
    </NetworkInfo>
    > instance.NetworkInfo.LinkStrength
    0x64

You can purchase an EMU from here:
http://www.amazon.com/Rainforest-EMU-2-Energy-Monitoring-Unit/dp/B00BGDPRAI


# Getting Started
### Installation

Installation is pretty simple in Linux/OS X.  To install the EMU serial api tools, simply type the following commands:

    git clone https://github.com/rainforestautomation/Emu-Serial-API.git
    cd ./Emu-Serial-API
    pip install -r ./requirements.txt

You can now easily get access to your EMU device through the serial port.

### Using the Library

The USB port on the EMU-2 is asynchronous and some commands take longer to execute than others. As a result, this API has been designed to be non-blocking and gives you direct control over the serial port. ( You have to call start_serial() and stop_serial() whe you want the emu object to listen to commands)

    emu_instance = emu('/tty/usbACM0')
    emu_instance.start_serial()
    emu_instance.get_current_summation_delivered()
    time.sleep(5)
    emu_instance.stop_serial()

All commands issed to the EMU2 through this API will return null. This included commands which invoke a response from the EMU. To access the returned data, you are required to wait for the EMU2 to response (up to 4 seconds), then you can read the attribute directly from the API object instance.

    emu_instance.CurrentSummationDelivered
    <CurrentSummationDelivered>
      <DeviceMacId>0xd8d5b900000041d7</DeviceMacId>
      <MeterMacId>0x000781000081fd17</MeterMacId>
      <TimeStamp>0x1c90932b</TimeStamp>
      <SummationDelivered>0x0000000006bc5b7d</SummationDelivered>
      <SummationReceived>0x0000000000000000</SummationReceived>
      <Multiplier>0x00000001</Multiplier>
      <Divisor>0x000003e8</Divisor>
      <DigitsRight>0x01</DigitsRight>
      <DigitsLeft>0x06</DigitsLeft>
      <SuppressLeadingZero>Y</SuppressLeadingZero>
    </CurrentSummationDelivered>

Or if you want a particular value part of that data:

    emu_instance.CurrentSummationDelivered.SummationDelivered
    0x0000000006bc5bcb

As the EMU-2 is constantly producing data, those object instance attributes will be written over as new data comes in. To get around this, we have implemented a history list which records 
commands from and to the EMU instance. Each item in the history list is composed of a history_obj:

    
    history_obj ={
        'origin':origin,(HOST or EMU)
        'type':tag,(Either the EMU's response root tag, or the command issued)
        'obj':obj, (None if origin = HOST, the response Object if origin = EMU)
        'raw': raw (the raw XML)
    }

You can iterate through the history like so:

    for history_obj in emu_instance.history:
        print history_obj['origin']
        if type(history_obj['obj'] == 'NetworkInfo'):
            print history_obj['obj'].Status

# API Commands

List of commands that can be issued:

    #creating emu object
    emu_instance = emu('/tty/usbACM0')
    #this will try to detrct environment, so no special care is needed for windows, just type emu('COMX')
    
    
    
    #meta commands
    #start serial, required before any othercommand can be issued
    emu.start_serial()
    #should be called when you no longer need to listen to emu
    emu.stop_serial()
    #command for printing to screen
    emu.readback()
    
    #Standard Commands
    emu.restart()
    emu.get_device_info()
    emu.get_network_info()
    emu.factory_reset()
    emu.factory_reset()
    emu.get_restart_info()
    emu.set_restart_info('TYPE', 'CONFIRM')
    emu.set_meter_attributes(multiplier,divisor)
    emu.set_fast_poll(frequency, duration)
    emu.get_fast_poll_status()
    emu.get_current_summation()
    emu.get_instantaneous_demand(refresh)
    emu.get_time(refresh)
    emu.set_current_price(price, trailing_digits)
    emu.set_meter_info('nickname','account','auth', 'host','enabled')
    emu.get_message()
    emu.get_local_attributes()
    emu.set_local_attributes(current_day_max_demand)
    emu.get_billing_periods()
    emu.set_billing_periods_list(number_of_periods)
    emu.set_biling_period(period,start)
    emu.get_price_blocks()
    emu.set_price_block(block,threshold,price)
    emu.get_schedule(mode)
    emu.get_profile_data(num_of_periods,interval_channel)
    emu.set_schedule(self,event,mode=None, frequency=None, enabled =None)
    emu.print_network_tables()
    
    #Accessing current emu state:(Provided the emu has sent state through serial to object)
    emu_instance.NetworkInfo
    emu_instance.MessageCluster
    emu_instance.TimeCluster
    emu_instance.InstantaneousDemand
    emu_instance.NetworkInfo
    emu_instance.PriceCluster
    emu_instance.DeviceInfo
    emu_instance.CurrentSummationDelivered
    emu_instance.ScheduleInfo
    emu_instance.BlockPriceDetail
    
    You can access attributes like so:
    emu_instance.DeviceInfo.DeviceMacId
    
#Comments or suggestions

The maintainer of this repo can be contacted at john dot lee at rainforestautomation dot com. Feel free to create issues  if the api does something unexpected


