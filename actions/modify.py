#!/usr/bin/env python
from st2common.runners.base_action import Action


class Modify(Action):

    def run(self, beertab, owner, operation, recipient):
        if not beertab:
            beertab = {}

        if operation == 'add':
            beertab[recipient] = beertab.get(recipient, 0) + 1
        elif operation == 'remove':
            if recipient in beertab:
                beertab[recipient] = beertab[recipient] - 1
                if beertab[recipient] <= 0:
                    del beertab[recipient]
            else:
                raise ValueError("{} doesn't owe {} any beer".format(recipient, owner))
        else:
            raise RuntimeError("Unknown operation: {}".format(operation))

        return beertab
