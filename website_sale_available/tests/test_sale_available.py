# License MIT (https://opensource.org/licenses/MIT).
# Copyright 2017 Kolushov Alexandr <https://github.com/KolushovAlexandr>

import flectra.tests


@flectra.tests.common.at_install(True)
@flectra.tests.common.post_install(True)
class TestUi(flectra.tests.HttpCase):
    def test_sale_available(self):
        # delay is added to be sure that all elements have been rendered properly
        self.phantom_js(
            "/",
            "flectra.__DEBUG__.services['web_tour.tour'].run('shop_sale_available', 1000)",
            "flectra.__DEBUG__.services['web_tour.tour'].tours.shop_sale_available.ready",
            login="admin",
        )
