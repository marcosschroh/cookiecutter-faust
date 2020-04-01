import faust

import settings

app = faust.App(**settings.FAUST_CONF)
