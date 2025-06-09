from graphviz import Digraph
import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBST:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izq = self._insertar_recursivo(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._insertar_recursivo(nodo.der, valor)
        return nodo  # No inserta duplicados

    def eliminar(self, valor):
        self.raiz = self._eliminar_recursivo(self.raiz, valor)

    def _eliminar_recursivo(self, nodo, valor):
        if nodo is None:
            return None
        if valor < nodo.valor:
            nodo.izq = self._eliminar_recursivo(nodo.izq, valor)
        elif valor > nodo.valor:
            nodo.der = self._eliminar_recursivo(nodo.der, valor)
        else:
            # Nodo encontrado: 3 casos
            if nodo.izq is None:
                return nodo.der
            elif nodo.der is None:
                return nodo.izq
            # Nodo con dos hijos: reemplazar por el menor del subárbol derecho
            temp = self._min_valor_nodo(nodo.der)
            nodo.valor = temp.valor
            nodo.der = self._eliminar_recursivo(nodo.der, temp.valor)
        return nodo

    def _min_valor_nodo(self, nodo):
        actual = nodo
        while actual.izq:
            actual = actual.izq
        return actual

    # Recorridos del árbol
    def preorder(self):
        resultado = []
        self._preorder_recursivo(self.raiz, resultado)
        return resultado

    def _preorder_recursivo(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.valor)
            self._preorder_recursivo(nodo.izq, resultado)
            self._preorder_recursivo(nodo.der, resultado)

    def inorder(self):
        resultado = []
        self._inorder_recursivo(self.raiz, resultado)
        return resultado

    def _inorder_recursivo(self, nodo, resultado):
        if nodo:
            self._inorder_recursivo(nodo.izq, resultado)
            resultado.append(nodo.valor)
            self._inorder_recursivo(nodo.der, resultado)

    def postorder(self):
        resultado = []
        self._postorder_recursivo(self.raiz, resultado)
        return resultado

    def _postorder_recursivo(self, nodo, resultado):
        if nodo:
            self._postorder_recursivo(nodo.izq, resultado)
            self._postorder_recursivo(nodo.der, resultado)
            resultado.append(nodo.valor)

    def generar_grafico(self, nombre_archivo="arbol_interactivo", mostrar_recorrido=None):
        if self.raiz is None:
            print("El árbol está vacío. No se puede generar el gráfico.")
            return
           
        dot = Digraph(format='png')
        dot.attr(rankdir='TB', fontname='Arial', size='12,8')
       
        # Obtener el orden del recorrido si se especifica
        orden_recorrido = {}
        if mostrar_recorrido:
            if mostrar_recorrido == 'preorder':
                recorrido = self.preorder()
                titulo = "Preorder (Raíz → Izq → Der)"
            elif mostrar_recorrido == 'inorder':
                recorrido = self.inorder()
                titulo = "Inorder (Izq → Raíz → Der)"
            elif mostrar_recorrido == 'postorder':
                recorrido = self.postorder()
                titulo = "Postorder (Izq → Der → Raíz)"
           
            # Crear diccionario con el orden de visita
            for i, valor in enumerate(recorrido, 1):
                orden_recorrido[valor] = i
           
            # Agregar título al gráfico
            dot.attr(label=f'\\n{titulo}\\nSecuencia: {" → ".join(map(str, recorrido))}',
                    labelloc='t', fontsize='14')
       
        self._agregar_nodos(dot, self.raiz, es_raiz=True, orden_recorrido=orden_recorrido)
       
        # Generar nombre de archivo apropiado
        if mostrar_recorrido:
            nombre_completo = f"{nombre_archivo}_{mostrar_recorrido}"
        else:
            nombre_completo = nombre_archivo
           
        dot.render(nombre_completo, cleanup=True)
        print(f"Imagen generada: {nombre_completo}.png")

    def generar_todos_los_graficos(self, nombre_base="arbol"):
        if self.raiz is None:
            print("El árbol está vacío. No se pueden generar los gráficos.")
            return
           
        print("Generando todos los gráficos...")
       
        # Gráfico básico (sin recorrido)
        self.generar_grafico(nombre_base)
       
        # Gráficos con recorridos
        recorridos = ['preorder', 'inorder', 'postorder']
        for recorrido in recorridos:
            self.generar_grafico(nombre_base, recorrido)
       
        print(f"¡Completado! Se generaron 4 archivos:")
        print(f"   • {nombre_base}.png (árbol básico)")
        print(f"   • {nombre_base}_preorder.png")
        print(f"   • {nombre_base}_inorder.png")
        print(f"   • {nombre_base}_postorder.png")

    def _agregar_nodos(self, dot, nodo, es_raiz=False, orden_recorrido=None):
        if nodo is None:
            return
           
        # Determinar color del nodo
        if es_raiz:
            color = 'lightgreen'
        elif nodo.izq is None and nodo.der is None:
            color = 'lightblue'
        else:
            color = 'lightgray'
       
        # Crear etiqueta del nodo
        if orden_recorrido and nodo.valor in orden_recorrido:
            # Mostrar valor y orden de recorrido
            label = f"{nodo.valor}\\n({orden_recorrido[nodo.valor]})"
            # Usar colores más intensos para destacar el recorrido
            if es_raiz:
                color = 'green'
            elif nodo.izq is None and nodo.der is None:
                color = 'deepskyblue'
            else:
                color = 'gray'
        else:
            label = str(nodo.valor)
       
        dot.node(
            str(nodo.valor),
            label=label,
            style='filled',
            fillcolor=color,
            shape='ellipse',
            fontname='Arial',
            fontsize='12'
        )
       
        # Agregar conexiones
        if nodo.izq:
            self._agregar_nodos(dot, nodo.izq, orden_recorrido=orden_recorrido)
            dot.edge(str(nodo.valor), str(nodo.izq.valor))
        if nodo.der:
            self._agregar_nodos(dot, nodo.der, orden_recorrido=orden_recorrido)
            dot.edge(str(nodo.valor), str(nodo.der.valor))

    def generar_numeros_aleatorios(self, cantidad):
        """Genera números aleatorios según la cantidad especificada"""
        # Limpiar el árbol actual
        self.raiz = None
       
        # Generar números aleatorios únicos
        numeros_generados = set()
       
        # Rango de números aleatorios (más amplio para evitar colisiones)
        rango_min = 1
        rango_max = cantidad * 10  # Rango amplio para evitar duplicados
       
        while len(numeros_generados) < cantidad:
            numero = random.randint(rango_min, rango_max)
            numeros_generados.add(numero)
       
        # Convertir a lista y mezclar para orden de inserción aleatorio
        lista_numeros = list(numeros_generados)
        random.shuffle(lista_numeros)
       
        # Insertar los números en el árbol
        for numero in lista_numeros:
            self.insertar(numero)
       
        print(f"Números generados aleatoriamente: {sorted(lista_numeros)}")
        print(f"Total de nodos: {len(lista_numeros)}")
        print(f"Orden de inserción: {lista_numeros}")
       
        return lista_numeros

    def mostrar_recorridos(self):
        if self.raiz is None:
            print("El árbol está vacío.")
            return
           
        print("\nRECORRIDOS DEL ÁRBOL:")
        print(f"Preorder:  {' → '.join(map(str, self.preorder()))}")
        print(f"Inorder:   {' → '.join(map(str, self.inorder()))}")
        print(f"Postorder: {' → '.join(map(str, self.postorder()))}")

# Menú Interactivo
def menu():
    arbol = ArbolBST()

    while True:
        print("\n MENÚ:")
        print("1. Insertar valores (separados por coma)")
        print("2. Eliminar valores (separados por coma)")
        print("3. Generar árbol con números aleatorios")
        print("4. Generar TODOS los gráficos (básico + recorridos)")
        print("5. Mostrar recorridos (texto)")
        print("6. Salir")
        opcion = input("Elegí una opción: ")

        if opcion == '1':
            entrada = input(" Ingresá valores a insertar (ej: 10,20,30): ")
            try:
                valores = [int(v.strip()) for v in entrada.split(",")]
                for v in valores:
                    arbol.insertar(v)
                print("Valores insertados.")
            except ValueError:
                print("Entrada inválida. Usá solo números separados por coma.")
               
        elif opcion == '2':
            entrada = input("🗑 Ingresá valores a eliminar (ej: 10,20): ")
            try:
                valores = [int(v.strip()) for v in entrada.split(",")]
                for v in valores:
                    arbol.eliminar(v)
                print("Valores eliminados (si existían).")
            except ValueError:
                print("Entrada inválida. Usá solo números separados por coma.")
               
        elif opcion == '3':
            while True:
                try:
                    cantidad = input("¿Cuántos nodos querés en el árbol? (3-50): ")
                    cantidad = int(cantidad)
                   
                    if cantidad < 3:
                        print("Mínimo 3 nodos para tener un árbol interesante.")
                        continue


                    elif cantidad > 50:
                        print("Máximo 50 nodos para mantener legible el gráfico.")
                        continue


                    else:
                        arbol.generar_numeros_aleatorios(cantidad)
                        break
                       
                except ValueError:
                    print("Por favor ingresá un número válido.")           
        
        elif opcion == '4':
            arbol.generar_todos_los_graficos() 
          
        elif opcion == '5':
            arbol.mostrar_recorridos() 
          
        elif opcion == '6':
            print("Programa finalizado.")
            break           

        else:
            print("Opción no válida. Intentá de nuevo.")

# Ejecutar
if __name__ == "__main__":
    menu()