#date 5/5/18
#working file
#gsm gps and gui

#Imports
from Tkinter import *
import os
import serial 
import time 
import RPi.GPIO as GPIO
from gpiozero import Buzzer
import random

#ui file name
creds = 'tempfile.txt' # This just sets the variable creds to 'tempfile.temp'

#buzzer setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.OUT)
buzzer = Buzzer(20)

#Check GSM is working
port = serial.Serial("/dev/ttyS0", 9600, timeout=3.0) 
print"GSM 300\n" 
print"List of operating Commands" 
print"Commands		functions" 
print"AT	to check operations" 
port.write('AT\r')		
rcv = port.read(20) 
print"GSM" + rcv

#Complete GPS
logvalfile=open('gpsvaluelog.txt','wb')
new=open('newgps.txt','wb')
logfile=open('gpslog.txt','wb')
port = serial.Serial("/dev/ttyS0", 9600, timeout=3.0)
port.flushInput()
port.flushOutput()
rcvdfile=port.read(1200)
pos1 = rcvdfile.find("$GPRMC")
pos2 = rcvdfile.find("\n",pos1)
loc = rcvdfile[pos1:pos2]
logfile.write(rcvdfile)
data = loc.split(',')
print(data)
pos11 = rcvdfile.find("$GPGGA")
pos22 = rcvdfile.find("\n",pos11)
loc1 = rcvdfile[pos11:pos22]
data1 = loc1.split(',')
if data[2]=='V':
	print 'No location found'
else:
	
	#print "UTC time="+data[1]+" UTC date=" + data[9]
    	gps_time=float(data[1])
    	gps_date=float(data[9])
		
    	gps_hour=int(gps_time/10000.0)
	gps_min= gps_time%10000.0
	gps_sec=gps_min%100.0
	gps_min=int(gps_min/100.0)
	gps_sec=int(gps_sec)
	
	gps_dd=int(gps_date/10000.0)
	gps_mm= gps_date%10000.0
	gps_yy=gps_mm%100.0
	gps_mm=int(gps_mm/100.0)
	gps_yy=int(gps_yy)

	print 'time=',gps_hour,':',gps_min,':',gps_sec
	
	print 'date=',gps_dd,'/',gps_mm,'/',gps_yy
		
	print "Latitude = "+data[3]+data[4]
	print "Longitude = "+data[5]+data[6]
	latact=float(data[3])
	longact=float(data[5])
		
	print "Speed = "+data[7]
	print "Course = "+data[8]
	print "\n"

	gps_time_gga=float(data1[1])
	gps_hour_gga=int(gps_time_gga/10000.0)
	gps_min_gga= gps_time_gga%10000.0
	gps_sec_gga=gps_min_gga%100.0
	gps_min_gga=int(gps_min_gga/100.0)
	gps_sec_gga=int(gps_sec_gga)
		
	new.write(data[8])
	print 'time=',gps_hour_gga,':',gps_min_gga,':',gps_sec_gga
				
	print "Latitude = "+data1[2]+data1[3]
	print "Longitude = "+data1[4]+data1[5]
	print "Satellites used= "+data1[7]
	print "Altitude = "+data1[9]
	print "\n"
	print(data1[2])
	lat=data1[2]
	a=lat[5:7]+'.'+lat[7:]
        b=lat[2:5]
        b=float(b)/60
	c=lat[0:2]
        c=float(c)
	a=float(a)/3600
	print(type(a) , type(b), type(c))
	print (lat[0:2])
	t = a+b+ c
	print(data1[4])
              
        long=data1[4]
	d=long[6:8]+'.'+long[8:]
        e=long[2:5]
        e=float(e)/60
	f=long[0:2]
        f=float(f)
	d=float(d)/3600
	print(type(d) , type(e), type(f))
	print (long[1:2])
	
	te = d+e+f
	print(te)
	arg=str(t)+','+str(te)
		
	logvalfile.write("\n"+'time='+str(gps_hour)+':'+str(gps_min)+':'+str(gps_sec)+"\n"+'date='+str(gps_dd)+'/'+str(gps_mm)+'/'+str(gps_yy)+"\n")
	logvalfile.write("\n"+"Latitude = "+data[3]+data[4]+"\n"
	+"Longitude = "+data[5]+data[6]+"\n"+"Speed = "+data[7]+"\n"
	+"Course = "+data[8]+"\n"+"Latitude = "+data1[2]+data1[3]+"\n"
	+ "Longitude = "+data1[4]+data1[5]+"\n"+ "Satellites used= "+data1[7]+"\n"
	+ "Altitude = "+data1[9])
port.flushInput()
port.flushOutput()

