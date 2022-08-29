# -*- coding: utf-8 -*-
"""
Author: Greg Kinzler, M.S. Eng.
Email: greg.kinzler@gmail.com
Advisor: Heng Ban, PhD
Organization: University of Pittsburgh

Inspired by: Dr. Nicolas Horny & Dr. Austin Fleming 
Université de Reims Champagne-Ardenne & Utah State University

This code can be used to control two lockin amplifiers, a LabJack DAQ, and a 
wavform generator. This will initalize the lockin and waveform generator and 
then take a single point measurment. There are other measurement types 
available in the DataLogging class.

Note: PyDAQ has other function under DataLogging class. Feel
free to look at the documentation to how the other functions work. To add your
own DataLogging functions, edit the PyDAQ.py code. If you would 
like to share your work, consider adding your functions in our GetHub 
repository. Link:

    
"""

import os

#Choose the path where the Data_taking_Module is saved.
path = 'C:\\Users\gek40\Desktop\PyDAQ'
os.chdir(path)

import PyDAQ as mod

#%% Lockin Parameters


# lock-in parameters
#Signal
harm = 1                #Set harmonic to 1st(fondamental), can be set to the ith harm 
filt = 18               #Set filter to  x dB, can be set to: 6,12,18,24 dB
voltage="A-B"           #Set voltage to mode X, can be set to: 'A' or 'A-B' 
current_mod="AC"        #Set current_mod to X, can be set to: 'AC' or 'DC'
shield="FLOAT"          #Set shield to X, can be set to: 'GROUND' or 'FLOAT'
current=0               #Set current range to x , can be set to 1microA (x=0) or 10nA (x=1)
#####Ref 
ext_trig="SIN"          #Set the external Trig to X, can be set to, sine (X="SIN"),POSTTL (X="POS"),negttl (X="NEG")
ext_input=1000000       #Set the External reference input to x, x can be set to 50 (50Ohm) or 1M (1MOhm)
amp=4.                  #Set the amplitude to x (in mV)
offset=0.               #Set the offset (dc level) to x (in V)
source="EXT"            #Set the source to X, can be set to: internal (X="INT"),External (X="EXT"), Dual (X="DUAL") or Chop (X="CHOP")
time_const = 3e-3       #Set the time measurment timeconstant.
f = 630                 #Set the measurment frequncy of the lockin in Hz
#%% Find Lockin in the device list.
mod.Lockin()
mod.Lockin.find_device()

#%% Assign the device name for the Lockin.
mod.Lockin.assign_dev('ASRL6::INSTR', '\r')

#%% Initalize the Lockin with your desired parameters.
mod.Lockin.initialize_lockin(filt, harm, current, voltage, shield, \
                             current_mod, ext_input, ext_trig, source, \
                                 amp, offset, f)
mod.Lockin.time_const(time_const) #Set the time constant of the lockin.

#%% Waveform Generator Parameters
Vpp=5.5555             #Set the peak-to-peak voltage of the waveform generator
voff=0                 #Set the DC voltgae off set of the waveform generator
sig="SIN"              #Set the type of waveform desired (x='SIN'), (x='SQR), ect.
f = 630                #Set the measurment frequncy of the waveform generator in Hz


#Use this for a frequency sweep.
impead=0.              #This can be used to vary the voltage of the wavfrom 
                       #generator based on an inductor's impedence.Use this 
                       #function if you wish to hold the current input constant 
                       #for a frequncy sweep test.

#%% Find Waveform Generator in device list.
mod.WaveGen.find_device()
mod.WaveGen.assign_dev('USB0::0x0957::0x2507::MY57101071::INSTR', '\n')

#%% Initialize the Waveform Generator with your desired parameters.
mod.WaveGen.initialize_gen(sig, f, Vpp, 0)

mod.WaveGen.output_on() #Turn on the ouput of the waveform generator.

#%% Single Point Example
mod.DataLogging.SinglePoint('test', '', f, Vpp, offset)