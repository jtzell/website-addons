# Copyright 2018 Kolushov Alexandr <https://it-projects.info/team/KolushovAlexandr>
# License MIT (https://opensource.org/licenses/MIT).

import flectra.tests
from flectra.api import Environment


@flectra.tests.common.at_install(True)
@flectra.tests.common.post_install(True)
class TestBarcodePickingUi(flectra.tests.HttpCase):
    def test_stock_picking_barcode(self):

        # needed because tests are run before the module is marked as
        # installed. In js web will only load qweb coming from modules
        # that are returned by the backend in module_boot. Without
        # this you end up with js, css but no qweb.
        cr = self.registry.cursor()
        assert cr == self.registry.test_cr
        env = Environment(cr, self.uid, {})
        env["ir.module.module"].search(
            [("name", "=", "stock_picking_barcode")], limit=1
        ).state = "installed"
        cr.release()

        # without a delay there might be problems on the steps whilst opening a POS
        # caused by a not yet loaded button's action
        self.phantom_js(
            "/web",
            "flectra.__DEBUG__.services['web_tour.tour'].run('tour_stock_picking_barcode', 1000)",
            "flectra.__DEBUG__.services['web_tour.tour'].tours.tour_stock_picking_barcode.ready",
            login="admin",
        )
