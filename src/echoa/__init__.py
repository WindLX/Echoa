from typing import Any

from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.rule import Rule


class Echoa:
    """
    基于 Rich 的 Echoa 控制台输出管理器
    支持创建独立的实例，避免不同项目间的冲突
    """

    def __init__(
        self,
        console: Console | None = None,
        prefix: str = "[Echoa]",
        enabled: bool = True,
    ) -> None:
        """
        初始化 Echoa 实例

        Args:
            console: Rich Console 实例，None 使用默认控制台
            prefix: 输出前缀
            enabled: 是否启用输出
        """
        self._console = console or Console()
        self._prefix = prefix
        self._enabled = enabled

    def set_console(
        self, console: Console | None = None, prefix: str | None = None
    ) -> None:
        """
        设置控制台实例和前缀

        Args:
            console: Rich Console 实例，None 保持当前控制台
            prefix: 输出前缀，None 保持当前前缀
        """
        if console is not None:
            self._console = console
        if prefix is not None:
            self._prefix = prefix

    def get_console(self) -> Console:
        """
        获取控制台实例

        Returns:
            Console: Rich Console 实例
        """
        return self._console

    def set_enabled(self, enabled: bool) -> None:
        """
        启用或禁用输出

        Args:
            enabled: 是否启用输出
        """
        self._enabled = enabled

    def is_enabled(self) -> bool:
        """
        检查是否启用输出

        Returns:
            bool: 是否启用
        """
        return self._enabled

    def set_prefix(self, prefix: str) -> None:
        """
        设置输出前缀

        Args:
            prefix: 新的输出前缀
        """
        self._prefix = prefix

    def get_prefix(self) -> str:
        """
        获取当前输出前缀

        Returns:
            str: 当前前缀
        """
        return self._prefix

    def info(self, message: str, **kwargs: Any) -> None:
        """
        输出信息消息

        Args:
            message: 消息内容
            **kwargs: 额外参数
        """
        if not self._enabled:
            return
        console = self.get_console()
        text = Text(f"{self._prefix} ", style="blue bold")
        text.append(message, style="white")
        console.print(text, **kwargs)

    def debug(self, message: str, **kwargs: Any) -> None:
        """
        输出调试消息

        Args:
            message: 消息内容
            **kwargs: 额外参数
        """
        if not self._enabled:
            return
        console = self.get_console()
        text = Text(f"{self._prefix} ", style="dim blue")
        text.append(f"[DEBUG] {message}", style="dim white")
        console.print(text, **kwargs)

    def warning(self, message: str, **kwargs: Any) -> None:
        """
        输出警告消息

        Args:
            message: 消息内容
            **kwargs: 额外参数
        """
        if not self._enabled:
            return
        console = self.get_console()
        text = Text(f"{self._prefix} ", style="yellow bold")
        text.append(f"⚠️  {message}", style="yellow")
        console.print(text, **kwargs)

    def error(self, message: str, **kwargs: Any) -> None:
        """
        输出错误消息

        Args:
            message: 消息内容
            **kwargs: 额外参数
        """
        if not self._enabled:
            return
        console = self.get_console()
        text = Text(f"{self._prefix} ", style="red bold")
        text.append(f"❌ {message}", style="red")
        console.print(text, **kwargs)

    def success(self, message: str, **kwargs: Any) -> None:
        """
        输出成功消息

        Args:
            message: 消息内容
            **kwargs: 额外参数
        """
        if not self._enabled:
            return
        console = self.get_console()
        text = Text(f"{self._prefix} ", style="green bold")
        text.append(f"✅ {message}", style="green")
        console.print(text, **kwargs)

    def panel(
        self, message: str, title: str = "", style: str = "blue", **kwargs: Any
    ) -> None:
        """
        输出面板消息

        Args:
            message: 消息内容
            title: 面板标题
            style: 面板样式
            **kwargs: 额外参数
        """
        if not self._enabled:
            return
        console = self.get_console()
        panel = Panel(message, title=title or self._prefix, border_style=style)
        console.print(panel, **kwargs)

    def rule(self, title: str = "", style: str = "blue", **kwargs: Any) -> None:
        """
        输出分隔线

        Args:
            title: 分隔线标题
            style: 样式
            **kwargs: 额外参数
        """
        if not self._enabled:
            return
        console = self.get_console()
        rule = Rule(title, style=style)
        console.print(rule, **kwargs)


# 提供一个默认的全局实例，保持向后兼容
_default_echoa = Echoa()


def create_echoa(
    console: Console | None = None, prefix: str = "[Echoa]", enabled: bool = True
) -> Echoa:
    """
    创建一个新的 Echoa 实例

    Args:
        console: Rich Console 实例，None 使用默认控制台
        prefix: 输出前缀
        enabled: 是否启用输出

    Returns:
        Echoa: 新的 Echoa 实例
    """
    return Echoa(console=console, prefix=prefix, enabled=enabled)


def set_echoa(console: Console | None = None, prefix: str = "[Echoa]") -> None:
    """
    设置默认 Echoa 控制台输出配置（向后兼容）

    Args:
        console: Rich Console 实例，None 使用默认控制台
        prefix: 输出前缀
    """
    _default_echoa.set_console(console, prefix)


def get_echoa() -> Echoa:
    """
    获取默认的 Echoa 控制台管理器实例（向后兼容）

    Returns:
        Echoa: 默认控制台管理器实例
    """
    return _default_echoa


def enable_echoa_output(enabled: bool = True) -> None:
    """
    启用或禁用默认 Echoa 输出（向后兼容）

    Args:
        enabled: 是否启用输出
    """
    _default_echoa.set_enabled(enabled)


# 为了向后兼容，提供默认实例的快捷方式
def info(message: str, **kwargs: Any) -> None:
    """使用默认实例输出信息消息"""
    _default_echoa.info(message, **kwargs)


def debug(message: str, **kwargs: Any) -> None:
    """使用默认实例输出调试消息"""
    _default_echoa.debug(message, **kwargs)


def warning(message: str, **kwargs: Any) -> None:
    """使用默认实例输出警告消息"""
    _default_echoa.warning(message, **kwargs)


def error(message: str, **kwargs: Any) -> None:
    """使用默认实例输出错误消息"""
    _default_echoa.error(message, **kwargs)


def success(message: str, **kwargs: Any) -> None:
    """使用默认实例输出成功消息"""
    _default_echoa.success(message, **kwargs)


def panel(message: str, title: str = "", style: str = "blue", **kwargs: Any) -> None:
    """使用默认实例输出面板消息"""
    _default_echoa.panel(message, title, style, **kwargs)


def rule(title: str = "", style: str = "blue", **kwargs: Any) -> None:
    """使用默认实例输出分隔线"""
    _default_echoa.rule(title, style, **kwargs)
