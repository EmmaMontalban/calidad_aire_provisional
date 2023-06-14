def calcular_ICA(data):
    '''
    Función para calcular el índíce de calidad del aire (ICA)
    
    Para ello primero calcula el indice de calidad del aire para cata contaminante atmosférico
    - ICA_SO2 = (Concentración_SO2 / Valor_Límite_SO2) * 100, Valor límite = 125 μg/m3
    - ICA_NO2 = (Concentración_NO2 / Valor_Límite_NO2) * 100, Valor límite = 40 μg/m3
    - ICA_PM10 = (Concentración_PM10 / Valor_Límite_PM10) * 100, Valor límite = 50 μg/m3
    - ICA_O3 = (Concentración_O3 / Valor_Límite_O3) * 100, Valor límite = 120 μg/m3
    
    Luego promedia los valores de ICA de los cuatro contaminantes para obtener el índice de calidad del aire (ICA) general
    - ICA = (ICA_SO2 + ICA_NO2 + ICA_PM10 + ICA_O3) / 4)
    '''
    concentraciones = ['SO2', 'PM10', 'O3', 'NO2']
    valores_limites = [125, 50, 120, 40]  # Valores límite de los contaminantes
    
    ica_columnas = ['ICA_SO2', 'ICA_PM10', 'ICA_O3', 'ICA_NO2']
    
    for i, concentracion in enumerate(concentraciones):
        ica_contaminante = (data[concentracion] / valores_limites[i]) * 100
        data[ica_columnas[i]] = ica_contaminante.round(2)
    
    ica_promedio = data[ica_columnas].mean(axis=1)
    data['ICA'] = ica_promedio.round(2)
        
    return data

def calc_missing(df):
    '''
    Método que calcula el porcentaje de valores nulos en cada columna
    '''
    missing_columns =[col for col in df.columns if df[col].isnull().sum() > 0]
    
    # Esta es otra opcion
    # for col in df.columns:
    #     if df[col].isnull().sum() > 0:
    #         missing_columns.append(col)
    
    for col in missing_columns:
        null_count = df[col].isnull().sum()
        total_count = df.shape[0]
        null_percent = (null_count / total_count) * 100
        print(f'{col} {null_count} / {total_count}= {null_percent:.2f} %')