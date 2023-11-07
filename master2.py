print("-----------------------Master Dictionnary-------------------------")
#1)Nan yon diksyone m rekipere tout valè yo, gras ak kle yo epi m retounen yon lis valè.
dik={'A':25, 22:'c', 'D':8.5}
lis_val=[]
val1=dik.get('A')
val2=dik.get(22)
val3=dik.get('D')
lis_val.append(val1)
lis_val.append(val2)
lis_val.append(val3)
print("Lè m retounen lis valè m te rekipere gras ak kle yo\nLi bay sa:",lis_val)

#2)Mande itilizatè a, tape yon valè... epi verifye si l gen akolad devan ak dèyè.
key_user=input("Tanpri tape yon valè: ")

if '{' in key_user[0] and '}' in key_user[::-1]:
    print("Valè ou tape a gen akolad devan ak dèyè")
elif '{' in key_user[0]:
       print("Valè ou tape a gen akolad devan selman")
elif '}' in key_user[::-1]:
       print("Valè ou tape a gen akolad dèyè selman")

else:
    print("Valè ou tape a pa gen akolad ni devan ni dèyè")

#3)M ap pakouri yon diksyonè(dik), epi m afiche tout kle yo.
for key in dik:
      #print(key) se yon lot fason m te ka afiche yo
      kle_yo=dik.keys()
print("Lè m pakouri diksyone a men tout kle li yo:\n",kle_yo)

#4)M ap pakouri yon diksyonè(dik), epi m afiche tout valè yo
for key in dik:
      vale_yo=dik.values()
print("Lè m pakouri diksyone a men tout valè li yo:\n",str(vale_yo))

#5)Pakouri yon diksyonè, pou w kapab kreye yon kopi(nouvo) sou disksyonè sa.
nouvo_dik = {cle: valeur for cle, valeur in dik.items()}
print("Kopi diksyone m nan bay sa:",nouvo_dik)

#6)Ajoute yon underscore devan ak dèyè tout valè ki se chenn nan diksyonè a
dict={'a':'Marie','b':4,'c':'Paul'}
for kle,v in dict.items():
    if isinstance(v, str):
         #dict[kle]=v.startswith("_") and v.endswith("_")
         dict[kle]="_"+v+"_"
print("Lè nou ajoute underscore devan ak dèyè tout valè ki se chenn yo\nLi ban nou sa:",dict)

#7)Nan yon diksyonè ki gen valè ki se chenn sèlman. Kreye yon nouvo diksyonè ki gen tout eleman ki gen valè ki dijit yo sèlman.  
dik_chenn={'p':'vert','k':'12r','f':'rouge','k':'66','l':'58'} 
dik_digit={}
for kle, val in dik_chenn.items():
     if val.isdigit():
          dik_digit[kle]=val
print("Apre tri,diksyonè dijit lan bay sa:",dik_digit)

#8)M pakouri yon disksyonè, pou m mete l sou fòm lis, kote chak eleman nan disksyonè sa, vin sou fòm tipl(kle, valè) anndan lis la
lis_tipl = [(kle, valè) for kle, valè in dik_digit.items()]  
print("Lis tipl(kle, valè) a bay sa:",lis_tipl)
     
#9)M ap pakouri yon lis tipl, pou m mete l sou fòm diksyonè
list_tuples=[("2",5), ("8",4)]
list_dict = {kle: valè for kle, valè in list_tuples} 
print("Lè m mete lis tipl la sou fom diksyone li banm sa:",list_dict)

#10)Kole 2 diksyonè ansanm pou fè youn, kote si gen eleman ki gen menm kle ap konkatene valè, swivan kondisyon sa yo
dict1={'a':5,'b':[2,3],'c':'Hello'}
dict2={'a':5,'m':(2,3),'c':'Guys'}
dict_3={}
for k, v in dict1.items():
    for k2, v2 in dict2.items():
        if k==k2:
            if isinstance(v,int) and isinstance(v2,int):
                    dict_3[k]=v+v2
        else:
               dict_3[k]=str(v) +str(v2)
               break
