# -*- coding: utf-8 -*-
{
    'name': "Library_author",

    'summary': """
        módulo de autores para la librería""",

    'description': """
  
    """,

    'author': "Fernando  López",
    'website': "http://apsl.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['library'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv,
        'views/library_author_view.xml'
    ],

    'aplication': True,
}