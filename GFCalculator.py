import os

def pad_zeroes(Cx, len1, len2):
	#insert zeroes at the beginning to reach the length of the longer array
	for i in range(abs(len1-len2)):
		Cx.insert(0,0)
	return Cx

def del_zeroes(Cx):
	#delete unneeded zeroes at the beginning of the array
	while((Cx[0]==0) and len(Cx)!=1):
		Cx.remove(0)
	return Cx

def addsub(Ax,Bx,disp,op):
	#addition and subtraction of galois field are the same

	space = len(B)-1
	if disp: #for displaying solution
		print '\t\t'+'   '*space+'    '*(len(B)-len(A))+'  '.join(str(i) for i in A)
		print '\t\t'+op+'   '*space+'  '*(len(A)-len(B))+'  '.join(str(i) for i in B)
		print '\t    '+'----'*(3*space)

	if len(Ax) > len(Bx):
		Bx = pad_zeroes(Bx, len(Ax), len(Bx))
	elif len(Ax) < len(Bx):
		Ax = pad_zeroes(Ax, len(Bx), len(Ax))

	result=[]
	for i in range(0,len(Ax)):
		result.append(Ax[i]^Bx[i]) #xor operation for every elements

	if disp: #for displaying solution
		print '\t\t'+'   '*space+'  '.join(str(i) for i in result)
	return result

def bin_mult(a,b,Px):
	#multiply 2 decimals, xor the result with P

	#just so the original values wont be change
	p = list(Px)
	#converts the decimal to binary
	A=[int(n) for n in (bin(a)[2:])]
	B=[int(n) for n in (bin(b)[2:])]

	#multiply each binary element of A to B
	result=[]
	for x in range(len(B)-1,-1,-1):
		prod=[]
		for i in range(len(A)):
			prod.append(A[i]&B[x]) #and operation same as multiplication
		for i in range((len(B)-1)-x):
			prod.append(0) #add necessary trailing zeroes if needed
		result = addsub(result,prod,0,'+') #xor the two products
	result=del_zeroes(result) #deletes any unneeded zeroes

	#mod Px if degree of resulting poly is longer than Px
	m = len(p)
	while(len(result)>m-1):
		for i in range(len(result)-len(p)): #appends necessary zeroes at the end
			p.append(0)
		result = addsub(result,p,0,'+') #xor the result with Px
		result = del_zeroes(result) #deletes unneeded zeroes at the head

	return int(''.join(map(str,result)),2) #converts the binary to dec


def mult(Ax,Bx,Px,disp):
	#multiplication of galois field

	space = len(B)-1
	if disp: #for displaying solution
		print '\t\t'+'   '*space+'    '*(len(B)-len(A))+'  '.join(str(i) for i in A)
		print '\t\t*'+'   '*space+'  '*(len(A)-len(B))+'  '.join(str(i) for i in B)
		print '\t    '+'----'*(3*space)

	#multiply each decimal element of Bx to Ax
	result = []
	space = len(B)-1
	for x in range(len(Bx)-1, -1, -1):
		prod = []
		for i in range(len(Ax)):
			prod.append(bin_mult(Ax[i],Bx[x],Px)) #produces list of decimal products
		for i in range((len(Bx)-1)-x): #append necessary zeroes at the end
			prod.append(0)
		result = addsub(result,prod,0,'+') #xor the products
		if disp: #for displaying solution
			print '\t',
			if x==0:
				print '+\t',
			else:
				print '\t',
			print '   '*space+'  '.join(str(i) for i in prod)
			space -= 1
	result = del_zeroes(result) #deletes unneeded zeroes at the head

	if disp: #for displaying solution
		print '\t    '+'----'*(3*(len(B)-1))
		print '\t\t'+'  '.join(str(i) for i in result)

	return result

def div(Ax,Bx,Px,disp):
	#division of galois field using long division

	space = len(Bx)-1

	output = []
	#while the dividend can still be divided by the divisor (dividend >= divisor)
	while (int(''.join(map(str,Ax))) >= int(''.join(map(str,Bx)))):
		x = Ax[0]/Bx[0] #divides the starting digits
		output.append(x) #x now becomes part of the solution
		y = mult(Bx,[x],Px,0) #multiply
		for i in range(len(Ax)-len(y)): #append necessary zeroes
			y.append(0)

		Ax = addsub(Ax,y,0,'-') #subtract #becomes the new dividend and eventually the remainder
		Ax = del_zeroes(Ax) #remove unneeded zeroes

		if disp: #for displaying solution
			print '\t\t'+'   '*space+'    '*(len(y)-len(A))+'  '.join(str(i) for i in A)
			print '\t\t'+'   '*space+'   '*(len(A)-len(y))+'  '.join(str(i) for i in y)+' = B * '+str(x)+' x^'+str(len(y)-len(B))
			print '\t    '+'----'*(3*space)

	if disp: #for displaying remainder
		print '\t\t'+'   '*space+'    '*(len(y)-len(Ax))+'  '.join(str(i) for i in Ax)+" = Remainder"
	#outputs the quotient and the remainder	
	return output, Ax

def printpoly(Cx):
	lenCx = len(Cx)
	deg = lenCx-1
	poly = ""
	for i in range(lenCx):
		if Cx[i]!=0:
			if Cx[i]==1 and i!=lenCx-1:
				poly+=("x^"+str(deg)+" + ")
			elif i==lenCx-1:
				poly+=(str(Cx[i]))
			elif i==lenCx-2:
				poly+=(str(Cx[i])+"x"+" + ")
			else:
				poly+=(str(Cx[i])+"x^"+str(deg)+" + ")
		deg -= 1
	return poly