#GUI functions
def Signup(): # This is the signup definition, 
    global pwordE # These globals just make the variables global to the entire script, meaning any definition can use them
    global nameE
    global emergency
    global roots
    
 
    roots = Tk() # This creates the window, just a blank one.
    roots.title('Signup') 
    roots.geometry('1600x900')# This renames the title of said window to 'signup'
    roots.configure(background='#ffcccc')

    image=PhotoImage(file="images.png")
    # label1.grid(row=0, column = 0, rowspan = 2, sticky=NW)
    
    label2 = Label(roots,image=image)
    label2.image = image 
    
    
    intruction = Label(roots, text='Please Enter Credidentials\n',bg='#ffcccc',fg="#e6005c") 
    intruction.config(font=("roboto", 35))# This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=1, column=0, sticky=E) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)
 
    nameL = Label(roots, text='New Username: ',fg="#e6005c", bg='#ffcccc') # This just does the same as above, instead with the text new username.
    pwordL = Label(roots, text='New Password: ',fg="#e6005c",bg='#ffcccc') # ^^
    emergencyL = Label(roots, text='Emergency contact: ',fg="#e6005c",bg='#ffcccc')
    nameL.config(font=("roboto", 25))
    pwordL.config(font=("roboto", 25))
    emergencyL.config(font=("roboto", 25))
    nameL.grid(row=2, column=0, sticky=W) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    pwordL.grid(row=3, column=0, sticky=W) # ^^
    emergencyL.grid(row=4, column=0, sticky=W)
 
    nameE = Entry(roots) # This now puts a text box waiting for input.
    pwordE = Entry(roots, show='*') # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    emergency = Entry(roots)

    nameE.config(font=("roboto", 25))
    pwordE.config(font=("roboto", 25))
    emergency.config(font=("roboto", 25))
    nameE.grid(row=2, column=1) # You know what this does now :D
    pwordE.grid(row=3, column=1) # ^^
    emergency.grid(row=4, column=1) 
    
    signupButton = Button(roots, text='Signup',bg='#ffcccc',fg="purple", command=FSSignup) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.config(font=("roboto", 30,"bold"))
    signupButton.grid(row=5,column=1, sticky=W)
    label2.grid(row=0, column = 1, sticky=NW)
    roots.mainloop() # This just makes the window keep open, we will destroy it soon
 
def FSSignup():
    with open(creds, 'w') as f: # Creates a document using the variable we made at the top.
        f.write(nameE.get()) # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
        f.write('\n') # Splits the line so both v
        #variables are on different lines.
        f.write(pwordE.get()) # Same as nameE just with pword var
        f.write('\n')
        f.write(emergency.get())
        f.close() # Closes the file
       
    print(emergency.get())
 
    roots.destroy() # This will destroy the signup window. :)
    Login() # This will move us onto the login definition :D
 
def Login():
    global nameEL
    global pwordEL # More globals :D
    global rootA
    # global cancel

    rootA = Tk() # This now makes a new window.
    rootA.title('Login') # This makes the window title 'login'
    rootA.geometry('1600x900')
    rootA.configure(background='#ffcccc')

    img=PhotoImage(file="images.png")
    # label1.grid(row=0, column = 0, rowspan = 2, sticky=NW)
    
    label3 = Label(rootA,image=img)
    label3.image = img
 
    intruction = Label(rootA, text='Please Login\n',fg="#e6005c",bg='#ffcccc') # More labels to tell us what they do
    intruction.config(font=("roboto", 25))
    intruction.grid(row=1,column=0,sticky=E) # Blahdy Blah
 
    nameL = Label(rootA, text='Username: ',fg="#e6005c",bg='#ffcccc') # More labels
    pwordL = Label(rootA, text='Password: ',fg="#e6005c",bg='#ffcccc') # 
    nameL.config(font=("roboto", 25))
    pwordL.config(font=("roboto", 25))
    nameL.grid(row=2, sticky=W)
    pwordL.grid(row=3, sticky=W)
 
    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.config(font=("roboto", 25))
    pwordEL.config(font=("roboto", 25))
    nameEL.grid(row=2, column=1)
    pwordEL.grid(row=3, column=1)
 
    loginB = Button(rootA, text='Login', command=CheckLogin, fg="purple",bg='#ffcccc') # This makes the login button, which will go to the CheckLogin def.
    loginB.config(font=("roboto", 30,"bold"))
    loginB.grid(row=5,column=1, sticky=W)
    label3.grid(row=0, column = 2, sticky=NW)
    # rmuser = Button(rootA, text='Delete User', fg='red', command=DelUser) # This makes the deluser button. blah go to the deluser def.
    # rmuser.grid(columnspan=2, sticky=W)
    rootA.mainloop()
 
