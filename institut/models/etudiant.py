# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re


class InstitutEtudiant(models.Model):
    _name = 'institut.etudiant'
    f_name = fields.Char('Full name : ', required=True)

    sex = fields.Selection([('female', 'Female'), ('male', 'Male')])
    image = fields.Image()
    startdate = fields.Char("Registration code : ", size=10)
    identity = fields.Char('Identity : ', size=8)
    adress = fields.Text('Address :')
    birthday = fields.Date('Date of Birth :')
    email = fields.Char('E-mail:')
    phone = fields.Char('Phone number :', size=8, required=True)

    classe_id = fields.Many2one('institut.classe', string='Class:', required=True)
    department_id = fields.Many2one('institut.department', string='Departement:', required=True)
    matiere_ids = fields.Many2many(related='classe_id.matiere_ids')
    classe_ids = fields.Many2one('institut.classe', string='Class :')

    # Fonction pour avoir le nom de l'etudiant comme titre dans le form
    def name_get(self):
        result = []
        for etudiant in self:
            nom = etudiant.f_name
        result.append((etudiant.id, nom))
        return result

        # Fonction pour envoyer des messages vers Whatsapp

    def send_message(self):
        if not self.phone:
            raise ValueError('Incorrect phone number')
        message = 'Hi %s' % self.f_name
        whatapp_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' % (self.phone, message)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': whatapp_api_url
        }
