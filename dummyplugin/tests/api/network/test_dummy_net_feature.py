from tempest.api.network import base
from tempest import test


class DummyFeatureTestJSON(base.BaseNetworkTest):
    @test.attr(type='smoke')
    @test.idempotent_id('8e03f417-47e9-4470-beff-0814bfb867d3')
    def test_create_update_delete_one_dummy(self):
        self.assertEqual(2, 2)
