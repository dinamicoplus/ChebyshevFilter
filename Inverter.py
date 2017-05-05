import numpy

def k_inverter(g,gn,Rg,Rl,L):
	k = []
	L_ = numpy.array([Rl])
	L_ = numpy.concatenate([numpy.ones(len(g))*L,L_])
	L_ = numpy.append(Rg,L_)
	g = numpy.append(g,gn)
	g = numpy.append(1,g)
	print('g: '+str(g))
	print('L_: '+str(L_))


	for i in range(1,len(g)-1,2):
		k.append(numpy.sqrt(L_[i-1]*L_[i]/(g[i-1]*g[i])))
		k.append(numpy.sqrt(L_[i]*L_[i+1]/(g[i]*g[i+1])))
	k = numpy.array(k)

	return k

def k_inverter_BP(g,gn,w0,a,Rg,Rl,L):
	k = []
	C = (1/(w0**2*L))
	L_ = numpy.array([Rl])
	L_ = numpy.concatenate([numpy.ones(len(g))*w0/a*L,L_])
	L_ = numpy.append(Rg,L_)
	g = numpy.append(g,gn)
	g = numpy.append(1,g)
	print('g: '+str(g))
	print('L_: '+str(L_))

	for i in range(1,len(g)-1,2):
		k.append(numpy.sqrt(L_[i-1]*L_[i]/(g[i-1]*g[i])))
		k.append(numpy.sqrt(L_[i]*L_[i+1]/(g[i]*g[i+1])))
	k = numpy.array(k)
	return k, C, L

def j_inverter(g,gn,Rg,Rl,C):
	j = []
	Gg = 1/Rg
	Gl = 1/Rl
	C_ = numpy.array([Gg])
	C_ = numpy.concatenate([numpy.ones(len(g))*C,C_])
	C_ = numpy.append(Gg,C_)
	g = numpy.append(g,gn)
	g = numpy.append(1,g)
	print('g: '+str(g))
	print('C_: '+str(C_))

	for i in range(1,len(g)-1,2):
		j.append(numpy.sqrt(C_[i-1]*C_[i]/(g[i-1]*g[i])))
		j.append(numpy.sqrt(C_[i]*C_[i+1]/(g[i]*g[i+1])))
	j = numpy.array(j)
	return j

def j_inverter_BP(g,gn,w0,a,Rg,Rl,C):

	j = []
	L = (1/(w0**2*C))
	Gg = 1/Rg
	Gl = 1/Rl
	C_ = numpy.array([Gg])
	C_ = numpy.concatenate([numpy.ones(len(g))*w0/a*C,C_])
	C_ = numpy.append(Gg,C_)
	g = numpy.append(g,gn)
	g = numpy.append(1,g)
	print('g: '+str(g))
	print('C_: '+str(C_))

	for i in range(1,len(g)-1,2):
		j.append(numpy.sqrt(C_[i-1]*C_[i]/(g[i-1]*g[i])))
		j.append(numpy.sqrt(C_[i]*C_[i+1]/(g[i]*g[i+1])))
	j = numpy.array(j)
	return j, C, L

def j_inverter_BP_txline(g,gn,a,Z0):

	j = []
	Y0 = 1/Z0
	Y = numpy.array([Y0])
	Y = numpy.concatenate([numpy.ones(len(g))*numpy.pi*Y0/2/a,Y])
	Y = numpy.append(Y0,Y)
	g = numpy.append(g,gn)
	g = numpy.append(1,g)
	print('g: '+str(g))

	for i in range(1,len(g)-1,2):
		j.append(numpy.sqrt((Y[i-1]*Y[i])/(g[i-1]*g[i])))
		j.append(numpy.sqrt((Y[i]*Y[i+1])/(g[i]*g[i+1])))
	j = numpy.array(j)
	return j