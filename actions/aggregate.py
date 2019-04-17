#!/usr/bin/env python
from st2common.runners.base_action import Action
import json
import six


class Aggregate(Action):

    def run(self, beertabs, recipient):
        result = {}
        # find all of the tabs with recipient in them and gather them up into
        # one dict keyed on the owner who owes the beer
        for owner, tab in six.iteritems(beertabs):
            if isinstance(tab, six.string_types):
                tab = json.loads(tab)

            if recipient in tab:
                result[owner] = tab[recipient]

        return result
