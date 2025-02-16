# Function to convert DMS integer format to decimal degrees
def dms_to_dd(dms):

    dms_tmp = abs(dms)
    
    seconds = dms_tmp - (dms_tmp // 10000) * 10000 
    
    minutes = (dms_tmp - seconds - ((dms_tmp - seconds) // 10000000) * 10000000) // 10000

    degrees = (dms_tmp - seconds - (minutes * 10000)) // 10000000

    seconds = seconds / 1000

    minutes = minutes / 10
    
    # Convert to decimal degrees
    dd = degrees + minutes / 60 + seconds / 3600
    
    return -dd if dms < 0 else dd  # Handle negative values for south/west

