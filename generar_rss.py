# -*- coding: utf-8 -*-

from feedgen.feed import FeedGenerator
import pandas as pd
fg = FeedGenerator()
fg.id(1)
fg.title("1938.com.es")
fg.author(
    {"name": "1938.com.es", "email": "1938web@gmail.com"}
)
fg.logo("https://1938.com.es/assets/imagenes/logo.png")
fg.link(href="https://1938.com.es/", rel="self")
fg.language("es")
fg.description("Videos sobre la información de interes sobre el diseño de aplicaciones moviles, ciencia de datos (BigData) y tecnologías de la información")
df = pd.read_csv('rss.csv', sep=';' ,header=0)

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
