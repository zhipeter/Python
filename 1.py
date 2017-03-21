db={}
def newuser():
	prompt='login desired:'
	while True:
		name=str(input(prompt))
		if name in db:
			prompt='name taken,try another'
			continue
		else:
			break
	pwd=str(input('password:'))
	db[name]=pwd
def olduser():
	name=str(input('login:'))
	pwd=str(input('password:'))
	password=db[name]
	if password==pwd:
		pass
	else:
		print ("login incorrect")
		return pwd
	print ("welcome back",name)
def showmeau():
	prompt="""
	(N)ew User Login
	(E)xisiting User Login
	(Q)uit
Enter ur choice:"""
	done=False
	while not done:
		chosen=False
		while not chosen:
			try:
				choice=str(input(prompt)[0])
			except (EOFError,KeyboardInterrupt):
				choice='q'
			print("\nU picked:[%s]"% choice)
			if choice not in 'neq':
				print("invalid option,try again")
			else:
				chosen=True
		if choice=='q':done=True
		if choice=='n':newuser()
		if choice=='e':olduser()
showmeau()