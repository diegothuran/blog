# coding: utf-8

import sys
sys.path.insert(0, '../../src')

' import pages by state '
from robo.pages.acre import pagina20_policia, jornalopiniao_politica, oestadoacre, pagina20_economia, agazetadoacre, \
    oaltoacre, oriobranco_politica, oriobranco_policial, pagina20, jornalatribuna, jornalopiniao_economia, \
    pagina20_politica, jornalopiniao_policia, oriobranco_geral, jornalopiniao

from robo.pages.alagoas import gazetaweb, primeiraedicao, gazetadealagoas, novoextra, tribunauniao, \
    tribunahoje, anoticia, cadaminuto

from robo.pages.amapa import aquiamapa, diariodoamapa

from robo.pages.amazonas import ojornaldailha, acritica_am, osolimoes

from robo.pages.bahia import jornalnovafronteira, rss_diariobahia, \
    atarde, correiodooeste, jornalimpacto, tribunafeirense, istoenoticia, novoeste, jornalanossavoz, jornalalerta, \
    folhasertaneja, aregiao, oecojornal
from robo.pages.bahia import folharegionalbahia, jornalfolhadoestado

from robo.pages.ceara import oestadoce, tribunadoceara, opovo, anoticiadoceara

from robo.pages.distrito_federal import folhacentrooeste, rss_senado, jornalregional, rss_estacaonews, jornaldebrasilia

from robo.pages.espirito_santo import gazetaonline, aquinoticias, tribunaonline, correiodoestadoonline, estadocapixaba, \
    noticiaagora, rss_folhaonline, jornalcorreiocapixaba

from robo.pages.goias import jornalopcao, jornalestadodegoias, oanapolis, opopular, jornalaguaslindas, ohoje, \
    diariodoestadogo, rss_jornalopcao, diariodeaparecida, tribunadoplanalto

from robo.pages.maranhao import atosefatos, oquartopoder, oestadoma

from robo.pages.mato_grosso import folhadoestado
from robo.pages.mato_grosso import gazetadigital, circuitomt, copopular

from robo.pages.mato_grosso_do_sul import atribunanews, acritica, jd1noticias, correiodoestado
from robo.pages.mato_grosso_do_sul import midiamax

from robo.pages.minas_gerais import hojeemdia, em, folhamg

from robo.pages.paraiba import jornaldaparaiba, correiodaparaiba

from robo.pages.parana import jornaldoonibusdecuritiba, impactopr, tribunapr, bemparana, diarioinduscom

from robo.pages.pernambuco import correiodepernambuco, jconline, folhape
from robo.pages.pernambuco import diariodepernambuco

from robo.pages.rio_de_janeiro import monitordigital, destakjornal, jb, odia, oglobo

from robo.pages.rio_grande_do_norte import tribunadonorte, tribunadenoticias, agorarn

from robo.pages.rio_grande_do_sul import correiodopovo, osul

from robo.pages.rondonia import correiodenoticia, diariodaamazonia

from robo.pages.roraima import folhabv, jornalroraimahoje

from robo.pages.santa_catarina import nsctotal_santa, anoticia_clicrbs, nsctotal, ndonline

from robo.pages.sao_paulo import fsp, diariodenoticias, jornalestacao, dci, meioemensagem, horadopovo, gazetasp, \
    metronews

from robo.pages.sergipe import jornaldodiase, jornaldesergipe, cinform

from robo.pages.tocantins import portalstylo, conexaoto, ogirassol, agora_to, jornaldotocantins

