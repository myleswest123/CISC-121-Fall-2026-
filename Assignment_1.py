#PermMissingElm
def solution(A) 
	n=len(A) #Shows how many numbers are in the array A
	found=[] #start an empty checklist
	for i in range (n+2): #repeat n+2 times 
		found.append(False) 
	for value in A: #take each number one at a time
		found[value]=True #mark this number as seen
	for number in range(1,n+2): #go through every number from 1 to n+1
		if found[number]== False: #if this number was never marked
			return number #this is the missing number 

#PermCheck
def solution(A)
	n=len(A)
	found=set() #Empty set to store the numbers we’ve seen 
	for value in A: #Take each number one at a time
		if value>n or value in found: #If the value is larger than list length or already exists
			return 0
		found.add(value) #put the value into the set
	return 1 #If no problems exist, it’s a permutation 

#OddOccurancesInArray
def solution(A)
	pile=set() #Creates a pile that the numbers will be added to 
	for number in A: #For every number in array A 
		if number in pile: #If the number exists in pile 
			pile.remove(number) #remove the number in the pile 
		else: 
			pile.add(number) #If no partner exists, the number is added to pile
		return pile.pop() #pops the lone number remaining in the pile as the answer 

#CyclicRotation
def solution(A)
	if len(A)==0: #This would be an empty list
		return A
	for i in range(K): #repeat K amount of times 
		last=A.pop() #Takes the last number in the list and pops it out
		A.insert(0,last) #Inserts the popped number into the first list spot 
	return A

#FrogStp
def solution (X, Y, D)
	distance= Y-X #Total distance the frog must travel 
	jumps=distance//D #How many full jumps will it take
	if distance % D !=0: #Is there still distance left over? 
		jumps+=1 #One more jump 
	return jumps 
