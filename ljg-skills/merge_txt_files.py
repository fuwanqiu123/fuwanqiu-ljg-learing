import os
import re
import glob


def extract_first_number(filename):
    """从文件名中提取第一个连续的数字序列，如果没有数字则返回无穷大"""
    match = re.search(r'\d+', filename)
    return int(match.group()) if match else float('inf')


def merge_txt_files(input_folder, output_file=None):
    """
    将指定文件夹中的所有 TXT 文件按文件名中的数字排序后合并。

    :param input_folder: 输入文件夹路径
    :param output_file: 输出文件路径，默认为 input_folder/merged_output.txt
    """
    if not os.path.isdir(input_folder):
        print(f"错误：'{input_folder}' 不是有效的文件夹路径。")
        return

    # 获取所有 txt 文件（不递归子文件夹）
    txt_files = glob.glob(os.path.join(input_folder, "*.txt"))

    if not txt_files:
        print(f"在 '{input_folder}' 中没有找到任何 .txt 文件。")
        return

    # 按文件名中的第一个数字排序
    txt_files.sort(key=lambda x: extract_first_number(os.path.basename(x)))

    # 默认输出文件
    if output_file is None:
        output_file = os.path.join(input_folder, "merged_output.txt")

    print(f"找到 {len(txt_files)} 个 TXT 文件，准备合并...")
    print("合并顺序：")
    for f in txt_files:
        print(f"  - {os.path.basename(f)}")

    # 合并内容
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for i, file_path in enumerate(txt_files):
            basename = os.path.basename(file_path)
            try:
                with open(file_path, 'r', encoding='utf-8') as infile:
                    content = infile.read()
                # 在每个文件内容之间加一个空行，方便区分
                outfile.write(content)
                if i < len(txt_files) - 1:
                    outfile.write('\n')
                print(f"已合并: {basename}")
            except Exception as e:
                print(f"读取文件 '{basename}' 时出错: {e}")

    print(f"\n合并完成！结果已保存到: {output_file}")


if __name__ == "__main__":
    # 修改这里指定你的文件夹路径
    folder_path = r"D:\BaiduSyncdisk\学习之旅\新建文件夹"  # 默认当前目录下的 txt_files 文件夹

    # 也可以直接指定输出文件路径，如：output_path = r".\merged_output.txt"
    output_path = None

    merge_txt_files(folder_path, output_path)
