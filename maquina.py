nombresproductos = ["agua", "refresco", "zumo"]
precioproductos = [0.50, 0.75, 0.95]
reservamonedas = [20, 20, 20, 20, 20, 20]
valoresmonedas = [2, 1, 0.50, 0.20, 0.10, 0.05]

def imprimirmenu(nombres, precios):
    cont = 0
    textomenu = ""
    for nombre in nombres:
        textomenu += f"{cont+1} - {nombre} : {precios[cont]} \n"
        cont += 1
    textomenu += f"{cont+1} - salir"
    print(textomenu)

def ingresaropcion():
    opcion = input("Introduce opción (1-3 para productos, 4 para salir): ")
    while opcion not in "1234":
        opcion = input("Introduce una opción válida (1-3 para productos, 4 para salir): ")
    return int(opcion) - 1

def ingresarimporte(opcion):
    precio = precioproductos[opcion]
    importeusuario = 0
    monedasintroducidas = []
    while importeusuario < precio:
        print(f"Le queda {round(precio - importeusuario, 2)}€")
        moneda = ingresarmoneda()
        importeusuario += moneda
        monedasintroducidas.append(moneda)
        if importeusuario > precio:
            resto = importeusuario - precio
            darcambio(resto)
            entregarproducto(nombresproductos[opcion])
            sumarmonedas(monedasintroducidas)

def darcambio(importe):
    vueltas = 0
    while importe > 0:
        for valor in sorted(valoresmonedas, reverse=True):  # Intentamos dar cambio con las monedas más grandes
            if valor <= importe:
                cantidad = int(importe // valor)
                importe -= cantidad * valor
                print(f"Te devuelvo {cantidad} monedas de {valor}€")
                break

def sumarmonedas(monedas):
    for moneda in monedas:
        index = valoresmonedas.index(moneda)
        reservamonedas[index] += 1

def entregarproducto(producto):
    print(f"Aquí tienes tu {producto}")

def ingresarmoneda():
    print("Monedas disponibles: 2€, 1€, 0.50€, 0.20€, 0.10€, 0.05€")
    moneda = float(input("Introduce una moneda válida: "))
    while moneda not in valoresmonedas:
        moneda = float(input("Introduce una moneda válida: "))
    return moneda

imprimirmenu(nombresproductos, precioproductos)
opcion = ingresaropcion()
if opcion < len(nombresproductos):
    ingresarimporte(opcion)
else:
    print("¡Hasta luego!")
