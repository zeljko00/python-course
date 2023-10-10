from inspect import currentframe, getframeinfo
print("===========================WITH EXCEPTION==========================")
try:
    print(getframeinfo(currentframe()).lineno," : ","Entered try block!")
    print(getframeinfo(currentframe()).lineno," : ","Executing logic!")
    print(getframeinfo(currentframe()).lineno," : ","Exiting try block!")
except:
    print(getframeinfo(currentframe()).lineno," : ","Entering except block!")
    print(getframeinfo(currentframe()).lineno," : ","Handling exception!")
    print(getframeinfo(currentframe()).lineno," : ","Exiting except block!")
else:
    print(getframeinfo(currentframe()).lineno," : ","Entering else block!")
    print(getframeinfo(currentframe()).lineno," : ","No exception was raised!")
    print(getframeinfo(currentframe()).lineno," : ","Exiting else block!")
finally:
    print(getframeinfo(currentframe()).lineno," : ","Entering finally block!")
    print(getframeinfo(currentframe()).lineno," : ","Executing logic independent of whether exception was raised or not!")
    print(getframeinfo(currentframe()).lineno," : ","Exiting finally block!")

print("=========================WITHOUT EXCEPTION=========================")
try:
    print(getframeinfo(currentframe()).lineno," : ","Entered try block!")
    print(getframeinfo(currentframe()).lineno," : ","Executing logic!")
    raise Exception()
    print(getframeinfo(currentframe()).lineno," : ","Exiting try block!")
except:
    print(getframeinfo(currentframe()).lineno," : ","Entering except block!")
    print(getframeinfo(currentframe()).lineno," : ","Handling exception!")
    print(getframeinfo(currentframe()).lineno," : ","Exiting except block!")
else:
    print(getframeinfo(currentframe()).lineno," : ","Entering else block!")
    print(getframeinfo(currentframe()).lineno," : ","No exception was raised!")
    print(getframeinfo(currentframe()).lineno," : ","Exiting else block!")
finally:
    print(getframeinfo(currentframe()).lineno," : ","Entering finally block!")
    print(getframeinfo(currentframe()).lineno," : ","Executing logic independent of whether exception was raised or not!")
    print(getframeinfo(currentframe()).lineno," : ","Exiting finally block!")