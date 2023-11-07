print("-----------------Master Str-------------------------------------------------------")
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
print("-----------------------------------------------------------------------------------")
print("----------------------------------Master list--------------------------------------")
#1)Kreye yon lis eleman ki divizib pa 2, nan entèval [0-n] enklizif
lis=[0,1,2,3,4,5,6,7,8,9,10]
modilo=[]
for el in lis:
    if el%2==0:
        modilo.append(el)
print("Men lis eleman ki divizib pa 2 nan enteval [0-10] lan:\n",modilo)
    
#2)Konveti yon lis antye an yon lis chen
Lis_ant=[0,2,5,6,9,7]
Lis_chen=[str(e) for e in Lis_ant]
print("Konvesyon yon lis antye an yon lis chene bay sa:\n",Lis_chen)
#3)Konvèti yon lis chen miniskil an majiskil
lisminiskil=['plumme','papier','cahier','c']
lismajiskil=[m.upper() for m in lisminiskil]
print("Lis chenn ['plumme','papier','cahier','c'] an majiskil bay sa:",list(lismajiskil))
#4) kreyasyon yon nouvo lis ki fèt ak eleman ki nan endèks ki divizib pa 3 yo sèlman
lis_s=[1,'a',3,'c',5,'e',7,'z']
lis_3=[lis_s[i] for i in range (len(lis_s)) if i%3==0]
print("Nan yon lis [1,'a',3,'c',5,'e',7,'z']Eleman ki nan endeks ki divizib pa 3 yo se:",lis_3)

#5) kreyasyon yon nouvo lis ki gen chak 3 eleman yo gwoupe anndan yon tipl
lis_i=[1,2,3,4,5,6,7,8,9] 
lis_tipl = [tuple(lis_i[i:i+3]) for i in range(0, len(lis_i), 3)]
print("Men yon nouvo lis avek chak 3 eleman yo andann yon tipl:",lis_tipl)

#6)Konvesyon an yon lis, ki pa gen okenn doublon.

lis_d= [1, 2, 2, 3, 3, 4, 5,'do','do','mi' ]

lis_s_d = list(set(lis_d))
print("Lis san doublon an bay sa:",lis_s_d)

#7)Kreyasyon yon nouvo lis, ki genyen sèlman eleman komen ant 2 lis ki egziste deja.
lis1=[10,11,12,13]
lis2=[10,12,13,14,16]
new_list=set(lis1) & set(lis2)
print("Men yon nouvo lis avek eleman komen de 2 lot lis:",list(new_list))

#8)Kreyasyon yon nouvo lis, ki genyen sèlman eleman distenge ant 2 lis yo.
nouvo_lis=list()
nouvo_lis=list(set(lis1) ^ set(lis2))
print("Men yon nouvo lis avek selman eleman inik pou chak lis",nouvo_lis)

#9)kreyasyon yon nouvo lis ak kle yo sèlman, epi yon lòt ak valè yo sèlman.

diksyone = {'A': 1, 'B': 2, 'C': 3, 'D': 4}

# Kreye yon nouvo lis ki gen sèlman kle yo
lis_kle = list(diksyone.keys())

# Kreye yon lòt lis ki gen sèlman valè yo
lis_vale = list(diksyone.values())

print("Lis kle diksyone an se:", lis_kle)
print("Lis vale dikansyone an se:", lis_vale)

#10)Reyinyon 3 lis ansanm, san okenn doublon
l1=[0,1,2,3,4,5,6,7,8]
l2=[0,2,4,6,8]
l3=[0,3,6,9]
reyinyon=list(set(l1+l2+l3))
print("Reyinyon 3 lis yo san dublon bay sa:",reyinyon)



        





