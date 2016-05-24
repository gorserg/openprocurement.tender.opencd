# -*- coding: utf-8 -*-
from openprocurement.api.utils import opresource
from openprocurement.tender.openua.views.complaint_document import TenderUaComplaintDocumentResource


@opresource(name='Tender CD Complaint Documents',
            collection_path='/tenders/{tender_id}/complaints/{complaint_id}/documents',
            path='/tenders/{tender_id}/complaints/{complaint_id}/documents/{document_id}',
            procurementMethodType='aboveThresholdCD',
            description="Tender complaint documents")
class TenderCDComplaintDocumentResource(TenderUaComplaintDocumentResource):
    pass
