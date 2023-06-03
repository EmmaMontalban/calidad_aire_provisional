# MAGNITUDES DE MEDIDA DE LOS CONTAMINANTES ATMOSFÉRICOS:

* 01 SO2: Dióxido de Azufre
* 08 NO2: Dióxido de Nitrógeno  
* 09 PM2.5: Partículas < 2.5 μm  
* 10 PM10: Partículas < 10 μm  
* 14 O3: Ozono 
* 

# ESTACIONES DE MEDIDA

01. 28079004: Pza. de España
02. 28079008: Escuelas Aguirre
03. 28079011 Av. Ramón y Caja
04. 28079016 Arturo Soria
05. 28079017 Villaverde Alto
06. 28079018 C/ Farolillo
07. 28079024 Casa de Campo
08. 28079027 Barajas
09. 28079035 Pza. del Carmen
10. 28079036 Moratalaz 
11. 28079038 Cuatro Caminos  
12. 28079039 Barrio del Pilar
13. 28079040 Vallecas
14. 28079047 Méndez Álvaro 
15. 28079048 Pº. Castellana 
16. 28079049 Retiro 
17. 28079050 Pza. Castilla 
18. 28079054 Ensanche Vallecas 
19. 28079055 Urb. Embajada (Barajas) 
20. 28079056 Plaza Elíptica 
21. 28079057 Sanchinarro 
22. 28079058 El Pardo 
23. 28079059 Parque Juan Carlos I 
24. 28079060 Tres Olivos 


# INDICE DE CALIDAD DEL AIRE (ICA)

El Índice de Calidad del Aire (ICA) establecido por la Red de Vigilancia y Control de la Contaminación Atmosférica de la Comunidad de Madrid (REVA). 
El ICA de Madrid se basa en la concentración de cuatro contaminantes principales: 

* dióxido de azufre (SO2)
* dióxido de nitrógeno (NO2)
* partículas en suspensión (PM10) 
* ozono (O3).

El cálculo del ICA de Madrid se realiza asignando un valor numérico a cada uno de los contaminantes y luego promediando estos valores ponderados. La fórmula utilizada para calcular el ICA es la siguiente:

- ICA = (ICA_SO2 + ICA_NO2 + ICA_PM10 + ICA_O3) / 4

Donde ICA_SO2, ICA_NO2, ICA_PM10 y ICA_O3 son los valores individuales del índice de calidad del aire para cada contaminante, que se calculan de la siguiente manera:

- ICA_SO2 = (Concentración_SO2 / Valor_Límite_SO2) * 100
- ICA_NO2 = (Concentración_NO2 / Valor_Límite_NO2) * 100
- ICA_PM10 = (Concentración_PM10 / Valor_Límite_PM10) * 100
- ICA_O3 = (Concentración_O3 / Valor_Límite_O3) * 100

En cada fórmula, se divide la concentración del contaminante por el valor límite establecido para ese contaminante y se multiplica por 100 para obtener un porcentaje. Luego, se promedian los valores de ICA de los cuatro contaminantes para obtener el índice de calidad del aire general.


* Supongamos que tenemos los siguientes datos ficticios para las concentraciones  de los contaminantes en Madrid:

    Dióxido de Azufre (SO2): Concentración = 15 μg/m³, Valor Límite = 50 μg/m³
    Dióxido de Nitrógeno (NO2): Concentración = 40 μg/m³, Valor Límite = 40 μg/m³
    Partículas en Suspensión (PM10): Concentración = 25 μg/m³, Valor Límite = 50 μg/m³
    Ozono (O3): Concentración = 60 μg/m³, Valor Límite = 120 μg/m³

## VALORES LIMITE CONTAMINANTES
Compuesto   Valor límite /      Concentración       Nº máximo de superaciones
            objetivo / 
            Umbral de Alerta

* PM10: 	Media anual. 	     40 μg/m3 	 
            Media diaria. 	     50 μg/m3 	         35 días/año
