#!/usr/bin/env python3
"""
火山云AI配图生成脚本
使用豆包Seedream 5.0模型生成专业金融/商业配图
支持单图生成和批量生成
"""

import os
import sys
import argparse
import json
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse
import urllib.request
import time


def get_size_param(size_str):
    """转换尺寸参数"""
    # 注意: 火山云API要求图片至少 3,686,400 像素 (约 1920x1920)
    # 所以所有默认尺寸都必须满足此最低要求
    size_map = {
        "16:9": "2560x1440",   # 3,686,400 — 满足最低要求
        "1:1": "1920x1920",    # 3,686,400 — 满足最低要求
        "9:16": "1440x2560",   # 3,686,400 — 满足最低要求
        "4:3": "2240x1680",    # 3,763,200 — 满足最低要求
        "2K": "2560x1440",
        "4K": "3840x2160",
    }
    return size_map.get(size_str, size_str)


def optimize_prompt_for_finance(topic, style="写实"):
    """针对金融/商业内容优化prompt"""
    
    # 金融视觉风格词库
    finance_keywords = {
        "科技": ["数据流", "神经网络", "代码矩阵", "数字光效", "科技感"],
        "商务": ["几何空间", "建筑线条", "现代都市", "专业商务", "精英感"],
        "数据": ["图表可视化", "K线图", "数据曲线", "信息图表", "仪表盘"],
        "投资": ["上升趋势", "金色光芒", "财富象征", "增长曲线", "机遇之光"],
        "全球": ["世界地图", "连接线", "全球网络", "国际化", "地球视角"],
    }
    
    # 基础专业渲染参数
    render_params = (
        "oc渲染，光线追踪，景深，超现实主义，"
        "细腻的丰富的色彩层次，质感真实，"
        "光影效果营造出氛围，广角透视效果，极致的光影"
    )
    
    # 根据主题选择配色
    if any(word in topic for word in ["科技", "AI", "数字", "智能", "量化"]):
        color_scheme = "深蓝主调，青色光效，霓虹点缀"
        category = "科技"
    elif any(word in topic for word in ["投资", "增长", "收益", "财富", "成功"]):
        color_scheme = "深蓝主调，金色光线，暖光点缀"
        category = "投资"
    elif any(word in topic for word in ["数据", "分析", "报告", "研究"]):
        color_scheme = "深蓝主调，银白数据流，冷色调"
        category = "数据"
    elif any(word in topic for word in ["全球", "国际", "市场", "贸易", "经济"]):
        color_scheme = "深蓝主调，金色网络线，科技感"
        category = "全球"
    else:
        color_scheme = "深蓝主调，金色光线点缀，专业商务感"
        category = "商务"
    
    # 构建优化后的prompt
    visual_elements = "，".join(finance_keywords[category][:3])
    
    optimized = (
        f"{topic}，{color_scheme}，{visual_elements}，"
        f"专业商务风格，抢视觉冲击力，电影大片质感，"
        f"{render_params}"
    )
    
    return optimized


def generate_image(prompt, size="16:9", watermark=True, output_dir="./generated_images"):
    """
    调用火山云API生成图片
    
    Args:
        prompt: 图片描述
        size: 尺寸，支持 16:9, 1:1, 9:16, 2K, 4K 或具体分辨率
        watermark: 是否添加水印
        output_dir: 图片保存目录
    
    Returns:
        dict: 包含url和local_path的字典
    """
    try:
        from openai import OpenAI
    except ImportError:
        print("错误：请安装openai库: pip install openai")
        sys.exit(1)
    
    # 从环境变量读取API Key
    api_key = os.environ.get("ARK_API_KEY")
    if not api_key:
        print("错误：未设置ARK_API_KEY环境变量")
        print("请执行: export ARK_API_KEY='your-api-key'")
        sys.exit(1)
    
    # 初始化客户端
    client = OpenAI(
        base_url=os.environ.get("ARK_BASE_URL"),
        api_key=api_key,
    )
    
    # 转换尺寸参数
    size_param = get_size_param(size)
    
    print(f"  📐 尺寸: {size} ({size_param})")
    print(f"  📝 Prompt: {prompt[:80]}...")
    
    try:
        # 调用API生成图片
        response = client.images.generate(
            model="doubao-seedream-5-0-260128",
            prompt=prompt,
            size=size_param,
            response_format="url",
            extra_body={
                "watermark": watermark,
            },
        )
        
        image_url = response.data[0].url
        
        # 下载并保存图片
        return download_image(image_url, prompt, output_dir)
        
    except Exception as e:
        print(f"  ❌ 生成失败: {e}")
        return {
            "url": None,
            "local_path": None,
            "filename": None,
            "error": str(e)
        }


