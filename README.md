openerp-message
==============

This module lets show notification window like osv.except_osv.

1. self.pool.get('ir.action.message').info(cr, uid, "Success", "Good news. It is works.")

2. self.pool.get('ir.action.message').warning(cr, uid, "Attention", "Good news. It is works.")

3. self.pool.get('ir.action.message').error(cr, uid, "Oops", "Access denied.")

System requirements:
------

OpenERP 6.1