* SO2   	Media diaria. 	     125 μg/m3 	         3 días/año
            Media horaria. 	     350 μg/m3 	         24 horas/año
            Umbral de alerta     500 μg/m3
            (3 horas consecutivas en área representativa de 100 km o zona o aglomeración entera). 	 	 
* NO2   	Media anual. 	     40 μg/m3 	 
            Media horaria. 	     200 μg/m3 	        18 horas/año
            Umbral de alerta     400 μg/m3
            (3 horas consecutivas en área representativa de 100 km o zona o aglomeración entera). 	 	 
* O3   	    Máxima diaria de     120 μg/m3 	        25 días /  año,
            las medias móviles octohorarias.  	promediados en un período de 3 años
            Umbral de información:
            Media horaria. 	      180 μg/m3 	 
            Umbral de alerta. 
            Media horaria. 	      240 μg/m3 	 
 	 

Calculamos el índice de calidad del aire para cada contaminante utilizando las fórmulas proporcionadas anteriormente:

ICA_SO2 = (15 / 50) * 100 = 30
ICA_NO2 = (40 / 40) * 100 = 100
ICA_PM10 = (25 / 50) * 100 = 50
ICA_O3 = (60 / 120) * 100 = 50

Luego, promediamos los valores de ICA de los cuatro contaminantes para obtener el índice de calidad del aire general:

ICA = (30 + 100 + 50 + 50) / 4 = 57.5

En este ejemplo ficticio, el índice de calidad del aire en Madrid sería de aproximadamente 57.5.


## CODIGO DE EJEMPLO PARA CALCULAR ICA.
# Crear función calcular_ICA
    def calcular_ICA(concentraciones, valores_limites):
        num_contaminantes = len(concentraciones)
        ica_total = 0
        
        for i in range(num_contaminantes):
            ica_contaminante = (concentraciones[i] / valores_limites[i]) * 100
            ica_total += ica_contaminante
        
        ica_promedio = ica_total / num_contaminantes
        return ica_promedio

# Datos de concentraciones de contaminantes ficticios en Madrid
concentraciones = [15, 40, 25, 60]  # SO2, NO2, PM10, O3
valores_limites = [50, 40, 50, 120]  # SO2, NO2, PM10, O3

# Calcular el índice de calidad del aire
ica = calcular_ICA(concentraciones, valores_limites)
print("El índice de calidad del aire en Madrid es:", ica)

### DATASET METEREOLOGIA

# CÓDIGOS DE MEDIDAS DE LOS DATOS METEREOLOGICOS:
 
    80: RADIACIÓN ULTRAVIOLETA
    81: VELOCIDAD DEL VIENTO
    82: DIRECCIÓN DEL VIENTO
    83: TEMPERATURA
    86: HUMEDAD RELATIVA
    87: PRESIÓN BARIOMÉTRICA
    88: RADIACIÓN SOLAR
    89: PRECIPITACIÓN 

# CÓDIGOS DE ESTACIONES
01. 28079102 J.M.D. Moratalaz
02. 28079103 J.M.D. Villaverde
03. 28079104 E.D.A.R. La China
04. 28079106 Centro Mpal. De Acústica
05. 28079107 J.M.D. Hortaleza
06. 28079108 Peñagrande
07. 28079109 J.M.D.Chamberí
08. 28079110 J.M.D.Centro
09. 28079111 J.M.D.Chamartin
10. 28079112 J.M.D.Vallecas 1
11. 28079113 J.M.D.Vallecas 2
12. 28079114 Matadero 01
13. 28079115 Matadero 02
14. 28079004 Plaza España
15. 28079008 Escuelas Aguirre
16. 28079016 Arturo Soria
17. 28079018 Farolillo
18. 28079024 Casa de Campo
19. 28079035 Plaza del Carmen
20. 28079036 Moratalaz
21. 28079038 Cuatro Caminos
22. 28079039 Barrio del Pilar
23. 28079054 Ensanche de Vallecas
24. 28079056 Plaza Elíptica
25. 28079058 El Pardo
26. 28079059 Juan Carlos I
