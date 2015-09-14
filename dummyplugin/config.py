from __future__ import print_function

from oslo_config import cfg

from tempest import config  # noqa

dummy_cfg_group = cfg.OptGroup(
    name="dummy_config_options",
    title="Extra tempest cfg options for a dummy plugin")
DummyCfgGroup = [
    cfg.StrOpt('funny_cfg_option',
               default="apple",
               help="The first funny cfg option.")]
