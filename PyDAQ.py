# -*- coding: utf-8 -*s-
"""
Created on Thu Aug 11 07:48:11 2022

Author: Greg Kinzler, M.S. Eng.
Email: greg.kinzler@gmail.com
Advisor: Dr. Heng Ban
University of Pittsburgh

Inspired by: Dr. Nicolas Horny & Dr. Austin Fleming 
Université de Reims Champagne-Ardenne & Utah State University

This software can be used to control any visa type device through the
PyVisa python package.

In its current configuration this software package will control up to two 
lockin amplifiers, a waveform generator, and a LabJack U3-LV DAQ simulatiously.

The measurement functions are:
    -Single Point Measurement
    -Time Series Measurment
    -Flow Measurement (Note: this was mainly for me but I have included for
                       reference of future functions)
    -Flow Measurement w/ Two Lockin Amplifiers (Note: this was mainly for me 
                                                but I have included for
                                                reference of future functions)
    -Frequency Sweep Measurment
    
"""
import pyvisa


class Lockin:
    
    #Define pyvisa's resource manager as a global parameter
    global rm
    rm = pyvisa.ResourceManager()
    
        
            
    def find_device() :
        #This function will find all devices connected to the PC through USB or
        #RS-232 ports. Then it will save the device as a variable.
        return print('Device options are:' + str(rm.list_resources()) + \
                '. Set the device name to its connected name (ex. ASRL5::INSTR)')
        
    def assign_dev(dev,term):
        #Once the devices list has been found we can assign the device to a 
        #variable to control it. Note you must enter the device name and the 
        #termenation. Try '\r' or '\n'. 
        
        
        time_out = 500 #set timeout to 500ms
        
        #This function will set the resources to connect to the lockin
        global lockin, ID_lockin
        lockin=rm.open_resource(dev, 
                                read_termination=term, 
                                timeout=time_out)
        
        #This will attemp to send and receive information from lock in
        ID_lockin = lockin.query('*IDN?')
        
        return print(str(ID_lockin) + ' ' + 'found: Lockin connection was successful.' \
                     ' Proceed with initialization.')
            
    def sinout(amp):
        # Command set sine out amplitude (in mV)
        lockin.write('SLVL '+ str(amp) +' MV')
        
    def Query(quest):
        return lockin.query(quest)
        
    def freq(f):
        lockin.write('FREQ'+ str(f))
            
    def time_const(time):
        #Set the Time Constant; 1microS (0), <=> 30 ks (21)    

        if 3e-6 > time and time >= 1e-6:
            lockin.write('OFLT 0')
        if 10e-6 > time and time >= 3e-6:
            lockin.write('OFLT 1')
        if 30e-6 > time and time >= 10e-6:
            lockin.write('OFLT 2')
        if 100e-6 > time and time >= 30e-6:
            lockin.write('OFLT 3')
        if 300e-6 > time and time >= 100e-6:
            lockin.write('OFLT 4')
        if 1e-3 > time and time >= 300e-6:
            lockin.write('OFLT 5')
        if 3e-3 > time and time >= 1e-3:
            lockin.write('OFLT 6')
        if 10e-3 > time and time >= 3e-3:
            lockin.write('OFLT 7')
        if 30e-3 > time and time >= 10e-3:
            lockin.write('OFLT 8')
       	if 100.e-3 > time and time >= 30.e-3 :
       		lockin.write("OFLT 9")
       	if 300.e-3 > time and time >= 100.e-3 :
       		lockin.write("OFLT 10")
       	if 1. > time and time >= 300.e-3 :
       		lockin.write("OFLT 11")
       	if 3. > time and time >= 1. :
       		lockin.write("OFLT 12")
       	if 10. > time and time >= 3. :
       		lockin.write("OFLT 13")
       	if 30. > time and time >= 10. :
       		lockin.write("OFLT 14")
       	if 100. > time and time >= 30. :
       		lockin.write("OFLT 15")
       	if 300. > time and time >= 100. :
       		lockin.write("OFLT 16")
       	if 1000. > time and time >= 300. :
            lockin.write("OFLT 17")
       	if 3000. > time and time >= 1000. :
       		lockin.write("OFLT 18")
       	if 10000. > time and time >= 3000. :
       		lockin.write("OFLT 19")
       	if 30000. > time and time >= 10000. :
       		lockin.write("OFLT 20")
       	if time >= 300. :
       		lockin.write("OFLT 21")

    	
    def sensitivity(V_sensitivity):
        #Set the Sensitivity; 1V (0), <=> 1nV (27)

    	if 0.5 < V_sensitivity and V_sensitivity <= 1 :
    		lockin.write("SCAL 0")
    	if 0.2 < V_sensitivity and V_sensitivity <= 0.5 :
    		lockin.write("SCAL 1")
    	if 0.1 < V_sensitivity and V_sensitivity <= 0.2 :
    		lockin.write("SCAL 2")
    	if 0.05 < V_sensitivity and V_sensitivity <= 0.1 :
    		lockin.write("SCAL 3")
    	if 0.02 < V_sensitivity and V_sensitivity <= 0.05 :
    		lockin.write("SCAL 4")
    	if 0.01 < V_sensitivity and V_sensitivity <= 0.02 :
    		lockin.write("SCAL 5")
    	if 0.005 < V_sensitivity and V_sensitivity <= 0.01 :
    		lockin.write("SCAL 6")
    	if 0.002 < V_sensitivity and V_sensitivity <= 0.005 :
    		lockin.write("SCAL 7")
    	if 0.001 < V_sensitivity and V_sensitivity <= 0.002 :
    		lockin.write("SCAL 8")
    	if 500.e-6 < V_sensitivity and V_sensitivity <= 0.001 :
    		lockin.write("SCAL 9")
    	if 200.e-6 < V_sensitivity and V_sensitivity <= 500.e-6 :
    		lockin.write("SCAL 10")
    	if 100.e-6 < V_sensitivity and V_sensitivity <= 200.e-6 :
    		lockin.write("SCAL 11")
    	if 50.e-6 < V_sensitivity and V_sensitivity <= 100.e-6 :
    		lockin.write("SCAL 12")
    	if 20.e-6 < V_sensitivity and V_sensitivity <= 50.e-6 :
    		lockin.write("SCAL 13")
    	if 10.e-6 < V_sensitivity and V_sensitivity <= 20.e-6 :
    		lockin.write("SCAL 14")
    	if 5.e-6 < V_sensitivity and V_sensitivity <= 10.e-6 :		
    		lockin.write("SCAL 15")
    	if 2.e-6 < V_sensitivity and V_sensitivity <= 5.e-6 :
    		lockin.write("SCAL 16")
    	if 1.e-6 < V_sensitivity and V_sensitivity <= 2.e-6 :
    		lockin.write("SCAL 17")
    	if 0.5e-6 < V_sensitivity and V_sensitivity <= 1.e-6 :
    		lockin.write("SCAL 18")
    	if 0.2e-6 < V_sensitivity and V_sensitivity <= 0.5e-6 :
    		lockin.write("SCAL 19")
    	if 0.1e-6 < V_sensitivity and V_sensitivity <= 0.2e-6 :
    		lockin.write("SCAL 20")
    	if 0.05e-6 < V_sensitivity and V_sensitivity <= 0.1e-6 :
    		lockin.write("SCAL 21")
    	if V_sensitivity <= 50.e-9 :
    		lockin.write("SCAL 22")

    def harm(harm):
        #Set harmonic of lockin
        lockin.write("HARM " + str(harm))
        
    def AC_DC(current_mod):
        #Set the current to : AC (i=0) , DC (i=1) 
        lockin.write("ICPL " + current_mod)
    
    def Filter(filt):
        #Set the Filter Slope; 6 (0), 12 (1), 18 (2),  24 (3)
        if filt == 6:
            i=0
        if filt == 12:
            i=1
        if filt == 18:
            i=2
        if filt == 24:
            i=3
        lockin.write("OFSL " + str(i))
    
    def shield(shield):
    	#Set the input shield to : float(i=0) , ground(i=1)
        lockin.write("IGND " + shield)

    def current(current):
        #Set the current range to 10micA or 1nA
        lockin.write("ICUR " + str(current))

    def source(ext_input,ext_trig,source,amp,offset):
        #Set reference source
        lockin.write("RSRC " + source)
    
        lockin.write("PHAS -180")
    
        if source == 'EXT':
    		#Set the external current mod 
            lockin.write("RTGG " + ext_trig)
    
    		#Set the external input 
            lockin.write("REFZ " + str(ext_input))
    
        if source =='INT':
    
    		#Set the ref amplitude to amp
            lockin.write('SLVL '+ str(amp) +' MV')
    
    
    		#Set the reference offset to offset
            lockin.write('SOFF '+str(offset)+' MV')  
    
        if source =='DUAL':
    
    		#Set the ref Amplitude to amp
            lockin.write('SLVL '+ str(amp) +' MV')
    
    
    		#Set the reference offset to offset
            lockin.write('SOFF '+str(offset)+' MV')  
    

    def initialize_lockin(filt,harm,current,voltage,shield,current_mod, \
                          ext_input,ext_trig,source,amp,offset,f):
                
    	#Use this function to set any inital setting of the lockin. After you 
        #have initialized the lockin use the other functions to change any 
        #individual settings
        
        #Options for Initialization:
        #voltage = 'A' or 'A-B'
        #current_mod = 'AC' or 'DC'
        #harm = 0 to 4        
        #filt = 6, 12, 18, or 24 dB
        #shield = 'GROUND' or 'FLOAT'
        #current = 1microA i=0 or 10nA i=1
        #ext_trig = sine (i="SIN"), POSTTL (i="POS"),negttl (i="NEG")
        #ext_input= 50 (50Ohm) or 1e6 (1MOhm)
        #source = Internal (i="INT"),External (i="EXT"), or Dual (i="DUAL")
        
    	#DEFAULT SETTINGS FOR THE LOCKIN
    	#Set set the voltage input mode to : A (i=0) A-B (i=1)
        lockin.write("ISRC " + voltage)
    
    
        #Set the current to : AC (i=0) , DC (i=1) 
        lockin.write("ICPL " + current_mod)
    
        #Set the frequency
        lockin.write("FREQ " + str(f))
        
    	#Setting the harmonic to the 0
        lockin.write("HARM " + str(harm))
    
    	#Set the Filter Slope; 6 (0), 12 (1), 18 (2),  24 (3)
        if filt == 6:
            i=0
        if filt == 12:
            i=1
        if filt == 18:
            i=2
        if filt == 24:
            i=3
        lockin.write("OFSL " + str(i))
    
    
    	#Set the input shield to : float(i=0) , ground(i=1)
        lockin.write("IGND " + shield)
    
    	#Set the current range to 10micA or 1nA
        lockin.write("ICUR " + str(current))
    
    	#Set reference source
        lockin.write("RSRC " + source)
    
        lockin.write("PHAS -180")
    
        if source == 'EXT':
    		#Set the external current mod 
            lockin.write("RTGG " + ext_trig)
    
    		#Set the external input 
            lockin.write("REFZ " + str(ext_input))
    
        if source =='INT':
    
    		#Set the ref amplitude to amp
            lockin.write('SLVL '+ str(amp) +' MV')
    
    
    		#Set the reference offset to offset
            lockin.write('SOFF '+str(offset)+' MV')  
    
        if source =='DUAL':
    
    		#Set the ref Amplitude to amp
            lockin.write('SLVL '+ str(amp) +' MV')
    
    
    		#Set the reference offset to offset
            lockin.write('SOFF '+str(offset)+' MV')
        return print('Lockin has been initialized')

