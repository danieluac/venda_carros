# -*- coding: utf-8 -*-
{
    'name': "venda_carros",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'base_automation', 'website_sale','website_sale_stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/shop_page.xml',
        'views/templates.xml',
         'views/sale_order_view.xml',
        'report/sales_check_report.xml',
        'report/report_header.xml',
        'email/templates_de_cotacoes.xml',
        'data/sales_auto_action.xml',
        'data/metodo_pagamento.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
