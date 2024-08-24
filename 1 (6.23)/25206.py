num1 = 0
num2 = 0

grdChart = { 
  "A+" : 4.5, "A0" : 4,
  "B+" : 3.5, "B0" : 3,
  "C+" : 2.5, "C0" : 2,
  "D+" : 1.5, "D0" : 1,
  "F" : 0
}


for i in range(1, 21): 
  sub, crd, grd = input().split() 
  if grd == "P": 
    continue 
  num1 += grdChart[grd] * float(crd) 
  num2 += float(crd) 
  
print(num1 / num2) 
