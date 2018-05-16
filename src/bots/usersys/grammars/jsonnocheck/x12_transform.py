# Provide for a 1 to 1 mapping from an X12 to a JSON document.
# `jsonnocheck` is a special type of `outmessage.Outmessage` that does not validate the outbound
# node structure.  Quite useful for us to get to the juicy insides of the X12 doc.

nextmessage = ({'BOTSID':'ISA'},)

syntax = {
    'charset': 'utf-8',
    'indented':True,
}

