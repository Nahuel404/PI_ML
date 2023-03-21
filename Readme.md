<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>


***¡Bienvenidos a la resolución del proyecto individual #1 de la carrera de data de henty!***
Mi nombre es Nahuel Marin y en los siguientes parrafos estaré explicando todo lo referido al trabajo hecho.



## **Introducción**
<hr>
Nos dieron como tarea encarnarnos en un data scientist que tenía como responsabilidad todos los pasos de la cración de una API y un modelo de recomendación de películas. Estos pasos incluían desde hacer un ETL hasta la codificación de la API y creación del modelo de recomendación.

## **Desarrollo**
<hr>
<h3>ETL</h3>
Comencé con el proceso de ETL importando el csv en un DataFrame de pandas, posteriormente cumpliendo las consignas especificadas en el Readme de la actividad(Todos los pasos serán ampliados en el video de youtube), las cuales eran generar un id a partir de la inicial de cada plataforma según corresponda y la columna "show_id", la cual cumplí con un bucle for. 
El siguiente paso especificado en la actividad fué reemplazar los nulos de la columna rating por la letra 'G', se cumplió usando la función '.fillna()' de pandas, para la tercera actividad había que cambiar el formato de las fechas a AAAA-mm-dd, primero había que transformar la columna que estaba en formato 'object' a formato fecha con '.to_datetime()', cambié todos los campos de textos a minúsculas y dividí la columna 'duration' en 'duration_type' y 'duration_int'.
Luego hice más transformaciones según creía necesario.

<h3>Desarrollo de la API</h3>

Para el desarrollo de la API utilicé el framework sugerido, FastApi, también implementé una función de lectura de html para el 'home' de la API, el resto es solo código de python, concretamente de la librería 'pandas'. Por último la ejecución en Local a través de 'uvicorn' y el deploy usando 'render'.

<h3>EDA(Análisis Exploratorio de Datos)</h3>

Para hacer el EDA utilicé además de pandas las librerias de saborn y missingno, busqué correlaciones y por último hice un dataframe con los valores que eran mas probable que usara para el modelo de recomendación.

<h3>Modelo de Recomendación</h3>

El desarrollo del modelo de recomendación fué complicado porque no me decidía si hacer un Árbol de Desiciones o un modelo basado en SVD. Tras investigar un poco vi que la mayoría de modelos de recomendación de contenido estaban basados o eran modelos SVD entonces me decanté por ese mismo.
Descargué un instalador de "VSstudio" el cuál me permitía instalar un entorno de desarrollo en c++ que me permitía de alguna forma instalar la librería "surprise" en el Notebook, esta librería cuenta con un modelo SVD así como con todas las herramientas para realizar el entrenamiento del modelo.

<p><a href=""> Video Explicativo</a></p>
<p><a href="https://www.linkedin.com/in/nahuel-marin-162219206"> Linkedin</a></p>