class Lockin_2:
    
    #Define pyvisa's resource manager as a global parameter
    global rm
    rm = pyvisa.ResourceManager()
    
        
            
    def find_device() :
        #This function will find all devices connected to the PC through USB or
        #RS-232 ports. Then it will save the device as a variable.
        # rm = pyvisa.ResourceManager()
        return print('Device options are:' + str(rm.list_resources()) + \
                '. Set the device name to its connected name (ex. ASRL5::INSTR)')
        
    def assign_dev(dev,term):
        #Once the devices list has been found we can assign the device to a 
        #variable to control it. Note you must enter the device name and the 
        #termenation. Try '\r' or '\n'. 
        
        
        time_out = 500 #set timeout to 500ms
        
        #This function will set the resources to connect to the lockin
        global lockin_2, ID_lockin_2
        lockin_2=rm.open_resource(dev, 
                                read_termination=term, 
                                timeout=time_out)
        
        #This will attemp to send and receive information from lock in
        ID_lockin_2 = lockin_2.query('*IDN?')
        
        return print(str(ID_lockin_2) + ' ' + 'found: Lockin connection was succesful.' \
                     ' Proceed with initialization.')
            
    def sinout(amp):
        # Command set sine out amplitude (in mV)
        lockin_2.write('SLVL '+ str(amp) +' MV')
        
    def Query(quest):
        return lockin_2.query(quest)
        
    def freq(f):
        lockin_2.write('FREQ'+ str(f))
            
    def time_const(time):
        #Set the Time Constant; 1microS (0), <=> 30 ks (21)    

        if 3e-6 > time and time >= 1e-6:
            lockin_2.write('OFLT 0')
        if 10e-6 > time and time >= 3e-6:
            lockin_2.write('OFLT 1')
        if 30e-6 > time and time >= 10e-6:
            lockin_2.write('OFLT 2')
        if 100e-6 > time and time >= 30e-6:
            lockin_2.write('OFLT 3')
        if 300e-6 > time and time >= 100e-6:
            lockin_2.write('OFLT 4')
        if 1e-3 > time and time >= 300e-6:
            lockin_2.write('OFLT 5')
        if 3e-3 > time and time >= 1e-3:
            lockin_2.write('OFLT 6')
        if 10e-3 > time and time >= 3e-3:
            lockin_2.write('OFLT 7')
        if 30e-3 > time and time >= 10e-3:
            lockin_2.write('OFLT 8')
       	if 100.e-3 > time and time >= 30.e-3 :
       		lockin_2.write("OFLT 9")
       	if 300.e-3 > time and time >= 100.e-3 :
       		lockin_2.write("OFLT 10")
       	if 1. > time and time >= 300.e-3 :
       		lockin_2.write("OFLT 11")
       	if 3. > time and time >= 1. :
       		lockin_2.write("OFLT 12")
       	if 10. > time and time >= 3. :
       		lockin_2.write("OFLT 13")
       	if 30. > time and time >= 10. :
       		lockin_2.write("OFLT 14")
       	if 100. > time and time >= 30. :
       		lockin_2.write("OFLT 15")
       	if 300. > time and time >= 100. :
       		lockin_2.write("OFLT 16")
       	if 1000. > time and time >= 300. :
            lockin_2.write("OFLT 17")
       	if 3000. > time and time >= 1000. :
       		lockin_2.write("OFLT 18")
       	if 10000. > time and time >= 3000. :
       		lockin_2.write("OFLT 19")
       	if 30000. > time and time >= 10000. :
       		lockin_2.write("OFLT 20")
       	if time >= 300. :
       		lockin_2.write("OFLT 21")

    	
    def sensitivity(V_sensitivity):
        #Set the Sensitivity; 1V (0), <=> 1nV (27)

    	if 0.5 < V_sensitivity and V_sensitivity <= 1 :
    		lockin_2.write("SCAL 0")
    	if 0.2 < V_sensitivity and V_sensitivity <= 0.5 :
    		lockin_2.write("SCAL 1")
    	if 0.1 < V_sensitivity and V_sensitivity <= 0.2 :
    		lockin_2.write("SCAL 2")
    	if 0.05 < V_sensitivity and V_sensitivity <= 0.1 :
    		lockin_2.write("SCAL 3")
    	if 0.02 < V_sensitivity and V_sensitivity <= 0.05 :
    		lockin_2.write("SCAL 4")
    	if 0.01 < V_sensitivity and V_sensitivity <= 0.02 :
    		lockin_2.write("SCAL 5")
    	if 0.005 < V_sensitivity and V_sensitivity <= 0.01 :
    		lockin_2.write("SCAL 6")
    	if 0.002 < V_sensitivity and V_sensitivity <= 0.005 :
    		lockin_2.write("SCAL 7")
    	if 0.001 < V_sensitivity and V_sensitivity <= 0.002 :
    		lockin_2.write("SCAL 8")
    	if 500.e-6 < V_sensitivity and V_sensitivity <= 0.001 :
    		lockin_2.write("SCAL 9")
    	if 200.e-6 < V_sensitivity and V_sensitivity <= 500.e-6 :
    		lockin_2.write("SCAL 10")
    	if 100.e-6 < V_sensitivity and V_sensitivity <= 200.e-6 :
    		lockin_2.write("SCAL 11")
    	if 50.e-6 < V_sensitivity and V_sensitivity <= 100.e-6 :
    		lockin_2.write("SCAL 12")
    	if 20.e-6 < V_sensitivity and V_sensitivity <= 50.e-6 :
    		lockin_2.write("SCAL 13")
    	if 10.e-6 < V_sensitivity and V_sensitivity <= 20.e-6 :
    		lockin_2.write("SCAL 14")
    	if 5.e-6 < V_sensitivity and V_sensitivity <= 10.e-6 :		
    		lockin_2.write("SCAL 15")
    	if 2.e-6 < V_sensitivity and V_sensitivity <= 5.e-6 :
    		lockin_2.write("SCAL 16")
    	if 1.e-6 < V_sensitivity and V_sensitivity <= 2.e-6 :
    		lockin_2.write("SCAL 17")
    	if 0.5e-6 < V_sensitivity and V_sensitivity <= 1.e-6 :
    		lockin_2.write("SCAL 18")
    	if 0.2e-6 < V_sensitivity and V_sensitivity <= 0.5e-6 :
    		lockin_2.write("SCAL 19")
    	if 0.1e-6 < V_sensitivity and V_sensitivity <= 0.2e-6 :
    		lockin_2.write("SCAL 20")
    	if 0.05e-6 < V_sensitivity and V_sensitivity <= 0.1e-6 :
    		lockin_2.write("SCAL 21")
    	if V_sensitivity <= 50.e-9 :
    		lockin_2.write("SCAL 22")

    def harm(harm):
        #Set harmonic of lockin
        lockin_2.write("HARM " + str(harm))
        
    def AC_DC(current_mod):
        #Set the current to : AC (i=0) , DC (i=1) 
        lockin_2.write("ICPL " + current_mod)
    
    def Filter(filt):
        #Set the Filter Slope; 6 (0), 12 (1), 18 (2),  24 (3)
        if filt == 6:
            i=0
        if filt == 12:
            i=1
        if filt == 18:
            i=2
        if filt == 24:
            i=3
        lockin_2.write("OFSL " + str(i))
    
    def shield(shield):
    	#Set the input shield to : float(i=0) , ground(i=1)
        lockin_2.write("IGND " + shield)

    def current(current):
        #Set the current range to 10micA or 1nA
        lockin_2.write("ICUR " + str(current))

    def source(ext_input,ext_trig,source,amp,offset):
        #Set reference source
        lockin_2.write("RSRC " + source)
    
        lockin_2.write("PHAS -180")
    
        if source == 'EXT':
    		#Set the external current mod 
            lockin_2.write("RTGG " + ext_trig)
    
    		#Set the external input 
            lockin_2.write("REFZ " + str(ext_input))
    
        if source =='INT':
    
    		#Set the ref amplitude to amp
            lockin_2.write('SLVL '+ str(amp) +' MV')
    
    
    		#Set the reference offset to offset
            lockin_2.write('SOFF '+str(offset)+' MV')  
    
        if source =='DUAL':
    
    		#Set the ref Amplitude to amp
            lockin_2.write('SLVL '+ str(amp) +' MV')
    
    
    		#Set the reference offset to offset
            lockin_2.write('SOFF '+str(offset)+' MV')  
    

    def initialize_lockin(filt,harm,current,voltage,shield,current_mod, \
                          ext_input,ext_trig,source,amp,offset,f):
                
    	#Use this function to set any inital setting of the lockin. After you 
        #have initialized the lockin use the other functions to change any 
        #individual settings
        
        #Options for Initialization:
        #voltage = 'A' or 'A-B'
        #current_mod = 'AC' or 'DC'
        #harm = 0 to 4        
        #filt = 6, 12, 18, or 24 dB
        #shield = 'GROUND' or 'FLOAT'
        #current = 1microA i=0 or 10nA i=1
        #ext_trig = sine (i="SIN"), POSTTL (i="POS"),negttl (i="NEG")
        #ext_input= 50 (50Ohm) or 1e6 (1MOhm)
        #source = Internal (i="INT"),External (i="EXT"), or Dual (i="DUAL")
        
    	#DEFAULT SETTINGS FOR THE LOCKIN
    	#Set set the voltage input mode to : A (i=0) A-B (i=1)
        lockin_2.write("ISRC " + voltage)
    
    
        #Set the current to : AC (i=0) , DC (i=1) 
        lockin_2.write("ICPL " + current_mod)
    
        #Set the frequency
        lockin_2.write("FREQ " + str(f))
        
    	#Setting the harmonic to the 0
        lockin_2.write("HARM " + str(harm))
    
    	#Set the Filter Slope; 6 (0), 12 (1), 18 (2),  24 (3)
        if filt == 6:
            i=0
        if filt == 12:
            i=1
        if filt == 18:
            i=2
        if filt == 24:
            i=3
        lockin_2.write("OFSL " + str(i))
    
    
    	#Set the input shield to : float(i=0) , ground(i=1)
        lockin_2.write("IGND " + shield)
    
    	#Set the current range to 10micA or 1nA
        lockin_2.write("ICUR " + str(current))
    
    	#Set reference source
        lockin_2.write("RSRC " + source)
    
        lockin_2.write("PHAS -180")
    
        if source == 'EXT':
    		#Set the external current mod 
            lockin_2.write("RTGG " + ext_trig)
    
    		#Set the external input 
            lockin_2.write("REFZ " + str(ext_input))
    
        if source =='INT':
    
    		#Set the ref amplitude to amp
            lockin_2.write('SLVL '+ str(amp) +' MV')
    
    
    		#Set the reference offset to offset
            lockin_2.write('SOFF '+str(offset)+' MV')  
    
        if source =='DUAL':
    
    		#Set the ref Amplitude to amp
            lockin_2.write('SLVL '+ str(amp) +' MV')
    
    
    		#Set the reference offset to offset
            lockin_2.write('SOFF '+str(offset)+' MV')
        return print('Lockin has been initialized')
       
