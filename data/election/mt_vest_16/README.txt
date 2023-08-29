2016 Montana precinct and election results shapefile.

## RDH Date retrieval
06/07/2021

## Sources
Election results from Montana Secretary of State (https://sosmt.gov/elections/results/)
 
Precinct shapefile primarily from Dave Ritts at the Montana State Library, pending submission to the U.S. Census Bureau's 2020 Redistricting Data Program. The following counties used 2016 precinct maps sourced from the respective county governments instead: Fallon, Phillips, Valley.

Precinct splits in Lake County were reversed based on the 2016 precinct shapefile from the county. The A/B subdivisions of Precinct 16 and Precinct 33 in Lewis and Clark were added based on county precinct maps.

## Fields metadata

Vote Column Label Format
------------------------
Columns reporting votes follow a standard label pattern. One example is:
G16PREDCli
The first character is G for a general election, P for a primary, C for a caucus, R for a runoff, S for a special.
Characters 2 and 3 are the year of the election.
Characters 4-6 represent the office type (see list below).
Character 7 represents the party of the candidate.
Characters 8-10 are the first three letters of the candidate's last name.

Office Codes
AGR - Commissioner of Agriculture
ATG - Attorney General
AUD - Auditor
COM - Comptroller
COU - City Council Member
DEL - Delegate to the U.S. House
GOV - Governor
H## - U.S. House, where ## is the district number. AL: at large.
HOD - House of Delegates, accompanied by a HOD_DIST column indicating district number
HOR - U.S. House, accompanied by a HOR_DIST column indicating district number
INS - Commissioner of Insurance
LAB - Commissioner of Labor
LTG - Lieutenant Governor
LND - Commissioner of Public Lands
PRE - President
PSC - Public Service Commissioner
PUC - Public Utilities Commissioner
RGT - State University Regent
RRC - Railroad Commissioner
SAC - State Court of Appeals
SOS - Secretary of State
SOV - Senate of Virginia, accompanied by a SOV_DIST column indicating district number
SPI - Superintendent of Public Instruction
SSC - State Supreme Court
TRE - Treasurer
USS - U.S. Senate

Party Codes
D and R will always represent Democrat and Republican, respectively.
See the state-specific notes for the remaining codes used in a particular file; note that third-party candidates may appear on the ballot under different party labels in different states.

## Fields
G16PRERTRU - Donald Trump (Republican Party)
G16PREDCLI - Hillary Clinton (Democratic Party)
G16PRELJOH - Gary Johnson (Libertarian Party)
G16PREGSTE - Jill Stein (Green Party)
G16PREOFUE - "Rocky" Roque de la Fuente (American Delta)

G16HALRZIN - Ryan Zinke (Republican Party)
G16HALDJUN - Denise Juneau (Democratic Party)
G16HALLBRE - Rick Breckenridge (Libertarian Party)

G16GOVRGIA - Greg Gianforte (Republican Party)
G16GOVDBUL - Steve Bullock (Democratic Party)
G16GOVLDUN - Ted Dunlap (Libertarian Party)

G16ATGRFOX - Tim Fox (Republican Party)
G16ATGDJEN - Larry Jent (Democratic Party)

G16SOSRSTA - Corey Stapleton (Republican Party)
G16SOSDLIN - Monica Lindeen (Democratic Party)
G16SOSLROO - Roger Roots (Libertarian Party)

G16AUDRROS - Matt Rosendale (Republican Party)
G16AUDDLAS - Jesse Laslovich (Democratic Party)

G16SPIRARN - Elsie Arntzen (Republican Party)
G16SPIDROM - Melissa Romano (Democratic Party)