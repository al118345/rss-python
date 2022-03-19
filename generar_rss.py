# -*- coding: utf-8 -*-

from feedgen.feed import FeedGenerator
import pandas as pd
#parametros a rellenar
nombre_autor = "1938.com.es"
email=  "1938web@gmail.com"
titulo=  "Web 1938.com.es"
logo= "https://1938.com.es/assets/imagenes/logo.png " #opcional
url = "https://1938.com.es/";
descripcion ="Videos sobre la información de interes sobre el diseño de aplicaciones moviles, ciencia de datos (BigData) y tecnologías de la información"

fg = FeedGenerator()
fg.id(1)
fg.title(titulo)
fg.author(
    {"name": nombre_autor, "email": email}
)
fg.logo(logo)
fg.link(href=url, rel="self")
fg.language("es")
fg.description(descripcion)

nombre_fichero ="rss.csv"
df = pd.read_csv(nombre_fichero, sep=';' ,header=0)
for index, row in df.iterrows():
    fe = fg.add_entry(order="append")
    fe.id(row['url'])
    fe.title(row['titulo'])
    fe.content(row['tematica'])
    fe.author(
        {"name": "Rubén Pérez ", "email": "1938web@gmail.com"}
    )
    fe.link({"href":  row['url'], "title": row['titulo']})

rssfeed = fg.rss_str(pretty=True)
fg.rss_file("rss_video.xml")
