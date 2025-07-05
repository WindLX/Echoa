#!/usr/bin/env python3
"""
Echoa 使用示例
展示如何创建独立的控制台实例，避免项目间冲突
"""

from rich.console import Console
from echoa import Echoa, create_echoa, info, debug, warning, error, success


def example_1_basic_usage():
    """示例 1: 基本使用方式"""
    print("=== 示例 1: 基本使用 ===")

    # 使用默认全局实例（向后兼容）
    info("这是一条信息消息")
    debug("这是一条调试消息")
    warning("这是一条警告消息")
    error("这是一条错误消息")
    success("这是一条成功消息")


def example_2_independent_instances():
    """示例 2: 创建独立的实例"""
    print("\n=== 示例 2: 独立实例 ===")

    # 项目 A 的控制台
    project_a_console = create_echoa(prefix="[ProjectA]")
    project_a_console.info("项目 A 的信息")
    project_a_console.success("项目 A 执行成功")

    # 项目 B 的控制台
    project_b_console = create_echoa(prefix="[ProjectB]")
    project_b_console.info("项目 B 的信息")
    project_b_console.warning("项目 B 有警告")

    # 两个实例完全独立，不会相互影响


def example_3_custom_console():
    """示例 3: 使用自定义 Rich Console"""
    print("\n=== 示例 3: 自定义控制台 ===")

    # 创建自定义的 Rich Console
    custom_console = Console(width=80, force_terminal=True)

    # 使用自定义控制台创建 Echoa 实例
    custom_echoa = create_echoa(console=custom_console, prefix="[Custom]")

    custom_echoa.panel("这是使用自定义控制台的面板消息", "自定义面板", "green")
    custom_echoa.rule("自定义分隔线", "magenta")


def example_4_inheritance():
    """示例 4: 继承 Echoa 创建特定功能"""
    print("\n=== 示例 4: 继承扩展 ===")

    class DatabaseEchoa(Echoa):
        """数据库相关的日志管理器"""

        def __init__(self, db_name: str, **kwargs):
            super().__init__(prefix=f"[DB:{db_name}]", **kwargs)
            self.db_name = db_name

        def query_log(self, sql: str, duration: float):
            """记录数据库查询"""
            self.debug(f"SQL: {sql} | Duration: {duration:.2f}ms")

        def connection_log(self, action: str):
            """记录连接状态"""
            if action == "connect":
                self.success(f"已连接到数据库 {self.db_name}")
            elif action == "disconnect":
                self.info(f"已断开数据库 {self.db_name} 连接")

    # 创建数据库日志实例
    db_logger = DatabaseEchoa("user_db")
    db_logger.connection_log("connect")
    db_logger.query_log("SELECT * FROM users WHERE id = ?", 15.6)
    db_logger.connection_log("disconnect")


def example_5_multiple_projects():
    """示例 5: 模拟多个项目使用场景"""
    print("\n=== 示例 5: 多项目场景 ===")

    # 模拟 Web 服务器项目
    class WebServerEchoa(Echoa):
        def __init__(self, server_name: str):
            super().__init__(prefix=f"[{server_name}]")

        def request_log(self, method: str, path: str, status: int):
            if status < 400:
                self.info(f"{method} {path} - {status}")
            else:
                self.error(f"{method} {path} - {status}")

    # 模拟数据处理项目
    class DataProcessorEchoa(Echoa):
        def __init__(self, processor_name: str):
            super().__init__(prefix=f"[{processor_name}]")

        def process_log(self, task: str, progress: int):
            self.info(f"{task} - {progress}% 完成")

    # 创建不同项目的实例
    web_server = WebServerEchoa("WebAPI")
    data_processor = DataProcessorEchoa("DataETL")

    # 各自独立工作，不会冲突
    web_server.request_log("GET", "/api/users", 200)
    data_processor.process_log("处理用户数据", 45)
    web_server.request_log("POST", "/api/login", 401)
    data_processor.process_log("清洗数据", 80)


def example_6_enable_disable():
    """示例 6: 启用/禁用功能"""
    print("\n=== 示例 6: 启用/禁用 ===")

    # 创建一个实例
    test_echoa = create_echoa(prefix="[Test]")

    test_echoa.info("这条消息会显示")

    # 禁用输出
    test_echoa.set_enabled(False)
    test_echoa.info("这条消息不会显示")

    # 重新启用
    test_echoa.set_enabled(True)
    test_echoa.info("这条消息又会显示了")


if __name__ == "__main__":
    example_1_basic_usage()
    example_2_independent_instances()
    example_3_custom_console()
    example_4_inheritance()
    example_5_multiple_projects()
    example_6_enable_disable()
