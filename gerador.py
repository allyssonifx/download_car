import geopandas as gpd
import pandas as pd
import os

# caminho = 'DATA\MG'
# pastas = os.listdir(caminho)
# caminho = caminho+'/'
# df = pd.DataFrame()

# shapes = []

# for p in pastas:
#     arquivos = os.listdir(caminho+p)
#     for a in arquivos:
#         if '.shp' in a and a not in shapes:
#             shapes.append(a)
# print('fim')
# dfs = []
# for s in shapes:
#     print(s)
#     count = 1
#     regulador = True
#     for p in pastas:
#         print(p+'>>>'+str(count))
#         arquivos = os.listdir(caminho+p)
#         if s in arquivos:
#             gdf = gpd.read_file(caminho+p+'/'+s)
#             gdf.crs='epsg:4674'
#             df = pd.concat([df,gdf])
#         if count >= (len(pastas)/2) and regulador:
#             gd = gpd.GeoDataFrame(df,geometry='geometry',crs='epsg:4674')
#             gd.to_file(caminho+s.replace(".shp","_1.gpkg"),layer='m',driver='GPKG')
#             df = pd.DataFrame()
#             regulador = False
#         count += 1
#     print('\n')
#     gd = gpd.GeoDataFrame(df,geometry='geometry',crs='epsg:4674')
#     gd.to_file(caminho+s.replace(".shp","_2.gpkg"),layer='m',driver='GPKG')
#     df = pd.DataFrame()


shs = os.listdir('DATA/MG')
shs2 = []
for s in shs:
    if '.gpkg' in s:
        shs2.append(s)

for c in range(0,len(shs2),2):
    print(shs2[c])
    print(shs2[c+1])
    gdf = gpd.read_file('DATA/MG/'+shs2[c],layer='m')
    gdf2 = gpd.read_file('DATA/MG/'+shs2[c+1],layer='m')
    print('LIDO')
    gdf3 = pd.concat([gdf,gdf2])
    print('gerando...')
    gdf3.to_file('DATA/MG/'+shs2[c].replace("_1","_F"),layer='m',driver='GPKG')


