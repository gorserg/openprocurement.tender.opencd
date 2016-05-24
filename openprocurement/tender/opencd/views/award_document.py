# -*- coding: utf-8 -*-
from openprocurement.api.views.award_document import TenderAwardDocumentResource as BaseResource
from openprocurement.api.utils import opresource


@opresource(name='Tender CD Award Documents',
            collection_path='/tenders/{tender_id}/awards/{award_id}/documents',
            path='/tenders/{tender_id}/awards/{award_id}/documents/{document_id}',
            procurementMethodType='aboveThresholdCD',
            description="Tender award documents")
class TenderAwardDocumentResource(BaseResource):
    """ Tender Award Document """