def inputVal(Cx):

	try:
		Cx = [int(x) for x in Cx.split(" ")]
		return 0
	except ValueError:
		if Cx == "":
			print "\n\tINVALID INPUT: Input cannot be empty.\n"
		elif Cx[len(Cx) - 1] == " ":
			print "\n\tINVALID INPUT: There should be no space at the end.\n"
		else:
			print "\n\tINVALID INPUT: Format must be integers separated by spaces.\n"
		return 1


while (True):
	os.system('cls' if os.name == 'nt' else 'clear')
	print"            _______       _       _         _______ _       _     _ "
	print"           (_______)     | |     (_)       (_______|_)     | |   | |"
	print"            _   ___ _____| | ___  _  ___    _____   _ _____| | __| |"
	print"           | | (_  (____ | |/ _ \| |/___)  |  ___) | | ___ | |/ _  |"
	print"           | |___) / ___ | | |_| | |___ |  | |     | | ____| ( (_| |"
	print"            \_____/\_____|\_)___/|_(___/   |_|     |_|_____)\_)____|"
	print"             _______       _             _                         "
	print"            (_______)     | |           | |         _              "
	print"             _       _____| | ____ _   _| | _____ _| |_ ___   ____ "
	print"            | |     (____ | |/ ___) | | | |(____ (_   _) _ \ / ___)"
	print"            | |_____/ ___ | ( (___| |_| | |/ ___ | | || |_| | |    "
	print"             \______)_____|\_)____)____/ \_)_____|  \__)___/|_|    "
	
	while(True):

		#get input
		print("\n\tEnter Polynomials A(x), B(x), P(x): (enter q to Quit)")
		Ax = raw_input("\t\tA(x) = ")
		Bx = raw_input("\t\tB(x) = ")
		Px = raw_input("\t\tP(x) = ")
		# for testing
		# Ax = "1 0 7 6"
		# Bx = "1 6 3"
		# Px = "1 0 1 1"

		#input validation
		if inputVal(Ax)==0 and inputVal(Bx)==0 and inputVal(Px)==0:
			break

	#exits the program when "e" is entered
	if ('q' in Ax or 'q' in Bx or 'q' in Px):
		os.system('cls' if os.name == 'nt' else 'clear')
		print"\n\n\n                 _______                 _ _                 _ "
		print"                (_______)               | | |               | |"
		print"                 _   ___  ___   ___   __| | |__  _   _ _____| |"
		print"                | | (_  |/ _ \ / _ \ / _  |  _ \| | | | ___ |_|"
		print"                | |___) | |_| | |_| ( (_| | |_) ) |_| | ____|_ "
		print"                 \_____/ \___/ \___/ \____|____/ \__  |_____)_|"
		print"                                                (____/         "
		exit()

	#turns the string into array of ints
	Ax = [int(i) for i in Ax.split()]
	Bx = [int(i) for i in Bx.split()]
	Px = [int(i) for i in Px.split()]
	#removes zeroes in front in case there is any
	Ax = del_zeroes(Ax)
	Bx = del_zeroes(Bx)
	Px = del_zeroes(Px)

	while (True):
		#just so the original values will not be changed
		A = list(Ax)
		B = list(Bx)
		P = list(Px)
		#enters what type of operation
		print "\n\t", "*"*60
		op = raw_input("\n\tWhat operation? \n\t\t1 - A(x) + B(x)\n\t\t2 - A(x) - B(x)\n\t\t3 - A(x) x B(x)\n\t\t4 - A(x) / B(x)\n\t\tc - Change values\n\t\tq - Quit\n\t")
		print "\n\t", "*"*60
		if op == '1': #addition
			print "\n\tA D D I T I O N"
			print "\n\tGiven:\n\t\tA(x) = ", printpoly(Ax), "\n\t\tB(x) = ", printpoly(Bx)
			print "\n\tSolution:\n"

			result = addsub(A,B,1,'+')
			print "\n\n\tA(x) + B(x) = ",printpoly(result)
		elif op == '2': #subtraction
			print "\n\tS U B S T R A C T I O N"
			print "\n\tGiven:\n\t\tA(x) = ", printpoly(Ax), "\n\t\tB(x) = ", printpoly(Bx)
			print "\n\tSolution:\n"

			result = addsub(A,B,1,'-')
			print "\n\n\tA(x) - B(x) = ",printpoly(result)
		elif op == '3': #multiplication
			print "\n\tM U L T I P L I C A T I O N"
			print "\n\tGiven:\n\t\tA(x) = ", printpoly(Ax), "\n\t\tB(x) = ", printpoly(Bx), "\n\t\tP(x) = ", printpoly(Px)
			print "\n\tSolution:\n"

			result = mult(A,B,P,1)
			print "\n\n\tAx * Bx = " + printpoly(result)
		elif op == '4': #division
			print "\n\tD I V I S I O N"
			print "\n\tGiven:\n\t\tA(x) = ", printpoly(Ax), "\n\t\tB(x) = ", printpoly(Bx)
			print "\n\tSolution:\n"

			result = div(A,B,P,1)
			print "\n\n\tAx / Bx = " + printpoly(result[0]) + "\tRemainder: " + printpoly(result[1])
		elif op == 'c': #change values
			break
		elif op == 'q': #quit
			os.system('cls' if os.name == 'nt' else 'clear')
			print"\n\n\n                 _______                 _ _                 _ "
			print"                (_______)               | | |               | |"
			print"                 _   ___  ___   ___   __| | |__  _   _ _____| |"
			print"                | | (_  |/ _ \ / _ \ / _  |  _ \| | | | ___ |_|"
			print"                | |___) | |_| | |_| ( (_| | |_) ) |_| | ____|_ "
			print"                 \_____/ \___/ \___/ \____|____/ \__  |_____)_|"
			print"                                                (____/         "
			exit()
		else:
			print "\n\tError: Enter Valid Operation"