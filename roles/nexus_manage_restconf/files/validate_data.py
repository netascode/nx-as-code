# simple wrapper to allow custom tag '!vault'

import sys
import yamale

schema = yamale.make_schema(sys.argv[1])


def _vault(loader, node):
    pass

#TODO: Fix issue with vault
data = yamale.make_data(sys.argv[2])

yamale.validate(schema, data, strict=True)
