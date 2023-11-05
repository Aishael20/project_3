#-----------------Master Str-------------------------------------------------------
#1)M mete tout karaktè yo an miniskil
chen="MWEN RenmeN Kou PYTHON an anpil"
print(chen)
chen_minis=chen.lower()
print(chen_minis)
#2)Koupe chenn nan tout kote ki gen espas.
koupe=chen.split(" ")
print(koupe)
#3 M mete premye lèt chak mo an majiskil
print("La mwen mete tout premye let chak mo an majiskil:\n",chen.title())
#4)N ap afichiche yon nouvo chèn ak tout inisyal yo
rekipere=[let[0] for let in koupe]
inisyal="".join(rekipere)
print("Men tout inisyal yo:",inisyal.lower())

#5)M ap ranplase tout karaktè "a" ki nan yon chenn pa "@"
ranplase=chen.replace("a","@")
print(ranplase)

#6)M Mete yon chenn karaktè devan dèyè, answit mete l an majiskil. 
Alanve=chen[::-1]
print("Le chenn nan alanve li bay sa:\n",Alanve)
majiskil=Alanve.upper()
print("le m mete fraz tet anba an majiskil\n Li banm:",majiskil)

#7)Afiche endeks premye karaktè "a" ki nan yon chenn. 
a=chen.index("a")
print("Endeks premye karaktè ti a se:",a)

#8)Afiche total tout endeks karaktè "a" ki nan yon chenn (Kit se a majiskil oubyen miniskil). 
konte=0
for el, nb_a in enumerate (chen):
    if nb_a=="a" or nb_a=="A":
        konte+=el
print("Total tout endeks karaktè a ou A ki nan chen nan se:",konte)

#9)Kreye yon lis ki gen endeks tout karaktè "a" ki nan yon chenn (Sèlman a miniskil)
lis_a=[]
for p, l in enumerate (chen):
    if l=="a":
        lis_a.append(p)
print("Men lis ki gen endeks tout karaktè ti a ki nan chenn lan:",lis_a)
#10)Retire tout espas ki nan yon chenn, 
# epi kole chenn sa ak kantite karaktè li genyen (Pa kontwole espas yo).
espas=chen.replace(" ","")
print("Chenn kole ak longe l san espas bay sa:\n",espas+str(len(espas)))
#    ---------------------------------------------------------------------------------------
print("----------------------------------Master list--------------------------------------")
#1)Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
lis=[0,1,2,3,4,5,6,7,8,9,10]
modilo=[]
for el in lis:
    if el%2==0:
        modilo.append(el)
print("Men lis eleman ki divizib pa 2 nan enteval [0-10] lan:\n",modilo)
    





