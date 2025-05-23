#hediin dotr too sanasan
#garh tovchig dartal while davtan
# 1 zoow too snasn 2 ih too sansn 3 baga too sans 4 grah"

import math
answer= "2"

while answer not in '4':
    
 n=int(input("hediiin too sansin "))    
 print("bi chinii sansn toog {} oroldlogo higd olj chadna".format(int(math.log(n,2) + 1)))
 
 low_n , high_n = 1 , n
 i=1
 print("oroldlog {} : chinii sansana too {} : ene mon uu ? ".format( i,  (low_n + high_n) // 2 ))
 
 answer = input(" 1. Zow too sanasan \n 2. Ih too sanasan \n 3. Baga too sanasan \n 4. Garah \n  ")

while answer != "1" and answer != "4":
     print()
     if answer not in "1234":
         input(" Chi buruu utga oruulsn bn \n 1. Zow too sanasan \n 2. Ih too sanasan \n 3. Baga too sanasan \n 4. Garah \n")
         continue
     i += 1
     if answer == "3":
         low_n = (low_n + high_n) //2
     elif answer == "-":
         low_n = (low_n + high_n) //2
         print("oroldlog {} : chinii sansana too {} : ene mon uu ? ".format( i , (low_n + high_n) // 2 ))
         answer = input(" 1. Zow too sanasan \n 2. Ih too sanasan \n 3. Baga too sanasan \n 4. Garah \n")
         if answer == 1:
             print(" zow hariult odoo gar ")
             #  ALDAATAI CODE 2 DEER ZASVAR ORN 