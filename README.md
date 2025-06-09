# Trabajo Práctico Integrador - Árboles Binarios

## 📋 Información General

**Materia:** Programación I  
**Carrera:** Tecnicatura Universitaria en Programación - UTN  
**Estudiantes:** Aguirre Luciano & Zupan Lucas  
**Fecha:** 09 de Junio de 2025

## 🎯 Objetivo

Implementación y análisis de un **Árbol Binario de Búsqueda (BST)** en Python, aplicando conceptos teóricos de estructuras de datos avanzadas con visualización gráfica interactiva.

## 🌳 Características del Proyecto

### Funcionalidades Principales

- ✅ **Inserción** dinámica de múltiples valores
- ✅ **Eliminación** controlada de nodos (incluye casos complejos con dos hijos)
- ✅ **Recorridos clásicos**: Preorden, Inorden, Postorden
- ✅ **Visualización gráfica** automática con Graphviz
- ✅ **Generación aleatoria** de árboles (3-50 nodos)
- ✅ **Interfaz interactiva** por consola

### Tipos de Visualización

- Árbol básico con colores diferenciados (raíz, nodos internos, hojas)
- Recorridos destacados con numeración y colores específicos
- Exportación automática de múltiples gráficos (.png)

## 🛠️ Tecnologías Utilizadas

- **Python 3.12**
- **Graphviz** (visualización)
- **Random** (generación de datos)
- **Visual Studio Code**

## 📦 Instalación

```bash
# Instalar dependencias de Python
pip install graphviz

# Instalar Graphviz (sistema)
# Windows: Descargar desde https://graphviz.org/download/
# Ubuntu/Debian: sudo apt-get install graphviz
# macOS: brew install graphviz
```

## 🚀 Uso

```bash
python arbol_bst.py
```

### Menú Interactivo

1. **Insertar valores** (separados por coma)
2. **Eliminar valores** (separados por coma)
3. **Generar árbol aleatorio** (3-50 nodos)
4. **Generar TODOS los gráficos** (básico + recorridos)
5. **Mostrar recorridos** (solo texto)
6. **Salir**

## 📊 Ejemplo de Uso

```python
# Insertar valores: 50,30,70,20,40,60,80
# Resultado: Árbol BST correctamente estructurado

# Recorridos generados:
# Preorder: 50 → 30 → 20 → 40 → 70 → 60 → 80
# Inorder:  20 → 30 → 40 → 50 → 60 → 70 → 80  (ordenado!)
# Postorder: 20 → 40 → 30 → 60 → 80 → 70 → 50
```

## 🎨 Archivos Generados

El programa crea automáticamente:

- `arbol.png` (árbol básico)
- `arbol_preorder.png` (recorrido preorden)
- `arbol_inorder.png` (recorrido inorden)
- `arbol_postorder.png` (recorrido postorden)

## ✅ Casos de Prueba Validados

| Operación                | Resultado Esperado      | Estado |
| ------------------------ | ----------------------- | ------ |
| Insertar [50,30,70]      | Árbol con raíz 50       | ✅     |
| Duplicados               | Ignorados correctamente | ✅     |
| Eliminar hoja            | Sin afectar estructura  | ✅     |
| Eliminar nodo con hijos  | Reemplazo por sucesor   | ✅     |
| Árbol aleatorio 30 nodos | Generación exitosa      | ✅     |

## 🏗️ Estructura del Código

```
├── class Nodo           # Representa cada elemento del árbol
├── class ArbolBST       # Funcionalidad principal del BST
│   ├── insertar()       # Inserción recursiva
│   ├── eliminar()       # Eliminación con 3 casos
│   ├── recorridos()     # Pre/In/Post orden
│   ├── visualización()  # Graphviz integration
│   └── menu()           # Interfaz de usuario
```

## 🎓 Conceptos Aplicados

- **Recursividad** en operaciones de árbol
- **Estructuras de datos jerárquicas**
- **Algoritmos de recorrido** (DFS variants)
- **Programación orientada a objetos**
- **Visualización de datos**
- **Manejo de casos edge** (eliminación compleja)

## 📈 Rendimiento

- Inserción/Búsqueda: **O(log n)** promedio
- Recorridos: **O(n)**
- Probado hasta **50 nodos** con rendimiento fluido

## 🔗 Enlaces

- **Video explicativo:** [LINK VIDEO INSERTAR]
- **Repositorio:** [LINK REPOSITORIO INSERTAR]

## 👥 Autores

- **Luciano Aguirre**
- **Lucas Zupan**

_Tecnicatura Universitaria en Programación - Universidad Tecnológica Nacional_
