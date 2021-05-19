from namecheap import Api
from odoo import models, fields, api


class N360ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'website_shop'

    saas_type = fields.Selection(
        [('app', "App"), ('domain', "domain"), ('email', "Email"), ('storage', "Storage"), ('training', "Training"),
         ('plan', "Plan"), ('consulting', "Consulting"),
         ], string="SaaS Type")
    depends = fields.Char('Depends')
    domain_search_method = fields.Selection([],
                                            help="""Specifies the type of search method that will be used to verify the existence of a given domain""")
    domain_register_method = fields.Selection([],
                                              help="""specifies the type of registration method that will be used to register the domain""")


class N360ProductProduct(models.Model):
    _inherit = 'product.product'
    _description = 'website_shop'

    saas_type = fields.Selection(
        [('app', "App"), ('domain', "domain"), ('email', "Email"), ('storage', "Storage"), ('training', "Training"),
         ('plan', "Plan"), ('consulting', "Consulting"),
         ], string="SaaS Type")
    depends = fields.Char('Depends')
    domain_search_method = fields.Selection([],
                                            help="""Specifies the type of search method that will be used to verify the existence of a given domain""")
    domain_register_method = fields.Selection([],
                                              help="""specifies the type of registration method that will be used to register the domain""")
