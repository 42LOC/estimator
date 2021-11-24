# -*- coding: utf-8 -*-
{
    'name': "Task estimation",

    'summary': """
        Tasks estimation""",

    'description': """
        Long description of module's purpose
    """,

    'author': "42loc",
    'website': "https://odoo-42loc.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Timesheets',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr', 'project'],

    # always loaded
    'data': [
        'security/estimator_security.xml',
        'security/ir.model.access.csv',
        'wizard/wizard_project_view.xml',
        'views/tasks.xml',
        'views/work_units.xml',
        'data/sequence.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
