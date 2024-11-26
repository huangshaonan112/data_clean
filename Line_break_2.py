import os

def process_line_extended(line):
    """
    如果某行以'导读'开头，并包含']'，根据符号的位置（开头、中间、结尾）进行不同的处理：
    1. 如果符号在开头：在最后一个']'后插入换行符，将后续内容移到下一行。
    2. 如果符号在中间第二个：在该符号后插入换行符，将后续内容移到下一行。
    3. 如果符号在结尾：在最后一个']'后插入换行符，将后续内容移到下一行。
    """
    if line.startswith("导读") and "]" in line:
        # 符号在结尾的情况（原逻辑）
        if line.rstrip().endswith("]"):
            return line + "\n"  # 保留原逻辑，直接返回处理结果
        
        # 符号在中间的情况（新增逻辑）
        second_bracket_index = line.find("]", line.find("]") + 1)  # 找到第二个']'
        if second_bracket_index != -1:
            return line[:second_bracket_index + 1] + "\n" + line[second_bracket_index + 1:]
        
        # 符号在开头的情况（新增逻辑）
        first_bracket_index = line.find("]")
        if first_bracket_index != -1:
            return line[:first_bracket_index + 1] + "\n" + line[first_bracket_index + 1:]
    return line

def process_file(file_path):
    """
    处理单个文件，对每行内容进行检查并替换符合条件的行（使用扩展逻辑）。
    """
    modified_lines = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            modified_lines.append(process_line_extended(line))  # 使用扩展的处理逻辑
    
    # 将修改后的内容写回文件
    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(modified_lines)

def process_folder(folder_path):
    """
    遍历文件夹及其子文件夹中的所有文件，处理每个文件。
    """
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                process_file(file_path)
                print(f"Processed file: {file_path}")
            except Exception as e:
                print(f"Error processing file {file_path}: {e}")

# 使用方法
if __name__ == "__main__":
    # 替换为目标文件夹路径（绝对路径）
    folder_path = r"C:\absolute\path\to\your\folder"  # 修改为实际的文件夹路径
    process_folder(folder_path)
