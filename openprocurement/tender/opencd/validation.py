# -*- coding: utf-8 -*-
from openprocurement.api.validation import validate_data
from openprocurement.tender.opencd.models import Qualification


def validate_patch_qualification_data(request):
    return validate_data(request, Qualification, True)