def CheckLogin():
    with open(creds) as f:
        data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
        e=data[2].rstrip()
        print(e)
    if nameEL.get() == uname and pwordEL.get() == pword: # Checks to see if you entered the correct data.
        rootA.destroy()
        r = Tk() # Opens new window
        r.title('Logged In')
        r.geometry('1600x900')
        r.configure(background='#ffcccc') # Makes the window a certain size
        # rlbl = Label(r, text='\n[+] Logged In') # "logged in" label
        # photo=PhotoImage(file='heart.png')
        # label=Label(r,image=photo)\
        # rootA.configure(background='#ffcccc')
        count1=140
        image=PhotoImage(file="heart.png")
        label1 = Label(image=image).pack(side="top")
        # label1.image = image 
        # label1.grid(row=0, column = 0, rowspan = 2, sticky=NW)
     
        # count1=0
        count=random.randint(68,80)
        # count=80
        time.sleep(60)
        x= Label(r, text="Heartbeat(in bpm):",fg="#e6005c",bg='#ffcccc')
        x.config(font=("roboto", 12))
        x.pack(side="left")
        y= Label(r, text=count,fg="#e6005c",bg='#ffcccc') # More labels
        y.config(font=("roboto", 12))
        y.pack(side="left")
        # for x in range(10):
        #         c=random.randint(68,80)
        #         x= Label(r, text="Heartbeat(in bpm):")
        #         y= Label(r, text=c) # More labels
        #         x.grid(row=count1,column=1, sticky=E)
        #         y.grid(row=count1,column=30, sticky=E)
        #         count1=count1+1
        # for x in range(7):
        #         x= Label(r, text="Heartbeat(in bpm):")
        #         y= Label(r, text=count) # More labels
        #         x.grid(row=count1,column=1, sticky=E)
        #         y.grid(row=count1,column=30, sticky=E)
        #         count1=count1+1
        # label.grid(row=1,column=1, sticky=W)
        #x.grid(row=1,column=2, sticky=E)
        #y.grid(row=2,column=2, sticky=E)
        # label.pack() # Pack is like .grid(), just different
        
        if(count>70):
            global n
            global cancel
            
            time.sleep(10)
            buzzer.on()
            time.sleep(1)
            buzzer.off()
            
            
            n = Toplevel()
            n.geometry('1600x900')
            n.title("sending message...")
            n.configure(background='#ffcccc')
            txt= Label(n, text="sending message to emergency contact number  "+e,fg="#e6005c",bg='#ffcccc')
            txt.config(font=("roboto", 30,"bold"))
            txt.pack(side="top")
                # canvas=Canvas(n,width=500,height=500)
                # canvas.pack()
            image3=PhotoImage(file="mssg1.png")
            # label3 = Label(image=image3).pack(side="top")
            optimized_canvas = Canvas(n,width=50, height=50,bg='#ffcccc')
            optimized_canvas.pack(fill=BOTH, expand=1)
            optimized_image = optimized_canvas.create_image(500,250, anchor=NW, image=image3)
            
            try:
                print "Sending Message...."
                #msg1 = "Emergency http://www.google.com/maps/place/28.6645460,77.2323220"
                msg1 = "Emergency http://www.google.com/maps/place/49.46800006494457,17.11514008755796"
                ms='emergency'
                #port.write('AT+CMGF=1'+'\r')
                #port.write('AT+CMGF=1'+'\r')
                #number = raw_input("Enter Mobile: ")
                port.write('AT+CMGS="'+e+'"\r')
                time.sleep(2)
                port.write(msg1)
                time.sleep(2)
                port.write('\x1A\r')
                
                print port.read(50)
            except:
                port.close()

            # gsm(msg1)
            # print(cancel)
            # cancel = Button(n, text='Cancel', command=CancelMessage) # This makes the login button, which will go to the CheckLogin def.
            # cancel.grid(columnspan=2, sticky=W)
            # print(cancel)
            n.mainloop() 
        r.mainloop()
              
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()
 
# def DelUser():
#     os.remove(creds) # Removes the file
#     rootA.destroy() # Destroys the login window
#     Signup() # And goes back to the start!
# def CancelMessage():
#      n.destroy() # This will destroy the cancel window. :)
   

if os.path.isfile(creds):
    Login()
else: # This if else statement checks to see if the file exists. If it does it will go to Login, if not it will go to Signup :)
    Signup()

os.system("gpsbabel -i NMEA -f gpslog.txt -o GPX -F gpslog.gpx")
os.system("gpsprune")  



