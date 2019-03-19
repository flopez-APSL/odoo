# -*- coding: utf-8 -*-
{
    'name': 'To-Do Application',
    'version': '1.0',
    'description': 'Manage your personal Tasks with this module.',
    'author': 'Fernando Lopez',
    'depends': ['mail'],
    'application': True,
    'data': ['security/ir.model.access.csv',
             'security/todo_access_rules.xml',
             'views/todo_menu.xml',
             'views/todo_view.xml',
             'views/res_partner_view.xml'],
    'aplication': True,

}


