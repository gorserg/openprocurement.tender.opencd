# -*- coding: utf-8 -*-
from openprocurement.tender.openua.views.question import TenderUaQuestionResource as BaseResource
from openprocurement.api.utils import opresource


@opresource(name='TenderCD Questions',
            collection_path='/tenders/{tender_id}/questions',
            path='/tenders/{tender_id}/questions/{question_id}',
            procurementMethodType='aboveThresholdCD',
            description="Tender questions")
class TenderQuestionResource(BaseResource):
    """ TenderCD Questions """
