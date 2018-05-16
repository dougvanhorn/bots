from bots.botsconfig import *

# http://skilchen.github.io/bots/configuration/grammars/syntax-params/
syntax = {
    'charset': 'utf-8',
    'indented': True,
    # Not needed for this file type.
    #'checkfixedrecordtooshort': False,
    # This is not a typo.
    #'decimaal': '.',
}


# http://skilchen.github.io/bots/configuration/grammars/structure/
structure = [
    {
        ID:'HEA',
        MIN:0,
        MAX:10000,
        QUERIES:{
            'frompartner':  {'BOTSID':'HEA','EANZENDER':None},
            'topartner':    {'BOTSID':'HEA','EANONTVANGER':None},
            'reference':    {'BOTSID':'HEA','FACTUURNUMMER':None},
            'testindicator':{'BOTSID':'HEA','TEST':None}},
        LEVEL:[
            {ID:'HAL',MIN:0,MAX:10},
            {ID:'LIN',MIN:0,MAX:10000,
                LEVEL:[
                    {ID:'LAL',MIN:0,MAX:10},
                    ]},
            {ID:'TOT',MIN:0,MAX:2},
            ]
    },
]

# http://skilchen.github.io/bots/configuration/grammars/nextmessage/
nextmessage = ({'BOTSID':'HEA'},)

# http://skilchen.github.io/bots/configuration/grammars/recorddefs/
recorddefs = {
    'HEA':[
            ['BOTSID','C',3,'A'],
            ['FOOD', 'C', 20, 'AN'],
            ['SOORT', 'C', 20, 'AN'],
            ['EANZENDER', 'C', 13, 'AN'],
            ['EANONTVANGER', 'C', 13, 'AN'],
            ['TEST', 'C', 1, 'AN'],
            ['FACTUURNUMMER', 'C', 17, 'AN'],
            ['FACTUURDATUM', 'C', 8, 'AN'],
            ['INDICATIEONTVANGSTBEVESTIGING', 'C', 3, 'AN'],
            ['SOORTFACTUUR', 'C', 3, 'AN'],
            ['EANAFNEMER', 'C', 13, 'AN'],
            ['BTWAFNEMER', 'C', 17, 'AN'],
            ['EANLEVERANCIER', 'C', 13, 'AN'],
            ['BTWLEVERANCIER', 'C', 17, 'AN'],
            ['EANAFLEVER', 'C', 13, 'AN'],
            ['EANHAALADRES', 'C', 13, 'AN'],
            ['EANEINDBESTEMMING', 'C', 13, 'AN'],
            ['EANFACTUUR', 'C', 13, 'AN'],
            ['BTWFACTUUR', 'C', 17, 'AN'],
            ['EANBONTVANGER', 'C', 13, 'AN'],
            ['LEVERDATUM', 'C', 12, 'AN'],
            ['ACCIJNSVRIJ', 'C', 3, 'AN'],
            ['VALUTA', 'C', 3, 'AN'],
            ['VERZENDBERICHTNUMMER', 'C', 17, 'AN'],
            ['ORDERNUMMERAFNEMER', 'C', 17, 'AN'],
            ['CORFACTUURNUMMER', 'C', 17, 'AN'],
            ['DAGNAFACTUUR1', 'C', 3, 'N'],
            ['PERCENTKORTING1', 'C', 12.4, 'N'],
            ['DAGNAFACTUUR2', 'C', 3, 'N'],
            ['PERCENTKORTING2', 'C', 12.4, 'N'],
            ['DAGNAFACTUUR3', 'C', 3, 'N'],
            ['PERCENTKORTING3', 'C', 12.4, 'N'],
          ],
    'HAL':[
            ['BOTSID','C',3,'A'],
            ['KORTINGTOESLAG', 'C', 3, 'AN'],
            ['SOORTKORTING', 'C', 3, 'AN'],
            ['KORTINGSBEDRAG', 'C', 20.3, 'N'],
            ['BTWTARIEF', 'C', 3, 'AN'],
            ['BTWPERCENTAGE', 'C', 12.4, 'N'],
          ],
    'LIN':[
            ['BOTSID','C',3,'A'],
            ['REGEL', 'C', 6, 'N'],
            ['ARTIKEL', 'C', 14, 'AN'],
            ['PROMOTIECODE', 'C', 17, 'AN'],
            ['ARTIKELOMSCHRIJVING', 'C', 35, 'AN'],
            ['GEFACTAANTAL', 'C', 16.3, 'N'],
            ['GELEVERDAANTAL', 'C', 16.3, 'N'],
            ['NETTOREGELBEDRAG', 'C', 20.3, 'N'],
            ['PRIJS', 'C', 20.4, 'N'],
            ['AANTALPRIJSBASIS', 'C', 16.3, 'N'],
            ['EENHEIDPRIJSBASIS', 'C', 3, 'AN'],
            ['BTWTARIEF', 'C', 3, 'AN'],
            ['BTWPERCENTAGE', 'C', 12.4, 'N'],
          ],
    'LAL':[
            ['BOTSID','C',3,'A'],
            ['KORTINGTOESLAG', 'C', 3, 'AN'],
            ['SOORTKORTING', 'C', 3, 'AN'],
            ['KORTINGSBEDRAG', 'C', 20.3, 'N'],
            ['BTWTARIEF', 'C', 3, 'AN'],
            ['BTWPERCENTAGE', 'C', 12.4, 'N'],
          ],
    'TOT':[
            ['BOTSID','C',3,'A'],
            ['TOTAALREGEL', 'C', 20.3, 'N'],
            ['TOTAALFACTUURKORTING', 'C', 20.3, 'N'],
            ['TOTAALBTW', 'C', 20.3, 'N'],
            ['TOTAALFACTUUR', 'C', 20.3, 'N'],
            ['GRONDSLAGBETKORTING', 'C', 20.3, 'N'],
            ['BTWTARIEF1', 'C', 3, 'AN'],
            ['BTWPERCENTAGE1', 'C', 12.4, 'N'],
            ['BTWGRONDSLAG1', 'C', 20.3, 'N'],
            ['BTWBEDRAG1', 'C', 20.3, 'N'],
            ['BTWTARIEF2', 'C', 3, 'AN'],
            ['BTWPERCENTAGE2', 'C', 12.4, 'N'],
            ['BTWGRONDSLAG2', 'C', 20.3, 'N'],
            ['BTWBEDRAG2', 'C', 20.3, 'N'],
            ['BTWTARIEF3', 'C', 3, 'AN'],
            ['BTWPERCENTAGE3', 'C', 12.4, 'N'],
            ['BTWGRONDSLAG3', 'C', 20.3, 'N'],
            ['BTWBEDRAG3', 'C', 20.3, 'N'],
            ['BTWTARIEF4', 'C', 3, 'AN'],
            ['BTWPERCENTAGE4', 'C', 12.4, 'N'],
            ['BTWGRONDSLAG4', 'C', 20.3, 'N'],
            ['BTWBEDRAG4', 'C', 20.3, 'N'],
          ],
}