print("kole 2 diksyone ansanm:\n",dict_3)
               
            
print("-----------------------------------------------------------")
print("-----------------------Master Function---------------------")
#1)Kreye yon fonksyon ki ap pran yon paramèt yon mo, epi li retounen envès la.
import random
import string
def fonct_enves(mo):
    enves=mo[::-1]
    print(enves)
    return enves
print("Envès hello se:")     
fonct_enves("hello")


#2)kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik
def kod_aleyatwa(n):
    karakte=string.ascii_letters
    kod=""
    for i in range(n):
        kod+=random.choice(karakte)
    return kod

t=kod_aleyatwa(5)
print(t)

#3)kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alfabetik, san repetisyon.
import random
import string

def kod_s_r(n):
    let_alfabetik = string.ascii_lowercase  # Lèt alfabetik la

    # Jenere yon kòd aleyatwa san repetisyon
    kòd = ''.join(random.sample(let_alfabetik, n))

    return kòd

kod_6 = kod_s_r(6)
print(kod_6)

#4)kreye yon fonksyon ki pou jenere yon kòd aleyatwa ki gen n karaktè alafanimerik, san repetisyon.
def kod_alfanimerik(n):
    alfanimerik=string.ascii_letters+string.digits
    kod_alfa=''.join(random.sample(alfanimerik,n))
    return kod_alfa
kod_alfanimerik(9)
print(kod_alfanimerik(9))

#5)M gen yon lis chenn,lis chenn. Jenere yon SLUG apati chenn nan. Nan yon SLUG, tout karaktè ki akseptab yo se: alfanimerik ak "-"
chenn="Kou piton avanse pou pitonis"
chif=random.randrange(10)
slug=chenn.replace(" ","-")+str(chif)
print(slug)

#6)Kreyasyon yon fonksyon ki ap separe chak lèt nan yon mo ak yon vigil
def fonk_vigil():
    mo="lune"
    separe=",".join(mo)
    
    return separe
print(fonk_vigil())

#7)Kreyasyon yon fonksyon ki ap kripte yon mo, avèk endèks li nan alfabè a. Chak karaktè dwe separe ak yon tirè.
def fonk_kripte(mo):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    mo_kripte = ''

    for l in mo.lower():
        if l.isalpha():
            indice = alphabet.index(l)
            mo_kripte += str(indice) + '-'
        else:
            mo_kripte += l + '-'

    mo_kripte = mo_kripte[:-1]#retire denye tirè a

    return mo_kripte
m_kripte = "BANK"
mo_kripte = fonk_kripte(m_kripte)
print("Mo kripte BANK =>",mo_kripte)

#8)Kreyasyon yon fonksyon ki ap dekripte yon mo ki fèt ak endèks chak lèt nan alfabè a, separe ak yon tirè.
#9)Kreye yon fonksyon ki ap pran 2 paramèt, epi ki pèmite valè yo. Answit li retounen tou 2 valè yo sou fòm Tuple.

def fonk_permute(A,B):
    P=A
    A=B
    B=P
    return A,B
tipl=fonk_permute(5,6)
print("Valè pemite yo sou fom tuple bay:",tuple(tipl))

#10)Kreye yon fonksyon ki ap pran yon non an paramèt, epi ki retounen inisyal yo. Atansyon ak non konpoze ak tirè yo.
def inisyal_non(non):
    name = non.replace('-', ' ')  # Retire tout tiret nan non an
    divize = name.split()  # Separe non an an mo yo
    inisyal = ''.join([mo[0] for mo in divize])  # Pran premye lèt nan chak mo

    return inisyal.upper()  # Retounen inisyal yo an majiskil

non = "Jean-Pierre Boyer"
inisyal = inisyal_non(non)
print("Inisyal non an se:",inisyal)  

    









