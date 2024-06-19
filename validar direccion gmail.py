def validar_direccion_email(email):
    if "@" in email:
        return True
    else : 
        return False
direccion_email = input("Ingrese su dirreccion de correo electronico : ")
if validar_direccion_email(direccion_email):
        print("la direccion de correo electronico es valida")
else:
        print("la direccion de correo electronico es invalido")
        
       