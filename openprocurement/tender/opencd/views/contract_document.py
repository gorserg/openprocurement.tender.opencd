# -*- coding: utf-8 -*-
from openprocurement.api.utils import opresource
from openprocurement.api.views.contract_document import TenderAwardContractDocumentResource as BaseResource


@opresource(name='Tender CD Contract Documents',
            collection_path='/tenders/{tender_id}/contracts/{contract_id}/documents',
            path='/tenders/{tender_id}/contracts/{contract_id}/documents/{document_id}',
            procurementMethodType='aboveThresholdCD',
            description="Tender contract documents")
class TenderAwardContractDocumentResource(BaseResource):
    """ Tender Award Contract Document """
