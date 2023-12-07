import dash
import pandas as pd
import plotly.express as px  
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from dash import html, dcc, callback, Input, Output

PM2_5 = pd.read_csv("PM2_5.csv")

dash.register_page(__name__)

map_figure = px.scatter_mapbox(PM2_5,
                          lat="latitud" ,
                          lon="longitud",
                          hover_name="valororig",
                          color="valororig",
                          size_max=50,
                          
                          opacity=0.5,
                          animation_frame='fecha',
                          mapbox_style='carto-positron')

fig1= px.histogram(PM2_5, x='city', y='valororig',histfunc='avg')
fig2= px.histogram(PM2_5[PM2_5['city']=='Monclova'], x='fecha', y='valororig',histfunc='avg',color_discrete_sequence=['indianred'],title='PM2.5 en Monclova')
fig2.update_layout(bargap=0.2)
fig3= px.histogram(PM2_5[PM2_5['city']=='Oaxaca'], x='fecha', y='valororig',histfunc='avg',color_discrete_sequence=['indianred'],title='PM2.5 en Oaxaca')
fig3.update_layout(bargap=0.2)
fig4= px.histogram(PM2_5[PM2_5['city']=='Valle de México'], x='fecha', y='valororig',histfunc='avg',color_discrete_sequence=['indianred'],title='PM2.5 en el Valle de Mexico',)
fig4.update_layout(bargap=0.2)
fig5= px.histogram(PM2_5[PM2_5['city']=='Toluca'], x='fecha', histfunc='avg', y='valororig',color_discrete_sequence=['Purple'],title='PM2.5 en Toluca')
fig5.update_layout(bargap=0.2)
fig6= px.histogram(PM2_5[PM2_5['city']=='Monterrey'], x='fecha', histfunc='avg', y='valororig',color_discrete_sequence=['Purple'],title='PM2.5 en Monterrey')
fig6.update_layout(bargap=0.2)

