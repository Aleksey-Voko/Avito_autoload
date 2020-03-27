import csv
from datetime import datetime, timedelta
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


def get_repr_world_time(in_date, out_format='%Y-%m-%dT%H:%M:00+03:00'):
    """
    Возвращает строку, представляющую дату и время, управляемую строкой формата.
    Отнимает от Московского времени (UTC+3) 3 часа (UTC+0)
    :param in_date: datetime.datetime(date)
    :param out_format: str [%Y-%m-%dT%H:%M:00+03:00]
    :return: str [2020-03-25T16:11:00+03:00]
    """
    in_date = in_date - timedelta(hours=3)
    return datetime.strftime(in_date, out_format)


def get_datetime(date_string, in_format='%d-%m-%Y;%H:%M'):
    """
    Возвращает дату и время, соответствующие date_string,
    проанализированные в соответствии с форматом.
    :param date_string: [25-03-2020;16:10]
    :param in_format: ['%d-%m-%Y;%H:%M']
    :return: datetime.datetime(date)
    """
    out_date = datetime.strptime(date_string, in_format)
    return out_date
