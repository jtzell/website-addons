import flectra.tests


@flectra.tests.common.at_install(True)
@flectra.tests.common.post_install(True)
class TestUi(flectra.tests.HttpCase):
    def test_search_tags(self):
        # delay is added to be sure that all elements have been rendered properly
        self.phantom_js(
            "/",
            "flectra.__DEBUG__.services['web_tour.tour'].run('website_sale_search_tags', 500)",
            "flectra.__DEBUG__.services['web_tour.tour'].tours.website_sale_search_tags.ready",
            login="admin",
        )


@flectra.tests.common.at_install(True)
@flectra.tests.common.post_install(True)
class TestModels(flectra.tests.SingleTransactionCase):
    def test_extend_domain(self):
        before = [
            "|",
            ("company_id", "=", 1),
            ("company_id", "=", False),
            "&",
            ("sale_ok", "=", True),
            ("event_ok", "=", False),
            "|",
            "|",
            "|",
            ("name", "ilike", u"iMac"),
            ("description", "ilike", u"iMac"),
            ("description_sale", "ilike", u"iMac"),
            ("product_variant_ids.default_code", "ilike", u"iMac"),
        ]

        expected_after = [
            "|",
            ("company_id", "=", 1),
            ("company_id", "=", False),
            "&",
            ("sale_ok", "=", True),
            ("event_ok", "=", False),
            "|",
            # this is added after _extend_domain
            ("tag_ids", "ilike", u"Example"),
            "|",
            "|",
            "|",
            ("name", "ilike", u"iMac"),
            ("description", "ilike", u"iMac"),
            ("description_sale", "ilike", u"iMac"),
            ("product_variant_ids.default_code", "ilike", u"iMac"),
        ]

        p = self.env["product.template"].create({"name": "test"})
        p.env.context = {"search_tags": u"Example"}
        self.assertEqual(p._extend_domain(before), expected_after)
