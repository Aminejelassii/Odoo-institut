# -*- coding: utf-8 -*-
{
    'name': "institut",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/etudiant_views.xml',
        'views/professeur_views.xml',
        'views/departement_view.xml',
        'views/classe_views.xml',
        'views/matiere.xml',
        'Cards/Card.xml',
        'Cards/Student_card.xml'
    ],
    # only loaded in demonstration mode
    'demo': [

    ],
}
