import matplotlib.pyplot as plt
#plt.plot([1,2,3,4], [1,4,9,16], 'ro')
#plt.axis([0, 6, 0, 20])
#plt.show()


W = 0.1
L = 0.22
mupcox = 17
VT = 0.83
VGS = range(5, 16, 2)

VDS = range(0, 6)
IDS = []

for _vgs in VGS:
	_ids = []
	for x in VDS:
		y = 0.5 * mupcox * W * ( x * ( _vgs - VT ) - (0.5 * x * x) ) / L
		_ids.append(y)
	IDS.append(_ids)

plt.plot(VDS, IDS[0], VDS, IDS[1], VDS, IDS[2], VDS, IDS[3], VDS, IDS[4], VDS, IDS[5])
plt.show()