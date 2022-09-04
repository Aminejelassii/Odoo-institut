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

    department_id = fields.Many2one('institut.department', string='Departement :')
    matiere_ids = fields.Many2many('institut.matiere', string='Subject :')
    classe_ids = fields.Many2many('institut.classe', string='Class :')

    @api.onchange('email')
    def validate_mail(self):
        if self.email:
            match = re.match('^([a-z0-9A-Z-]+)*@[a-z]+(\.[a-z]{2,4})$', self.email)
            if match == None:
                raise ValueError('Invalid E-mail')

    def name_get(self):
        result = []
        for professeur in self:
            nom = professeur.f_name
            result.append((professeur.id, nom))
            return result

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

    @api.constrains('birthday', 'startdate')
    def chek_date(self):
        if self.birthday > self.startdate:
            raise ValueError('Date of birth must be less than start date.')

# def send_mail(self):
#   self.ensure_one()
#  mail = self.env.ref("institut.model_institut_professeur").id
# ctx = {
#    'default_model': 'institut.professeur',
#    'default_res_id': self.id,
##   'default_use_mail': bool(mail),
# 'default_mail': mail,
# 'default_composition_mode': 'comment',
# 'email_to': self.email,

# }
# return {
#   'type': 'ir.actions.act_window',
#  'view_type': 'form',
# 'view_mode': 'form',
# 'res_model': 'mail.compose.message',
#   'target': 'new',
#  'context': ctx,
# }
