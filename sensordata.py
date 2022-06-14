def getValue(sensor):
    '''
    this will give you the value read on an i2c pin attached to the adc
    
    the channels that can be input are:
        -0x10
        -0x20
        -0x40
        -0x80
    '''
    import smbus
    from bitswitch import bitswitcher
    
    I2CADDR = 0x21
    bus = smbus.SMBus(1)

    bus.write_byte( I2CADDR, sensor )
    value = bus.read_word_data( I2CADDR, sensor )
    return bitswitcher(value)

def getalldata(n, heart, conduct, temp, breath, yellow, red):
    from csvhandler import writetofile
    from redyellowbuttons import yellowPressed, redPressed
    for _ in xrange(16):
        heart.newvalue(getValue(0x40))
        conduct.newvalue(getValue(0x80))
        temp.newvalue(getValue(0x20))
        breath.newvalue(getValue(0x10))
        if yellowPressed():
            yellow.newvalue(100)
        else:
            yellow.newvalue(0)
        if redPressed():
            red.newvalue(100)
        else:
            red.newvalue(0)
        writetofile(yellow.lastvalue, red.lastvalue, breath.lastvalue, heart.lastvalue, conduct.lastvalue, temp.lastvalue)
        n += 1
        
        