# coding=utf-8

import proposal, accept

myID = 0;
proposalID = 0;

# Ballotnum, initially <0,0>
# AcceptNum, initially, <0,0>
# AcceptVal


# Phase Prepare - LEADER

# if leader then
# BallotNum ← 〈BallotNum.num+1, myId〉
# send (“prepare”, BallotNum) to all

proposalNum = 2

def prepare(post):
	global proposalID
	blogpost = post
	proposalID += 1
	propose = proposal(myID, proposalID)
	return propose


def receivePromise(accepted):
	# receive proposebla bla


    return None




# Phase Accept - LEADER

# Upon receive (“ack”, BallotNum, b, val) from majority
# if all vals = ⊥ then myVal = initial value else myVal = received val with highest b
# send (“accept”, BallotNum, myVal) to all /* proposal */

# Deciding

# Upon receive (“accept”, b, v) from n-t decide v
# periodically send (“decide”, v) to all
# Upon receive (“decide”, v) decide v

