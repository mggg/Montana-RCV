2018 Montana precinct and election shapefile.

## RDH Date retrieval
06/07/2021

## Sources
Election results from Montana Secretary of State (https://sosmt.gov/elections/results/)
 
Precinct shapefile primarily from Dave Ritts at the Montana State Library, pending submission to the U.S. Census Bureau's 2020 Redistricting Data Program. The A/B subdivisions of Precinct 16 and Precinct 33 in Lewis and Clark were added based on county precinct maps.

## Fields metadata

Vote Column Label Format
------------------------
Columns reporting votes follow a standard label pattern. One example is:
G16PREDCli
The first character is G for a general election, P for a primary, S for a special, and R for a runoff.
Characters 2 and 3 are the year of the election.
Characters 4-6 represent the office type (see list below).
Character 7 represents the party of the candidate.
Characters 8-10 are the first three letters of the candidate's last name.

Office Codes
A## - Ballot amendment, where ## is an identifier
AGR - Commissioner of Agriculture
ATG - Attorney General
AUD - Auditor
CFO - Chief Financial Officer
CHA - Council Chairman
COC - Corporation Commissioner
COM - Comptroller
CON - State Controller
COU - City Council Member
CSC - Clerk of the Supreme Court
DEL - Delegate to the U.S. House
GOV - Governor
H## - U.S. House, where ## is the district number. AL: at large.
HOD - House of Delegates, accompanied by a HOD_DIST column indicating district number
HOR - U.S. House, accompanied by a HOR_DIST column indicating district number
INS - Insurance Commissioner
LAB - Labor Commissioner
LND - Commissioner of Public/State Lands
LTG - Lieutenant Governor
MAY - Mayor
MNI - State Mine Inspector
PSC - Public Service Commissioner
PUC - Public Utilities Commissioner
RGT - State University Regent
SAC - State Appeals Court
SBE - State Board of Education
SOC - Secretary of Commonwealth
SOS - Secretary of State
SPI - Superintendent of Public Instruction
SPL - Commissioner of School and Public Lands
SSC - State Supreme Court
TAX - Tax Commissioner
TRE - Treasurer
UBR - University Board of Regents/Trustees/Governors
USS - U.S. Senate

Party Codes
D and R will always represent Democrat and Republican, respectively.
See the state-specific notes for the remaining codes used in a particular file; note that third-party candidates may appear on the ballot under different party labels in different states.

## Fields
G18USSRROS - Matt Rosendale (Republican Party)
G18USSDTES - Jon Tester (Democratic Party)
G18USSLBRE - Rick Breckenridge (Libertarian Party)

G18HALRGIA - Greg Gianforte (Republican Party)
G18HALDWIL - Kathleen Williams (Democratic Party)
G18HALLSWA - Elinor Swanson (Libertarian Party)

G18CSCRGRE - Bowen Greenwood (Republican Party)
G18CSCDREN - Rex Renk (Democratic Party)
G18CSCLROO - Roger Roots (Libertarian Party)