def download_image(url, prompt_hint, output_dir):
    """下载图片到本地"""
    
    # 创建保存目录
    save_dir = Path(output_dir)
    save_dir.mkdir(parents=True, exist_ok=True)
    
    # 生成文件名
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    # 从prompt中提取简短主题作为文件名
    topic = "image"
    if prompt_hint:
        # 提取前20个字符作为主题
        topic = "".join(c for c in prompt_hint[:20] if c.isalnum() or c in "_-")
        topic = topic.replace(" ", "_").replace("，", "_").replace(",", "_")
    
    filename = f"{timestamp}_{topic}.png"
    local_path = save_dir / filename
    
    try:
        # 下载图片
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.0"
        }
        req = urllib.request.Request(url, headers=headers)
        
        with urllib.request.urlopen(req, timeout=60) as response:
            with open(local_path, 'wb') as f:
                f.write(response.read())
        
        return {
            "url": url,
            "local_path": str(local_path.absolute()),
            "filename": filename,
            "error": None
        }
        
    except Exception as e:
        return {
            "url": url,
            "local_path": None,
            "filename": None,
            "error": str(e)
        }


def batch_generate(topics_file, size="16:9", style="写实", output_dir="./generated_images", delay=3):
    """
    批量生成图片
    
    Args:
        topics_file: JSON文件路径，包含多个主题或prompt
        size: 图片尺寸
        style: 图片风格
        output_dir: 保存目录
        delay: 每次请求间隔秒数（避免触发限流）
    """
    try:
        with open(topics_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"❌ 读取文件失败: {e}")
        sys.exit(1)
    
    if isinstance(data, list):
        items = data
    elif isinstance(data, dict) and "topics" in data:
        items = data["topics"]
    else:
        print("❌ 文件格式错误，需要是主题列表或包含topics字段的对象")
        sys.exit(1)
    
    total = len(items)
    print(f"🎯 批量生成模式: 共 {total} 张图片")
    print(f"💾 保存目录: {output_dir}")
    print("="*50)
    
    results = []
    success_count = 0
    
    for i, item in enumerate(items, 1):
        use_topic_mode = True  # 默认主题模式
        
        if isinstance(item, str):
            # 简单字符串，使用主题模式
            topic = item
            item_style = style
            item_size = size
            final_prompt = optimize_prompt_for_finance(topic, item_style)
        elif isinstance(item, dict):
            # 字典格式，判断是主题模式还是提示词模式
            if "prompt" in item:
                # 有prompt字段，使用提示词模式（直接使用）
                use_topic_mode = False
                final_prompt = item["prompt"]
                topic = item.get("topic", "自定义Prompt")
                item_size = item.get("size", size)
            elif "topic" in item:
                # 有topic字段，使用主题模式（自动优化）
                topic = item["topic"]
                item_style = item.get("style", style)
                item_size = item.get("size", size)
                final_prompt = optimize_prompt_for_finance(topic, item_style)
            else:
                print(f"\n[{i}/{total}] ⚠️ 跳过：未找到topic或prompt字段")
                continue
        else:
            print(f"\n[{i}/{total}] ⚠️ 跳过：格式错误")
            continue
        
        mode_str = "主题模式" if use_topic_mode else "提示词模式"
        print(f"\n[{i}/{total}] 🎨 {topic[:40]}... ({mode_str})")
        
        if not use_topic_mode:
            print(f"  📝 直接使用用户Prompt")
        
        # 生成图片
        result = generate_image(
            prompt=final_prompt,
            size=item_size,
            watermark=True,
            output_dir=output_dir
        )
        
        if result["error"]:
            print(f"  ❌ 失败: {result['error']}")
        else:
            print(f"  ✅ 成功: {result['filename']}")
            success_count += 1
        
        results.append({
            "topic": topic,
            "prompt": final_prompt,
            "mode": "topic" if use_topic_mode else "prompt",
            **result
        })
        
        # 延迟，避免触发限流
        if i < total:
            print(f"  ⏳ 等待 {delay} 秒...")
            time.sleep(delay)
    
    # 输出总结
    print("\n" + "="*50)
    print("📊 批量生成完成")
    print("="*50)
    print(f"✅ 成功: {success_count}/{total}")
    print(f"💾 保存目录: {output_dir}")
    
    # 保存结果报告
    report_path = Path(output_dir) / f"batch_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"📄 详细报告: {report_path}")
    
    return results


