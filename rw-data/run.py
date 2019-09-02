import sys
import os
import csv2json
import json

sys.path.append(
    os.path.abspath(
        './lib'
    )
)

DIST_FOLDER = os.path.abspath('../dist')
CSV_FOLDER = os.path.abspath('../lib/rw-csv')

def main():
    print(CSV_FOLDER)
    for root, dirs, files in os.walk(CSV_FOLDER):
        for name in files:
            if not name.endswith('.csv'):
                continue

            full_path = os.path.join(root, name)

            dir_name = os.path.dirname(full_path)
            folder_name = os.path.split(dir_name)[-1]

            # make folder
            dist_folder = os.path.join(DIST_FOLDER, folder_name)
            os.makedirs(dist_folder, exist_ok=True)

            data = csv2json.read_csv(full_path)

            dist_file = os.path.join(
                dist_folder,
                f"{name.split('.')[0]}.json"
            )

            with open(dist_file, 'w') as f:
                json.dump(data, f, indent=4)

            print(dist_file)


if __name__ == '__main__':
    main()