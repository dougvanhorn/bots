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
    botsglobal.logger.debug('x12_nocheck mapping code is running!  W00T!')

    # receive ISA; send out as json.
    transform.inn2out(inn,out)
