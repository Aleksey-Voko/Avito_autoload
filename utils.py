import csv
from pathlib import Path


def get_list_of_dicts_from_csv_file(input_file, encoding='utf-8',
                                    newline='', delimiter=','):
    """
    читает список словарей из csv файла

    newline='' исправляет '\r\r\n' -> '\r\n'
    https://docs.python.org/3/library/csv.html#id3

    delimiter - разделитель [,] or [;]

    docs -> https://docs.python.org/3/library/csv.html
    """
    out_list = []
    with open(Path(input_file), encoding=encoding, newline=newline) as f_in:
        csv_reader = csv.DictReader(f_in, delimiter=delimiter)
        for row in csv_reader:
            out_list.append(row)
    return out_list
