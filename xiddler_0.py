import math
target = 100


for R in range(10,target,1):
	for a in range(1,R,1):
		for ax in range(a+1,R,1):
			if a**2 + ax**2 == R**2:
				for b in range (a+1,R,1):
					for bx in range(b+1,R,1):
						if b**2 + bx**2 == R**2:
							cx = bx - (ax -bx)
							if (math.isqrt(R**2 - cx**2))**2 == R**2 - cx**2 :
								print(a,b,int(math.sqrt(R**2 - cx**2)),R)
