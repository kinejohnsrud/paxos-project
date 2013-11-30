# coding=utf-8
import math

serverID = 3			# server ID
myValue = ""
proposalID = serverID	# ProposalID increments 10 with each prepare. Last digit is the server ID
acceptedPromise = []
acceptedAccepted = []
notAcceptedPromise = []
majority = 3
maxProposalID = 0


def prepare(post):
	global proposalID
	global maxProposalID
	myValue = post 		# Set the local value to the received post-message
	maxProposalID += 10
	proposalID = math.floor(maxProposalID/10) * 10 + serverID
	
	propose = {'senderID': serverID, 'proposalID' : proposalID}
	return propose


def receivePromise(accepted):
	global myValue
	global acceptedPromise
	global maxProposalID
	global notAcceptedPromise
	
	# If we receive older proposal or a NACK, it shoud not count in the majority
	if accepted['type'] == "ACK": 
		acceptedPromise.append(accepted)
	elif accepted['type'] == "NACK":
		notAcceptedPromise.append(accepted)

	# If the majority consists of rejections (NACK), add the value to the front of Paxos-queue (restart)
	if len(notAcceptedPromise) >= majority:
		# Need to find a way to insert value into restart
		notAcceptedPromise = []
		acceptedPromise = []
		return "RESTART"

	# If we have received reply from the majority
	elif len(acceptedPromise) >= majority:
		
		# Find the maximum proposal id of all the accepted promises returned from the acceptors
		maxProposalID = max(promise['proposalID'] for promise in acceptedPromise)	# Will this one handle "None"?
		for promise in acceptedPromise:
			if maxProposalID != None:
				# If not all proposal IDs are None, set myValue to the value of the proposal 
				# with the highest proposal ID
				if promise['proposalID'] == maxProposalID:
					# promise['value'] should be added to the front of the paxos queue
					accept = {'senderID': serverID, 'proposalID' : proposalID, 'value' : promise['value']}
					# Reset the list of accepted promises when we broadcast the accept message
					notAcceptedPromise = []
					acceptedPromise = []
					return accept
		accept = {'senderID': serverID, 'proposalID' : proposalID, 'value' : myValue}
		# Reset the list of accepted promises when we broadcast the accept message
		notAcceptedPromise = []
		acceptedPromise = []
		return accept
	return None

	# TEST:
	# When three ACKs is received (and 1 or 2 NACKs):
	#   All has value None, some has value None, none has value None
	# When three NACKs is received: does not have solution yet ?


def receiveAccepted(accepted):
	global acceptedAccepted
	acceptedAccepted.append(accepted)

	# Require a majority
	if len(acceptedAccepted) >= majority: 
		# If we have majority, check if any of the acc-messages has a proposal ID higher than the local
		# If so, restart proposal
		for accepted in acceptedAccepted:
			if accepted['proposalID'] > proposalID:
				acceptedAccepted = []	# resets the list
				return "RESTART"
		acceptedAccepted = []
		return myValue
	return None

	# TEST:
	# receive all three with equal or lower proposalID
	# receive some lower, some higher


# acc = {'senderID': None, 'proposalID' : 3, 'value' : "BestestePost"}
# acc2 = {'senderID': None, 'proposalID' : 3, 'value' : "blogtest"}
# acc3 = {'senderID': None, 'proposalID' : 3, 'value' : "bestPost"}
# print receiveAccepted(acc)
# print receiveAccepted(acc2)
# print receiveAccepted(acc3)


# acc = {'senderID': None, 'proposalID' : 9, 'value' : "BestestePost"}
# acc2 = {'senderID': None, 'proposalID' : 2, 'value' : "blogtest"}
# acc3 = {'senderID': None, 'proposalID' : 5, 'value' : "bestPost"}
# print receivePromise(acc)
# print receivePromise(acc2)
# print receivePromise(acc3)['value']

