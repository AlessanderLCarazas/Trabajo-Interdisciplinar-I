# Gestor Académico: Asistencia y Notas

## Descripción
Este proyecto es una aplicación de escritorio desarrollada en Python que permite gestionar la asistencia y las calificaciones de estudiantes en diferentes cursos. Está diseñado para simplificar el registro, análisis y generación de reportes, ofreciendo una solución integral para el monitoreo del desempeño académico.

Este trabajo fue desarrollado como proyecto final del curso **Trabajo Interdisciplinar I**, integrando conceptos de programación, diseño de interfaces gráficas y análisis de datos.

---

## Características

### **Gestor de Asistencia**
- **Registro Diario**: Permite registrar la asistencia de los estudiantes en cada clase.
- **Cálculo Automático**: Calcula el porcentaje de asistencia acumulado por estudiante.
- **Reportes en PDF**: Genera reportes detallados con estadísticas de asistencia.
- **Gráficos de Visualización**: Incluye gráficos de barras y pastel para ilustrar los datos.

### **Gestor de Notas**
- **Registro de Notas**: Almacena notas continuas y parciales para cada estudiante.
- **Promedios Automáticos**: Calcula automáticamente los promedios finales basados en ponderaciones específicas de cada curso.
- **Análisis de Desempeño**: Identifica a los estudiantes en riesgo de desaprobar y genera estadísticas de rendimiento.
- **Generación de Reportes**: Exporta los resultados finales a archivos PDF.

### **Interfaz Gráfica**
- **Tkinter**: Diseño sencillo e intuitivo para facilitar la interacción del usuario.
- **Navegación por Cursos**: Permite seleccionar rápidamente un curso y realizar tareas específicas.
- **Opciones de Reporte**: Botones dedicados para generar reportes y visualizar estadísticas.

---

## Estructura del Proyecto

El proyecto incluye los siguientes archivos principales:

- **`asistencia(cursos).py`**: Manejo de la asistencia diaria, generación de gráficos y reportes.
- **`notas(cursos).py`**: Gestión de notas continuas y parciales, cálculo de promedios y generación de reportes.
- **`notas_2(cursos).py`**: Funciones adicionales para reportes y análisis de desempeño.
- **Carpetas de Datos**: Contiene archivos `.txt` para almacenar la información persistente de asistencia y calificaciones.

---

## Requisitos de Instalación

### **Software Necesario**
- **Python 3.x**: Asegúrate de tener instalado Python en tu sistema.

### **Instalación de Dependencias**
Ejecuta el siguiente comando para instalar las bibliotecas necesarias:
```bash
pip install matplotlib pillow aspose-words
