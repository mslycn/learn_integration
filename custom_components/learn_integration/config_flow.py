from homeassistant import config_entries
from.const import DOMAIN

class ExampleConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Example config flow."""
    # 它创建的条目的模式版本
    # 如果版本更改，Home Assistant将调用你的迁移方法
    VERSION = 1
    MINOR_VERSION = 1
