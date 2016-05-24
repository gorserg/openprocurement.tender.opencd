# -*- coding: utf-8 -*-
from openprocurement.api.utils import opresource
from openprocurement.api.views.cancellation_document import TenderCancellationDocumentResource as BaseResource


@opresource(name='Tender CD Cancellation Documents',
            collection_path='/tenders/{tender_id}/cancellations/{cancellation_id}/documents',
            path='/tenders/{tender_id}/cancellations/{cancellation_id}/documents/{document_id}',
            procurementMethodType='aboveThresholdCD',
            description="Tender CD cancellation documents")
class TenderCancellationDocumentResource(BaseResource):
    """ Cancellation Document """
