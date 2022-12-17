# -*- coding: utf-8 -*-

{
    'name': " I Tech Product Fields",
    'version': "15.0.0.0",
    'summary': "Display Box Field in Product,Sales,Purchases,Reordering Rule,Transfers",
    'description': """ Display Box Field in Product,Sales,Purchases,Reordering Rule,Transfers. 
	""",
    'author': "I Tech",
    'website': "http://www.ejaftech.com/",
    'depends': ['base', 'sale_stock','purchase'],
    'data': [
        "security/ir.model.access.csv",
        'views/product.xml',
        'views/company.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
