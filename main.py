

def mostrar_menu():
    menu: str = """
[*] Calculadora - By Juanjo 
  1 - sumar
  2 - restar
  4 - multiplicar
  5 - dividir
  5 - salir
                 """
    
    print(menu)


def main():
    mostrar_menu()
    opcion: str = input("[?] Introduce una opción: ");


main()