' import Gabriel pages '
from robo.pages.gabriel import osdivergentes, domingoscosta, telepadi, torcedores, vermelho, blogdopaulonunes, b9, \
    marcossilverio, grandesnomesdapropaganda, brasildefato, apublica, observatoriodatelevisao, gospelprime, \
    blastingnews, papelpop, valor, rss_multiplos, politicanarede, blogdopaulinho, ptnacamara, fabiocampana, viomundo, \
    nocaute, balaiodokotscho, blogdoataide, blogdoprimo, sputniknews, portaldapropaganda, convergenciadigital, \
    tribunadainternet, noticiasdatv, istoe, jornallivre, correiodobrasil, operamundi, migalhas, diplomatique, \
    blogdomiro, oab, folha_sp, abert, blogdoluciosorge, agenciabrasil, blogdoneylopes, buzzfeed_news_br, \
    jornaisvirtuais, revistaforum, outraspalavras, blogmarcosfrahm, poncheverde, veja, lulacerda, ocombatente, \
    ceticismopolitico, ancine, falandoverdades, camara, eb, cinegnose, estadao, jota, tribunadajustiça, huffpostbrasil, \
    imprensaviva, rufandobombo, saibamais, jaderbarbalho, avozeavezdajuventude, carta_maior, elielbezerra, blogdomello, \
    administradores, tijolaco, abi, osamigosdopresidentelula, telesintese, ebc, extra_globo, esporteemidia, \
    revistapress, adrenaline, moneytimes, blogdoskarlack, blogdorovai, jornaldocomercio, mundodomarketing, cartamaior, \
    folha_piaui, congressoemfoco, comunicadores, blogdafloresta, blogdoriella, natelinha, ocafezinho, blogdomaringoni

' import general pages '
from robo.pages import agenciabrasil_ebc, bastidoresdopoder, bbc, cartacapital, diariocatarinense, diariodocentrodomundo, \
    diariodonordeste, exame, gauchazh, globo_eleicoes, infomoney, istoedinheiro, jornalestadodeminas, \
jovempan, marceloauler, ne10, oantagonista, r7, veja_ultimas, uol
from robo.pages import correio24horas, gazetadopovo, dinheirorural, rss_globo, justificando_artigos, tnh1, elpais, \
    terra_noticias, justificando, diariodocentrodomundo_mundo, tribunadosertao

""" List of pages """
PAGES_UOL = [uol]

PAGES_RSS_GLOBO = [rss_globo]

PAGES_RSS_GLOBO_ELEICOES = [globo_eleicoes]

PAGES_RSS_MULTIPLOS = [rss_multiplos]

PAGES_GABRIEL = [abert, abi, administradores, adrenaline, agenciabrasil, ancine, apublica, avozeavezdajuventude, b9,
                 balaiodokotscho,
                 blastingnews, blogdafloresta, blogdoataide, blogdoluciosorge, blogdomaringoni, blogdomello, blogdomiro,
                 blogdoneylopes, blogdopaulinho,
                 blogdopaulonunes, blogdoprimo, blogdoriella, blogdorovai, blogdoskarlack, blogmarcosfrahm,
                 brasildefato, buzzfeed_news_br, camara,
                 carta_maior, cartamaior, ceticismopolitico, cinegnose, comunicadores, congressoemfoco,
                 convergenciadigital, correiodobrasil, diariodocentrodomundo,
                 diplomatique, domingoscosta, eb, ebc, elielbezerra, esporteemidia, estadao, extra_globo, fabiocampana,
                 falandoverdades, folha_piaui, folha_sp,
                 gospelprime, grandesnomesdapropaganda, huffpostbrasil, imprensaviva, istoe, jaderbarbalho,
                 jornaisvirtuais, jornaldocomercio, jornallivre, jota,
                 justificando, lulacerda, marcossilverio, migalhas, moneytimes, mundodomarketing, natelinha, nocaute,
                 noticiasdatv, oab, observatoriodatelevisao,
                 ocafezinho, ocombatente, operamundi, osamigosdopresidentelula, osdivergentes, outraspalavras, papelpop,
                 politicanarede,
                 poncheverde, portaldapropaganda, ptnacamara, revistaforum, revistapress, rufandobombo, saibamais,
                 sputniknews, telepadi,
                 telesintese, tijolaco, torcedores, tribunadainternet, tribunadajustiça, valor, veja, vermelho,
                 viomundo]

