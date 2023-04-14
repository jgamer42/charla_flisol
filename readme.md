# Introduccion al web scrapping

Este es un ejemplo de un proyecto de Web Scraping usando Scrapy, para ello estan las siguientes [Diapositivas de apoyo](https://tome.app/jaime-a37/raspa-la-web-con-python-y-scrappy-clgfy41nq076iak43p54vm9xt)

## Descripción

Este proyecto contiene un spider de Scrapy que extrae información de citas de la página [quotes to scrape](http://quotes.toscrape.com/). El spider recopila la cita, el autor y las etiquetas asociadas.

## Requisitos

Python 3.6 o superior
Scrapy
Ejecución
Para ejecutar el spider, desde la carpeta principal del proyecto, ejecuta el siguiente comando:

`scrapy crawl quotes`

Los resultados se imprimirán en la terminal. Si deseas guardar los resultados en un archivo CSV, puedes ejecutar el siguiente comando:

`scrapy crawl quotes -o quotes.csv`

Autor [Jaime Andres Valencia](https://www.linkedin.com/in/jgamer42/)
