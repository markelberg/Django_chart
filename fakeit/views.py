import pandas as pd
import base64
import matplotlib.pyplot as plt
from io import BytesIO
from django.views import generic
from django.shortcuts import render

class IndexView(generic.ListView):
    template_name = "graphic.html"
    context_object_name = "graph"

    def get_queryset(self):
        df = pd.read_csv('csv/elecciones_autonomicas_madrid_2023.csv')

        # Limpiamos los datos y convertir la columna de votos a números
        df = df[df['VOTOS_2023'] != '-']
        df['VOTOS_2023'] = df['VOTOS_2023'].str.replace('.', '', regex=False)
        df['VOTOS_2023'] = pd.to_numeric(df['VOTOS_2023'])

        df_filtrado = df[df['VOTOS_2023'] > 20000]

        fig, ax = plt.subplots()
        wedges, _ = ax.pie(df_filtrado['VOTOS_2023'], labels=df_filtrado['PARTIDO'])

        legend = [f"{label}: {votes} votos" for label, votes in zip(df['PARTIDO'], df['VOTOS_2023'])]
        ax.legend(wedges, legend, loc="center right", fontsize='large', bbox_to_anchor=(1, 0, 0.5, 1))

        plt.tight_layout()

        # Convertimos el gráfico a una imagen en formato PNG
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        # Codificamos la imagen en base64 para mostrarla en la plantilla HTML
        graphic = base64.b64encode(image_png).decode('utf-8')
        return graphic