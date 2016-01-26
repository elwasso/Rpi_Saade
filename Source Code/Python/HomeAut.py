import RPi.GPIO as GPIO
import smtplib
from time import sleep

#Set Mapping mode
GPIO.setmode(GPIO.BCM)

#Setting Outputs
# 5		-->	Electric Heater
# 6		-->	Diesel Heater
# 13    -->	Washing Machine
EH=5
DH=6
WM=13
op =[EH,DH,WM]

#Create Status Array
# statOp=[0,0,0]

#Settign Inputs
# 12 --> EDL
# 16 --> Genset
EDL=12
GST=16
iEH=23
iDH=24
iWM=25
ip =[EDL,GST,iEH,iDH,iWM]

#Set outputs and initialize them to off upon start
for pn in op:
	GPIO.setup(pn,GPIO.OUT, initial=GPIO.HIGH)

#Set Inputs and add pull down resistor
for pn in ip:
	GPIO.setup(pn,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

#Initialize previous values
pEDL=GPIO.input(EDL)
pGST=GPIO.input(GST)

#This code assumes the pririty is for EDL

def SendmeEmail(Src):
	smtpUser = 'wasaadeh@gmail.com'
	smtpPass = 'Wasnouna.305'

	toAdd = ['wasaadeh@gmail.com', 'antoun.nayla@gmail.com']
	fromAdd = smtpUser

	subject = 'Back Home ' + str(Src)
	header = 'To: ' + ", ".join(toAdd) + '\n' + 'From: ' + '\n' + 'Subject: ' + subject
	#body = 'From within a python script ' + str(Src)

	
	s= smtplib.SMTP('smtp.gmail.com',587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(smtpUser, smtpPass)
	s.sendmail(fromAdd, toAdd, header + '\n\n')
	s.quit()

#Send an email to mark a restart
SendmeEmail("Raspberry Pi just Started")


def TurnOutputsOff():
	for pn in op:
		GPIO.output(pn,1)

# def TurnOutputsOn():
# 	for pn in op:
# 		si = ReadStatus(pn)
# 		GPIO.output(pn,int(si))

# def SaveStatus(OPT):
# 	f = open("/var/www/Raspberry/txtFiles/st" + str(OPT) + ".txt", "w")
# 	a = GPIO.input(OPT)
# 	f.write(str(a))

def ReadStatus(OPT):
	f = open("/var/www/Raspberry/txtFiles/st" + str(OPT) + ".txt", "r")
	sta = f.read()
	std=int(sta)
	f.close()
	return std


#Set values on restart same as text files
if pEDL :
	for pn in op:
		ii = ReadStatus(pn)
		GPIO.output(pn,1-ii)

#Check if a button is pressed for more than the set value
def ManualTurnOn(IPT):

	print("Entered Manual Turn On loop " + str(IPT) +" "+ str(GPIO.input(IPT)))

	pressed = 1
	pressedOK = 0
	counter = 0
	while ( pressed == 1 ):
		if ( GPIO.input(IPT) == True ):
			# button is still pressed
			counter = counter + 1

			# break if we count beyond 20 (long-press is a shutdown)
			if (counter >= 20):
				pressed = 0
				pressedOK = 1
			else:
				sleep(0.05)
		else:
			# button has been released
			pressed = 0

	if pressedOK == 1:
		if IPT ==iEH:
			if not GPIO.input(EH):
				GPIO.output(EH, True)
			else:
				GPIO.output(EH, False)
			
		elif IPT == iDH:
			if not GPIO.input(DH):
				GPIO.output(DH, True)
			else:
				GPIO.output(DH, False)

		elif IPT == iWM:
			if not GPIO.input(WM):
				GPIO.output(WM, True)
			else:
				GPIO.output(WM, False)
			

#Define the functions to execute when inputs are detected
def genCallback(sEDL, sGST):
	global pEDL
	global pGST
	#Variable to check if something changed
	st = False
	txt_1 =""
	txt_2 =""
	stat =" "
	fstat=""

	#print("Entered loop " + str(sEDL) +", "+ str(sGST))
	if (sEDL != pEDL):
		st = True
		if not sEDL :
			TurnOutputsOff()
			txt_1="EDL is now OFF, turning everything off "
			stat=" 000"
		elif sEDL :
			for pn in op:
				ii = ReadStatus(pn)
				GPIO.output(pn,1-ii)
				stat = stat + str(ii)
			txt_1="EDL is now ON, "
			
		pEDL = sEDL

	if (sGST != pGST):
		st = True
		if not sGST :
			txt_2="GST is now OFF"
		elif sGST :
			ii=ReadStatus(6)
			GPIO.output(6,1-ii)
			if ii == 1:
				txt_2="GST is now ON, Diesel Heater is ON"
			else:
				txt_2="GST in now ON"
		pGST = sGST
		if stat == " " :
			stat=" 000"

	if st:
		if stat[1] == "1" :
			fstat= " |Electric Heater is now ON |"
		if stat[2] == "1" :
			fstat=fstat + " | Diesel Heater is now ON |"
		if stat[3] == "1" :
			fstat = fstat +" | Washing Machine is now ON"
		SendmeEmail(txt_1 + txt_2 + fstat)

			
#Set callback functions
#GPIO.add_event_detect(EDL, GPIO.BOTH, callback=genCallback, bouncetime=200)
#GPIO.add_event_detect(GST, GPIO.BOTH, callback=genCallback, bouncetime=200)

GPIO.add_event_detect(iEH, GPIO.RISING, callback=ManualTurnOn, bouncetime=100)
GPIO.add_event_detect(iDH, GPIO.RISING, callback=ManualTurnOn, bouncetime=100)
GPIO.add_event_detect(iWM, GPIO.RISING, callback=ManualTurnOn, bouncetime=100)

while 1:

	try:
		#Current Values
		cEDL=GPIO.input(EDL)
		cGST=GPIO.input(GST)

		genCallback(cEDL,cGST)
		sleep(5)

	except KeyboardInterrupt:
		GPIO.cleanup()