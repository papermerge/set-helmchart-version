import os

from setappversion.utils import (
    get_file_content,
    set_file_content,
    replace_ver
)


def main():
    # path to helmchart file e.g. "charts/docs/Chart.yaml"
    file_path = os.environ["INPUT_HELMCHART_FILE"]
    # new app version to be set in helmchart e.g. "1.5.6"
    new_version = os.environ["INPUT_NEW_APP_VERSION"]

    content = get_file_content(file_path)
    new_content = replace_ver(content, str(new_version))
    set_file_content(file_path, new_content)


if __name__ == "__main__":
    main()
