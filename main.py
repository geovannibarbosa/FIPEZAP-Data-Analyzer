import data_loader as dl
import calculate_metrics as cm

valores = cm.calcular_valores(dl.df)
analise = valores.analise_estatistica()
outlier = valores.identificar_outliers(analise[3], analise[4])
valores.plotar_distribuicao_normal()
valores.plotar_boxplot()
valores.plotar_curva_indice_tempo()
print (analise)
