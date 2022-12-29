import os,time

def cleaner():
        temp = os.listdir("static/temp")
        if len(temp) != 0 :
            print(True)
            for file in temp:
              if file != "ignore":
                    os.remove("static/temp/"+ file)
                    time.sleep(.1)

        else:
            print(False)
    
