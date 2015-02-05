from osv import osv, fields

class stock_picking_prisme(osv.osv):
    _name = "stock.picking"
    _inherit = "stock.picking"
    
    _columns = {
        "psi_transporter": fields.char("Transporter", 255),
    }
      
stock_picking_prisme()
