# custom_components/learn_integration/__init__.py

"""
async_setup函数，这是Home Assistant集成的入口点。


async_setup 函数

集成的初始化入口，Home Assistant 启动时自动调用。

async_setup函数的作用是设置集成，注册实体或服务等。只创建了一个状态实体，，只是一个示例。

函数内部调用了hass.states.async_set来创建一个状态实体，实体ID是"learn_integration.world"，状态值为"hello word"。然后返回True表示初始化成功

参数​​：
hass: Home Assistant 核心对象，用于与系统交互。
config: 集成的配置数据（


"""


import asyncio


DOMAIN = "learn_integration"   
# DOMAIN的定义，每个集成只有一个DOMAIN，"learn_integration"。

async def async_setup(hass, config):
    hass.states.async_set("learn_integration.world", "hello word")
    # 在 Home Assistant 状态机中创建一个实体，实体 ID 为 learn_integration.world，状态值为 "hello word"，字符串 "hello word"，可替换为数值、布尔值或其他类型。。
 
    # Return boolean to indicate that initialization was successful.
    # 返回 True 表示集成初始化成功；若返回 False，Home Assistant 会记录错误。
    return True

# https://developers.home-assistant.io/docs/creating_component_index#the-minimum
# https://blog.csdn.net/tre4321/article/details/144350503
