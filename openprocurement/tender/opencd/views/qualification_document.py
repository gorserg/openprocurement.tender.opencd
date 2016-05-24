# -*- coding: utf-8 -*-
from openprocurement.api.utils import (
    get_file,
    save_tender,
    upload_file,
    apply_patch,
    update_file_content_type,
    json_view,
    context_unpack,
    APIResource,
)
from openprocurement.api.validation import (
    validate_file_update,
    validate_file_upload,
    validate_patch_document_data,
)
from openprocurement.tender.opencd.utils import qualifications_resource


@qualifications_resource(
    name='TenderCD Qualification Documents',
    collection_path='/tenders/{tender_id}/qualifications/{qualification_id}/documents',
    path='/tenders/{tender_id}/qualifications/{qualification_id}/documents/{document_id}',
    procurementMethodType='aboveThresholdCD',
    description="Tender qualification documents")
class TenderQualificationDocumentResource(APIResource):

    @json_view(permission='view_tender')
    def collection_get(self):
        """Tender Qualification Documents List"""
        if self.request.params.get('all', ''):
            collection_data = [i.serialize("view") for i in self.context.documents]
        else:
            collection_data = sorted(dict([
                (i.id, i.serialize("view"))
                for i in self.context.documents
            ]).values(), key=lambda i: i['dateModified'])
        return {'data': collection_data}

    @json_view(permission='edit_tender', validators=(validate_file_upload,))
    def collection_post(self):
        """Tender Qualification Document Upload
        """
        if self.request.validated['tender_status'] != 'active.pre-qualification':
            self.request.errors.add('body', 'data', 'Can\'t add document in current ({}) tender status'.format(self.request.validated['tender_status']))
            self.request.errors.status = 403
            return
        qualification = self.request.validated['qualification']
        if qualification.status != 'pending':
            self.request.errors.add('body', 'data', 'Can\'t add document in current qualification status')
            self.request.errors.status = 403
            return
        document = upload_file(self.request)
        self.context.documents.append(document)
        if save_tender(self.request):
            self.LOGGER.info('Created tender qualification document {}'.format(document.id),
                        extra=context_unpack(self.request, {'MESSAGE_ID': 'tender_qualification_document_create'}, {'document_id': document.id}))
            self.request.response.status = 201
            document_route = self.request.matched_route.name.replace("collection_", "")
            self.request.response.headers['Location'] = self.request.current_route_url(_route_name=document_route, document_id=document.id, _query={})
            return {'data': document.serialize("view")}

    @json_view(permission='view_tender')
    def get(self):
        """Tender Qualification Document Read"""
        if self.request.params.get('download'):
            return get_file(self.request)
        document = self.request.validated['document']
        document_data = document.serialize("view")
        document_data['previousVersions'] = [
            i.serialize("view")
            for i in self.request.validated['documents']
            if i.url != document.url
        ]
        return {'data': document_data}

    @json_view(validators=(validate_file_update,), permission='edit_tender')
    def put(self):
        """Tender Qualification Document Update"""
        if self.request.validated['tender_status'] != 'active.pre-qualification':
            self.request.errors.add('body', 'data', 'Can\'t update document in current ({}) tender status'.format(self.request.validated['tender_status']))
            self.request.errors.status = 403
            return
        qualification = self.request.validated['qualification']
        if qualification.status != 'pending':
            self.request.errors.add('body', 'data', 'Can\'t update document in current qualification status')
            self.request.errors.status = 403
            return
        document = upload_file(self.request)
        self.request.validated['qualification'].documents.append(document)
        if save_tender(self.request):
            self.LOGGER.info('Updated tender qualification document {}'.format(self.request.context.id),
                        extra=context_unpack(self.request, {'MESSAGE_ID': 'tender_qualification_document_put'}))
            return {'data': document.serialize("view")}

    @json_view(content_type="application/json", validators=(validate_patch_document_data,), permission='edit_tender')
    def patch(self):
        """Tender Qualification Document Update"""
        if self.request.validated['tender_status'] != 'active.pre-qualification':
            self.request.errors.add('body', 'data', 'Can\'t update document in current ({}) tender status'.format(self.request.validated['tender_status']))
            self.request.errors.status = 403
            return
        qualification = self.request.validated['qualification']
        if qualification.status != 'pending':
            self.request.errors.add('body', 'data', 'Can\'t update document in current qualification status')
            self.request.errors.status = 403
            return
        if apply_patch(self.request, src=self.request.context.serialize()):
            update_file_content_type(self.request)
            self.LOGGER.info('Updated tender qualification document {}'.format(self.request.context.id),
                        extra=context_unpack(self.request, {'MESSAGE_ID': 'tender_qualification_document_patch'}))
            return {'data': self.request.context.serialize("view")}
