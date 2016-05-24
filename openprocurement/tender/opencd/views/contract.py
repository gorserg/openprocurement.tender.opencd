# -*- coding: utf-8 -*-
from openprocurement.api.utils import opresource
from openprocurement.tender.openua.views.contract import TenderUaAwardContractResource as BaseResource


@opresource(name='Tender CD Contracts',
            collection_path='/tenders/{tender_id}/contracts',
            path='/tenders/{tender_id}/contracts/{contract_id}',
            procurementMethodType='aboveThresholdCD',
            description="Tender CD contracts")
class TenderAwardContractResource(BaseResource):
    """ """
