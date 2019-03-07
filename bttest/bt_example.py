# it seems that what you need is the bluetooth facade. 
# Here are some commands pertaining to bluetooth that might be helpful to you:
'''
bluetoothAccept
bluetoothActiveConnections
bluetoothConnect
bluetoothDiscoveryCancel
bluetoothDiscoveryStart
bluetoothGetConnectedDeviceName
bluetoothGetLocalAddress
bluetoothGetLocalName
bluetoothGetRemoteDeviceName
bluetoothGetScanMode
bluetoothIsDiscovering
bluetoothMakeDiscoverable
bluetoothRead
bluetoothReadBinary
bluetoothReadLine
bluetoothReadReady
bluetoothSetLocalName
bluetoothStop
bluetoothWrite
bluetoothWriteBinary
checkBluetoothState
toggleBluetoothState
'''

# To call any of these commands you would do something like
'''
import android
droid = android.Android()
#call your commands with droid.bluetoothcommand
droid.bluetoothDiscoveryStart()
#or
droid.toggleBluetoothState(True)
'''


# Here is an example of some bluetooth functions,
# it is included with SL4A, but I added the comments for clarity:

'''
import android #for bluetooth functions
import time #for waiting

#get everything setup
droid = android.Android()

#turn on bluetooth
droid.toggleBluetoothState(True)

#ask user
droid.dialogCreateAlert('Be a server?')
droid.dialogSetPositiveButtonText('Yes')
droid.dialogSetNegativeButtonText('No')
droid.dialogShow()

#get user response to question
result = droid.dialogGetResponse()

#if the result is 'Yes' ('positive') then is_server is set to True
is_server = result.result['which'] == 'positive'

if is_server:
  #so if is_server is true make the device discoverable and accept the next connection
  droid.bluetoothMakeDiscoverable()
  droid.bluetoothAccept()
else:
  #attempts to connect to a device over bluetooth, the logic being that if the phone
  #is not receiving a connection then the user is attempting to connect to something
  droid.bluetoothConnect()


if is_server:
  result = droid.getInput('Chat', 'Enter a message').result #Gets a message to send 
  #via bluetooth
  if result is None:
    droid.exit() #exit if nothing is in the message
  droid.bluetoothWrite(result + '\n') #otherwise write the message

while True: #receives a message
  message = droid.bluetoothReadLine().result
  droid.dialogCreateAlert('Chat Received', message)
  droid.dialogSetPositiveButtonText('Ok')
  droid.dialogShow()
  droid.dialogGetResponse()
  result = droid.getInput('Chat', 'Enter a message').result
  if result is None:
    break
  droid.bluetoothWrite(result + '\n')

droid.exit()
 '''