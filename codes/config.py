import codes.parameters as pt

def getLoad(command):
    if command[0] == 'setres':
        pt.setResolution(command[1])
        return f"Resolution set to {command[1]}dpi successfully."
    elif command[0] == 'setbg':
        pt.setBackgroundColour(command[1])
        return f"Background colour set to {command[1]} successfully."
    elif command[0] == 'settc':
        pt.setTextcolour(command[1])
        return f"Text colour set to {command[1]} successfully"
    elif command[0] == 'setm':
        pt.setMargin(command[1])
        return f"Margins set to {command[1]} successfully."
    elif command[0] == 'seto':
        pt.setOpacity(command[1])
        return f"Opacity set to {command[1]} successfully."
    elif command[0] == 'getall':
        return f"""Resolution: {pt.getResolution()}
Background Colour: {pt.getBackgroundColour()}
Text Colour: {pt.getTextcolour()}
Margins: {pt.getMargin()}
Opacity: {pt.getOpacity()}"""
    elif command[0] == 'getres':
        return f"Resolution set to {pt.getResolution()}dpi."
    elif command[0] == 'getbg':
        return f"Background colour set to {pt.getBackgroundColour} successfully."
    elif command[0] == 'gettc':
        return f"Text colour set to {pt.getTextcolour} successfully"
    elif command[0] == 'getm':
        return f"Margins set to {pt.getMargin} successfully."
    elif command[0] == 'geto':
        return f"Opacity set to {pt.getOpacity} successfully."