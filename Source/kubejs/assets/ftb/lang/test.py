import os
import re

# ==================== 配置区域 ====================
# 【重要】请把这里改成你的真实文件夹路径（建议用绝对路径，比如 "D:/Minecraft/workspace"）
TARGET_DIR = r"D:/mc/mod/FTB-Skies2-Aero/Source/kubejs/assets/ftb/lang" 
# ==================================================

# 精准修复表
# 精准修复表
SAFE_REPLACEMENTS = {
    r"⚠(\xa0|\s)?": "⚠",
    r"→": "→",
    r"✔": "✔",  # 兼容部分变体
    r"✔": "✔",
    r"°": "°",
    r"©": "©",
    # ---------------- 修复此处 ----------------
    r"(\xa0|\s)?": "",  # 直接把 及其后缀的乱码空格替换为空（即彻底删除）
    r"": "",            # 预防性清理孤立的     # ------------------------------------------
}

# 自动将路径转换为绝对路径，防止相对路径找不到
abs_target_dir = os.path.abspath(TARGET_DIR)
print(f"==========================================")
print(f"🔍 启动扫描...")
print(f"📍 目标绝对路径: {abs_target_dir}")

if not os.path.exists(abs_target_dir):
    print(f"❌ 错误：找不到目标文件夹，请检查路径是否正确！")
    exit()

scan_count = 0
fix_count = 0

def fix_file_permanently(file_path):
    global fix_count
    try:
        # 用 utf-8 读取，如果遇到无法解码的字符直接忽略（保证中文不报错）
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        # 检查并替换
        modified = False
        for pattern, replacement in SAFE_REPLACEMENTS.items():
            if re.search(pattern, content):
                content = re.sub(pattern, replacement, content)
                modified = True
        
        # 如果有改动，写回文件
        if modified:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ [修复成功] -> {os.path.basename(file_path)}")
            fix_count += 1
            
    except Exception as e:
        print(f"⚠️ [处理出错] {os.path.basename(file_path)}: {e}")

# 递归遍历目录
for root, dirs, files in os.walk(abs_target_dir):
    # 打印正在扫描的子目录，让你知道程序正在工作
    if files:
        print(f"📂 正在扫描目录: {root}")
    
    for file in files:
        scan_count += 1
        file_path = os.path.join(root, file)
        
        # 排除掉常见的二进制文件（图片、压缩包等），其他文本文件一律尝试处理
        if not file.lower().endswith((".png", ".jpg", ".jpeg", ".jar", ".zip", ".gz", ".class")):
            fix_file_permanently(file_path)

print(f"==========================================")
print(f"🎉 扫描结束！")
print(f"📊 总共扫描到文件数: {scan_count}")
print(f"🛠️ 成功修复文件数: {fix_count}")
print(f"==========================================")