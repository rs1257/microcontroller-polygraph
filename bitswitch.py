def bitswitcher(x):
   
    lowbyte = x >> 8
    highbyte = x << 8

    result = (highbyte | lowbyte) & 0xFFF
    
    return result
   
