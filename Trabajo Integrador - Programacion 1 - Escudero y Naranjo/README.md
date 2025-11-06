# 🌍 Gestión de Datos de Países en Python

## 📝 Descripción del Programa

Este proyecto es el **Trabajo Práctico Integrador (TPI)** de la asignatura **Programación I**. Se trata de una aplicación de consola desarrollada en **Python** cuyo objetivo es gestionar información de países a partir de un archivo de valores separados por comas (**CSV**).

La aplicación implementa estructuras fundamentales de Programación I (listas, diccionarios, funciones, condicionales) para ofrecer un menú interactivo que permite al usuario realizar las siguientes operaciones:

* **Carga de Datos:** Lee los datos de países desde el archivo `paises.csv`.
* **Búsqueda y Filtrado:** Permite la búsqueda por nombre y el filtrado por continente, rango de población o rango de superficie.
* **Ordenamiento:** Reorganiza la lista de países por nombre, población o superficie (ascendente o descendente).
* **Estadísticas:** Calcula indicadores clave como el promedio de población y superficie, y el conteo de países por continente, además de identificar los países con mayor y menor población.

---

## 💻 Instrucciones de Uso

### 🛠️ Requisitos

Asegúrese de tener **Python 3.x** instalado en su sistema.

### 🚀 Ejecución del Programa

1.  **Clonar el Repositorio:**
    ```bash
    git clone [https://github.com/](https://github.com/)[TU_USUARIO]/[TU_REPOSITORIO].git
    cd [nombre del repositorio]
    ```
    *(Nota: Reemplace la URL de ejemplo con la URL real de su repositorio en GitHub)*

2.  **Archivos Necesarios:**
    Asegúrese de que los siguientes archivos se encuentren en el directorio principal:
    * `Gestion-datos-paises.py` (El código fuente del programa)
    * `paises.csv` (El archivo de datos)

3.  **Ejecutar:**
    Abra una terminal o línea de comandos en el directorio del proyecto y ejecute el archivo principal:
    ```bash
    python Gestion-datos-paises.py
    ```

4.  **Interacción:**
    El programa mostrará un menú principal. Ingrese el número de la opción deseada y siga las instrucciones en pantalla.

---

## 📊 Ejemplos de Entradas y Salidas

Al iniciar el programa, se presentará el menú principal:

### **Entrada: Menú Principal**

MENÚ DE GESTIÓN DE PAÍSES

1.Buscar país por nombre

2.Filtrar por continente

3.Filtrar por rango de población

4.Filtrar por rango de superficie

5.Ordenar países

6.Mostrar estadísticas

7.Salir 

Ingrese una opción:

### **Ejemplo 1: Ordenar Países (Opción 5)**

Si desea ordenar los países por población de forma descendente:

* **Entrada del Usuario:**
    ```
    Ingrese una opción: 5
    Ordenar por (nombre/poblacion/superficie): poblacion
    Ascendente o descendente? (a/d): d
    ```
* **Salida del Programa:**
    El programa imprimirá la lista de países, comenzando por el de mayor población.

    ```
    {'nombre': 'China', 'poblacion': 1402112000, 'superficie': 9596961, 'continente': 'Asia'} 
    {'nombre': 'India', 'poblacion': 1380004385, 'superficie': 3287263, 'continente': 'Asia'} 
    ...
    ```

### **Ejemplo 2: Mostrar Estadísticas (Opción 6)**

* **Entrada del Usuario:**
    ```
    Ingrese una opción: 6
    ```
* **Salida del Programa:**
    La función de estadísticas devolverá los indicadores clave del conjunto de datos.

    ```
    País con mayor población: China (1402112000) 
    País con menor población: Islandia (341243) 
    Promedio de población: 130833139.81 
    Promedio de superficie: 2221376.57 
    Cantidad de países por continente: 
    - América: 8 
    - Asia: 19 
    - Europa: 14 
    - Oceanía: 2 
    - África: 7
    ```

---

## 👥 Participación de los Integrantes

El proyecto fue desarrollado por **Lautaro Naranjo** y **Martin Escudero**.

* **Lautaro Naranjo:**
    * Carga de datos desde CSV (`cargar_paises`).
    * Función de búsqueda por nombre (`buscar_pais`).
    * Funciones de filtrado (Continente, Población, Superficie).
* **Martin Escudero:**
    * Implementación del menú principal y la lógica de interacción.
    * Función de ordenamiento (`ordenar_paises`).
    * Función de estadísticas (`estadisticas`).

Ambos trabajamos en la **integración final**, modificando y probando el código para garantizar la coherencia y correcta funcionalidad de los datos entre los módulos.