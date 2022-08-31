#Condicionales para rango, clasificación, comparar, tomar decisiones. **definir rangos 2 condiciones Op logicos negacion Y O.
# se llama main porque es algo que ya toco el remoto, si no lo hubiera tocado se llamaria master, si tiene cambios git status, git add.

#ENTRADA= VARIABLES = REFERENCIAS EN MEMORIA
nivelAgua = int (input("Digite el nivel de agua: "))

#PROCESO
if(nivelAgua >= 0 and nivelAgua < 20):
    #SALIDA
    print(f'El nivel de agua es {nivelAgua} y este es bajo')
elif(nivelAgua >= 20 and nivelAgua < 400):
     #SALIDA
    print(f'El nivel de agua es {nivelAgua} operando normalmente')
elif(nivelAgua >= 400):
     #SALIDA
    print(f'El nivel de agua es {nivelAgua} Llamen a fico')
else:
     #SALIDA
    print("El nivel de agua no es valido")

