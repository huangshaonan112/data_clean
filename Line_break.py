import os

def process_line(line):
    """
    如果某行以'读'开头，并包含']'，在最后一个']'后添加换行符，将后续内容换到下一行。
    """
    if line.startswith("读") and "]" in line:
        last_bracket_index = line.rfind("]")
        # 插入换行符
        return line[:last_bracket_index + 1] + "\n" + line[last_bracket_index + 1:]
    return line

def process_file(file_path):
    """
    处理单个文件，对每行内容进行检查并替换符合条件的行。
    """
    modified_lines = []
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            modified_lines.append(process_line(line))
    
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
    # 直接设置需要处理的文件夹绝对路径
    folder_path = r"C:\absolute\path\to\your\folder"  # 将此路径修改为实际路径
    process_folder(folder_path)


