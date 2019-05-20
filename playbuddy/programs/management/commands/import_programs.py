from pathlib import Path

from django.core.management.base import BaseCommand

import pandas as pd

from channels.models import Channel
from movies.models import Movie
from programs.models import Program


class Command(BaseCommand):
    def handle(self, *args, **options):
        file_collection = (
            '01_AIS_EPG_HBO_HD.xlsx',
            '02_AIS_EPG_HBO_Family.xlsx',
            '03_AIS_EPG_HBO_Hit.xlsx',
            '04_AIS_EPG_HBO_Signature.xlsx',
            '05_AIS_EPG_RED_BY_HBO.xlsx',
            '06_AIS_EPG_HBO_Cinemax.xlsx',
            '08_AIS_EPG_FOX_FAMILY_MOVIES.xlsx',
            '09_AIS_EPG_FOX_MOVIES.xlsx',
            '10_AIS_EPG_FOX_ACTION_MOVIES.xlsx',
            '11_AIS_EPG_WB.xlsx',
        )

        for file_name in file_collection:
            current_dir = Path('.').cwd()
            file_path = current_dir / 'data' / file_name

            with pd.ExcelFile(file_path) as xlsx:
                df = pd.read_excel(xlsx, 'Sheet1', index_col=0)
                for index, row in df.iterrows():
                    self.create_program(index, row, file_name)

    def create_program(self, index, row, file_name):
        channel, _ = Channel.objects.get_or_create(name=file_name)
        movie, _ = Movie.objects.get_or_create(name=row['Program'])
        program, _ = Program.objects.get_or_create(
            movie=movie,
            channel=channel,
            start_time=row['Start Time'],
            end_time=row['End Time'],
            date=row['Date'].date()
        )
        print(f'{index}: {program}')

