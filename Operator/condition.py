def extract_condition_code(file_path):
    with open(file_path, 'r', encoding='UTF-8') as file:
        code = file.read()

    condition_start = code.find("condition{") + len("condition{")
    condition_end = code.find("}", condition_start)

    condition_code = code[condition_start:condition_end].strip()
    condition_code = condition_code.replace("infinite_loop = True", "while True")
    replacement = r"alert_mo(module[\"alert\"][\"url\"],module[\"alert\"][\"message\"])"
    condition_code = condition_code.replace("alert", replacement)
    return condition_code




# def convert_condition_code(condition_code):
#     converted_code = condition_code.replace("condition{", "").replace("}", "").strip()
#     return converted_code

# 条件コードをファイルから抽出




