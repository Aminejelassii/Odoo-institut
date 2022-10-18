# -*- coding: utf-8 -*-

from odoo import models, fields, api
import re


class InstitutProfesseur(models.Model):
    _name = 'institut.professeur'
    f_name = fields.Char('Full name : ', required=True)
    image = fields.Image()
    sex = fields.Selection([('female', 'Female'), ('male', 'Male')])
    identity = fields.Char('Identity : ', size=8)
    adress = fields.Text('Address :')
    birthday = fields.Date('Date of Birth :')
    startdate = fields.Date('Start date : ')
    email = fields.Char('E-mail :')
    phone = fields.Char('Phone number :', size=8, required=True)

    # Utilisation des relations Many2one et Many2many

    department_id = fields.Many2one('institut.department', string='Departement :')
    matiere_ids = fields.Many2many('institut.matiere', string='Subject :')
    classe_ids = fields.Many2many('institut.classe', string='Class :')

    # Fonction pour contrôler le saisie d'email
    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^([a-z0-9A-Z-]+)*@[a-z]+(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise ValueError('Invalid E-mail')

    # Fonction pour avoir le nom de professeur comme titre dans le form
    def name_get(self):
        result = []
        for professeur in self:
            nom = professeur.f_name
            result.append((professeur.id, nom))
            return result

    # Fonction pour envoyer des messages vers Whatsapp
    def send_message(self):
        if not self.phone:
            raise ValueError('Incorrect phone number')
        message = 'salut %s' % self.f_name
        whatapp_api_url = 'https://api.whatsapp.com/send?phone=%s&text=%s' % (self.phone, message)
        return {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': whatapp_api_url
        }

    # Fonction pour éviter l'erreur de la date
    @api.constrains('birthday', 'startdate')
    def chek_date(self):
        if self.birthday > self.startdate:
            raise ValueError('Date of birth must be less than start date.')
