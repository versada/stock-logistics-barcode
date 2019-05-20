# -*- coding: utf-8 -*-
##############################################################################
#
#    Author:  Author Guewen Baconnier
#    Copyright 2012-2014 Camptocamp SA
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

{
    'name': 'Multiple Barcodes on Products',
    'version': '12.0.1.0.0',
    'author': "Camptocamp,Odoo Community Association (OCA)",
    'maintainer': 'Camptocamp',
    'category': 'Warehouse',
    'complexity': "normal",  # easy, normal, expert
    'depends': [
        'base',
        'product',
        'barcodes',
        'sales_team',
    ],
    'description': """
Multiple Barcodes on Products
=============================

Allow Multiple Barcodes on products.
A list of barcodes is available for each product with a priority, so a
main barcode is defined.
""",
    'website': 'http://www.camptocamp.com',
    'data': [
        'security/ir.model.access.csv',
        'views/product_product.xml',
    ],
    'installable': False,
    'pre_init_hook': 'pre_init_hook',
    'post_init_hook': 'post_init_hook',
    'auto_install': False,
    'license': 'AGPL-3',
}
