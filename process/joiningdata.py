import geopandas
import maup


mt_vtd = geopandas.read_file("data/election/mt_vtd").to_crs(epsg=32100)
mt_blocks = geopandas.read_file('data/election/cblock2010').to_crs(epsg=32100)
mt_blocks['TOTPOP'] = mt_blocks['P0010001']

election_2020 = geopandas.read_file("data/election/mt_vest_20").to_crs(epsg=32100)
races_20 = ['G20PRERTRU', 'G20PREDBID', 'G20USSRDAI', 'G20USSDBUL', 'G20GOVRGIA', 'G20GOVDCOO']

election_2018 = geopandas.read_file("data/election/mt_vest_18").to_crs(epsg=32100)
races_18 = ['G18USSRROS', 'G18USSDTES']

# maup 2020 election data
parts_20 = maup.intersections(election_2020, mt_vtd)
weights_20 = mt_blocks['TOTPOP'].groupby(maup.assign(mt_blocks, parts_20)).sum()
weights_20 = maup.normalize(weights_20, level=0)
mt_vtd[races_20] = maup.prorate(parts_20, election_2020[races_20], weights=weights_20)

# maup 2018 election data
parts_18 = maup.intersections(election_2018, mt_vtd)
weights_18 =  mt_blocks['TOTPOP'].groupby(maup.assign(mt_blocks, parts_18)).sum()
weights_18 = maup.normalize(weights_18, level=0)
mt_vtd[races_18] = maup.prorate(parts_18, election_2018[races_18], weights=weights_18)

mt_vtd.to_csv('data/election/mt_vtd_elex.csv') 
