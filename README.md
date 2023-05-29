# PORTAL DEL AYUNTAMIENTO DE MADRID

* Esta es la url donde está el conjunto de datos del proyecto.
    https://datos.madrid.es/sites/v/index.jsp?vgnextoid=aecb88a7e2b73410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD


* En este enlace está la interpretación de las columnas de los csv.
    https://datos.madrid.es/FWProjects/egob/Catalogo/MedioAmbiente/Aire/Ficheros/Interprete_ficheros_%20calidad_%20del_%20aire_global.pdf

   
# PORTAL DE CONSULTAS DE FOMENTO 
* Es la base de datos de fomento donde se pueden hacer consultas sobre las emisiones que provocan efecto invernadero según el tipo de vehículos

    https://apps.fomento.gob.es/BDOTLE/inicioBD.aspx


# PORTAL ESTADÍSTICO DE LA DGT
* Se pueden sacar informes del parque de vehiculos por año de matriculación, carburante y tipo de vehiculo. He preparado unos dataset para ver si nos pueden servir de algo con otros datos que recopilemos:
   
   https://sedeapl.dgt.gob.es/WEB_IEST_CONSULTA/

  He preparado un csv y he probado que se puede cargar con pandas, hay que estudiar si los datos nos sirven para el análisis.

  MadridVehiculos.csv (este es el csv que he preparado)

# Asociación Española de Fabricantes de Automóviles y Camiones
* Informes de matriculaciones de vehículos en un año y según el tipo de carburante.
    Matriculaciones de turismos y todoterrenos (Se puede filtrar por Comunidad Autónoma)
    Matriculaciones de vehículos comerciales ligeros
    Matriculaciones de vehículos industriales, autobuses y microbuses

    https://anfac.com/cifras-clave/
   
# OBJETIVOS:
1. Escenario 1: Modelo predictivo de los efectos de la calidad del aire en la salud.
* Calidad del aire vs niveles de polen, teniendo en cuenta datos metereológicos
* Datos: Aire, metereología

2. Escenario 2: Modelo predictivo de los efectos del tráfico en la calidad del aire.
* Calidad del aire vs intensidad del tráfico
* Datos: aire, tráfico

3. Escenario 3: Modelo predictivo de los efectos de los tipos de vehículos y carburante en la calidad del aire.
* Calidad del aire vs tipo carburante de vehículos
* Datos: aire, vehículos

# CONTAMINANTES PARA EL ESTUDIO:
En Madrid, los más relevantes en cuanto a sus efectos para la salud son:
* Dióxido de nitrógeno (NO2):
    Es un contaminante atmosférico que se produce fundamentalmente en las combustiones de los vehículos de motor.

    Hasta el 80% de las emisiones de este contaminante procede del tráfico rodado, sobre todo de los vehículos diésel. El resto de las emisiones se origina durante la combustión de gas, petróleo y carbón, en centrales térmicas, actividades industriales, calefacciones, incineradoras, etc

    Los principales síntomas asociados a episodios de alta contaminación por dióxido de nitrógeno son:
    - Picor de ojos, nariz y garganta.
    - Irritación de los bronquios con tos, flemas, dificultad para respirar.

* Partículas en suspensión: 
    Constituyen un contaminante atmosférico procedente    tanto de fuentes naturales (tormentas de arena, erupciones volcánicas, incendios forestales, etc.) como de la actividad humana (tráfico, especialmente vehículos diésel, incineradoras, calefacciones de carbón, minería, procesos industriales, etc.).
    - PM2,5 (tamaño inferior a 2,5 micras): 
        Proceden fundamentalmente de la actividad humana, pueden penetrar hasta las partes más profundas del pulmón y pasar a la sangre, y por ello resultan especialmente nocivas.
    - PM10 ():tamaño inferior a 10 micras
        Al ser más grandes quedan en buena parte retenidas en las porciones superiores del aparato respiratorio, como las fosas nasales o los grandes bronquios. Resultan menos perjudiciales para la salud que las PM2,5, pero no son inocuas y se ha observado un aumento de la demanda de atención urgente por crisis asmáticas cuando aumenta su concentración en el aire.

    En nuestra Comunidad, una causa muy frecuente de aumento de partículas es la llegada de polvo del desierto del Sáhara empujado por vientos del sur.

    Este polvo, que puede permanecer en el aire durante horas y presentarse como una neblina de color marrón, puede llevar en su composición materia mineral (arcillas, cuarzos, carbonatos, etc.) y también biológico, como fragmentos vegetales, polen, virus, bacterias, etc.


* Ozono troposférico(O3):
    Es un gas incoloro que puede resultar beneficioso o nocivo para la salud, dependiendo de si se encuentra en las capas más altas de la atmósfera o a nivel del suelo. Por ello se habla de:

    - Ozono bueno (ozono estratosférico): 
        Se localiza en la estratosfera, a una distancia de la superficie terrestre de entre 12 a 50 km, formando una capa que nos protege de los dañinos rayos ultravioleta del sol. Este es el ozono al que se hace referencia cuando se habla del “agujero de la capa de ozono”.
    - Ozono malo (ozono troposférico): 
        Se localiza en la troposfera, es decir, la parte de la atmósfera donde se desarrolla la vida humana. Este ozono se forma como resultado de reacciones químicas, en presencia de la luz solar, a partir de los contaminantes emitidos por automóviles, centrales térmicas, refinerías, procesos industriales diversos etc. Cuanto mayor sea la luz solar y la temperatura, mayor será la cantidad de ozono que se forme; por ello, las mayores concentraciones de este gas se dan en verano.


    Los posibles síntomas asociados a episodios de contaminación por ozono, entre otros, son:

    - Irritación ocular y de las vías respiratorias con tos, molestias de garganta, dolor torácico al respirar profundamente.
    - Mayor dificultad para respirar con normalidad, sobre todo al hacer ejercicio.
    - Mayor susceptibilidad a las infecciones respiratorias.
    - Ataques de asma y agravamiento de ésta y otras enfermedades  respiratorias, como el enfisema o la bronquitis crónica.






