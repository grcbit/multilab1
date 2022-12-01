# -*- coding: utf-8 -*-
{
    'name': "Product Discount Limit",
    'summary': """
        This module is allow to set discount limit on product and product category | Sale Discount limit | Invoice Discount Limit | Invoice Discount limit on product category | Product Category discount limit | Maximum Discount | Sale Discount Restrict | Invoice Discount""",
    'description': """
        This module is allow to set discount limit on product and product category.""",    
    'version': '1.0',
    'author': "Preway IT Solutions",
    'category': 'Sales Management',
    'depends': ['sale', 'account'],
    'data': [
        'security/product_security.xml',
        'views/product_views.xml',
    ],
    'price': 15.0,
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    "license": "LGPL-3",
    "images":["static/description/Banner.png"],
}
