import dash
import pandas as pd
import plotly.express as px  
import plotly.graph_objects as go
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from dash import html, dcc, callback, Input, Output

PM2_5 = pd.read_csv("PM2_5.csv")

dash.register_page(__name__, path='/')

def personas(nombre, matricula, carrera, imagen, id_p):
    return html.Div([
        html.Img(src=f"/assets/{imagen}.jpeg",width="120px"),
        html.Div([
            html.P([
                html.Span("Nombre: "),
                f"{nombre}"
            ]),
            html.P([
                html.Span("Matricula: "),
                f"{matricula}"
            ]),
            html.P([
                html.Span("Carrera: "),
                f"{carrera}"
            ]),
    ], className="info")],id=f"{id_p}",n_clicks=0)

def divs_texto(seccion, texto):
    return html.Div([
            html.H2(f"{seccion.capitalize()}"),
            html.P(f"{texto}")
        ], className=f"{seccion}")
    

def clase():
    return html.Div([
        html.Img(src="/assets/stadistic.png", width="100px"),
        html.Div([
            html.P([
                html.Span("Materia: "),
                "Modelación estadística para la toma de decisiones"
            ]),
            html.P([
                html.Span("Grupo: "),
                "201"
            ]),
            html.P([
                html.Span("Profesores: "),
                "Elisabetta Crescio, Jorge Becerril"
            ])
        ], className="info_materia")
    ], className="materia")

px.set_mapbox_access_token("pk.eyJ1Ijoib2xpdmVyLWEwMTAyNjQ4OCIsImEiOiJjbDhtaWd5NTIwczdqM3h0b2h4bXR0Z2pzIn0.2NW5sn-yQx9KfGgmADDeIA")

fig = px.scatter_mapbox(PM2_5,
                          lat="latitud" ,
                          lon="longitud",
                          hover_name="valororig",
                          color="valororig",
                          size_max=50,
                          
                          opacity=0.5,
                          animation_frame='fecha',
                          mapbox_style='carto-positron')

layout = html.Div([
    html.Div([
        html.Div([
            html.Div([html.Img(src="/assets/tec.svg", width="100px")],className="tec"),
            html.Div([html.H1("Reto: Calidad del Aire")],className="titulo"),
            clase()
        ],className="col1"),
        html.Div([
            personas("Carlos Alfonso Alberto Salazar", "A01026175", "IDM", "C", "p1"),
            personas("Oliver Burguete López", "A01026488", "IDM", "O", "p2"),
            personas("Arnulfo Romero Souza", "A01783149", "IDM", "A", "p3"),
            personas("Daniel Alejandro Martinez Cienfuegos", "A01745412", "IDM", "D", "p4")
        ],className="nosotros")
    ], className = "header"),

    html.Div([
        divs_texto("introduccion", "La contaminación atmosférica por partículas contaminantes es una de las contaminaciones más dañinas para la humanidad, y lamentablemente cada día nosotros somos los responsables de elevar estos contaminantes y dañarnos a nosotros mismos."),
        divs_texto("Problematica", "Las partículas PM2.5 tienen un efecto mayor en la salud humana sobre todo por su composición, que puede ser más tóxica y se caracteriza principalmente por la presencia de sulfatos, nitratos, ácidos, metales y carbono negro. Estas partículas, son un indicador representativo común de la contaminación del aire y afectan a más personas que cualquier otro contaminante."),
        dcc.Link(
            html.Div([
                html.H2("Resultados"),
                html.P("Mapa interactivo de los estados de la república afectados por el PM2.5 con una evolución marcada por día, desde enero de 2018 hasta enero de 2019. La intensidad del color en los puntos representa el valor del PM2.5 en tal día, como se puede observar en la escala, mientras más amarillo sea el color, mayor será el valor del contaminante PM2.5, y mientras más azul, menor será este valor.")
            ], className="resultados"),href="/dash"),
        divs_texto("conclusiones", "A través del análisis de datos, pudimos entender y observar el comportamiento de las partículas PM2.5 en los diferentes estados de México. Encontramos patrones de comportamiento durante un año, donde se pudo observar que los niveles de este contaminante eran altos durante invierno y bajaban durante verano. Además de que encontramos relaciones entre ciudades con un mismo estilo de vida o que fueran ciudades cercanas.")
    ], className="contenedor2"),
    html.Div([
        html.H2("Mapa"),
        dcc.Graph(figure=fig),
    ]),
    html.Div([
        html.H2("Bibliográfia"),
        html.Ul([
            html.Li("Datos Abiertos de México - datos.gob.mx. (2022). Datos.gob.mx. https://datos.gob.mx/blog/ventilando-datos-abiertos-sobre-calidad-del-aire?category=aprende&tag=educacion"),
            html.Li("Gobierno de México. (2021). Partículas suspendidas PM10 y PM2.5 dañan la salud y el medio ambiente. Recuperado de https://www.gob.mx/semarnat/articulos/particulas-suspendidas-pm10-y-pm2-5-danan-salud-y-medio-ambiente"),
            html.Li("¿Qué es el Cambio Climático y cómo nos afecta? | ACCIONA. (2020). Acciona.com. https://www.acciona.com/es/cambio-climatico/"),
            html.Li("OEHHA. (2022). ¿Qué es PM2.5?. Recuperado de https://oehha.ca.gov/calenviroscreen/indicator/pm25"),
        ])
    ], className="bibliografia"),
], className="contenedor")

@callback(
    Output('p1', 'className'),  
    Input('p1', 'n_clicks'),
)
def update_output(n_clicks):
    if n_clicks%2!=0:
        return 'on'
    else:
        return 'off'
@callback(
    Output('p2', 'className'),
    Input('p2', 'n_clicks'),
)
def update_output(n_clicks):
    if n_clicks%2!=0:
        return 'on'
    else:
        return 'off'
@callback(
    Output('p3', 'className'),
    Input('p3', 'n_clicks'),
)
def update_output(n_clicks):
    if n_clicks%2!=0:
        return 'on'
    else:
        return 'off'
@callback(
    Output('p4', 'className'),
    Input('p4', 'n_clicks'),
)
def update_output(n_clicks):
    if n_clicks%2!=0:
        return 'on'
    else:
        return 'off'

