import os

from tempest import config
from tempest.test_discover import plugins

import config as d_config


class DummyTempestPlugin(plugins.TempestPlugin):
    def load_tests(self):
        base_path = os.path.split(os.path.dirname(
            os.path.abspath(__file__)))[0]
        test_dir = "dummyplugin/tests"
        full_test_dir = os.path.join(base_path, test_dir)
        return full_test_dir, base_path

    def register_opts(self, conf):
        config.register_opt_group(
            conf, d_config.dummy_cfg_group,
            d_config.DummyCfgGroup)

    def get_opt_lists(self):
        return [(d_config.dummy_cfg_group.funny_cfg_option,
                d_config.DummyCfgGroup)]
