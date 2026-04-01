#!/usr/bin/env python3
"""
测试数据库连通性
"""

import socket
import subprocess
import sys

def test_tcp_connection(host, port, timeout=5):
    """测试TCP端口连通性"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return result == 0
    except Exception as e:
        return False

def test_ping(host):
    """测试ping连通性"""
    try:
        result = subprocess.run(
            ['ping', '-c', '3', '-W', '2', host],
            capture_output=True,
            text=True,
            timeout=10
        )
        return result.returncode == 0
    except:
        return False

def test_mysql_connection(host, port, user, password, database):
    """测试MySQL连接"""
    try:
        import pymysql
        conn = pymysql.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
            connect_timeout=5
        )
        conn.close()
        return True
    except ImportError:
        return None  # pymysql未安装
    except Exception as e:
        return False

def main():
    print("=" * 80)
    print("数据库连通性测试")
    print("=" * 80)
    
    # 测试目标
    DB_HOST = '10.65.69.253'
    DB_PORT = 3306
    
    print(f"\n目标数据库: {DB_HOST}:{DB_PORT}")
    print("-" * 80)
    
    # 1. 测试ping
    print("\n【1. Ping测试】")
    print(f"   命令: ping -c 3 {DB_HOST}")
    ping_result = test_ping(DB_HOST)
    if ping_result:
        print(f"   结果: ✅ 可达")
    else:
        print(f"   结果: ❌ 不可达（网络不通或主机禁用ping）")
    
    # 2. 测试TCP端口
    print("\n【2. TCP端口测试】")
    print(f"   目标: {DB_HOST}:{DB_PORT}")
    tcp_result = test_tcp_connection(DB_HOST, DB_PORT)
    if tcp_result:
        print(f"   结果: ✅ 端口开放")
    else:
        print(f"   结果: ❌ 端口不可达（网络隔离或防火墙阻挡）")
    
    # 3. 测试MySQL连接（如果有凭据）
    print("\n【3. MySQL连接测试】")
    print(f"   注意: 需要有效的数据库凭据")
    
    # 检查pymysql
    try:
        import pymysql
        print(f"   PyMySQL: ✅ 已安装")
    except ImportError:
        print(f"   PyMySQL: ❌ 未安装 (pip install pymysql)")
        print("\n" + "=" * 80)
        print("测试完成")
        print("=" * 80)
        return
    
    # 尝试使用sjht_financial.py中的配置
    DB_CONFIG = {
        'host': DB_HOST,
        'port': DB_PORT,
        'user': 'ro_ciawind_yanjiuzu@tn_pro_ciawind#cl_p_ob4_sj',
        'password': 'Ro_Ci09a_Y6jz',
        'database': 'gildata'
    }
    
    print(f"   尝试连接...")
    mysql_result = test_mysql_connection(
        DB_CONFIG['host'],
        DB_CONFIG['port'],
        DB_CONFIG['user'],
        DB_CONFIG['password'],
        DB_CONFIG['database']
    )
    
    if mysql_result is None:
        print(f"   结果: ⚠️  跳过（PyMySQL未安装）")
    elif mysql_result:
        print(f"   结果: ✅ 连接成功")
    else:
        print(f"   结果: ❌ 连接失败")
        print(f"\n   可能原因:")
        print(f"   - 网络隔离（当前环境无法访问内网）")
        print(f"   - 防火墙阻挡")
        print(f"   - 数据库服务未运行")
        print(f"   - 凭据过期或无效")
    
    # 4. 网络环境信息
    print("\n【4. 网络环境信息】")
    try:
        # 获取本机IP
        hostname = socket.gethostname()
        local_ip = socket.getaddrinfo(hostname, None)[0][4][0]
        print(f"   主机名: {hostname}")
        print(f"   本机IP: {local_ip}")
    except:
        print(f"   本机IP: 获取失败")
    
    # 测试外网连通性
    print(f"\n   外网连通性测试:")
    external_hosts = [
        ('baidu.com', 80),
        ('eastmoney.com', 443),
    ]
    for host, port in external_hosts:
        result = test_tcp_connection(host, port, timeout=3)
        status = "✅" if result else "❌"
        print(f"   {status} {host}:{port}")
    
    # 总结
    print("\n" + "=" * 80)
    print("测试总结")
    print("=" * 80)
    print(f"\n目标数据库 {DB_HOST}:{DB_PORT}")
    print(f"  - Ping:      {'✅ 可达' if ping_result else '❌ 不可达'}")
    print(f"  - TCP端口:   {'✅ 开放' if tcp_result else '❌ 不可达'}")
    print(f"  - MySQL:     {'✅ 成功' if mysql_result else '❌ 失败' if mysql_result is not None else '⚠️  跳过'}")
    
    if not tcp_result:
        print(f"\n❌ 结论: 当前环境无法访问目标数据库")
        print(f"   建议: 使用网络版脚本(sjht_financial_web.py)或配置VPN/代理")
    else:
        print(f"\n✅ 结论: 网络层可达，请检查MySQL凭据")
    
    print("\n" + "=" * 80)

if __name__ == "__main__":
    main()
