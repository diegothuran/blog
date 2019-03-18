# coding: utf-8

import sys
sys.path.insert(0, '../../src')

' import pages by state '
from robo.pages.acre import agazetadoacre, jornalatribuna, jornalopiniao, jornalopiniao_economia, jornalopiniao_policia, jornalopiniao_politica, oaltoacre,\
oestadoacre, oriobranco_geral, oriobranco_policial, oriobranco_politica, pagina20, pagina20_economia, pagina20_policia, pagina20_politica

from robo.pages.alagoas import anoticia, cadaminuto, correiodopovo, gazetadealagoas, gazetaweb, novoextra, primeiraedicao, tribunahoje, tribunauniao

from robo.pages.amapa import aquiamapa, diariodoamapa

from robo.pages.amazonas import acritica_am, ojornaldailha, osolimoes

from robo.pages.bahia import aregiao, atarde, correiodooeste, folharegionalbahia, folhasertaneja, istoenoticia, jornalalerta, jornalanossavoz, jornalfolhadoestado,\
jornalimpacto, jornalnovafronteira, novoeste, oecojornal, rss_diariobahia, tribunafeirense

from robo.pages.ceara import anoticiadoceara, oestadoce, opovo, tribunadoceara

from robo.pages.distrito_federal import camara, correiobraziliense, folhacentrooeste, jornaldebrasilia, jornalregional, rss_estacaonews, rss_senado

from robo.pages.espirito_santo import aquinoticias, correiodoestadoonline, estadocapixaba, gazetaonline, jornalcorreiocapixaba, noticiaagora, \
rss_folhaonline, tribunaonline

from robo.pages.goias import diariodeaparecida, diariodoestadogo, jornalaguaslindas, jornalopcao, jornalestadodegoias, oanapolis, ohoje, opopular, \
rss_jornalopcao, tribunadoplanalto

from robo.pages.maranhao import atosefatos, oestadoma, oquartopoder

from robo.pages.mato_grosso import circuitomt, copopular, folhadoestado, gazetadigital

from robo.pages.mato_grosso_do_sul import acritica, atribunanews, correiodoestado, jd1noticias, midiamax

from robo.pages.minas_gerais import em, folhamg, hojeemdia

from robo.pages.paraiba import correiodaparaiba, jornaldaparaiba

from robo.pages.parana import bemparana, diarioinduscom, gazetadopovo, impactopr, jornaldoonibusdecuritiba, tribunapr

from robo.pages.pernambuco import correiodepernambuco, diariodepernambuco, folhape, jconline

from robo.pages.rio_de_janeiro import correiodobrasil, destakjornal, jb, monitordigital, odia, oglobo

from robo.pages.rio_grande_do_norte import agorarn, tribunadenoticias, tribunadonorte

from robo.pages.rio_grande_do_sul import correiodopovo, osul

from robo.pages.rondonia import correiodenoticia, diariodaamazonia

from robo.pages.roraima import folhabv, jornalroraimahoje

from robo.pages.santa_catarina import anoticia_clicrbs, ndonline, nsctotal_santa, nsctotal

from robo.pages.sao_paulo import brasildefato, dci, diariodenoticias, estadao, fsp, gazetasp, horadopovo, jornalestacao, meioemensagem, metronews, valor

from robo.pages.sergipe import cinform, jornaldesergipe, jornaldodiase

from robo.pages.tocantins import agora_to, conexaoto, jornaldotocantins, ogirassol, portalstylo

