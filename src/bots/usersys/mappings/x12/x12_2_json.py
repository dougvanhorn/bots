#mapping-script
from pprint import pprint as pp

import bots.transform as transform
from bots import botsglobal

def main(inn,out):
    """Mapping function.

    When everything in `botsindex.py` is configured correctly, and the inbound x12 is valid, this
    function will be called.

    In here you would write code to read the data found on Inmessage and write it to the outmessage.
    When you do that, the node on the outmessage is validated against the outbound grammar (in this
    plugin, that's `tojson`).  If the outbound data is valid, then you get a file.

    Arguments:
        inn: an inmessage.Inmessage instance
        out: an outmessage.Outmessage instance
    """
    botsglobal.logger.debug('x12_2_json mapping code is running!  W00T!')

    # I'm not doing in lookups right now, just writing out an example file.
    # In order to make sense of the inbound X12 data, we will need to purchase documenation from the
    # EDI folks.  I think they're roughly $850 per spec.  That would hopefully get us the knowledge
    # to know what each field attribute is in the X12 (ST, N1, N4, W66, LX, ...).  Without that,
    # we're really limited in our understanding of what to do with the data once it's parsed.
    out.put({'BOTSID':'HEA','FOOD':'SPAM HAM EGGS'})
    out.put({'BOTSID':'HEA'}, {'BOTSID': 'TOT', 'TOTAALREGEL': '1234.45'})
    out.put({'BOTSID':'HEA'}, {'BOTSID': 'TOT', 'TOTAALBTW': '7.0'})

    inn.root.display()
    out.root.display()

    #transform.inn2out(inn,out)  #receive ISA; send out as json.
