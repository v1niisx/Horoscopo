#Consulta Signo
print('-'* 5,'Consultar Signo','-' * 5)

#Entradas
dia = int(input("digite o dia que nasceu: ").strip())
mes = int(input("digite o mes: ").strip())

print('-'* 29)

#Processamento e saida
if dia>=20 and dia<=31 and mes==3 or dia>=1 and dia<=19 and  mes==4:
   print ("Seu Signo é: aries")
elif dia>=20 and dia<=30 and mes==4 or dia>=1 and dia<=20 and mes==5:
   print ("Seu Signo é: touro")
elif dia>=21 and dia<=31 and mes==5 or dia>=1 and dia<=20 and mes==6:
   print ("Seu Signo é: gemeos")
elif dia>=22 and dia<=30 and mes==6 or dia>=1 and dia<=22 and mes==7:
   print ("Seu Signo é: Câncer")
elif dia>=23 and dia<=31 and mes==7 or dia>=1 and dia<=22 and mes==8:
   print ("Seu Signo é: Leao")
elif dia>=23 and dia<=31 and mes==8 or dia>=1 and dia<=22 and mes==9:
   print ("Seu Signo é: Virgem")
elif dia>=23 and dia<=30 and mes==9 or dia>=1 and dia<=22 and mes==10:
   print ("Seu Signo é: Libra")
elif dia>=23 and dia <=31 and mes==10 or dia>=1 and dia<=21 and mes==11:
   print ("Seu Signo é: Escorpiao")
elif dia>=22 and dia<=30 and mes==11 or dia>=1 and dia<=21 and mes==12:
   print ("Seu Signo é: Sagitario")
elif dia>=22 and dia<=31 and mes==12 or dia>=1 and dia<=19 and mes==1:
  print ("Seu Signo é: Capricornio")
elif dia>=20 and dia<=31 and mes==1 or dia>=1 and dia<=18 and mes==2:
  print ("Seu Signo é: Aquario")
elif dia>=19 and dia<=29 and mes==2 or dia>=1 and dia<=20 and mes==3:
  print ("Seu Signo é: Peixes")
else:
  print ("invalido")
#end
print('-'* 29)
