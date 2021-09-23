# Copyright 2019 Denis Mudarisov <https://it-projects.info/team/trojikman>
# License MIT (https://opensource.org/licenses/MIT).

from flectra.tests import HttpCase, tagged


@tagged("post_install", "at_install")
class TestUi(HttpCase):
    def test_open_url(self):
        self.browser_js(
            "/",
            "flectra.__DEBUG__.services['web_tour.tour'].run('website_login_background_check')",
            "flectra.__DEBUG__.services['web_tour.tour'].tours.website_login_background_check.ready",
            login=None,
        )
