import pandas as pd



def filter_by (df,column,value):
    ''''Recibe un df y devuelve un df filtrado segun los valores de la columna recibida'''
    filtered_df = df[df[f"{column}"] == f"{value}"]
    return filtered_df



def cambioBudget(str_column_value):
    '''Recibe los valores de las columnas que se refieren al dinero y quita el símbolo del dólar'''
    str_column_value.split("$")
    return int(str_column_value[2])

def exporto(nombre_df):
    nombre_df.to_csv(f"data/{nombre_df}.csv", index =False)