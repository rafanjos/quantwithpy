# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

from fundamentalista.fundamentalista import findata
import matplotlib.pyplot as plt
import seaborn as sns

tick = 'PETR4'

fca = findata.fca(tick)
bpa = findata.bpa(tick)
bpp = findata.bpp(tick)
dre = findata.dre(tick)
dva = findata.dva(tick)


### MÚLTIPLOS DE MERCADO ###
roa_2019 = fca['2019'][2] / bpa['2019'][0] * 100

liquidez_corr_2019 = bpa['2019'][1] / bpp['2019'][1] * 100

margem_bruta_2019 = dre['2019'][2] / dre['2019'][0] * 100

lucro = [fca['2019'][2], fca['2018'][2]]
labels = ['2019', '2018']

plt.barh(labels, lucro)
plt.title('Lucro Líquido PETR4')
