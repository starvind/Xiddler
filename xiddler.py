import math

for R in range(3,66,1):
	for dsquare in range(2,R**2+1,1) : 			
		for xsquare in range (1,min(dsquare, (int(R - math.sqrt(dsquare))**2)) + 1,1):
			Bsquare = R**2 - dsquare
			if (math.isqrt(Bsquare))**2 == R**2 - dsquare: 		#check if B is a positive integer							
				Asquare =  R**2 - dsquare - xsquare - 2*math.sqrt(dsquare*xsquare)
				if (math.isqrt(int(Asquare)))**2 == Asquare and Asquare > 0:		#check if A is a positive integer 
					Csquare = R**2 - dsquare - xsquare + 2*math.sqrt(dsquare*xsquare)
					if (math.isqrt(int(Csquare)))**2 == Csquare:						#check if C is a positive integer
						print(R, dsquare, xsquare, int(Asquare), int(Bsquare), int(Csquare))
