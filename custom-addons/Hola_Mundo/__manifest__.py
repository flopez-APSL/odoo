# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Modulo Hola Mundo',
    'version': '1.0',
    'author': 'Fernando Lopez Lopez',
    'website': 'https://www.apsl.net',
    'description': """
Ejemplo de Hola Mundo.
    """,
    'depends': ['base'],
    'data': [
        'views/hola_mundo.xml',
    ],
    'installable': True,
    'auto_install': True,
}
