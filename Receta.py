#----------------------------------------------
# Asistente de cocina virtual
#----------------------------------------------

print("BIENVENIDO A DELIMASTER ")
nombre = input("CUAL ES TU NOMBRE: ")

#platillos
print ('''
       1. Ensalda Cesar con pollo
       2. Wrap de pollo con salsa Cesar
       3. Sandwich clasico de pollo 
       ''')

while True:
    try:
        orden =int(input("QUE DESEAS ORDENAR HOY?: "))
        if orden<1 or orden>3:
            print("ERROR, POR FAVOR INGRESE UN NUMERO ENTRE 1 Y 3")
            continue
        match orden:
            case 1: 
                print("¡TU ORDEN ES ENSALADA CESAR! ")
                break
            case 2:
                print ("¡TU ORDEN ES WRAP DE POLLO! ")
                break
            case 3:
                print ("¡TU ORDEN ES SANDWICH CLASICO DE POLLO! ")
                break
    except ValueError:
        print("INGRESE UN NUMERO ENTERO ")
                

#cuantos con bucle 
while True:
    try:
        cuantos=int(input("CUANTOS DESEAS ORDENAR?: "))
        if cuantos>0 :
            break
        else:
            print("ERROR, POR FAVOR INGRESE UN NUMERO ENTERO ")
    except ValueError:
        print("INGRESE UN NUMERO ENTERO ")

#funciones

def preparar_salsa_cesar():
    while True:
        try:
            pimienta= (input("¿DESEAS AGREGAR PIMIENTA A TU COMIDA? (Y/N) "))
            if pimienta!="Y" and pimienta!="N":
                print("ERROR, POR FAVOR ESCRIBE (Y/N)")
                pimienta_negra_molida = False
            else:
                pimienta_negra_molida = True
                break
        except:
            print("INGRESA SOLO LOS CARACTERES Y o N")  
    return pimienta_negra_molida


def preparar_ensalada_cesar(vegetales, salsa_cesar):
    prepara_salsa_cesar()
    return 

def preparar_wrap_cesar():
    return

def preparar_sandwich_pollo():
    return

def presentacion(tiras, normal):
    if tiras:
        print("AGREGASTE EL POLLO EN TIRAS ")
    elif normal:
        print("AGREGASTE EL POLLO A LA PLANCHA ")

def prepara_salsa_cesar(pimienta_negra_molida):
    return


#orden a realizar (preparacion..)
match orden:
    case 1:
        pimenta_negra_molida =preparar_salsa_cesar()
        preparar_ensalada_cesar(pimenta_negra_molida)
        
        
    case 2:
        preparar_wrap_cesar()
    case 3: 
        preparar_sandwich_pollo()




    
    