PAGES_DIVERSOS = [agenciabrasil_ebc, bastidoresdopoder, bbc, cartacapital, correio24horas, diariocatarinense,
                  diariodocentrodomundo, diariodocentrodomundo_mundo,
                  diariodonordeste, dinheirorural, elpais, exame, gauchazh, gazetadopovo, infomoney, istoedinheiro,
                  jornalestadodeminas, jovempan,
                  justificando_artigos, justificando, marceloauler, ne10, oantagonista, r7, terra_noticias, tnh1,
                  tribunadosertao, veja_ultimas]

PAGES_ESTADOS_ATE_MARANHAO = [agazetadoacre, jornalatribuna, jornalopiniao, jornalopiniao_economia,
                              jornalopiniao_policia, jornalopiniao_politica, oaltoacre,
                              oestadoacre, oriobranco_geral, oriobranco_policial, oriobranco_politica, pagina20,
                              pagina20_economia, pagina20_policia, pagina20_politica,
                              anoticia, cadaminuto, correiodopovo, gazetadealagoas, gazetaweb, novoextra,
                              primeiraedicao, tribunahoje, tribunauniao,
                              aquiamapa, diariodoamapa, acritica_am, ojornaldailha, osolimoes, aregiao, atarde,
                              correiodooeste, folharegionalbahia, folhasertaneja,
                              istoenoticia, jornalalerta, jornalanossavoz, jornalfolhadoestado, jornalimpacto,
                              jornalnovafronteira, novoeste, oecojornal, rss_diariobahia,
                              tribunafeirense, anoticiadoceara, oestadoce, opovo, tribunadoceara, camara,  #correiobraziliense,
                              folhacentrooeste, jornaldebrasilia, jornalregional,
                              rss_estacaonews, rss_senado, aquinoticias, correiodoestadoonline, estadocapixaba,
                              gazetaonline, jornalcorreiocapixaba, noticiaagora,
                              rss_folhaonline, tribunaonline, diariodeaparecida, diariodoestadogo, jornalaguaslindas,
                              jornalopcao, jornalestadodegoias, oanapolis, ohoje,
                              opopular, rss_jornalopcao, tribunadoplanalto, atosefatos, oestadoma, oquartopoder]

PAGES_OUTROS_ESTADOS = [circuitomt, copopular, folhadoestado, gazetadigital, acritica, atribunanews, correiodoestado,
                        jd1noticias, midiamax,
                        em, folhamg, hojeemdia, correiodaparaiba, jornaldaparaiba, bemparana, diarioinduscom, impactopr,
                        jornaldoonibusdecuritiba, tribunapr,
                        correiodepernambuco, diariodepernambuco, folhape, jconline, destakjornal, jb, monitordigital,
                        odia, oglobo,
                        agorarn, tribunadenoticias, tribunadonorte, correiodopovo, osul, correiodenoticia,
                        diariodaamazonia, folhabv, jornalroraimahoje,
                        anoticia_clicrbs, ndonline, nsctotal_santa, nsctotal, brasildefato, dci, diariodenoticias,
                        estadao, fsp, gazetasp, horadopovo, jornalestacao,
                        meioemensagem, metronews, valor, cinform, jornaldesergipe, jornaldodiase, agora_to, conexaoto,
                        jornaldotocantins, ogirassol, portalstylo]


