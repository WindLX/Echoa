from typing import Any

from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.rule import Rule


class Echoa:
    """
    基于 Rich 的 Echoa 控制台输出管理器
    """

    _console: Console | None = None
    _enabled: bool = True
    _prefix: str = "[Echoa]"

    @classmethod
    def set_console(
        cls, console: Console | None = None, prefix: str = "[Echoa]"
    ) -> None:
        """
        设置控制台实例和前缀

        Args:
            console: Rich Console 实例，None 使用默认控制台
            prefix: 输出前缀
        """
        cls._console = console or Console()
        cls._prefix = prefix

    @classmethod
    def get_console(cls) -> Console:
        """
        获取控制台实例

        Returns:
            Console: Rich Console 实例
        """
        if cls._console is None:
            cls._console = Console()
        return cls._console

    @classmethod
    def set_enabled(cls, enabled: bool) -> None:
        """
        启用或禁用输出

        Args:
            enabled: 是否启用输出
        """
        cls._enabled = enabled

    @classmethod
    def is_enabled(cls) -> bool:
        """
        检查是否启用输出

        Returns:
            bool: 是否启用
        """
        return cls._enabled

    @classmethod
    def info(cls, message: str, **kwargs: Any) -> None:
        """
        输出信息消息

        Args:
            message: 消息内容
            **kwargs: 额外参数
        """
        if not cls._enabled:
            return
        console = cls.get_console()
        text = Text(f"{cls._prefix} ", style="blue bold")
        text.append(message, style="white")
        console.print(text, **kwargs)

    @classmethod
    def debug(cls, message: str, **kwargs: Any) -> None:
        """
        输出调试消息

        Args:
            message: 消息内容
            **kwargs: 额外参数
        """
        if not cls._enabled:
            return
        console = cls.get_console()
        text = Text(f"{cls._prefix} ", style="dim blue")
        text.append(f"[DEBUG] {message}", style="dim white")
        console.print(text, **kwargs)

    @classmethod
    def warning(cls, message: str, **kwargs: Any) -> None:
        """
        输出警告消息

        Args:
            message: 消息内容
            **kwargs: 额外参数
        """
        if not cls._enabled:
            return
        console = cls.get_console()
        text = Text(f"{cls._prefix} ", style="yellow bold")
        text.append(f"⚠️  {message}", style="yellow")
        console.print(text, **kwargs)

    @classmethod
    def error(cls, message: str, **kwargs: Any) -> None:
        """
        输出错误消息

        Args:
            message: 消息内容
            **kwargs: 额外参数
        """
        if not cls._enabled:
            return
        console = cls.get_console()
        text = Text(f"{cls._prefix} ", style="red bold")
        text.append(f"❌ {message}", style="red")
        console.print(text, **kwargs)

    @classmethod
    def success(cls, message: str, **kwargs: Any) -> None:
        """
        输出成功消息

        Args:
            message: 消息内容
            **kwargs: 额外参数
        """
        if not cls._enabled:
            return
        console = cls.get_console()
        text = Text(f"{cls._prefix} ", style="green bold")
        text.append(f"✅ {message}", style="green")
        console.print(text, **kwargs)

    @classmethod
    def panel(
        cls, message: str, title: str = "", style: str = "blue", **kwargs: Any
    ) -> None:
        """
        输出面板消息

        Args:
            message: 消息内容
            title: 面板标题
            style: 面板样式
            **kwargs: 额外参数
        """
        if not cls._enabled:
            return
        console = cls.get_console()
        panel = Panel(message, title=title or cls._prefix, border_style=style)
        console.print(panel, **kwargs)

    @classmethod
    def rule(cls, title: str = "", style: str = "blue", **kwargs: Any) -> None:
        """
        输出分隔线

        Args:
            title: 分隔线标题
            style: 样式
            **kwargs: 额外参数
        """
        if not cls._enabled:
            return
        console = cls.get_console()
        rule = Rule(title, style=style)
        console.print(rule, **kwargs)


def set_echoa(console: Console | None = None, prefix: str = "[Echoa]") -> None:
    """
    设置 Echoa 控制台输出配置

    Args:
        console: Rich Console 实例，None 使用默认控制台
        prefix: 输出前缀
    """
    Echoa.set_console(console, prefix)


def get_echoa() -> type[Echoa]:
    """
    获取 Echoa 控制台管理器类

    Returns:
        type[EchoaConsole]: 控制台管理器类
    """
    return Echoa


def enable_echoa_output(enabled: bool = True) -> None:
    """
    启用或禁用 Echoa 输出

    Args:
        enabled: 是否启用输出
    """
    Echoa.set_enabled(enabled)
