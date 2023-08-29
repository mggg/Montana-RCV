2020 Montana precinct and election results shapefile.

## RDH Date retrieval
06/07/2021

## Sources
Election results from Montana Secretary of State (https://sosmt.gov/elections/results/)

Precinct shapefile primarily from Dave Ritts at the Montana State Library, as prepared for submission to the U.S. Census Bureau's 2020 Redistricting Data Program. 

## Fields metadata

Vote Column Label Format
------------------------
Columns reporting votes follow a standard label pattern. One example is:
G20PRERTRU
The first character is G for a general election, C for recount results, P for a primary, S for a special, and R for a runoff.
Characters 2 and 3 are the year of the election.
Characters 4-6 represent the office type (see list below).
Character 7 represents the party of the candidate.
Characters 8-10 are the first three letters of the candidate's last name.

Office Codes

ATG - Attorney General
AUD - Auditor
COC - Corporation Commissioner
COU - City Council Member
DEL - Delegate to the U.S. House
GOV - Governor
H## - U.S. House, where ## is the district number. AL: at large.
INS - Insurance Commissioner
LTG - Lieutenant Governor
PRE - President
PSC - Public Service Commissioner
SAC - State Appeals Court (in AL: Civil Appeals)
SCC - State Court of Criminal Appeals
SOS - Secretary of State
SPI - Superintendent of Public Instruction
USS - U.S. Senate

Party Codes
D and R will always represent Democrat and Republican, respectively.
See the state-specific notes for the remaining codes used in a particular file; note that third-party candidates may appear on the ballot under different party labels in different states.

## Fields

G20PRERTRU - Donald J. Trump (Republican Party)
G20PREDBID - Joseph R. Biden (Democratic Party)
G20PRELJOR - Jo Jorgensen (Libertarian Party)

G20USSRDAI - Steve Daines (Republican Party)
G20USSDBUL - Steve Bullock (Democratic Party)

G20HALRROS - Matt Rosendale (Republican Party)
G20HALDWIL - Kathleen Williams (Democratic Party)

G20GOVRGIA - Greg Gianforte (Republican Party)
G20GOVDCOO - Mike Cooney (Democratic Party)
G20GOVLBIS - Lyman Bishop (Libertarian Party)

G20ATGRKNU - Austin Knudsen (Republican Party)
G20ATGDGRA - Raph Graybill (Democratic Party)

G20SOSRJAC - Christi Jacobsen (Republican Party)
G20SOSDBEN - Bryce Bennett (Democratic Party)

G20AUDRDOW - Troy Downing (Republican Party)
G20AUDDMOR - Shane A. Morigeau (Democratic Party)
G20AUDLROO - Roger Roots (Libertarian Party)

G20SPIRARN - Elsie Arntzen (Republican Party)
G20SPIDROM - Melissa Romano (Democratic Party)
G20SPILLEA - Kevin Leatherbarrow (Libertarian Party)

## Processing Steps

The three precincts in Treasure County were merged as the county transitioned to a single countywide precinct prior to the 2020 election.