' import Gabriel pages '
from robo.pages.gabriel import abert, abi, administradores, adrenaline, agenciabrasil, ancine, apublica, avozeavezdajuventude, b9, balaiodokotscho, \
blastingnews, blogdafloresta, blogdoataide, blogdoluciosorge, blogdomaringoni, blogdomello, blogdomiro, blogdoneylopes, blogdopaulinho, \
blogdopaulonunes, blogdoprimo, blogdoriella, blogdorovai, blogdoskarlack, blogmarcosfrahm, brasildefato, buzzfeed_news_br, camara, \
carta_maior, cartamaior, ceticismopolitico, cinegnose, comunicadores, congressoemfoco, convergenciadigital, correiodobrasil, diariodocentrodomundo, \
diplomatique, domingoscosta, eb, ebc, elielbezerra, esporteemidia, estadao, extra_globo, fabiocampana, falandoverdades, folha_piaui, folha_sp, \
gospelprime, grandesnomesdapropaganda, huffpostbrasil, imprensaviva, istoe, jaderbarbalho, jornaisvirtuais, jornaldocomercio, jornallivre, jota, \
justificando, lulacerda, marcossilverio, migalhas, moneytimes, mundodomarketing, natelinha, nocaute, noticiasdatv, oab, observatoriodatelevisao, \
ocafezinho, ocombatente, operamundi, osamigosdopresidentelula, osdivergentes, otvfoco, outraspalavras, papelpop, polibiobraga, politicanarede, \
poncheverde, portaldapropaganda, ptnacamara, revistaforum, revistapress, rss_multiplos, rufandobombo, saibamais, sputniknews, telepadi, \
telesintese, tijolaco, torcedores, tribunadainternet, tribunadajustiça, valor, veja, vermelho, viomundo

' import general pages '
from robo.pages import agenciabrasil_ebc, bastidoresdopoder, bbc, cartacapital, correio24horas, diariocatarinense, diariodocentrodomundo, \
diariodocentrodomundo_mundo, diariodonordeste, dinheirorural, elpais, exame, gauchazh, gazetadopovo, globo_eleicoes, infomoney, istoedinheiro, jornalestadodeminas, \
jovempan, justificando_artigos, justificando, marceloauler, ne10, oantagonista, r7, rss_globo, terra_noticias, tnh1, tribunadosertao, veja_ultimas, uol

""" List of pages """
PAGES_UOL = [uol]

PAGES_RSS_GLOBO = [rss_globo]

PAGES_RSS_GLOBO_ELEICOES = [globo_eleicoes]

PAGES_RSS_MULTIPLOS = [rss_multiplos]

PAGES_GABRIEL = [abert, abi, administradores, adrenaline, agenciabrasil, ancine, apublica, avozeavezdajuventude, b9, balaiodokotscho, 
        blastingnews, blogdafloresta, blogdoataide, blogdoluciosorge, blogdomaringoni, blogdomello, blogdomiro, blogdoneylopes, blogdopaulinho, 
        blogdopaulonunes, blogdoprimo, blogdoriella, blogdorovai, blogdoskarlack, blogmarcosfrahm, brasildefato, buzzfeed_news_br, camara, 
        carta_maior, cartamaior, ceticismopolitico, cinegnose, comunicadores, congressoemfoco, convergenciadigital, correiodobrasil, diariodocentrodomundo, 
        diplomatique, domingoscosta, eb, ebc, elielbezerra, esporteemidia, estadao, extra_globo, fabiocampana, falandoverdades, folha_piaui, folha_sp, 
        gospelprime, grandesnomesdapropaganda, huffpostbrasil, imprensaviva, istoe, jaderbarbalho, jornaisvirtuais, jornaldocomercio, jornallivre, jota, 
        justificando, lulacerda, marcossilverio, migalhas, moneytimes, mundodomarketing, natelinha, nocaute, noticiasdatv, oab, observatoriodatelevisao, 
        ocafezinho, ocombatente, operamundi, osamigosdopresidentelula, osdivergentes, outraspalavras, papelpop, politicanarede, 
        poncheverde, portaldapropaganda, ptnacamara, revistaforum, revistapress, rufandobombo, saibamais, sputniknews, telepadi, 
        telesintese, tijolaco, torcedores, tribunadainternet, tribunadajustiça, valor, veja, vermelho, viomundo]

