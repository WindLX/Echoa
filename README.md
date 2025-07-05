# Echoa

Echoa 是一个基于 [Rich](https://github.com/Textualize/rich) 的 Python 控制台输出管理器，提供统一、优雅的日志与消息输出接口。

## 安装

```bash
pip install echoa

uv add echoa
```

## 快速开始

```python
from echoa import Echoa, set_echoa, enable_echoa_output

# 可选：自定义控制台和前缀
set_echoa(prefix="[MyApp]")

Echoa.info("普通信息")
Echoa.debug("调试信息")
Echoa.warning("警告信息")
Echoa.error("错误信息")
Echoa.success("成功信息")
Echoa.panel("面板内容", title="面板标题")
Echoa.rule("分隔线")

# 启用/禁用输出
enable_echoa_output(False)
Echoa.info("这条不会被输出")
```

## API 协议说明

### Echoa 类方法

- `set_console(console: Console | None = None, prefix: str = "[Echoa]")`  
  设置 Rich 控制台实例和输出前缀。
- `get_console() -> Console`  
  获取当前控制台实例。
- `set_enabled(enabled: bool)`  
  启用或禁用所有输出。
- `is_enabled() -> bool`  
  检查当前输出是否启用。
- `info(message: str, **kwargs)`  
  输出普通信息（蓝色）。
- `debug(message: str, **kwargs)`  
  输出调试信息（灰蓝色）。
- `warning(message: str, **kwargs)`  
  输出警告信息（黄色）。
- `error(message: str, **kwargs)`  
  输出错误信息（红色）。
- `success(message: str, **kwargs)`  
  输出成功信息（绿色）。
- `panel(message: str, title: str = "", style: str = "blue", **kwargs)`  
  输出带边框的面板。
- `rule(title: str = "", style: str = "blue", **kwargs)`  
  输出分隔线。

### 辅助函数

- `set_echoa(console: Console | None = None, prefix: str = "[Echoa]")`  
  设置 Echoa 控制台输出配置。
- `get_echoa() -> type[Echoa]`  
  获取 Echoa 控制台管理器类。
- `enable_echoa_output(enabled: bool = True)`  
  启用或禁用 Echoa 输出。

## 依赖
- [rich](https://github.com/Textualize/rich)

## 协议
Echoa 遵循 MIT 协议，详见 LICENSE 文件。
