from tempest.api.network import base
from tempest import config
from tempest import test

CONF = config.CONF


class DummyFeatureTestJSON(base.BaseNetworkTest):
    @test.attr(type='smoke')
    @test.idempotent_id('8e03f417-47e9-4470-beff-0814bfb867d3')
    def test_create_update_delete_one_dummy(self):
        if CONF.dummy_config_options.funny_cfg_option == 'funny':
            self.assertEqual(
                2, 2,
                'In the config there is {d_cfg}, so 2 equals with2.'.format(
                    d_cfg=CONF.dummy_config_options.funny_cfg_option))
        elif CONF.dummy_config_options.funny_cfg_option == 'not_funny':
            msg = 'In the config there is {d_cfg}, so 2 not equals with 3.'
            self.assertEqual(
                2, 3,
                msg.format(
                    d_cfg=CONF.dummy_config_options.funny_cfg_option))
        else:
            self.assertEqual(42, 42)
