# 🌍 Análisis de la Calidad del Aire en Madrid (2019-2023)

## 🔍 Problema Identificado
La contaminación atmosférica está provocada por la emisión de determinadas sustancias que generan efectos perjudiciales en el medio ambiente y la salud. El **ozono troposférico** y las **partículas en suspensión (PM10, PM2.5)** son los más preocupantes, con efectos que van desde irritaciones leves hasta enfermedades respiratorias graves y mortalidad prematura.

## 🎯 Objetivo
📊 **Modelo predictivo de los efectos de la calidad del aire en la salud**

- Analizar la relación entre **calidad del aire y salud** 🏥 considerando datos meteorológicos 🌦️.
- Fuentes de datos: **Calidad del aire** y **Meteorología**.
- Datos obtenidos del **Portal del Ayuntamiento de Madrid** 🏛️.


## 🗂️ Estructura del Proyecto
📂 **Carpetas y archivos clave:**
```
📦 Calidad_Aire_Madrid
 ├── 📂 data               # Conjuntos de datos originales y procesados
 │   ├── calidad_aire_2022.csv
 │   ├── meteo_2022.csv
 │   └── estaciones.csv
 ├── 📂 notebooks          # Notebooks de análisis y modelado
 │   ├── 1_EDA.ipynb
 │   ├── 2_Modelado.ipynb
 │   ├── 3_Predicciones.ipynb
 │   └── 4_Visualizacion.ipynb
 ├── 📂 modelos            # Modelos entrenados
 │   ├── modelo_arima.pkl
 │   ├── modelo_regresion.pkl
 │   └── evaluacion_modelos.txt
 ├── 📂 dashboards         # Informes y visualizaciones en Power BI
 │   ├── dashboard.pbix
 ├── 📂 imagenes           # Gráficos generados
 ├── 📂 assets             # Documentos adicionales
 │   ├── presentacion_calidad_aire.pdf
 ├── requirements.txt      # Dependencias del proyecto
 ├── README.md             # Documentación del proyecto
```

## 🛠️ Instalación del Proyecto
Para instalar y ejecutar el proyecto en tu entorno local, sigue estos pasos:

1. **Clonar el repositorio**:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd Calidad_Aire_Madrid
   ```
2. **Crear y activar un entorno virtual (opcional pero recomendado)**:
   ```bash
   python -m venv env
   source env/bin/activate  # En MacOS/Linux
   env\Scripts\activate    # En Windows
   ```
3. **Instalar las dependencias**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Ejecutar los notebooks**:
   - Abrir Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - Navegar a la carpeta `notebooks/` y ejecutar los análisis.

5. **Visualizar el dashboard en Power BI**:
   - Abrir el archivo `dashboard.pbix` en Power BI.

## 🛠️ Tecnologías y Herramientas Utilizadas
- **🖥️ Lenguajes de Programación:** Python 🐍
- **📚 Bibliotecas:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-Learn 📊
- **🗄️ Bases de Datos:** PostgreSQL 🐘, MySQL 🛢️
- **📊 Visualización:** Power BI 📈
- **🔗 Control de Versiones:** Git 🔄 y GitHub 🐙

## 💡 Solución Propuesta
Se ha desarrollado un **Índice de Calidad del Aire (ICA)** que permite monitorear los niveles de contaminación y establecer límites para evaluar el cumplimiento de normativas. El ICA categoriza la calidad del aire en seis niveles:
1. **Buena** ✅
2. **Razonablemente buena** 🟢
3. **Regular** 🟡
4. **Desfavorable** 🟠
5. **Muy desfavorable** 🔴
6. **Extremadamente desfavorable** ⚠️

Los contaminantes incluidos en el ICA son:
- **PM10** 🌪️
- **PM2.5** 🌫️
- **O3 (Ozono troposférico)** ☁️
- **NO2 (Dióxido de nitrógeno)** 🚗💨
- **SO2 (Dióxido de azufre)** 🏭

## 📥 Recogida de Datos
🔗 **Fuentes oficiales:**
- **[Calidad del Aire](https://datos.madrid.es/sites/v/index.jsp?vgnextoid=aecb88a7e2b73410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD)** 📊
- **[Meteorología](https://datos.madrid.es/sites/v/index.jsp?vgnextoid=fa8357cec5efa610VgnVCM1000001d4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD)** 🌦️

📅 **Datos horarios desde:**
- Calidad del aire: **2001**
- Meteorología: **2019**

📍 **Estaciones de control seleccionadas:**
1. **Escuelas Aguirre** (Urbana Tráfico)
2. **C/ Farolillo** (Urbana Fondo)
3. **Casa de Campo** (Suburbana)
4. **Plaza del Carmen** (Urbana Fondo)
5. **Moratalaz** (Urbana Tráfico)

## 📖 Análisis de Datos
📜 **Arquitectura del Proyecto:**
1. **ETL (Extracción, Transformación y Limpieza)**
   - Datos extraídos del Ayuntamiento de Madrid 📥.
   - Tratamiento de **outliers** con la técnica del **rango intercuartílico** 📊.
2. **EDA (Análisis Exploratorio de Datos)**
   - **Univariante** 📈
   - **Bivariante** 🔄
   - **Multivariante** 🔬
3. **Modelos Predictivos** 🧠
   - **Regresión Lineal Simple** 📉
   - **ARIMA (2,1,2)** para predicción de tendencias temporales ⏳

## 📊 Visualización de Resultados
El análisis se complementa con un **informe interactivo en Power BI**, donde se pueden consultar:
- **Estaciones de medida** 📌
- **Análisis detallado de contaminantes** 📊
- **Factores influyentes en la temperatura** 🌡️

---
🔬 **Este estudio busca entender mejor cómo la calidad del aire afecta nuestra salud y proporcionar herramientas para la toma de decisiones públicas y personales.** 💡💚

---
## Contacto
Para consultas o colaboraciones, contactar a cualquiera de los integrantes del equipo.

## 📌 Grupo 1:
- **Emma Montalbán**
- **Erika Samara Alvares**
- **Juan Carlos Menéndez Gijón**
- **Francisco Polonio Monterroso**

---
📂 **Acceso a la Presentación:**  
👉 [Presentación del Proyecto](assets/presentacion_calidad_aire.pdf) 📑  