layout = html.Div([
    html.H1("Análisis", className="Titulo"),
    html.Div([
        dcc.Graph(figure=map_figure)
    ], className="Mapa"),
    html.Div([
            html.H2("General"),
            html.P("Mapa interactivo de los estados de la república afectados por el PM2.5 con una evolución marcada por día, desde enero de 2018 hasta enero de 2019. La intensidad del color en los puntos representa el valor del PM2.5 en tal día, como se puede observar en la escala, mientras más amarillo sea el color, mayor será el valor del contaminante PM2.5, y mientras más azul, menor será este valor."),
            html.P("Se puede observar cómo en los primeros meses del año varios estados llegan al color amarillo, y en la época veraniega y otoñal se ve que estos valores incluso bajan tanto que la escala tiene que actualizar sus parámetros.")
    ], className="map-analisis"),
    html.Div([
        dcc.Graph(figure=fig1),
        html.P("El promedio de la mayoría de las ciudades están por debajo de 50, menos 4 ciudades que tienen valores muy elevados, en especial lo notamos en Monclova, que tiene su promedio muy atípico, cercano a 250. "),
        html.Img(src="/assets/GH.png", className="hid")
    ], className="G1", id="G1",n_clicks=0),
    html.Div([
        dcc.Graph(figure=fig2),
        html.P("Notamos que en ambas ciudades el valor no pasa de 1000, esto puede ser debido a que es el límite del instrumento de medición. ")
    ], className="G2", id="G2",n_clicks=0),
    html.Div([
        dcc.Graph(figure=fig3),
        html.P("Notamos que en ambas ciudades el valor no pasa de 1000, esto puede ser debido a que es el límite del instrumento de medición. ")
    ], className="G3", id="G3",n_clicks=0),
    html.Div([
        dcc.Graph(figure=fig4),
        html.Div([            
            html.P("Dentro del Valle de México se observa que la época en donde más se liberan combustibles es en enero del 2018, de aquí ha ido en subidas y bajadas pero finalmente para inicios del 2019, los niveles de estas partículas aumentan de nuevo. Notamos los valores más bajos entorno a los meses veraniegos y otoñales."),
            html.P("https://oehha.ca.gov/calenviroscreen/indicator/pm25")
        ])
    ], className="G4", id="G4",n_clicks=0),
    html.Div([
        dcc.Graph(figure=fig5),
        html.P("Podemos ver que Toluca al igual que el Valle de México tiene sus valores máximos de particulas PM2.5 en los meses de enero de cada año, y de igual manera aqui notamos que en meses de verano y otoño estos valores bajan.")
    ], className="G5", id="G5",n_clicks=0),
    html.Div([
        dcc.Graph(figure=fig6),
        html.P("Notamos que los valores de Monterrey son menores, sus valores máximos no pasan de 40. De igual manera, notamos cómo sus valores máximos en los meses de invierno, en este caso a finales de 2018 e inicios de 2019. De igual manera, vemos que hay 3 valores negativos, que ignoraremos pues consideramos que es un error o de la transcripción de datos o error del instrumento de medición."),
    ], className="G6", id="G6",n_clicks=0),
    html.Div([
        html.Img(src="/assets/G7.png"),
        html.P("Notamos un comportamiento sumamente parecido, con sus altas y bajas en los mismos meses del año.")
    ], className="G7", id="G7", n_clicks=0),
    html.Div([
        html.Img(src="/assets/G8.png"),
        html.P("Si observamos bien esta gráfica, nos dice que el PM2.5 ha tenido mayores picos en Toluca. Podemos notar una tendencia muy similar en las 3 ciudadades, como ya lo habíamos discutido, con valores muy altos a incicios de ambos años y que van decreciendo durante el año.")
    ], className="G8", id="G8", n_clicks=0),
    html.Div([
        html.H4("Comparación de PM2.5 entre Valle de México, Toluca y Monterrey. En la gráfica de la izquierda se aprecia el análisis entre Valle de México vs Toluca. En la gráfica de la derecha el análisis entre las 3 ciudades."),
        html.H4("Datos desde 2018 hasta inicios de 2019.")
    ], className="h4t l"),
    html.Div([
        html.H4("Gráfico de frecuencia y periodograma del comportamiento del PM2.5 en la República Mexicana."),
        html.H4("Los datos se analizaron por hora.")
    ], className="h4t"),
    html.Div([
            html.Img(src="/assets/G9.png"),
            html.P("En esta gráfica se puede ver que hay una frecuencia muy clara, es decir, que estos datos se repiten cada cierto tiempo. Para saber cuál es este periodo de tiempo se hacen unos cálculos, y los resultados se pueden ver en el periodograma")
    ], className="G9", id="G9", n_clicks=0),
    html.Div([
            html.Img(src="/assets/G10.png"),
            html.P("Podemos ver que en promedio la frecuencia es de 22. Como los datos están medidos por hora, esto significa que el periodo de las partículas PM2.5 es aproximadamente cada 22 horas, lo que se podría ver como cada hora pico en las ciudades, donde hay más autos circulando y más actividad industrial lo que genera que se eleven los contaminantes.")
    ], className="G10", id="G10", n_clicks=0),
    html.Div([
        html.H2("Prueba de Hipótesis"),
        html.P("Intervalo de confianza Valle de México:"),
        html.P("(23.20, 23.39)"),
        html.Br(),
        html.P("Intervalo de confianza Toluca:"),
        html.P("(32.68, 33.09)"),
        html.Br(),
        html.P("Intervalo de confianza Monterrey:"),
        html.P("(16.89, 19.26)"),
        html.Br(),
        html.P("Ninguno de los 3 intervalos se parecen, Parece que el promedio de Toluca es el más alto y el de Monterrey el más bajo. Se evalúa el intervalo de confianza para la diferencia de las medias de las 3 ciudades."),
        html.Br(),
        html.P("Medias comparadas entre Toluca y Valle de México:"),
        html.P("(9.37, 9.81)"),
        html.Br(),
        html.P("Medias comparadas entre Toluca y Monterrey:"),
        html.P("(13.60, 16.01)"),
        html.Br(),
        html.P("Medias comparadas entre Monterrey y Valle de México:"),
        html.P("(4.03, 6.41)"),
        html.Br(),
        html.P("Ningún intervalo de comparación contiene al 0, por lo que el promedio de Toluca es significativamente más alto y el de Monterrey significativamente más bajo y ninguna de las 3 ciudades se relacionan."),
        html.Br(),
        html.P("Para probar esta hipótesis, se hace una prueba de hipótesis para diferencia de medias. La prueba es de 2 colas con una significancia de 0.05."),
        html.Br(),
        html.P("Medias comparadas entre Toluca y Valle de México:"),
        html.P("p value= 0.0"),
        html.Br(),
        html.P("Medias comparadas entre Toluca y Monterrey:"),
        html.P("p value= 2.5409574557173115e-127"),
        html.Br(),
        html.P("Medias comparadas entre Monterrey y Valle de México:"),
        html.P("p value= 8.961219438207213e-18"),
        html.Br(),
        html.P("Al ser esta una prueba manual entre cada par de ciudades, se hará uso del análisis ANOVA para comprobar si efectivamente el valor P es 0."),
        html.Br(),
        html.P("p value=0.0"),
        html.Br(),
        html.P("Y por último, también haremos la prueba Tukey que minimiza los errores en estas pruebas."),
        html.Br(),
        html.P("Multiple Comparison of Means - Tukey HSD, FWER=0.05"),
        html.P("==================================================="),
        html.P("group1 group2 meandiff p-adj  lower   upper  reject"),
        html.P("---------------------------------------------------"),
        html.P("mex    mtr  -5.2179  -0.0 -5.9555 -4.4804   True"),
        html.P("mex    tol    9.591  -0.0   8.898 10.2839   True"),
        html.P("mtr    tol  14.8089  -0.0 13.9349 15.6829   True"),
        html.P("---------------------------------------------------"),
        html.Br(),
        html.P("Podemos observar que en las 3 pruebas los 3 valores P son 0, esto nos dice que se rechaza la hipótesis nula y sí existe una relación entre estas 3 ciudades. Lo cual era lo esperado, pues sobre todo ciudades como Monterrey y el Valle de México tienen un estilo de vida muy similar, y Toluca y el Valle de México son ciudades que están juntas, por lo que es lógico pensar que existe una relación. Ahora que sabemos esto, es lógico que el promedio del Valle de México esté entre las otras 2 ciudades."),
    ],className="Hipo", id="Hipo", n_clicks=0),
    html.Div([
        html.H2("Bibliográfia"),
        html.Ul([
            html.Li("Datos Abiertos de México - datos.gob.mx. (2022). Datos.gob.mx. https://datos.gob.mx/blog/ventilando-datos-abiertos-sobre-calidad-del-aire?category=aprende&tag=educacion"),
            html.Li("Gobierno de México. (2021). Partículas suspendidas PM10 y PM2.5 dañan la salud y el medio ambiente. Recuperado de https://www.gob.mx/semarnat/articulos/particulas-suspendidas-pm10-y-pm2-5-danan-salud-y-medio-ambiente"),
            html.Li("¿Qué es el Cambio Climático y cómo nos afecta? | ACCIONA. (2020). Acciona.com. https://www.acciona.com/es/cambio-climatico/"),
            html.Li("OEHHA. (2022). ¿Qué es PM2.5?. Recuperado de https://oehha.ca.gov/calenviroscreen/indicator/pm25"),
        ])
    ], className="bibliografia"),
], className="contenedor contenedor_dash")

