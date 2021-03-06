import csv
from . import common
from .. import core as fismatic


def test_matrix():
    fismatic.run(common.SOURCE_DOC)

    with open("matrix.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)

        column_headings = csv_reader.fieldnames[1:]
        assert column_headings[0:4] == [
            "AC-1: Part a",
            "AC-1: Part b",
            "AC-2: Part a",
            "AC-2: Part b",
        ]

        # check that the columns match the rows
        csv_reader = csv.reader(csv_file)
        row_headings = [row[0] for row in csv_reader]
        assert row_headings == column_headings
