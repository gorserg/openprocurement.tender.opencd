# -*- coding: utf-8 -*-
from openprocurement.tender.openua.views.lot import TenderUaLotResource as TenderLotResource

from openprocurement.api.utils import (
    save_tender,
    opresource,
    json_view,
    context_unpack
)
from openprocurement.api.validation import (
    validate_lot_data,
)


@opresource(name='Tender CD Lots',
            collection_path='/tenders/{tender_id}/lots',
            path='/tenders/{tender_id}/lots/{lot_id}',
            procurementMethodType='aboveThresholdCD',
            description="Tender CD lots")
class TenderCDLotResource(TenderLotResource):

    @json_view(content_type="application/json", validators=(validate_lot_data,), permission='edit_tender')
    def collection_post(self):
        """Add a lot
        """
        if not self.validate_update_tender('add'):
            return
        lot = self.request.validated['lot']
        tender = self.request.validated['tender']
        tender.lots.append(lot)
        if self.request.authenticated_role == 'tender_owner':
            tender.invalidate_bids_data()
        if save_tender(self.request):
            self.LOGGER.info('Created tender lot {}'.format(lot.id),
                        extra=context_unpack(self.request, {'MESSAGE_ID': 'tender_lot_create'}, {'lot_id': lot.id}))
            self.request.response.status = 201
            self.request.response.headers['Location'] = self.request.route_url('Tender CD Lots', tender_id=tender.id, lot_id=lot.id)
            return {'data': lot.serialize("view")}
