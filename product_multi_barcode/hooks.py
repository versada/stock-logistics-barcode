# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.

from odoo import SUPERUSER_ID, api


def pre_init_hook(cr):
    cr.execute("""
        CREATE TEMPORARY TABLE tmp_product_barcode_relations AS
        SELECT id, barcode from product_product WHERE barcode IS NOT NULL
    """)


def post_init_hook(cr, registry):
    cr.execute("""
        INSERT INTO product_barcode(name, product_id, sequence)
        SELECT t.barcode, t.id, 1
        FROM tmp_product_barcode_relations t
    """)
    env = api.Environment(cr, SUPERUSER_ID, {})
    env['product.product'].search([])._compute_barcode()
