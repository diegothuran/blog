# coding: utf-8

import sys
sys.path.insert(0, '../../src')

from pages.util import load_pages

from Model.Relevancia_Site import Relevancia_Site
from Database import relevancia_site_table

from sklearn.preprocessing import MinMaxScaler
import numpy as np
import math

def get_indice_relevancia():
    """
    indice_relevancia = (1 - MinMax(log(X)))
    """
    sites, log_base = [], []
    for page in load_pages.PAGES:
        sites.append(page.NAME)
        if(page.GLOBAL_RANK is not None):
            log_base.append(math.log(page.GLOBAL_RANK))
        else:
            log_base.append(None)
    
    scaled_indices = MinMaxScaler().fit_transform(np.array(log_base).reshape(-1, 1))
    indice_relevancia = 1 - scaled_indices
    indice_relevancia = [x * 10 for x in indice_relevancia[:, 0]]
#     for i in range(len(indice_relevancia)):
#         print(load_pages.PAGES[i])
#         print(load_pages.PAGES[i].NAME)
#         print(indice_relevancia[i])
    return zip(sites, indice_relevancia)


def save_update_indice_relevancia():
    tuplas_site_relevancia = get_indice_relevancia()
    print(tuplas_site_relevancia)
    for tupla in tuplas_site_relevancia:
        try:
            print(tupla)
            #estrutura tupla: (site, relevancia)
            site = tupla[0]
            relevancia = "{0:.2f}".format(tupla[1])
            relevancia_inicial = relevancia
            
            relevancia_site = Relevancia_Site([site], [relevancia], [relevancia_inicial])
            relevancia_site_in_db = relevancia_site_table.check(relevancia_site)
            if(relevancia_site_in_db):
                relevancia_site_table.update(relevancia_site)
                # nao usar o update_com_relevancia_inicial pois basta atualizar a relevancia atual
    #             relevancia_site_table.update_com_relevancia_inicial(relevancia_site)
            else:
                relevancia_site_table.save(relevancia_site)
        except:
            pass
        
''' to save/update the relevancias'''
save_update_indice_relevancia()