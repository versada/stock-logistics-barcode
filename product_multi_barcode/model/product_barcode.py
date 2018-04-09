# -*- coding: utf-8 -*-
# This file is part of Odoo. The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.

from odoo import api, fields, models


class ProductBarcode(models.Model):
    _name = 'product.barcode'
    _description = "List of Barcode for a product."
    _order = 'sequence'

    name = fields.Char('Barcode', size=13)
    product_id = fields.Many2one('product.product', 'Product', required=True)
    sequence = fields.Integer()

    @api.model
    def create(self, vals):
        """Create barcode with a sequence higher than all
        other products when it is not specified"""
        if not vals.get('sequence') and vals.get('product_id'):
            barcodes = self.search([('product_id', '=', vals['product_id'])])
            vals['sequence'] = max(
                (barcode.sequence for barcode in barcodes), default=0) + 1
        return super(ProductBarcode, self).create(vals)
