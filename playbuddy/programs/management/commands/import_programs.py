from pathlib import Path

from django.core.management.base import BaseCommand

import pandas as pd

from movies.models import Movie
from programs.models import Program

current_dir = Path('.').cwd()
file_path = current_dir / 'programs' / 'management' / 'commands' / '01_AIS_EPG_HBO_HD.xlsx'


class Command(BaseCommand):
    def handle(self, *args, **options):
        with pd.ExcelFile(file_path) as xlsx:
            df = pd.read_excel(xlsx, 'Sheet1', index_col=0)
            for index, row in df.iterrows():
                self.create_program(index, row)

    def create_program(self, index, row):
        movie, _ = Movie.objects.get_or_create(name=row['Program'])
        program, _ = Program.objects.get_or_create(
            movie=movie,
            start_time=row['Start Time'],
            end_time=row['End Time'],
            date=row['Date'].date()
        )
        print(f'{index}: {program}')

