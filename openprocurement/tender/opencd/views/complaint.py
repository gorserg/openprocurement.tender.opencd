# -*- coding: utf-8 -*-
from openprocurement.api.utils import opresource
from openprocurement.tender.openua.views.complaint import TenderUaComplaintResource


@opresource(name='Tender CD Complaints',
            collection_path='/tenders/{tender_id}/complaints',
            path='/tenders/{tender_id}/complaints/{complaint_id}',
            procurementMethodType='aboveThresholdCD',
            description="Tender CD complaints")
class TenderCDComplaintResource(TenderUaComplaintResource):

    @staticmethod
    def complaints_len(tender):
        return sum([len(i.complaints) for i in tender.awards], sum([len(i.complaints) for i in tender.qualifications], len(tender.complaints)))
