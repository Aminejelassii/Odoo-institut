# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InstitutMatiere(models.Model):
    _name = 'institut.matiere'
    name = fields.Char()
    code = fields.Char('Coefficient :', size=1)


