# -----------------------------------------
# Programa: Califimaster Pro
# Autor: [Maria Fernanda Reid]
# Descripción: Analiza calificaciones, promedios y estadísticas estudiantiles.
# -----------------------------------------

print("BIENVENIDO AL SISTEMA INTELIGENTE DE ANALISIS DE NOTAS  ")
nombre_usuario= input("¿CUAL ES TU NOMBRE?: ")

# Paso 1: Se solicita la calificacion individual con espeificaciones
while True:
    try:
        nota= int(input("INGRESA TU CALIFICACION: "))
        if 0<= nota <=100:
            break 
        else:
            print("ERROR, LA CALIFICACION DEBE ESTAR ENTRE 0 Y 100")
    except ValueError:
        print("INGRESE UN NUMERO ENTERO ")

# Paso 2: Evaluamos si el usuario ha aprobado o reprobado 
if nota >=70:
    print(f"APROBADO CON EXCELENCIA EN {nota}!")
elif nota >=60:
    print(f"APROBADO CON :{nota}." )
elif nota>=50:
    print(f"EN RECUPERACION CON: {nota}.")
else:
    print(f"REPROBADO CON: {nota}.")

# Paso 3: Solicitamos lista de calificaciones separadas por comas 
while True:
    entrada_lista = input("INGRESA TUS CALIFICACIONES DEL PERIODO (separadas por comas): ")
    try:
        lista_notas = [float(n.strip()) for n in entrada_lista.split(',')]
        if all(0 <= n <= 100 for n in lista_notas) and lista_notas:
            suma_total = sum(lista_notas)
            promedio = suma_total / len(lista_notas)

            if promedio >= 60:
                print(f"FELICIDADES {nombre_usuario}, HAS APROBADO CON {promedio:.2f}!")
            else:
                print(f"LO SENTIMOS {nombre_usuario}, HAS REPROBADO CON {promedio:.2f}!")
                print(f"TE FALTARON {(60 - promedio):.2f} PUNTOS PARA APROBAR.")
            break
        else:
            print("ERROR: TODAS LAS CALIFICACIONES DEBEN ESTAR ENTRE 0 Y 100")
    except ValueError:
        print("ERROR: ASEGURATE DE INGRESAR SOLO NUMEROS VALIDOS SEPARADOS POR COMAS")

# Paso 4: Contar calificaciones mayores 
while True:
     try:
          valor_comparar=float(input("INGRESA UN VALOR PARA COMPARAR: "))
          break
     except ValueError:
          print("ERROR, INGRESA UN NUMERO ENTERO. ")
     
contador=0
index=0
while index<len(lista_notas):
     if lista_notas[index]>valor_comparar:
          contador+=1
     index+=1
print(f"HAY {contador} CALIFICIONES MAYORES A {valor_comparar}. ")

# Paso 5: Verificar y contar calificaciones especificas 
while True:
     try:
          calificaciones_especificas=float(input("INGRESA LA CALIFICACION ESPECIFICA QUE DESEAS BUSCAR"))
          break
     except ValueError:
        print("ERROR, DEBES INGRESAR UN NUMERO ENTERO")

cantidad_encontrada= 0
for nota_actual in lista_notas:
     if nota_actual== calificaciones_especificas:
          cantidad_encontrada +=1
          continue
     if nota_actual <0 or nota_actual>100:
          break 
if cantidad_encontrada>0:
     print(f"LA CALIFICACION {calificaciones_especificas} APARECE {cantidad_encontrada}")
else: 
     print(f"LA CALIFICACION {calificaciones_especificas} NO SE ENCUENTRA EN LA LISTA ")

# Fin del programa 
print(f"{nombre_usuario} Gracias por usar Califimaster pro. ")
     
