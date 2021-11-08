Este proyecto trata sobre en enriquecimiento de un dataset a través de los datos de una API.

Se han usado las siguientes librerías:

-Pandas: https://pandas.pydata.org/docs/
-Seaborn: https://seaborn.pydata.org/
-matplotlib: https://matplotlib.org/stable/contents.html

El dataset fue extraído de la página kaggle: https://www.kaggle.com/stefanoleone992/imdb-extensive-dataset

La API utilizada es la propia de IMDb: https://imdb-api.com/
Para utilizar esta API es necesario registrarse y pedir una key.

Una vez se tiene el dataset, se utiliza la API para sacar el póster de las películas. En este caso se usaro las películas de Los Vengadores (Marvel).
Una nueva columna refleja la información obtenida con la API.

Después se intenta hacer un estudio sobre si un gasto mayor conlleva también una mejor puntuación por parte de la crítica, pero teniendo solo 4 entradas no es fiable.

Para ello se utilizan las películas dirigidas por Cristopher Nolan.