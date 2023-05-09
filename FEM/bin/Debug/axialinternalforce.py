def axialinternalforce(numberElements,elementNodes,xx,yy,displacements,E,A):
	import numpy as np
	import math
	numberElements=int(numberElements)
	E=float(E)
	A=float(A)

	elementNodes_1 = elementNodes
	n_rows = elementNodes_1.GetLength(0)
	n_cols = elementNodes_1.GetLength(1)
	elementNodes= np.zeros((n_rows,n_cols),dtype=int)
	for i in range(n_rows):
		for j in range(n_cols):
			elementNodes[i, j] = elementNodes_1[i, j]
	xx_1 = xx
	yy_1 = yy
	n_rows_1 = xx_1.GetLength(0)
	xx=np.zeros((n_rows_1,1),dtype=float)
	yy=np.zeros((n_rows_1,1),dtype=float)
	for i in range(n_rows_1):
		xx[i]=xx_1[i]
		yy[i]=yy_1[i]

	elementNodes = np.matrix(elementNodes)

	displacements_1=displacements
	n_rows_2 = displacements_1.GetLength(0)
	displacements=np.zeros((n_rows_2,1),dtype=float)
	for i in range(n_rows_2):
		displacements[i]=displacements_1[i]

	internal=np.zeros((numberElements,1))
	for i in range(0,numberElements) :
		indice=elementNodes[i]
		elementDof=[indice[0,0]*2-2, indice[0,0]*2-1, indice[0,1]*2-2, indice[0,1]*2-1]
		xa=xx[indice[0,1]-1]-xx[indice[0,0]-1]
		ya=yy[indice[0,1]-1]-yy[indice[0,0]-1]
		length_element=math.sqrt(xa*xa+ya*ya)
		c=xa/length_element
		s=ya/length_element
		idx=np.ix_(elementDof)
		internal[i]=E*A/length_element*np.matmul(np.array([-c,-s,c,s]),displacements[el])
	#internal[i]= internal.reshape((numberElements,1))	
	return internal