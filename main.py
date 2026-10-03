productos = []
seguir = True
while seguir:
    opcion = input("Elija una opcion: \n1.Agregar producto\n2.Visualizar productos\n3.Buscar producto\n4.Eliminar producto\n5.Salir\n").strip()
    if opcion.isdigit():
        match opcion:
            case "1":
                producto = []
                nombre = input("Ingrese el nombre del producto: ").strip().lower()
                if nombre == "":
                    print("[ALERTA] Nombre de producto no valido")
                    continue
                else:
                    producto.append(nombre)
                categoria = input("Ingrese la categoria del producto: ").strip().lower()
                if categoria == "":
                    print("[ALERTA] Categoria de producto no valida")
                    continue
                else:
                    producto.append(categoria)
                precio = input("Ingrese el precio del producto: ").strip() 
                if precio == "" or not precio.isdigit() or int(precio) <= 0:
                    print("[ALERTA] Precio de producto no valido")
                    continue
                else:
                    producto.append(int(precio))
                productos.append(producto)
                print("[EXITO] Producto agregado correctamente")
            case "2":
                if len(productos) > 0:
                    productos.sort()
                    for i in range(len(productos)):
                        print(f"Producto {i + 1}: nombre: {productos[i][0].capitalize()}, categoria: {productos[i][1].capitalize()}, precio: {productos[i][2]}")
                else:
                    print("[ALERTA] No hay productos para mostrar")
            case "3":
                if len(productos) > 0:
                    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip().lower()
                    if nombre_buscar == "":
                        print("[ALERTA] Nombre de producto no valido")
                        continue
                    else:
                        encontrado = False
                        for i in range(len(productos)):
                            if productos[i][0] == nombre_buscar:
                                encontrado = True
                                print(f"Producto {i + 1}: nombre: {productos[i][0].capitalize()}, categoria: {productos[i][1].capitalize()}, precio: {productos[i][2]}")
                        if not encontrado:
                            print("[ALERTA] Producto no encontrado")
                else:
                    print("[ALERTA] No hay productos para mostrar")   
            case "4":
                if len(productos) > 0:
                    index_eliminar = input("Ingrese el numero del producto a eliminar: ").strip()
                    if index_eliminar == "" or not index_eliminar.isdigit():
                        print("[ALERTA] Numero de producto no valido")
                        continue
                    else:
                        if int(index_eliminar) > 0 and int(index_eliminar) <= len(productos):
                            productos.pop(int(index_eliminar) - 1)
                            print("[EXITO] Producto eliminado correctamente")
                        else:
                            print("[ALERTA] El numero ingresado no existe en la lista")   
                else:
                    print("[ALERTA] No hay productos para eliminar")
            case "5":
                print("Saliendo del programa...")
                seguir = False
            case _:
                print("[ALERTA] Opcion fuera de rango (elija un numero de 1 a 5)") 
    else:
        print("[ALERTA] Opcion no valida")
