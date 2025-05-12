# custom_components/learn_integration/__init__.py

import asyncio


DOMAIN = "learn_integration"

async def async_setup(hass, config):
    hass.states.async_set("learn_integration.world", "hello word")
    # Return boolean to indicate that initialization was successful.
    # 返回布尔值以指示初始化成功
    return True

# https://developers.home-assistant.io/docs/creating_component_index#the-minimum
# https://blog.csdn.net/tre4321/article/details/144350503
