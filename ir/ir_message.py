#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################################################
#
#    Shpionus
#    Copyright (C) 2013
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from osv import fields, osv
from tools.translate import _
from openerp import SUPERUSER_ID


_type = [
    ('warning', 'Warning'),
    ('info', 'Information'),
    ('error', 'Error'),
    ]


class action_message(osv.osv_memory):
    _name = "ir.action.message"
    _table = "ir_act_message"

    _columns = {
        'title': fields.char('Title', size=256, required=True, ),
        'message': fields.text('Message', ),
        'type': fields.selection(_type, 'Type', ),
    }

    _defaults = {
        'type': 'warning',
    }

    _req_name = 'title'

    def _get_view_id(self, cr, uid):
        res = self.pool.get('ir.model.data').get_object_reference(cr, SUPERUSER_ID,
            'openerp-message', 'view_ir_act_message_form')
        if res:
            return res[1]
        else:
            return False

    def notify(self, cr, uid, id, context):
        message = self.browse(cr, SUPERUSER_ID, id)

        message_type = "message"
        for t in _type:
            if t and t[0] == message.type:
                message_type = t[1]
                break

        res = {
            'name': '%s: %s' % (_(message_type), _(message.title)),
            'vie_type': 'form',
            'view_mode': 'form',
            'view_id': self._get_view_id(cr, uid),
            'res_model': 'ir.action.message',
            'domain': [],
            'context': context,
            'type': 'ir.actions.act_window',
            'target': 'new',
            'res_id': message.id
        }
        return res

    def warning(self, cr, uid, title, message, context=None):
        id = self.create(cr, SUPERUSER_ID, {'title': title, 'message': message, 'type': 'warning'})
        res = self.notify(cr, SUPERUSER_ID, id, context)
        return res

    def info(self, cr, uid, title, message, context=None):
        id = self.create(cr, SUPERUSER_ID, {'title': title, 'message': message, 'type': 'info'})
        res = self.notify(cr, SUPERUSER_ID, id, context)
        return res

    def error(self, cr, uid, title, message, context=None):
        id = self.create(cr, SUPERUSER_ID, {'title': title, 'message': message, 'type': 'error'})
        res = self.notify(cr, SUPERUSER_ID, id, context)
        return res

action_message()
