#-----------------------Master Dictionnaire-------------------------
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

