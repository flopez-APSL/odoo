# -*- coding: utf-8 -*-
{
    'name': "Calendar for the library",

    'summary': """
        Calendar for Library Module""",

    'description': """
        make a calendar.
    """,

    'author': "Fernando  López",
    'website': "http://apsl.net",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'library',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['library'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/book_date_view.xml'
    ],

    'aplication': True,

}