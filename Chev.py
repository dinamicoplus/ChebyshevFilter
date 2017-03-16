import numpy

import matplotlib.pyplot as plt

f, p = plt.subplots(1, 2)

def FilterChev(a_p,a_s,w_s):

	n = Filter_Order(a_p,a_s,w_s);

	eps = numpy.sqrt(1/10**(-a_p/10)-1)

	T0 = numpy.array([0,1]);
	T1 = numpy.array([1,0]);

	if (n == 1):
		Tn = T1
	else:
		Tn = CoefChev(T1,T0);
		for i in range(int(n-2)):
			Tn = CoefChev(Tn[0],Tn[1])

	Ew_2 = (eps**2)*numpy.convolve(Tn[0],Tn[0])+numpy.concatenate([numpy.zeros([2*int(n)]),[1]])
	print('Ew_2: '+str(Ew_2))

	E, kt = E_from_Ew_2(Ew_2)

	Es_2 = numpy.convolve(E,E*numpy.array(numpy.resize([1,-1], len(E))[::-1])) # E(s)*E(-s)

	print('Es_2: '+str(Es_2))

	Fs_2 = Es_2 - numpy.concatenate([numpy.zeros(len(Es_2)-1),[kt**2]])
	Fs_2.real[abs(Fs_2.real)<5e-14] = 0.0
	print('Fs_2: '+str(Fs_2))
	
	F = F_from_Fs_2(Fs_2)
	print('F: '+str(F))

	Z_num, Z_den = Z_from_E_F(E,F,1)

	Dn0 = Z_num
	Dn1 = Z_den
	g = []
	T = []
	for i in range(len(Dn0)-1):
		# print('Dn0['+str(i)+']: '+str(Dn0))
		# print('Dn1['+str(i)+']: '+str(Dn1))
		T = numpy.polydiv(Dn0,Dn1)
		# print('T: '+str(T))
		g.append(T[0][0])
		Dn0 = Dn1
		Dn1 = T[1]
	g.append(T[0][1])
	g = numpy.array(g).real
	plt.show()
	return g

def Filter_Order(a_p,a_s,w_s):
	n = numpy.ceil(numpy.arccosh(numpy.sqrt((10**(a_s/10)-1)/(10**(a_p/10)-1)))/numpy.arccosh(w_s))
	return n


def CoefChev(Tn_1,Tn_0):
    Tnn_1 = 2*numpy.convolve(numpy.array([1,0]),Tn_1)-numpy.concatenate([[0],Tn_0])
    Tnn_0 = numpy.concatenate([[0],Tn_1]);
    return Tnn_1, Tnn_0

def E_from_Ew_2(ew_2):
	E2_poles = numpy.roots(ew_2)*1j
	print('E2_poles: '+str(E2_poles))
	E_poles = numpy.array([k for k in E2_poles if k.real<0])
	print('E_poles: '+str(E_poles))
	E = numpy.poly(E_poles).real
	print('E: '+str(E))
	kt = 1/numpy.sqrt(ew_2[0])
	p[0].scatter(E_poles.real,E_poles.imag)
	return E, kt

def F_from_Fs_2(fs_2):
	F2_zeros = numpy.array(numpy.roots(fs_2))
	print('F2_zeros: '+str(F2_zeros))
	
	F_zeros = [k for k in F2_zeros if (k.real<=0.0)]
	# if ((len(F2_zeros)/2)%2 == 0)&(len(F2_zeros)>6):
	# 	F_zeros.append(1j)
	# 	F_zeros.append(-1j)
	if(list(F_zeros).count(0.0)>1):
		F_zeros.remove(0.0)
	F_zeros = numpy.array(F_zeros)

	print('F_zeros: '+str(F_zeros))


	p[1].scatter(F_zeros.real,F_zeros.imag)
	F = numpy.poly(F_zeros)

	return F

def Z_from_E_F(E,F,kr):

	if(len(F)>len(E)):
		E = numpy.append([0],E)
	Z_num = E + kr*F
	Z_den = E - kr*F

	Z_num = [x for x in Z_num if x.real!=0]
	Z_den = [x for x in Z_den if x.real!=0]

	if(len(Z_den)>len(Z_num)):
		W = Z_num
		Z_num = Z_den
		Z_den = W

	print('Z_num: '+str(Z_num))
	print('Z_den: '+str(Z_den))
	return Z_num, Z_den