PAGES_DIVERSOS = [agenciabrasil_ebc, bastidoresdopoder, bbc, cartacapital, correio24horas, diariocatarinense, diariodocentrodomundo, diariodocentrodomundo_mundo, 
        diariodonordeste, dinheirorural, elpais, exame, gauchazh, gazetadopovo, infomoney, istoedinheiro, jornalestadodeminas, jovempan, 
        justificando_artigos, justificando, marceloauler, ne10, oantagonista, r7, terra_noticias, tnh1, tribunadosertao, veja_ultimas]

PAGES_ESTADOS_ATE_MARANHAO = [agazetadoacre, jornalatribuna, jornalopiniao, jornalopiniao_economia, jornalopiniao_policia, jornalopiniao_politica, oaltoacre,
        oestadoacre, oriobranco_geral, oriobranco_policial, oriobranco_politica, pagina20, pagina20_economia, pagina20_policia, pagina20_politica,
        anoticia, cadaminuto, correiodopovo, gazetadealagoas, gazetaweb, novoextra, primeiraedicao, tribunahoje, tribunauniao,
        aquiamapa, diariodoamapa, acritica_am, ojornaldailha, osolimoes, aregiao, atarde, correiodooeste, folharegionalbahia, folhasertaneja, 
        istoenoticia, jornalalerta, jornalanossavoz, jornalfolhadoestado, jornalimpacto, jornalnovafronteira, novoeste, oecojornal, rss_diariobahia, 
        tribunafeirense, anoticiadoceara, oestadoce, opovo, tribunadoceara, camara, #correiobraziliense, 
        folhacentrooeste, jornaldebrasilia, jornalregional, 
        rss_estacaonews, rss_senado, aquinoticias, correiodoestadoonline, estadocapixaba, gazetaonline, jornalcorreiocapixaba, noticiaagora, 
        rss_folhaonline, tribunaonline, diariodeaparecida, diariodoestadogo, jornalaguaslindas, jornalopcao, jornalestadodegoias, oanapolis, ohoje, 
        opopular, rss_jornalopcao, tribunadoplanalto, atosefatos, oestadoma, oquartopoder]

PAGES_OUTROS_ESTADOS = [circuitomt, copopular, folhadoestado, gazetadigital, acritica, atribunanews, correiodoestado, jd1noticias, midiamax,
        em, folhamg, hojeemdia, correiodaparaiba, jornaldaparaiba, bemparana, diarioinduscom, impactopr, jornaldoonibusdecuritiba, tribunapr,
        correiodepernambuco, diariodepernambuco, folhape, jconline, destakjornal, jb, monitordigital, odia, oglobo, 
        agorarn, tribunadenoticias, tribunadonorte, correiodopovo, osul, correiodenoticia, diariodaamazonia, folhabv, jornalroraimahoje,
        anoticia_clicrbs, ndonline, nsctotal_santa, nsctotal, brasildefato, dci, diariodenoticias, estadao, fsp, gazetasp, horadopovo, jornalestacao, 
        meioemensagem, metronews, valor, cinform, jornaldesergipe, jornaldodiase, agora_to, conexaoto, jornaldotocantins, ogirassol, portalstylo]


