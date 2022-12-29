import os



def file_avalable(file):
    
    temp = os.listdir('static/temp')
    temp2 = []
    for fil in temp:
        base, ext = os.path.splitext(fil)
        temp2.append(base)
    if file in temp2:
        return True
    else:
        return False
    
