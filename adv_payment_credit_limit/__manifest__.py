# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Advance Credit Check Rules',
    'version': '1.0.0',
    'summary': 'Allows to configure advance credit check rules and apply on customer',
    'sequence': 21,
    'description': """
        Allows to configure advance credit check rules and apply on customer
    """,
    'category': 'Sales',
    'author': 'Synconics Technologies Pvt. Ltd.',
    'website': 'http://www.synconics.com',
    'images': [
        'static/description/main_screen.png'
    ],
    'depends': ['payment_credit_limit'],
    'data': [
            'data/credit_code_data.xml',
            'security/ir.model.access.csv',
            'views/partner_view.xml',
            'views/credit_code_view.xml',
    ],
    'demo': [],
    'price': 60,
    'currency': 'EUR',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
}
