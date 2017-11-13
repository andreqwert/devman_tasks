import os
from collections import Counter
import pandas as pd


def get_files_names(folderpath):
    files_paths = []
    for dirpath, dirnames, filenames in os.walk(folderpath):
        for filename in filenames:
            filename = os.path.join(dirpath, filename)
            files_paths.append(filename)
    return files_paths


def get_files_sizes(files_paths):
    files_sizes = []
    for every_file in files_paths:
        files_sizes.append(os.path.getsize(every_file))
    return files_sizes


def make_table_with_data(files_paths, files_sizes):
    files_names_without_paths = [os.path.split(path)[1] for path in files_paths]
    allfiles = pd.DataFrame({'Size':files_sizes, 'Name':files_names_without_paths, 'Full_path':files_paths})
    return allfiles


def search_duplicates(allfiles):
    allfiles['Duplicate'] = allfiles.duplicated(['Size', 'Name'])
    only_duplicates = allfiles[allfiles.Duplicate == True]
    only_duplicates = only_duplicates[['Full_path']]
    print('\nThe following files are duplicates:\n', only_duplicates)
    return only_duplicates


def main():
    folderpath = input('Enter the path to folder:\n')
    if os.path.exists(folderpath):
        names = get_files_names(folderpath)
        sizes = get_files_sizes(names)
        table_data = make_table_with_data(names, sizes)
        duplicates = search_duplicates(table_data)
    else:
        print('Wrong path to folder!')


if __name__ == '__main__':
    main()
