#!/usr/local/bin/python
# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, '../../src')
from Model.News import News
from Database import connection, relevancia_site_table
import datetime
from dateutil import parser
import postagem.Util as Util
from Model.Relevancia_Site import Relevancia_Site 
import numpy as np

from lexical_analyzer_package import pessoas_lexical
from pessoas_postagem import pessoas_post
import pandas as pd

# site = 'bbc'
# # estrutura tupla = (id, site, relevancia)
# # tupla = relevancia_site_table.select(site)
# 
# 
# dates = [datetime.date(2018, 11, 1), datetime.date(2018, 11, 2), datetime.date(2018, 11, 3), datetime.date(2018, 11, 4), 
#          datetime.date(2018, 11, 5), datetime.date(2018, 11, 6), datetime.date(2018, 11, 7), datetime.date(2018, 11, 8),
#          datetime.date(2018, 11, 9), datetime.date(2018, 11, 10), datetime.date(2018, 11, 11), datetime.date(2018, 11, 12), datetime.date(2018, 11, 13)]
# for date in dates:
#     relevancia_site_table.select_form_date(date)


chart = '<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.3/Chart.js"></script>\
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.3/Chart.min.js"></script>\
<canvas id="myChart" width="400" height="400"></canvas>\
<script>\
var ctx = document.getElementById("myChart").getContext("2d");\
var myChart = new Chart(ctx, {\
    type: "bar",\
    data: {\
        labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],\
        datasets: [{\
            label: "# of Votes",\
            data: [12, 19, 3, 5, 2, 3],\
            backgroundColor: [\
                "rgba(255, 99, 132, 0.2)",\
                "rgba(54, 162, 235, 0.2)",\
                "rgba(255, 206, 86, 0.2)",\
                "rgba(75, 192, 192, 0.2)",\
                "rgba(153, 102, 255, 0.2)",\
                "rgba(255, 159, 64, 0.2)"\
            ],\
            borderColor: [\
                "rgba(255,99,132,1)",\
                "rgba(54, 162, 235, 1)",\
                "rgba(255, 206, 86, 1)",\
                "rgba(75, 192, 192, 1)",\
                "rgba(153, 102, 255, 1)",\
                "rgba(255, 159, 64, 1)"\
            ],\
            borderWidth: 1\
        }]\
    },\
    options: {\
        scales: {\
            yAxes: [{\
                ticks: {\
                    beginAtZero:true\
                }\
            }]\
        }\
    }\
});\
</script>'


row = {'titulos': [], 'links': [], 'noticia': [], 'image': [], 'abstract': [], 'date': []}
row['titulos'].append('teste')
row['noticia'].append('teste' + chart)
row['links'].append('teste')
row['abstract'].append('teste' + chart)
row['date'].append(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
row['image'].append(0)
row = pd.DataFrame(row)
# news = News(row['abstract'], row['noticia'], row['date'], row['links'], row['titulos'], row['image'])
df, categories = pessoas_lexical.lexical_corpus_and_title(row)
pessoas_post.post_news(df)
