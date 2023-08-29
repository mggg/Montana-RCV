import geopandas 
import pandas as pd
from shapely.geometry import Point

"""
AGR - Agriculture Commissioner
ATG - Attorney General
AUD - Auditor
COC - Corporation Commissioner
COU - City Council Member
DEL - Delegate to the U.S. House
GOV - Governor
H## - U.S. House, where ## is the district number. AL: at large.
INS - Insurance Commissioner
LAB - Labor Commissioner
LAN - Commissioner of Public Lands
LTG - Lieutenant Governor
PRE - President
PSC - Public Service Commissioner
RRC - Railroad Commissioner
SAC - State Appeals Court (in AL: Civil Appeals)
SCC - State Court of Criminal Appeals
SOS - Secretary of State
SSC - State Supreme Court
SPI - Superintendent of Public Instruction
TRE - Treasurer
USS - U.S. Senate
"""

voting_districts = geopandas.read_file("data/election/mt_vtd/mt_vtd.shp")

election_2020 = geopandas.read_file("data/election/mt_vest_20/mt_vest_20.shp")
#G20PRERTRU - Donald J. Trump (Republican Party)
#G20PREDBID - Joseph R. Biden (Democratic Party)
#G20PRELJOR - Jo Jorgensen (Libertarian Party)

#G20GOVRGIA - Greg Gianforte (Republican Party)
#G20GOVDCOO - Mike Cooney (Democratic Party)
#G20GOVLBIS - Lyman Bishop (Libertarian Party)

election_2018 = geopandas.read_file("data/election/mt_vest_18/mt_vest_18.shp")
#G18USSRROS - Matt Rosendale (Republican Party)
#G18USSDTES - Jon Tester (Democratic Party)
#G18USSLBRE - Rick Breckenridge (Libertarian Party)


election_2016 = geopandas.read_file("data/election/mt_vest_16/mt_vest_16.shp")
#G16PRERTRU - Donald Trump (Republican Party)
#G16PREDCLI - Hillary Clinton (Democratic Party)
#G16PRELJOH - Gary Johnson (Libertarian Party)
#G16PREGSTE - Jill Stein (Green Party)
#G16PREOFUE - "Rocky" Roque de la Fuente (American Delta)


######################################33

"""
merge data sets together
"""

elections_18_16 = election_2018.merge(election_2016, on = 'COUNTYFP10')
elections_18_16_20 = elections_18_16.merge(election_2020, on = 'COUNTYFP10')


election_data = elections_18_16_20[[ 'COUNTYFP10','G18USSRROS', 'G18USSDTES', 'G18USSLBRE', 'G16PRERTRU','G16PREDCLI','G16PRELJOH','G16PREGSTE', 'G16PREOFUE','STATEFP10', 'COUNTY', 'NAME', 'SOSPRECINC', 'G20PRERTRU', 'G20PREDBID',
       'G20PRELJOR','G20GOVRGIA', 'G20GOVDCOO', 'G20GOVLBIS','geometry']]

print(election_data.columns)

voting_districts_edited = voting_districts.merge(elections_18_16_20, on = 'geometry')

print(voting_districts_edited.columns)