class WaveGen:
    global rm
    rm = pyvisa.ResourceManager()
    
        
            
    def find_device() :
        #This function will find all devices connected to the PC through USB or
        #RS-232 ports. Then it will save the device as a variable.
        # rm = pyvisa.ResourceManager()
        return print('Device options are:' + str(rm.list_resources()) + \
                '. Set the device name to its connected name (ex. ASRL5::INSTR)')
        
    def assign_dev(dev,term):
        #Once the devices list has been found we can assign the device to a 
        #variable to control it. Note you must enter the device name and the 
        #termenation. Try '\r' or '\n'. 
        
        
        time_out = 500 #set timeout to 500ms
        
        #This function will set the resources to connect to the lockin
        global fun_gen, ID_gen
        fun_gen=rm.open_resource(dev, 
                                read_termination=term, 
                                timeout=time_out)
        
        #This will attemp to send and receive information from lock in
        ID_gen = fun_gen.query('*IDN?')
        
        return print(str(ID_gen) + ' ' +'found: Waveform generator connection was ' \
                     'succesful. Proceed with initialization.')
                     
    def set_wave(typ):
    	#options are: SINE, SQUARE, RAMP, PULSE, NOISE, ARB ,DC
    	fun_gen.write('FUNC '+ str(typ))

    def set_freq(freq):
        fun_gen.write('FREQ ' + str(freq))

    def set_voltage(amp, offset):
    	fun_gen.write("VOLT " + str(amp))
    	fun_gen.write("VOLT:OFFS " + str(offset))

    def output_on():
        fun_gen.write("OUTP ON")
        
    def output_off():
        fun_gen.write("OUTP OFF")

    def output_impead(impead):
    	fun_gen.write("OUTP LOAD "+str(impead))

    	#Sets the reference CHANNEL 2 IS THE REFERENCE
    def ref_on(sig,amp,offset):
    	fun_gen.write("FUNC "+sig)
    	fun_gen.write("VOLT "+str(amp))
    	fun_gen.write("VOLT:OFFS "+str(offset))
        
    def initialize_gen(wave, freq, volt, offset):
        fun_gen.write('FUNC ' + str(wave))
        fun_gen.write('VOLT ' + str(volt))
        fun_gen.write('VOLT:OFFS ' + str(offset))
        fun_gen.write('FREQ ' + str(freq))
        return print('Waveform generator has been initialized')

