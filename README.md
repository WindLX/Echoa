# Echoa

Echoa 是一个基于 [Rich](https://github.com/Textualize/rich) 的 Python 控制台输出管理器，提供统一、优雅的日志与消息输出接口。支持创建独立的实例，避免不同项目间的冲突。

## 特性

- 🎨 基于 Rich 的美观输出
- 🔄 支持多个独立实例，避免项目冲突
- 🎯 可继承扩展，实现特定功能
- 📝 完整的类型支持
- 🔧 灵活的配置选项

## 安装

```bash
pip install echoa

uv add echoa
```

## 基本使用

### 1. 使用默认全局实例（向后兼容）

```python
from echoa import info, debug, warning, error, success

info("普通信息")
debug("调试信息")
warning("警告信息")
error("错误信息")
success("成功信息")
```

### 2. 创建独立实例（推荐）

```python
from echoa import create_echoa

# 创建项目专用的控制台实例
app_console = create_echoa(prefix="[MyApp]")
app_console.info("应用启动成功")
app_console.warning("配置文件不存在，使用默认配置")

# 创建另一个独立实例
db_console = create_echoa(prefix="[Database]")
db_console.success("数据库连接成功")
db_console.error("查询超时")
```

### 3. 自定义 Rich Console

```python
from rich.console import Console
from echoa import create_echoa

# 使用自定义 Rich Console
custom_console = Console(width=120, force_terminal=True)
echoa = create_echoa(console=custom_console, prefix="[Custom]")

echoa.panel("这是面板内容", title="自定义面板", style="green")
echoa.rule("分隔线", style="magenta")
```

## 高级用法

### 继承扩展

```python
from echoa import Echoa

class DatabaseLogger(Echoa):
    """数据库专用日志管理器"""
    
    def __init__(self, db_name: str):
        super().__init__(prefix=f"[DB:{db_name}]")
        self.db_name = db_name
    
    def query_log(self, sql: str, duration: float):
        """记录查询日志"""
        self.debug(f"SQL: {sql} | Duration: {duration:.2f}ms")
    
    def connection_log(self, connected: bool):
        """记录连接状态"""
        if connected:
            self.success(f"已连接到数据库 {self.db_name}")
        else:
            self.info(f"已断开数据库 {self.db_name} 连接")

# 使用
db_logger = DatabaseLogger("user_db")
db_logger.connection_log(True)
db_logger.query_log("SELECT * FROM users", 15.6)
```

### 多项目场景

```python
from echoa import create_echoa

# 不同项目使用独立实例，互不冲突
web_api = create_echoa(prefix="[WebAPI]") 
data_processor = create_echoa(prefix="[DataETL]")
cache_service = create_echoa(prefix="[Cache]")

# 各自独立工作
web_api.info("API 服务启动")
data_processor.info("开始处理数据")
cache_service.info("缓存清理完成")
```

## API 参考

### Echoa 类

#### 构造函数
```python
def __init__(
    self,
    console: Console | None = None,
    prefix: str = "[Echoa]",
    enabled: bool = True
) -> None
```

#### 实例方法

- `set_console(console: Console | None = None, prefix: str | None = None)`  
  设置 Rich 控制台实例和输出前缀
- `get_console() -> Console`  
  获取当前控制台实例
- `set_enabled(enabled: bool)`  
  启用或禁用所有输出
- `is_enabled() -> bool`  
  检查当前输出是否启用
- `set_prefix(prefix: str)`  
  设置输出前缀
- `get_prefix() -> str`  
  获取当前输出前缀
- `info(message: str, **kwargs)`  
  输出普通信息（蓝色）
- `debug(message: str, **kwargs)`  
  输出调试信息（灰蓝色）
- `warning(message: str, **kwargs)`  
  输出警告信息（黄色）
- `error(message: str, **kwargs)`  
  输出错误信息（红色）
- `success(message: str, **kwargs)`  
  输出成功信息（绿色）
- `panel(message: str, title: str = "", style: str = "blue", **kwargs)`  
  输出带边框的面板
- `rule(title: str = "", style: str = "blue", **kwargs)`  
  输出分隔线

### 便捷函数

#### 创建实例
```python
def create_echoa(
    console: Console | None = None,
    prefix: str = "[Echoa]",
    enabled: bool = True
) -> Echoa
```

#### 默认全局实例（向后兼容）
- `set_echoa(console: Console | None = None, prefix: str = "[Echoa]")`  
  设置默认实例的控制台配置
- `get_echoa() -> Echoa`  
  获取默认实例
- `enable_echoa_output(enabled: bool = True)`  
  启用或禁用默认实例的输出

#### 默认实例快捷方式
```python
# 这些函数使用默认全局实例
info(message: str, **kwargs)
debug(message: str, **kwargs)
warning(message: str, **kwargs)
error(message: str, **kwargs)
success(message: str, **kwargs)
panel(message: str, title: str = "", style: str = "blue", **kwargs)
rule(title: str = "", style: str = "blue", **kwargs)
```

## 最佳实践

1. **为每个项目创建独立实例**，避免全局状态冲突
2. **使用继承扩展功能**，实现项目特定的日志需求
3. **合理设置前缀**，便于识别不同模块的输出
4. **在生产环境中禁用调试输出**，提高性能

## 依赖
- [rich](https://github.com/Textualize/rich)

## 协议
Echoa 遵循 MIT 协议，详见 LICENSE 文件。
