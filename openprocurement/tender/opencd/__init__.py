from openprocurement.tender.opencd.models import Tender
from logging import getLogger
from pkg_resources import get_distribution

PKG = get_distribution(__package__)

LOGGER = getLogger(PKG.project_name)


def includeme(config):
    LOGGER.info('init competitive dialog plugin')
    config.add_tender_procurementMethodType(Tender)
    config.scan("openprocurement.tender.opencd.views")
