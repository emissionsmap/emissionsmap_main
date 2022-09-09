import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df_new = pd.read_csv('/home/alex/Escritorio/emissionsmap_main/src/geospatial/data/predicciones.csv')
dfbar = pd.read_csv('/home/alex/Escritorio/emissionsmap_main/src/geospatial/data/subenergy.csv')


def barPlot():
    list = []
    pais_df = dfbar[(dfbar['Codigo'].isna() != True) & (dfbar['Pais'] != 'World')]
    anio = pais_df[pais_df['Anio']== 2021]
    for Pais in anio['Pais'].unique():
        total = anio[anio['Pais']==Pais]['Renovables'].sum(axis=0)
        total_2 = anio[anio['Pais']==Pais]['Renovables']
        list.extend([[Pais, total]])

        
    # Creacion de dataframe
    paises_renovables = pd.DataFrame(list, columns=['Pais', 'Renovables']).sort_values(by='Renovables',ascending=False)

    # Plotting 10 Paises 2021
    fig = px.bar(paises_renovables.head(10), x='Pais', y='Renovables',color='Renovables', title='Top 10 Paises que utilizan Energia Renovables')
    
    return fig._repr_html_()


def linealPlot():

    fig= go.Figure(data=[
        go.Scatter(
        x=df_new['Anio'],
        y=df_new['Var_Prod_Ener'],
        mode='lines', 
        name='Participacion Produccion Energia (%)',
        line=dict(color='cyan')
        ),
        go.Scatter(
        x=df_new['Anio'],
        y=df_new['Var_Emicion_Co2'],
        mode='lines',
        name='Participacion Emision CO2 (%)'
        )
    
    ])
    fig.update_layout(
        height=300, width=1000,
        plot_bgcolor='black',
        paper_bgcolor= 'black',
        font_color='#cee3e1',
        legend=dict(
            x=0.05,
            y=1,
            title_font_family="Times New Roman",
            font=dict(
                family="Courier",
                size=12,
                color="LightSteelBlue"
            ),
            bgcolor="Black",
            bordercolor="LightSteelBlue",
            borderwidth=1
        ),
        xaxis=dict(showgrid=False,showline=True,linecolor='rgb(255,255,255)'),
        yaxis=dict(showgrid=False),
        margin=dict(l=10,r=10,b=10,t=10)
    )
    return fig._repr_html_()

def emisionco2():
    list = []
    df = pd.read_csv('/home/alex/Escritorio/emissionsmap_main/src/geospatial/data/energyco2.csv')
    for Pais in df['Pais'].unique():
        emisionco_2 = df.groupby('Pais').count()['Emision De Co2'].reset_index().sort_values(by='Emision De Co2',ascending=False)
        emisionco_2.style.background_gradient(cmap='winter')
        total = df[df['Pais']==Pais]['Emision De Co2'].sum(axis=0)
        total_2 = df[df['Pais']==Pais]['Emision De Co2']
        list.extend([[Pais, total]])
    # Creacion de dataframe
    df = pd.DataFrame(list, columns=['Pais', 'Emision De Co2']).sort_values(by='Emision De Co2',ascending=False)

    # Plotting 20 Paises 2021
    fig = px.bar(df.head(10), x='Pais', y='Emision De Co2', color='Emision De Co2', title='Top 10 Paises que utilizan Energia Emision De Co2')
    fig.update_layout( title='Top 10 Paises que utilizan Energia Emision De Co2',
                            title_x=0.15,
                            margin=dict(t=70, b=0, l=70, r=40),
                            hovermode="x unified",
                            xaxis_tickangle=360,
                            xaxis_title='Pais', yaxis_title="Emision De Co2",
                            plot_bgcolor='#2d3035', paper_bgcolor='#2d3035',
                            title_font=dict(size=25, color='#a5a7ab', family="Lato, sans-serif"),
                            font=dict(color='white'),
                            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
                            )
    return fig._repr_html_()