PAGES = [# page from the states
        agazetadoacre, jornalatribuna, jornalopiniao, jornalopiniao_economia, jornalopiniao_policia, jornalopiniao_politica, oaltoacre,
        oestadoacre, oriobranco_geral, oriobranco_policial, oriobranco_politica, pagina20, pagina20_economia, pagina20_policia, pagina20_politica,
        anoticia, cadaminuto, correiodopovo, gazetadealagoas, gazetaweb, novoextra, primeiraedicao, tribunahoje, tribunauniao,
        aquiamapa, diariodoamapa, acritica_am, ojornaldailha, osolimoes, aregiao, atarde, correiodooeste, folharegionalbahia, folhasertaneja, 
        istoenoticia, jornalalerta, jornalanossavoz, jornalfolhadoestado, jornalimpacto, jornalnovafronteira, novoeste, oecojornal, rss_diariobahia, 
        tribunafeirense, anoticiadoceara, oestadoce, opovo, tribunadoceara, camara, #correiobraziliense, 
        folhacentrooeste, jornaldebrasilia, jornalregional, 
        rss_estacaonews, rss_senado, aquinoticias, correiodoestadoonline, estadocapixaba, gazetaonline, jornalcorreiocapixaba, noticiaagora, 
        rss_folhaonline, tribunaonline, diariodeaparecida, diariodoestadogo, jornalaguaslindas, jornalopcao, jornalestadodegoias, oanapolis, ohoje, 
        opopular, rss_jornalopcao, tribunadoplanalto, atosefatos, oestadoma, oquartopoder, 
        # pages ate o maranhao
         circuitomt, copopular, folhadoestado, gazetadigital, acritica, atribunanews, correiodoestado, jd1noticias, midiamax,
         em, folhamg, hojeemdia, correiodaparaiba, jornaldaparaiba, bemparana, diarioinduscom, impactopr, jornaldoonibusdecuritiba, tribunapr,
         correiodepernambuco, diariodepernambuco, folhape, jconline, destakjornal, jb, monitordigital, odia, oglobo, 
         agorarn, tribunadenoticias, tribunadonorte, correiodopovo, osul, correiodenoticia, diariodaamazonia, folhabv, jornalroraimahoje,
         anoticia_clicrbs, ndonline, nsctotal_santa, nsctotal, brasildefato, dci, diariodenoticias, estadao, fsp, gazetasp, horadopovo, jornalestacao, 
         meioemensagem, metronews, valor, cinform, jornaldesergipe, jornaldodiase, agora_to, conexaoto, jornaldotocantins, ogirassol, portalstylo,
          
         #paginas diversas
         agenciabrasil_ebc, bastidoresdopoder, bbc, cartacapital, correio24horas, diariocatarinense, diariodocentrodomundo, diariodocentrodomundo_mundo, 
         diariodonordeste, dinheirorural, elpais, exame, gauchazh, gazetadopovo, globo_eleicoes, infomoney, istoedinheiro, jornalestadodeminas, jovempan, 
         justificando_artigos, justificando, marceloauler, ne10, oantagonista, r7, rss_globo, terra_noticias, tnh1, tribunadosertao, veja_ultimas, uol,
  
         # paginas gabriel
         abert, abi, administradores, adrenaline, agenciabrasil, ancine, apublica, avozeavezdajuventude, b9, balaiodokotscho, 
        blastingnews, blogdafloresta, blogdoataide, blogdoluciosorge, blogdomaringoni, blogdomello, blogdomiro, blogdoneylopes, blogdopaulinho, 
        blogdopaulonunes, blogdoprimo, blogdoriella, blogdorovai, blogdoskarlack, blogmarcosfrahm, brasildefato, buzzfeed_news_br, camara, 
        carta_maior, cartamaior, ceticismopolitico, cinegnose, comunicadores, congressoemfoco, convergenciadigital, correiodobrasil, diariodocentrodomundo, 
        diplomatique, domingoscosta, eb, ebc, elielbezerra, esporteemidia, estadao, extra_globo, fabiocampana, falandoverdades, folha_piaui, folha_sp, 
        gospelprime, grandesnomesdapropaganda, huffpostbrasil, imprensaviva, istoe, jaderbarbalho, jornaisvirtuais, jornaldocomercio, jornallivre, jota, 
        justificando, lulacerda, marcossilverio, migalhas, moneytimes, mundodomarketing, natelinha, nocaute, noticiasdatv, oab, observatoriodatelevisao, 
        ocafezinho, ocombatente, operamundi, osamigosdopresidentelula, osdivergentes, outraspalavras, papelpop, politicanarede, 
        poncheverde, portaldapropaganda, ptnacamara, revistaforum, revistapress, rufandobombo, saibamais, sputniknews, telepadi, 
        telesintese, tijolaco, torcedores, tribunadainternet, tribunadajustiça, valor, veja, vermelho, viomundo, rss_multiplos
]
