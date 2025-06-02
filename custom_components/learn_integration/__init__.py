# custom_components/learn_integration/__init__.py

"""
async_setup函数，这是Home Assistant集成的入口点。集成添加后，会执行该函数。这是一个异步的setup会被hass系统加载时调用。


async_setup 函数

集成的初始化入口，Home Assistant 启动时自动调用。

async_setup函数的作用是设置集成，注册实体或服务等。只创建了一个状态实体，，只是一个示例。

函数内部调用了hass.states.async_set来创建一个状态实体，实体ID是"learn_integration.world"，状态值为"hello word"。然后返回True表示初始化成功

参数​​：
hass: Home Assistant 核心对象，用于与系统交互。
config: 集成的配置数据


示例
Tuya-Local integration
在 Home Assistant 中作为自定义组件运行，其主要逻辑在 custom_components/localtuya/__init__.py 文件中。这个文件实现了 Home Assistant 的集成接口，负责初始化设备，管理设备状态以及接收和发送命令到 Tuya 设备。

当Home Assistant加载这个组件时，setup() 函数会被调用，用于设置组件并发现本地网络中的 Tuya 设备。同时，async_discover_devices() 可能被用来自动发现新设备，而 async_added_to_hass() 处理将组件添加到 Home Assistant 实例时的事件

                        
原文链接：https://blog.csdn.net/gitblog_00687/article/details/141208354


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

# 添加集成后，会执行该函数
async def async_setup_entry(hass, entry):
    # 在这里设置配置流
    return True

# 在前端删除集成配置时，会执行该函数
# 关闭HomeAssistant时，会执行该函数
async def async_unload_entry(hass, entry):
    # 卸载配置流
    return True


# https://juejin.cn/post/7260389344669843512


# https://developers.home-assistant.io/docs/creating_component_index#the-minimum
# https://blog.csdn.net/tre4321/article/details/144350503
# https://developers.home-assistant.io/blog/2024/10/31/core-config-moved/
