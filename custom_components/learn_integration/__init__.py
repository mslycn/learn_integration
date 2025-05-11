DOMAIN = "hello_state"

async def async_setup(hass, config):
    await hass.states.async_set("hello_state.world", "Paulus")
    # 返回布尔值以指示初始化成功
    return True