class DataLogging:
    #This class is inended to log data for transient studies, single point 
    #studies, and sweep studies.
    global date
    
   

    def SinglePoint(fileName,path,freq,Vpp,offset):
        import os
        import glob
        import csv
        import datetime
        global date
        date = datetime.datetime.now()
        
        def MakeFile(path,fileName):
            #This function will create a .csv file of the data for this 
            #experiment. You must specify where you would like to save the 
            #file and its name. If the file exists there will be and _# added 
            #to the file. This will prevent data being overwritten.
            
            if not os.path.exists(path): #If the file does not exist create one.
                os.makedirs(path)               
                print( "The file "+ str(path) +" has been created")    

            os.chdir(path)		#Set directory to the path specifid.
            list =glob.glob("*.csv")	#Find all .csv files in .
            
            #If the file name exists add an _# to the end of the file.
            i = 1
            length = len(fileName)
            for j in list:		
                if j[:length] == fileName:	
                    i = i+1			
            newname2= path + fileName + '_' + str(i) + '.csv'
            return newname2
        

        print('Experiment Date:' + ' ' + date.strftime('%a, %d/%m/%Y'))
        print('Experiment Time: ' + date.strftime('%I:%M %p'))
        print('Experiment Equipment: ' + ID_gen)
        print('                      ' + ID_lockin)
        data = MakeFile(fileName, path) #Create a .csv data file
        
        header = ['Freq','Vpp_gen', 'V_Mag','Phase'] #if you are using 
                                                    #different headers please 
                                                    #change this line of code
        print ('Frequency         Mag      Phase (Deg)         Vpp_Gen')
        
        with open(data, 'w', encoding='UTF8', newline='') as f:    
            writer = csv.writer(f)
            writer.writerow(['Experiment Date:' + ' ' + date.strftime('%a, %d/%m/%Y')])
            writer.writerow(['Experiment Time: ' + date.strftime('%I:%M %p')])
            writer.writerow(['Experiment Equipment: '])
            writer.writerow([ID_gen])
            writer.writerow([ID_lockin])
            writer.writerow(header) #Write the header of your .csv file
        
            WaveGen.set_freq(freq) #Set the frequency of waveform gen
            WaveGen.set_voltage(Vpp, offset) #Set voltage of waveform gen
            
            WaveGen.output_on() #Turn the waveform gen on
            
            amp=float(lockin.query("OUTP? 3"))	#Get ampliture of signal from lockin
            phase=float(lockin.query("OUTP? 4")) #Get phase of signal from lockin
            
            print('   ' + str(freq) + '         ' + str(amp) + '        '
                  + str(phase) + '           ' + str(Vpp))
            
            writer.writerow([freq,Vpp,amp,phase]) #Write data to new line on .csv file
            os.chdir("../" + path)
    
    def TimeDependentMeasure(fileName,path,freq,Vpp,offset,start, stop, step,
                             plot=False, xlable=None, ylable=None, title=None,
                             y_model=None, x_model=None):
        #This function will measure and record data as a function of time by
        #using a lockin-ampilifer and a waveform generator.
        import os
        import glob
        import csv
        import numpy as np
        import time
        import datetime
        global date
        import matplotlib.pyplot as plt

        date = datetime.datetime.now()
        
        if plot == True:
            #Initalize ploting values
            time_plt = []
            voltage_plt = []
            amp=0
        
        def MakeFile(path,fileName):
            #This function will create a .csv file of the data for this 
            #experiment. You must specify where you would like to save the 
            #file and its name. If the file exists there will be and _# added 
            #to the file. This will prevent data being overwritten.
            
            if not os.path.exists(path): #If the file does not exist create one.
                os.makedirs(path)               
                print( "The file "+ str(path) +" has been created")    

            os.chdir(path)		#Set directory to the path specifid.
            list =glob.glob("*.csv")	#Find all .csv files in .
            
            #If the file name exists add an _# to the end of the file.
            i = 1
            length = len(fileName)
            for j in list:		
                if j[:length] == fileName:	
                    i = i+1			
            newname2= path + fileName + '_' + str(i) + '.csv'
            return newname2
        

        print('Experiment Date:' + ' ' + date.strftime('%a, %d/%m/%Y'))
        print('Experiment Time: ' + date.strftime('%I:%M %p'))
        print('Experiment Equipment: ' + ID_gen)
        print('                      ' + ID_lockin)
        data = MakeFile(fileName, path) #Create a .csv data file
        
        header = ['Freq','Vpp_gen', 'V_Mag','Phase','Time'] #if you are using 
                                                    #different headers please 
                                                    #change this line of code
        print('Frequency         Mag      Phase (Deg)         Vpp_Gen' +        
               '      Time' )
        
        with open(data, 'w', encoding='UTF8', newline='') as f:    
            writer = csv.writer(f)
            writer.writerow(['Experiment Date:' + ' ' + date.strftime('%a, %d/%m/%Y')])
            writer.writerow(['Experiment Time: ' + date.strftime('%I:%M %p')])
            writer.writerow(['Experiment Equipment: '])
            writer.writerow([ID_gen])
            writer.writerow([ID_lockin])
            writer.writerow(header) #Write the header of your .csv file
        
            WaveGen.set_freq(freq) #Set the frequency of waveform gen
            WaveGen.set_voltage(Vpp, offset) #Set voltage of waveform gen
            
            WaveGen.output_on() #Turn the waveform gen on
            
            t = np.arange(start,stop,step)
            
            start_time = time.time()
            for i in range(len(t)+1):
                amp=float(lockin.query("OUTP? 3"))	#Get ampliture of signal from lockin
                phase=float(lockin.query("OUTP? 4")) #Get phase of signal from lockin
                time.sleep(step) #Pause for next measurement
                
                end = time.time()
                time_iter = end - start_time #Find how long the iteration took.
                print('   ' + str(freq) + '         ' + str(amp) + '        '
                  + str(phase) + '           ' + str(Vpp) + '          ' + 
                  str(round(time_iter,2)))
            
                writer.writerow([freq,Vpp,amp,phase,round(time_iter,2)]) #Write data to new line on .csv file
 
            if plot == True:
                #Please add model data if you would like to fit data
                #that you are measuring to a model in real time.
                time_plt.append(time_iter)
                voltage_plt.append(amp*1000)
                
                plt.figure(figsize = (12,6), dpi = 300)
                plt.plot(y_model,x_model, '--r')
                plt.plot(time_plt,voltage_plt,'b*')
                plt.xlabel(xlable, fontsize = 12)
                plt.ylabel(ylable, color = 'k', fontsize = 12)
                plt.title(title, color = 'k', fontsize = 16)
                plt.show()
                
            os.chdir("../" + path)
            
    def FlowMeasurement(fileName,path,freq,Vpp,offset, start, stop, step, AIN, 
                        n, plot=False, xlable=None, ylable=None, title=None,
                        y_model=None, x_model=None):
        #This function will measure and record data for a flow loop using a 
        #Lock in amplifier, waveform generator, and reference hall effect flow
        #meter. Note the reference flow meter is recorded using a LabJack U3-LV
        #DAQ. If you wish to use a different device, you will have to edit this
        #code
        
        import matplotlib.pyplot as plt
        import os
        import glob
        import csv
        import numpy as np
        import time
        import u3
        import datetime
        global date
        date = datetime.datetime.now()
        
        cwd = os.getcwd()
        
        #Define and intialize the LabJack U3-LV device
        dev = u3.U3()
        dev.configIO(FIOAnalog=0xFF, EIOAnalog=0xFF) #Configure all inputs to analog.
        
        
        def MakeFile(path,fileName):
            #This function will create a .csv file of the data for this 
            #experiment. You must specify where you would like to save the 
            #file and its name. If the file exists there will be and _# added 
            #to the file. This will prevent data being overwritten.
            
            if not os.path.exists(path): #If the file does not exist create one.
                os.makedirs(path)               
                print( "The file "+ str(path) +" has been created")    

            os.chdir(path)		#Set directory to the path specifid.
            list =glob.glob("*.csv")	#Find all .csv files in .
            
            #If the file name exists add an _# to the end of the file.
            i = 1
            length = len(fileName)
            for j in list:		
                if j[:length] == fileName:	
                    i = i+1			
            newname2= path + fileName + '_' + str(i) + '.csv'
            return newname2
        

        print('Experiment Date:' + ' ' + date.strftime('%a, %d/%m/%Y'))
        print('Experiment Time: ' + date.strftime('%I:%M %p'))
        print('Experiment Equipment: ' + ID_gen)
        print('                      ' + ID_lockin)
        data = MakeFile(fileName, path) #Create a .csv data file
        
        header = ['Freq','Vpp_gen', 'V_Mag','Phase','Flow_Rate (gal/min)','Time'] #if you are using 
                                                    #different headers please 
                                                    #change this line of code
        print('Frequency         Mag      Phase (Deg)         Vpp_Gen' +        
               '      Time             Flow_Rate (gal/min)')
        
        with open(data, 'w', encoding='UTF8', newline='') as f:    
            writer = csv.writer(f)
            writer.writerow(['Experiment Date:' + ' ' + date.strftime('%a, %d/%m/%Y')])
            writer.writerow(['Experiment Time: ' + date.strftime('%I:%M %p')])
            writer.writerow(['Experiment Equipment: '])
            writer.writerow([ID_gen])
            writer.writerow([ID_lockin])
            writer.writerow(header) #Write the header of your .csv file
        
            WaveGen.set_freq(freq) #Set the frequency of waveform gen
            WaveGen.set_voltage(Vpp, offset) #Set voltage of waveform gen
            
            WaveGen.output_on() #Turn the waveform gen on
            
            t = np.arange(start,stop,step)
            t_start = time.time()
            
            if plot == True:
                #Initalize ploting values
                flow_plt = []
                voltage_plt = []
                gal_min=0
                amp=0
            
            for i in range(len(t)+1):
                #This is where the measurment takes place for lock in
                amp=float(lockin.query("OUTP? 3"))	#Get ampliture of signal from lockin
                phase=float(lockin.query("OUTP? 4")) #Get phase of signal from lockin
                
                #This is where measurment will take place for reference device
                n = n #Set averageing constant for flow calcuation
                count = 0 #Initalize the count for flow calculation
                flow_data = []
                start_time = time.time()
                
                for j in range(n):
                    flow = dev.getAIN(AIN) #Get flow voltage measurment from LabJack U3
                    flow_data.append(flow) #Save voltage to data set
                    count = np.sum(np.diff(flow_data) > 1) #Count if pulse (i.e. strong change in voltage)
                    #time.sleep(step/n) #This is my ISSUE
                end = time.time()

                freq_flow = count/(end-start_time) #Calculate frequncy of pulses
                
                if freq_flow < 3:
                    flow_rate = 0
                else:
                    #Note: This flow function is specific to my sensor
                    flow_rate = 0.146*freq_flow + 1.2435 #Calculate flow rate GPM
                gal_min = flow_rate
                
                t_iter_end = time.time() 
                t_iter  = t_iter_end - t_start
                
                #Print the current time step the user
                print('   ' + str(freq) + '         ' + str(amp) + '        '
                  + str(phase) + '           ' + str(Vpp) + '          ' + 
                  str(round(t_iter,2)) + '          ' + str(round(gal_min,2)))
               
                #Save the data to .csv file
                writer.writerow([freq,Vpp,amp,phase,round(gal_min,2),\
                                 round(t_iter,2)]) #Write data to new line on .csv file
                
                #If you want plot the data while measuring
                if plot == True:
                    #Please add model data if you would like to fit data
                    #that you are measuring to a model in real time.
                    flow_plt.append(gal_min)
                    voltage_plt.append(amp*1000)
                    
                    plt.figure(figsize = (12,6), dpi = 300)
                    plt.plot(y_model,x_model, '--r')
                    plt.plot(flow_plt,voltage_plt,'b*')
                    plt.xlabel(xlable, fontsize = 12)
                    plt.ylabel(ylable, color = 'k', fontsize = 12)
                    plt.title(title, color = 'k', fontsize = 16)
                    plt.show()
                    
                #Wait for next time step
                time.sleep(step)
                
            os.chdir(cwd) #set directory back to where module is located
            
    def FlowMeasurementTwoLock(fileName,path,freq,Vpp,offset, start, stop, 
                               step, AIN, n, plot=False, xlable=None, 
                               ylable=None, title=None, y_model=None, 
                               x_model=None):
        #This function will measure and record data for a flow loop using a 
        #Lock in amplifier, waveform generator, and reference hall effect flow
        #meter. Note the reference flow meter is recorded using a LabJack U3-LV
        #DAQ. If you wish to use a different device, you will have to edit this
        #code
        
        import matplotlib.pyplot as plt
        import os
        import glob
        import csv
        import numpy as np
        import time
        import u3
        import datetime
        global date
        date = datetime.datetime.now()
        
        cwd = os.getcwd()
        
        #Define and intialize the LabJack U3-LV device
        dev = u3.U3()
        dev.configIO(FIOAnalog=0xFF, EIOAnalog=0xFF) #Configure all inputs to analog.
        
        
        def MakeFile(path,fileName):
            #This function will create a .csv file of the data for this 
            #experiment. You must specify where you would like to save the 
            #file and its name. If the file exists there will be and _# added 
            #to the file. This will prevent data being overwritten.
            
            if not os.path.exists(path): #If the file does not exist create one.
                os.makedirs(path)               
                print( "The file "+ str(path) +" has been created")    

            os.chdir(path)		#Set directory to the path specifid.
            list =glob.glob("*.csv")	#Find all .csv files in .
            
            #If the file name exists add an _# to the end of the file.
            i = 1
            length = len(fileName)
            for j in list:		
                if j[:length] == fileName:	
                    i = i+1			
            newname2= path + fileName + '_' + str(i) + '.csv'
            return newname2
        

        print('Experiment Date:' + ' ' + date.strftime('%a, %d/%m/%Y'))
        print('Experiment Time: ' + date.strftime('%I:%M %p'))
        print('Experiment Equipment: ' + ID_gen)
        print('                      ' + ID_lockin)
        print('                      ' + ID_lockin_2)

        data = MakeFile(fileName, path) #Create a .csv data file
        
        header = ['Freq','Vpp_gen', 'V_Mag_S1','Phase_S1','V_Mag_S2','Phase_S2'
                  ,'S1-S2','Flow_Rate (gal/min)','Time']    #if you are using 
                                                    #different headers please 
                                                    #change this line of code
        print('Frequency    Mag_S1    Phase_S1    Mag_S2   Phase_S2' +        
               '   S1-S2   Vpp_Gen     Time'+    
               '   Flow_Rate (gal/min)')
        
        with open(data, 'w', encoding='UTF8', newline='') as f:    
            writer = csv.writer(f)
            writer.writerow(['Experiment Date:' + ' ' + date.strftime('%a, %d/%m/%Y')])
            writer.writerow(['Experiment Time: ' + date.strftime('%I:%M %p')])
            writer.writerow(['Experiment Equipment: '])
            writer.writerow([ID_gen])
            writer.writerow([ID_lockin])
            writer.writerow([ID_lockin_2])
            writer.writerow(header) #Write the header of your .csv file
        
            WaveGen.set_freq(freq) #Set the frequency of waveform gen
            WaveGen.set_voltage(Vpp, offset) #Set voltage of waveform gen
            
            WaveGen.output_on() #Turn the waveform gen on
            
            t = np.arange(start,stop,step)
            t_start = time.time()
            
            if plot == True:
                #Initalize ploting values
                flow_plt = []
                voltage_plt_1 = []
                voltage_plt_2 = []
                gal_min=0
                amp=0
            
            for i in range(len(t)+1):
                #This is where the measurment takes place for lock in
                amp=float(lockin.query("OUTP? 3"))	#Get ampliture of signal from lockin #1
                phase=float(lockin.query("OUTP? 4")) #Get phase of signal from lockin #1
                
                amp_2=float(lockin_2.query("OUTP? 0"))	#Get ampliture of signal from lockin #2
                phase_2=float(lockin_2.query("OUTP? 3")) #Get phase of signal from lockin #2
                
                amp_diff = amp-amp_2
                
                #This is where measurment will take place for reference device
                n = n #Set averageing constant for flow calcuation
                count = 0 #Initalize the count for flow calculation
                flow_data = []
                start_time = time.time()
                
                for j in range(n):
                    flow = dev.getAIN(AIN) #Get flow voltage measurment from LabJack U3
                    flow_data.append(flow) #Save voltage to data set
                    count = np.sum(np.diff(flow_data) > 1) #Count if pulse (i.e. strong change in voltage)
                    #time.sleep(step/n) #This is my ISSUE
                end = time.time()

                freq_flow = count/(end-start_time) #Calculate frequncy of pulses
                
                if freq_flow < 3:
                    flow_rate = 0
                else:
                    flow_rate = 0.146*freq_flow + 1.2435# Calculate flow rate GPM
                gal_min = flow_rate
                
                t_iter_end = time.time() 
                t_iter  = t_iter_end - t_start
                
                #Print the current time step the user
                print('   ' + str(freq) + '        ' + str(round(amp,3)) + '     '
                  + str(round(phase,0)) + '      ' + str(round(amp_2,3)) + '      ' + 
                  str(round(phase_2,0)) + '     ' + str(round(amp_diff,3)) + '     ' +
                  str(round(Vpp,2)) + '      ' +
                  str(round(t_iter,2)) + '           ' + str(round(gal_min,2)))
               
                #Save the data to .csv file
                writer.writerow([freq,Vpp,amp,phase,amp_2,phase_2,amp_diff,\
                                 round(gal_min,2),\
                                 round(t_iter,2)]) #Write data to new line on .csv file
                
                #If you want plot the data while measuring
                if plot == True:
                    #Note this plot is specific for the water flow loop in our 
                    #lab. Please change the function if you would like to plot
                    #some other data.
                    flow_plt.append(gal_min)
                    voltage_plt_1.append(amp*1000)
                    voltage_plt_2.append(amp_2*1000)
                    voltage_diff = np.array(voltage_plt_1)-np.array(voltage_plt_2)
                    
                    #Please add model data if you would like to fit data
                    #that you are measuring to a model in real time.
                    flow_plt.append(gal_min)

                    plt.figure(figsize = (12,6), dpi = 300)
                    plt.plot(y_model,x_model, '--r')
                    plt.plot(flow_plt,voltage_diff,'b*')
                    plt.xlabel(xlable, fontsize = 12)
                    plt.ylabel(ylable, color = 'k', fontsize = 12)
                    plt.title(title, color = 'k', fontsize = 16)
                    plt.show()
                   
                #Wait for next time step
                time.sleep(step)
                
            os.chdir(cwd) #set directory back to where module is located
            
    def FreqSweep(fileName,path,freq,Vpp,offset, f_start, f_stop, f_step, 
                  time_const, plot=False, xlable=None, 
                  ylable=None, title=None, y_model=None, 
                  x_model=None):
        #This function will measure and record data for a frequency sweep using 
        #a Lock in amplifier, and waveform generator.
        import matplotlib.pyplot as plt
        import os
        import glob
        import csv
        import numpy as np
        import time
        import datetime
        global date

        date = datetime.datetime.now()
        
        cwd = os.getcwd()
        
        def MakeFile(path,fileName):
            #This function will create a .csv file of the data for this 
            #experiment. You must specify where you would like to save the 
            #file and its name. If the file exists there will be and _# added 
            #to the file. This will prevent data being overwritten.
            
            if not os.path.exists(path): #If the file does not exist create one.
                os.makedirs(path)               
                print( "The file "+ str(path) +" has been created")    

            os.chdir(path)		#Set directory to the path specifid.
            list =glob.glob("*.csv")	#Find all .csv files in .
            
            #If the file name exists add an _# to the end of the file.
            i = 1
            length = len(fileName)
            for j in list:		
                if j[:length] == fileName:	
                    i = i+1			
            newname2= path + fileName + '_' + str(i) + '.csv'
            return newname2
        
        #Define an array of the frequencies being sweept
        f_sweep = np.arange(start = f_start, stop = f_stop,step = f_step)
    
        print('Experiment Date:' + ' ' + date.strftime('%a, %d/%m/%Y'))
        print('Experiment Time: ' + date.strftime('%I:%M %p'))
        print('Experiment Equipment: ' + ID_gen)
        print('                      ' + ID_lockin)
        data = MakeFile(fileName, path) #Create a .csv data file
        
        header = ['Freq','Vpp_gen', 'V_Mag','Phase','Flow_Rate (gal/min)','Time'] #if you are using 
                                                    #different headers please 
                                                    #change this line of code
        print('Frequency         Mag      Phase (Deg)         Vpp_Gen')
        
        with open(data, 'w', encoding='UTF8', newline='') as f:    
            writer = csv.writer(f)
            writer.writerow(['Experiment Date:' + ' ' + date.strftime('%a, %d/%m/%Y')])
            writer.writerow(['Experiment Time: ' + date.strftime('%I:%M %p')])
            writer.writerow(['Experiment Equipment: '])
            writer.writerow([ID_gen])
            writer.writerow([ID_lockin])
            writer.writerow(header) #Write the header of your .csv file
        
            WaveGen.set_freq(freq) #Set the frequency of waveform gen
            WaveGen.set_voltage(Vpp, offset) #Set voltage of waveform gen
            
            WaveGen.output_on() #Turn the waveform gen on
            
            t_start = time.time()
            
            if plot == True:
                #Initalize ploting values
                freq_plt = []
                voltage_plt = []
                phase_plt = []
                
            for i in range(len(f_sweep)):
                WaveGen.set_freq(f_sweep[i]) #set waveform gen to new frequency
                
                Lockin.time_const(time_const) #set lockin time constant
                Lockin.source(1000000, "SIN", 'EXT', 4, 0)
                
                time.sleep(5*time_const) #Allow for lockin to settel for 5 
                                         # time constants
                                         
                #This is where the measurment takes place for lock in
                amp=float(lockin.query("OUTP? 3"))	#Get ampliture of signal from lockin
                phase=float(lockin.query("OUTP? 4")) #Get phase of signal from lockin
                
                t_iter_end = time.time() 
                t_iter  = t_iter_end - t_start
                
                #Print the current time step the user
                print('   ' + str(freq) + '         ' + str(amp) + '        '
                  + str(phase) + '           ' + str(Vpp) + '          ' + 
                  str(round(t_iter,2)))
               
                #Save the data to .csv file
                writer.writerow([freq,Vpp,amp,phase,round(t_iter,2)]) #Write data to new line on .csv file
                
                #If you want plot the data while measuring
                if plot == True:
                    #Please add model data if you would like to fit data
                    #that you are measuring to a model in real time.
                    freq_plt.append(f_sweep[i])
                    voltage_plt.append(amp*1000)
                    phase_plt.append(phase)
                    
                    plt.figure(figsize = (12,6), dpi = 300)
                    
                    plt.subplot(1,2,1)
                    plt.plot(freq_plt,phase_plt, 'g*')
                    plt.xlabel('Frequency [Hz]', fontsize = 12)
                    plt.ylabel('Phase [Deg]', color = 'k', fontsize = 12)
                    plt.title('Frequency Sweep', color = 'k', fontsize = 16)
                    
                    
                    plt.subplot(1,2,2)
                    plt.plot(y_model,x_model, '--r')
                    plt.plot(freq_plt,voltage_plt,'b*')
                    plt.xlabel('Frequency [Hz]', fontsize = 12)
                    plt.ylabel('Voltage [mV]', color = 'k', fontsize = 12)
                    plt.title('Voltage Output', color = 'k', fontsize = 16)
                    
                    plt.show()
                    
            os.chdir(cwd) #set directory back to where module is located
                
                
        
        
        
        
        
        
        
        
        