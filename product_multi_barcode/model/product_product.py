# -*- coding: utf-8 -*-
##############################################################################
#
#    Author: Guewen Baconnier
#    Copyright 2012 Camptocamp SA
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from odoo import api, fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    barcode_ids = fields.One2many(
        'product.barcode', 'product_id', string='Barcodes')
    barcode = fields.Char(
        string='Main Barcode', compute='_compute_barcode',
        inverse='_inverse_barcode', search='_search_barcode', store=False)

    @api.multi
    @api.depends('barcode_ids')
    def _compute_barcode(self):
        for product in self:
            product.barcode = product.barcode_ids[:1].name

    @api.multi
    def _inverse_barcode(self):
        for product in self:
            if (
                product.barcode and product.barcode not in
                product.mapped('barcode_ids.name')
            ):
                product.barcode_ids.create({
                    'name': product.barcode,
                    'product_id': product.id,
                })

    def _search_barcode(self, operator, value):
        barcodes = self.env['product.barcode'].search(
            [('name', operator, value)], limit=None)
        return [('id', 'in', barcodes.mapped('product_id').ids)]

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        """overwrite the search method in order to search
        on all barcode codes of a product when we search an barcode"""

        barcode_terms = [x for x in args if x[0] == 'barcode']
        if barcode_terms:
            # get the operator of the search
            barcode_operator = barcode_terms[0][1]
            # get the value of the search
            barcode_value = barcode_terms[0][2]
            # search the barcode
            barcode_ids = self.env['product.barcode'].search(
                [('name', barcode_operator, barcode_value)]).ids

            # get the other arguments of the search
            args = [x for x in args if x[0] != 'barcode']
            # add the new criterion
            args += [('barcode_ids', 'in', barcode_ids)]
        return super(ProductProduct, self).search(
            args, offset=offset, limit=limit, order=order, count=count)
