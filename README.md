## Project Information
local 

192.168.2.50 rpi

/data/homeassistant202405/custom_components/learn_integration

remote:https://github.com/mslycn/learn_integration

## step by step

创建一个名为“learn-integration”的Home Assistant自定义集成

首先，对于不熟悉Home Assistant集成的新手来说，可能不了解代码的结构。对各个部分的功能和它们如何协同工作不太清楚。不知道组件的执行流程，从哪个函数方法调用，配置的数据存储在哪里，怎么保存自己需要的数据

代码包括目录结构、manifest.json配置、init.py的核心代码，以及测试步骤等。


同步函数和异步函数（setup与async_setup）：直接学习异步函数
不带UI配置界面的集成和带UI配置界面的集成：直接学习带UI配置界面的集成


第一步：最小化集成
这是一个最简单的集成结构示例.
后面逐步添加更多功能，例如实体定义、配置流和国际化支持。





测试可以发现，代码调用顺序是：

ha->__init__.py->PLATFORMS中顺序调用async_setup


测试可以发现，代码调用顺序是：

Config_flow.py->__init__.py->PLATFORMS中顺序调用async_setup_entry


自定义集成的logo图标,设备图标,以及实体的图标都在哪里定义

## 对象
没有任何开发经验的开发者自己学习写集成

## 应用
有些硬件太小众了怎么自己写集成

mainfest.json

{
  "domain": "learn_integration",
  "name": "Learn Integration",
  "version": "v0.1.0",
  "codeowners": ["@mslycn"],
  "config_flow": true,
  "dependencies": [],
  "documentation": "https://github.com/mslycn/learn_integration/blob/main/README.m",
  "integration_type": "hub",
  "iot_class": "cloud_polling",
  "requirements": []
}


domain：集成的唯一标识符，用于在系统中识别和区分不同的集成。它是一个字符串值，必须是唯一的。
name：集成的名称，用于在用户界面中显示。它是一个字符串值，可以是本地化的名称。
documentation：集成的文档链接，可以指向集成的详细文档、说明或支持网页。它是一个URL字符串。
dependencies：集成所依赖的其他集成。它是一个字符串数组，列出了其他集成的domain，以表明当前集成需要这些其他集成才能正常运行。
codeowners：指定代码所有者的信息，用于在代码仓库中指定负责维护和审核集成代码的人员。它是一个字符串数组，包含GitHub用户名或电子邮件地址。
config_flow：指定集成是否包含配置流。配置流用于向用户提供配置选项，以便设置集成。它是一个布尔值，可以是true或false。

## Thanks
My heartfelt thanks to:
- [integration template](https://github.com/ludeeus/integration_blueprint) a template for HA integrations.




