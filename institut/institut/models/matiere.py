# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InstitutMatiere(models.Model):
    _name = 'institut.matiere'
    name = fields.Char()
    code = fields.Char('Coefficient :', size=1)

    #department_id = fields.Many2one('university.department', string='Departement:')
    #professeur_ids = fields.Many2many('university.professeur', string='Professor:')
