import time

print("TimeSpeedCalculator")
print("\nBased on time dilation")
uni = 3.09*10*18*700
mass = 150000000000000000000000000000000000000000000000000000
objmass = float(input("The Object's Mass (in kg however without placing the unit):  "))
state =  (objmass / uni + 1)
print(f"\nThe state of time is: if its 0, time is stopped. if one or above that, time is working. \nHOWEVER, if the object is more larger then the UNIVERSE itself. \nTime will go into a BROKEN STATE (NULL). \nThe STATE of TIME according to MASS is: {state}")
c = 299792458
void = c
equ = uni * mass * state + c / void
actualt = equ / 3600
print(f"The actual speed of time is: {actualt} billion seconds per seconds, 1s per s is 3600 seconds.")
time.sleep(5)
print("\n The delay of time is 3600 seconds but the speed is something else. \nHowever, the speed is affected due to time dilation. ")
print(f"The time dilation states that the speed of an object will affect the speed of time.")
time.sleep(5)
print("\nSuppose I send a kid at space at 99% {c} meters per seconds (or speed of light).\n And keep one on earth. \nThe one that is in space have time slower for him. \nSo when he returns to earth at age of 25.\n The one on earth would be ~100 years old.")
print("\nand 1 seconds per seconds is the delay it can get upto.")
time.sleep(5)
print("The speed is calculated by the formula of:")
print(f"\n Universe Expansion Speed * Mass of the UNIVERSE * STATE OF TIME * SPEED OF LIGHT / void. or: {uni} * {mass} * {state} + {c} / {void}")
print(f"\nVoid is also just 100% speed of light.")
time.sleep(5)
print("Everything is CAREFULLY RESEARCHED.\n My facts may be wrong. But i just cant prove myself.\n\n Made by @AlanCodes0 on YT or Alan.")
