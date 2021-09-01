from pymongo.message import query
import connection as net
import os
import random

#Creando la base de datos
mydb = net.client["mydatabase"]
mycol = mydb["Centro Escolares"]

while True:
     os.system("cls")
     print("Menu: ")
     print("1.Insertar un CE")
     print("2.Visualizar base de datos de los CE")
     print("3.Actualizar un CE")
     print("4.Eliminar un CE")
     print("5.Salir")
     option= int(input("Ingrese su opcion:\n"))
    
     if option == 1:
         Nombre=input("Ingrese el nombre del centro escolar:\n")
         Departamento = input("Ingrese el departamento:\n")
         Municipio = input("Ingrese el municipio:\n")
         ID = random.randrange(0,1000000)
         mydict = {"_id":ID,
                  "Nombre":Nombre,
                  "Departamento":Departamento,
                  "Municipio":Municipio
                 }
         insertar = mycol.insert_one(mydict)

     elif option == 2:
         for x  in mycol.find():
            print(x)
         print("Presione una tecla para continuar")
         input()

     elif option == 3:
         ID = int(input("Ingrese el ID del CE que desea actualizar:\n"))
         queryID = {"_id":ID}
         if queryID in mycol.find(queryID,{"_id":1,"Nombre":0,"Departamento":0,"Municipio":0}):
            
            myquery = queryID
            print("Seleccione que dato actualizara del CE:")
            print("1.Nombre")
            print("2.Departamento")
            print("3.Municipio")
            option = int(input("Seleccione opcion:\n"))
            if option == 1:
               Nombre = input("Ingrese el nuevo nombre:\n")
               newquery = {"$set":{"Nombre":Nombre}}
               mycol.update_one(myquery,newquery)
            elif option == 2:
               Departamento = input("Ingrese nuevo departamento:\n")
               newquery = {"$set":{"Departamento":Departamento}}
               mycol.update_one(myquery,newquery)
            elif option == 3:
               Municipio = input("Ingrese nuevo municipio:\n")
               newquery = {"$set":{"Municipio":Municipio}}
               mycol.update_one(myquery,newquery)
            else:
               print("Opcion invalida")
         
            for x  in mycol.find():
               print(x)
            print("Presione una tecla para continuar")
            input()
         else:
            print("ID no encontrado")
            print("Presione una tecla para continuar")
            input()

         
     elif option == 4:
        ID = int(input("Ingrese el ID del CE que desea eliminar:\n"))
        myquery = {"_id":ID}
        mycol.delete_one(myquery)
        for x  in mycol.find():
            print(x)
        print("Presione una tecla para continuar")
        input()

     else:
        print("Saliendo...")
        break

