# -*- coding: utf-8 -*-
{
    'name': "venda_carros",

    'summary': """
    SISTEMA DE GESTÃO DE VENDA DE CARROS
        """,

    'description': """
         SISTEMA DE GESTÃO DE VENDA DE CARROS
    """,

    'author': "Daniel AC",
    'website': "http://github.com/daneiluac",
    'category': 'website',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'base_automation', 'website_sale', 'website_sale_stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/shop_page.xml',
        'views/templates.xml',
         'views/sale_order_view.xml',
        'views/views.xml',
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