PAGES = [# page from the states
    agazetadoacre, jornalatribuna, jornalopiniao, jornalopiniao_economia, jornalopiniao_policia, jornalopiniao_politica,
    oaltoacre,
    oestadoacre, oriobranco_geral, oriobranco_policial, oriobranco_politica, pagina20, pagina20_economia,
    pagina20_policia, pagina20_politica,
    anoticia, cadaminuto, correiodopovo, gazetadealagoas, gazetaweb, novoextra, primeiraedicao, tribunahoje,
    tribunauniao,
    aquiamapa, diariodoamapa, acritica_am, ojornaldailha, osolimoes, aregiao, atarde, correiodooeste,
    folharegionalbahia, folhasertaneja,
    istoenoticia, jornalalerta, jornalanossavoz, jornalfolhadoestado, jornalimpacto, jornalnovafronteira, novoeste,
    oecojornal, rss_diariobahia,
    tribunafeirense, anoticiadoceara, oestadoce, opovo, tribunadoceara, camara, #correiobraziliense,
    folhacentrooeste, jornaldebrasilia, jornalregional,
    rss_estacaonews, rss_senado, aquinoticias, correiodoestadoonline, estadocapixaba, gazetaonline,
    jornalcorreiocapixaba, noticiaagora,
    rss_folhaonline, tribunaonline, diariodeaparecida, diariodoestadogo, jornalaguaslindas, jornalopcao,
    jornalestadodegoias, oanapolis, ohoje,
    opopular, rss_jornalopcao, tribunadoplanalto, atosefatos, oestadoma, oquartopoder,
        # pages ate o maranhao
    circuitomt, copopular, folhadoestado, gazetadigital, acritica, atribunanews, correiodoestado, jd1noticias, midiamax,
    em, folhamg, hojeemdia, correiodaparaiba, jornaldaparaiba, bemparana, diarioinduscom, impactopr,
    jornaldoonibusdecuritiba, tribunapr,
    correiodepernambuco, diariodepernambuco, folhape, jconline, destakjornal, jb, monitordigital, odia, oglobo,
    agorarn, tribunadenoticias, tribunadonorte, correiodopovo, osul, correiodenoticia, diariodaamazonia, folhabv,
    jornalroraimahoje,
    anoticia_clicrbs, ndonline, nsctotal_santa, nsctotal, brasildefato, dci, diariodenoticias, estadao, fsp, gazetasp,
    horadopovo, jornalestacao,
    meioemensagem, metronews, valor, cinform, jornaldesergipe, jornaldodiase, agora_to, conexaoto, jornaldotocantins,
    ogirassol, portalstylo,
          
         #paginas diversas
    agenciabrasil_ebc, bastidoresdopoder, bbc, cartacapital, correio24horas, diariocatarinense, diariodocentrodomundo,
    diariodocentrodomundo_mundo,
    diariodonordeste, dinheirorural, elpais, exame, gauchazh, gazetadopovo, globo_eleicoes, infomoney, istoedinheiro,
    jornalestadodeminas, jovempan,
    justificando_artigos, justificando, marceloauler, ne10, oantagonista, r7, rss_globo, terra_noticias, tnh1,
    tribunadosertao, veja_ultimas, uol,
  
         # paginas gabriel
    abert, abi, administradores, adrenaline, agenciabrasil, ancine, apublica, avozeavezdajuventude, b9, balaiodokotscho,
    blastingnews, blogdafloresta, blogdoataide, blogdoluciosorge, blogdomaringoni, blogdomello, blogdomiro,
    blogdoneylopes, blogdopaulinho,
    blogdopaulonunes, blogdoprimo, blogdoriella, blogdorovai, blogdoskarlack, blogmarcosfrahm, brasildefato,
    buzzfeed_news_br, camara,
    carta_maior, cartamaior, ceticismopolitico, cinegnose, comunicadores, congressoemfoco, convergenciadigital,
    correiodobrasil, diariodocentrodomundo,
    diplomatique, domingoscosta, eb, ebc, elielbezerra, esporteemidia, estadao, extra_globo, fabiocampana,
    falandoverdades, folha_piaui, folha_sp,
    gospelprime, grandesnomesdapropaganda, huffpostbrasil, imprensaviva, istoe, jaderbarbalho, jornaisvirtuais,
    jornaldocomercio, jornallivre, jota,
    justificando, lulacerda, marcossilverio, migalhas, moneytimes, mundodomarketing, natelinha, nocaute, noticiasdatv,
    oab, observatoriodatelevisao,
    ocafezinho, ocombatente, operamundi, osamigosdopresidentelula, osdivergentes, outraspalavras, papelpop,
    politicanarede,
    poncheverde, portaldapropaganda, ptnacamara, revistaforum, revistapress, rufandobombo, saibamais, sputniknews,
    telepadi,
    telesintese, tijolaco, torcedores, tribunadainternet, tribunadajustiça, valor, veja, vermelho, viomundo,
    rss_multiplos
]
