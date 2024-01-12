from django.core.management.base import BaseCommand
from django_seed import Seed
from video.models import Video  # video 앱의 Video 모델을 임포트합니다.


class Command(BaseCommand):
    help = "Seeds the database with Video data"

    def add_arguments(self, parser):
        parser.add_argument('--number', type=int, default=10, help='Number of videos to seed')

    def handle(self, *args, **options):
        number = options['number']
        seeder = Seed.seeder()

        seeder.add_entity(Video, number, {
            'video_id': lambda x: seeder.faker.lexify(text='??????????'),
            'title': lambda x: seeder.faker.sentence(),
            'channel_title': lambda x: seeder.faker.name(),
            'published_at': lambda x: seeder.faker.past_date(),
            'view_count': lambda x: seeder.faker.random_number(digits=5),
            'paid_product_placement': lambda x: seeder.faker.boolean(),
        })

        inserted_pks = seeder.execute()
        self.stdout.write(self.style.SUCCESS(f'Successfully seeded {number} videos.'))