@callback(
    Output('G1', 'className'),  
    Input('G1', 'n_clicks'),
)
def update_output(n_clicks):
    if n_clicks%2!=0:
        return 'on_g'
    else:
        return 'off'
@callback(
    Output('G2', 'className'),
    Input('G2', 'n_clicks'),
)
def update_output(n_clicks):
    if n_clicks%2!=0:
        return 'on_g'
    else:
        return 'off'
@callback(
    Output('G3', 'className'),
    Input('G3', 'n_clicks'),
)
def update_output(n_clicks):
    if n_clicks%2!=0:
        return 'on_g'
    else:
        return 'off'
@callback(
    Output('G4', 'className'),
    Input('G4', 'n_clicks'),
)
def update_ouxtput(n_clicks):
    if n_clicks%2!=0:
        return 'on_g1'
    else:
        return 'off'
@callback(
    Output('G5', 'className'),
    Input('G5', 'n_clicks'),
)
def update_output(n_clicks):
    if n_clicks%2!=0:
        return 'on_g1'
    else:
        return 'off'
@callback(
    Output('G6', 'className'),
    Input('G6', 'n_clicks'),
)
def update_output(n_clicks):
    if n_clicks%2!=0:
        return 'on_g1'
    else:
        return 'off'
@callback(
    Output('G7', 'className'),
    Input('G7', 'n_clicks'),
)
def update_output(n_clicks):
    if n_clicks%2!=0:
        return 'G7 on_g2'
    else:
        return 'G7 off'
@callback(
    Output('G8', 'className'),
    Input('G8', 'n_clicks'),
)
def update_output(n_clicks):
    if n_clicks%2!=0:
        return 'G8 on_g2'
    else:
        return 'G8 off'
@callback(
    Output('G9', 'className'),
    Input('G9', 'n_clicks'),
)
def update_output(n_clicks):
    if n_clicks%2!=0:
        return 'G9 on_g3'
    else:
        return 'G9 off'
@callback(
    Output('G10', 'className'),
    Input('G10', 'n_clicks'),
)
def update_output(n_clicks):
    if n_clicks%2!=0:
        return 'G10 on_g3'
    else:
        return 'G10 off'
@callback(
    Output('Hipo', 'className'),
    Input('Hipo', 'n_clicks'),
)
def update_output(n_clicks):
    if n_clicks%2!=0:
        return 'Hipo onH'
    else:
        return 'Hipo off'