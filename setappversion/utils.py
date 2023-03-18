import re


VERSION_PATTERN = re.compile(r"appVersion: \"(.+)\"[\n]*")


def get_file_content(file_path: str) -> str:
    with open(file_path, "r") as file:
        content = file.read()

    return content


def set_file_content(file_path: str, content: str):
    with open(file_path, "w") as file:
        file.write(content)



def replace_ver(text: str, new_ver: str) -> str:
    match = VERSION_PATTERN.search(text)

    if match:
        return re.sub(
            VERSION_PATTERN,
            f'appVersion: "{new_ver}"\n',
            text,
            count=1
        )

    return None
