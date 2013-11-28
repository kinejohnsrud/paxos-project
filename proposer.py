# coding=utf-8

myID = 3			# server ID
myValue = 7
proposalID = 0	
acceptedPromise = []
acceptedAccepted = []
majority = 3

proposalNum = 2

def prepare(post):
	global proposalID
	blogpost = post
	proposalID += 1
	propose = {'senderID': myID, 'proposalID' : proposalID}
	return propose


def receivePromise(accepted):
	global myValue
	global acceptedPromise
	acceptedPromise.append(accepted)
	if len(acceptedPromise) >= majority:
		for promise in acceptedPromise:
			if promise['proposalID'] != None and promise['value'] != None:
				 myValue = max(value['value'] for value in acceptedPromise)
		acceptedPromise = []
		return {'senderID': myID, 'proposalID' : proposalID, 'value' : myValue}
	return None


def receiveAccepted(accepted):
	global acceptedAccepted
	acceptedAccepted.append(accepted)
	if len(acceptedAccepted) >= majority:
		for accepted in acceptedAccepted:
			if accepted['value'] != myValue:
				return None
		return myValue
	return None





#acc = accept(None, None, None)
#acc2 = accept(None, 5, 6)
#acc3 = accept(None, None, None)
#print receivePromise(acc)
#print receivePromise(acc2)
#print receivePromise(acc3).value



