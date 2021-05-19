from namecheap import Api
from odoo import models, fields, api
from datetime import date

class N360ProductTemplate(models.Model):
    _inherit = 'sale.order'
    _description = 'website_shop'

    def payment_confirmed(self):
       self.state = 'done'

    def date_today(self):
        return date.today().strftime("%d-%m-%Y")

    def money_formart(self, money):
        return format(money, ',').replace(',', '.')


