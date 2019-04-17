#!/usr/bin/env python
from st2common.runners.base_action import Action


class Modify(Action):

    def run(self, beertab, person, user, operation):
        if not beertab:
            beertab = {}

        if operation == 'add':
            beertab[person] = beertab.get(person, 0) + 1
        elif operation == 'remove':
            if person in beertab:
                if beertab[person] > 0:
                    beertab[person] = beertab[person] - 1
                else:
                    raise ValueError("{} doesn't owe {} any beer".format(person, user))
            else:
                raise ValueError("{} doesn't have a beer tab open for {}".format(person, user))
        else:
            raise RuntimeError("Unknown operation: {}".format(operation))

        return beertab
