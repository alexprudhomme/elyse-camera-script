# take file path as input

# create copy of file
# do formatting
# save file

# put file in same place as original file

import argparse
import csv
import os

def main():
    parser = argparse.ArgumentParser(description='Format a file')
    parser.add_argument('-f', '--files',nargs='+' ,type=str, help='Description of argument 1')
    args = parser.parse_args()
    file_paths = args.files

    for file_path in file_paths:
        rows = get_rows(file_path)
        create_file(rows, file_path)



def get_rows(file_path):
    print("Finding wanted rows from file: " + file_path)

    with open(file_path, 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        current_video_path = ""
        rows_for_new_file = []
        for row in csv_reader:
            if row[3] != current_video_path and row[3] != "":
                current_video_path = row[3]
                rows_for_new_file.append(row)


    return rows_for_new_file

def create_file(rows, old_file_path):
    output_file_path, extension = os.path.splitext(old_file_path)
    new_output_file = f'{output_file_path}_formatted{extension}'

    print("Creating new file: " + new_output_file)
    with open(new_output_file, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        for row in rows:
            csv_writer.writerow(row)
    
if __name__ == "__main__":
    main()
