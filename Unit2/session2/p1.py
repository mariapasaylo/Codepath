#U
#Input: dictionary votes - key:name value:number of votes
#candidate name as string
#Output: return updated dictionary

#M
#similar to frequency table

#P
# if candidate in votes
# votes[candidate] increase by one
# if not (else)
# votes[candidate] = 1
#return updated dictionary

#I
def cast_vote(votes, candidate):
    if candidate in votes:
        votes[candidate] +=1
    else:
        votes[candidate] = 1
    
    return votes



#testing
votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)