# -*- coding: utf-8 -*-
from openprocurement.api.utils import opresource
from openprocurement.tender.openua.views.award import TenderUaAwardResource as BaseResource


@opresource(name='Tender CD Awards',
            collection_path='/tenders/{tender_id}/awards',
            path='/tenders/{tender_id}/awards/{award_id}',
            description="Tender CD awards",
            procurementMethodType='aboveThresholdCD')
class TenderAwardResource(BaseResource):
    """ CD award resource """