def main():
    parser = argparse.ArgumentParser(
        description="火山云AI配图生成工具 - 支持单图和批量生成，两种输入模式",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
╔════════════════════════════════════════════════════════════════╗
║                     两种输入模式说明                              ║
╠════════════════════════════════════════════════════════════════╣
║  【主题模式】--topic    提供文章主题，系统自动优化Prompt           ║
║  【提示词模式】--prompt 提供详细画图描述，原样使用不做修改         ║
╚════════════════════════════════════════════════════════════════╝

示例 - 单图:
  # 【主题模式】根据主题自动生成（适合快速配图）
  python generate_image.py --topic "新能源行业投资机会"
  
  # 【提示词模式】使用详细描述（适合精确控制画面）
  python generate_image.py --prompt "深蓝背景，金色光线，上升曲线，科技感，oc渲染"
  
  # 指定保存目录
  python generate_image.py --topic "AI量化交易" --output ./my_images

示例 - 批量生成:
  # 批量生成 - 从JSON文件读取
  python generate_image.py --batch topics.json --output ./batch_images
  
  # 批量生成 - 自定义延迟（避免限流）
  python generate_image.py --batch topics.json --delay 5

批量生成JSON文件格式:
  # 简单主题列表（自动优化）
  ["新能源行业投资机会", "AI量化交易策略"]
  
  # 带参数的主题（自动优化）
  [
    {"topic": "新能源行业", "size": "16:9"},
    {"topic": "AI量化交易", "size": "1:1", "style": "插画"}
  ]
  
  # 使用详细prompt（原样使用，不做修改）
  [
    {"prompt": "深蓝背景，金色光线，上升曲线，科技感"},
    {"prompt": "抽象的金融数据可视化，蓝金配色，3D效果"}
  ]
  
  # 混合模式（主题+提示词）
  [
    {"topic": "新能源行业", "size": "16:9"},           ← 主题模式（自动优化）
    {"prompt": "深蓝背景，金色光线..."},               ← 提示词模式（直接使用）
    {"topic": "AI量化交易", "style": "插画"}           ← 主题模式（自动优化）
  ]
        """
    )
    
    # 单图参数
    parser.add_argument(
        "--topic", "-t",
        help="文章主题（将自动优化prompt）"
    )
    parser.add_argument(
        "--prompt", "-p", 
        help="直接提供图片描述"
    )
    
    # 批量参数
    parser.add_argument(
        "--batch", "-b",
        help="批量生成模式：JSON文件路径，包含多个主题"
    )
    parser.add_argument(
        "--delay", "-d",
        type=int,
        default=3,
        help="批量模式下的请求间隔秒数 (默认: 3)"
    )
    
    # 通用参数
    parser.add_argument(
        "--size", "-s",
        default="16:9",
        choices=["16:9", "1:1", "9:16", "4:3", "2K", "4K"],
        help="图片尺寸 (默认: 16:9)"
    )
    parser.add_argument(
        "--style",
        default="写实",
        choices=["写实", "插画", "扁平", "3D", "水墨"],
        help="图片风格"
    )
    parser.add_argument(
        "--no-watermark",
        action="store_true",
        help="不添加水印"
    )
    parser.add_argument(
        "--output", "-o",
        default="./generated_images",
        help="图片保存目录 (默认: ./generated_images)"
    )
    
    args = parser.parse_args()
    
    # 批量模式
    if args.batch:
        batch_generate(
            topics_file=args.batch,
            size=args.size,
            style=args.style,
            output_dir=args.output,
            delay=args.delay
        )
        return
    
    # 单图模式
    if not args.topic and not args.prompt:
        parser.print_help()
        print("\n❌ 错误: 请提供 --topic、--prompt 或 --batch 参数")
        sys.exit(1)
    
    # 确定最终prompt
    if args.prompt:
        final_prompt = args.prompt
        print("🎯 模式: 直接描述生成")
    else:
        final_prompt = optimize_prompt_for_finance(args.topic, args.style)
        print("🎯 模式: 主题智能优化")
        print(f"📋 原始主题: {args.topic}")
        print(f"✨ 优化后Prompt:\n{final_prompt}\n")
    
    print(f"💾 保存目录: {args.output}")
    print("="*50)
    
    # 生成图片
    result = generate_image(
        prompt=final_prompt,
        size=args.size,
        watermark=not args.no_watermark,
        output_dir=args.output
    )
    
    # 输出结果
    print("\n" + "="*50)
    if result["error"]:
        print(f"❌ 生成失败: {result['error']}")
    else:
        print("✅ 生成成功")
        print(f"🌐 在线查看: {result['url']}")
        if result['local_path']:
            print(f"💾 本地文件: {result['local_path']}")
    print("="*50)


if __name__ == "__main__":
    main()
