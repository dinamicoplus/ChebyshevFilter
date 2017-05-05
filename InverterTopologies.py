import numpy

def j_inverter_c(j,w0,C):
	C_ = j / w0

	Cp = [C-C_[x]-C_[x+1] for x in range(len(C_[0:-1:]))]

	return Cp, C_

def j_inverter_L(j,w0,L):
	L_ = 1 / (j*w0)

	Lp = [L-L_[x]-L_[x+1] for x in range(len(L_[0:-1:]))]

	return Lp, L_

def k_inverter_L(k,w0,L):
	Lp = k / w0

	L_ = [L-Lp[x]-Lp[x+1] for x in range(len(Lp[0:-1:]))]

	return Lp, L_

def k_inverter_c(k,w0,C):
	Cp = 1 / (k*w0)

	C_ = [C-Cp[x]-Cp[x+1] for x in range(len(Cp[0:-1:]))]

	return Cp, C_

def k_inverter_txline(k,Z0):
	X0_Z0 = (k/Z0)/(1-(k/Z0)^2);
	phi = -numpy.arctan(2*X0_Z0)
	X0 = X0_Z0 * Z0

	return phi, X0

def j_inverter_txline(j,Y0):
	B_Y0 = (j/Y0)/(1-(j/Y0)**2);
	phi = -numpy.arctan(2*B_Y0)
	B = B_Y0 * Y0

	return phi, B