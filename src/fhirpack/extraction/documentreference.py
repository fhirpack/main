from typing import Union


from fhirpy.lib import SyncFHIRResource
from fhirpy.lib import SyncFHIRReference
import fhirpack.utils as utils

import fhirpack.extraction.base as base


class ExtractorDocumentReferenceMixin(base.BaseExtractorMixin):
    def getDocumentReference(self, *args, **kwargs):

        return self.getResources(*args, resourceType="DocumentReference", **kwargs)
