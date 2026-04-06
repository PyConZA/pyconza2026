import random
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django_countries import countries
from visa.models import VisaInvitationLetter


class Command(BaseCommand):
    help = 'Create mock visa letter requests for testing'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=20,
            help='Number of mock visa letters to create (default: 20)'
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing visa letters before creating new ones'
        )

    def handle(self, *args, **options):
        count = options['count']
        
        if options['clear']:
            deleted_count = VisaInvitationLetter.objects.count()
            VisaInvitationLetter.objects.all().delete()
            self.stdout.write(
                self.style.WARNING(f'Deleted {deleted_count} existing visa letters')
            )

        # Sample data for generating realistic mock data
        first_names = [
            'John', 'Jane', 'Michael', 'Sarah', 'David', 'Emily', 'James', 'Emma',
            'Robert', 'Olivia', 'William', 'Ava', 'Richard', 'Isabella', 'Joseph',
            'Sophia', 'Thomas', 'Mia', 'Christopher', 'Charlotte', 'Daniel', 'Amelia',
            'Matthew', 'Harper', 'Anthony', 'Evelyn', 'Mark', 'Abigail', 'Donald',
            'Elizabeth', 'Steven', 'Sofia', 'Paul', 'Ella', 'Andrew', 'Madison',
            'Joshua', 'Scarlett', 'Kenneth', 'Victoria', 'Kevin', 'Aria', 'Brian',
            'Grace', 'George', 'Chloe', 'Timothy', 'Camila', 'Ronald', 'Penelope'
        ]
        
        last_names = [
            'Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller',
            'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez',
            'Wilson', 'Anderson', 'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin',
            'Lee', 'Perez', 'Thompson', 'White', 'Harris', 'Sanchez', 'Clark',
            'Ramirez', 'Lewis', 'Robinson', 'Walker', 'Young', 'Allen', 'King',
            'Wright', 'Scott', 'Torres', 'Nguyen', 'Hill', 'Flores', 'Green',
            'Adams', 'Nelson', 'Baker', 'Hall', 'Rivera', 'Campbell', 'Mitchell',
            'Carter', 'Roberts'
        ]

        # Popular countries for visa applications
        common_countries = [
            'US', 'IN', 'CN', 'NG', 'BR', 'MX', 'PH', 'VN', 'EG', 'ET',
            'PK', 'BD', 'KE', 'UG', 'TZ', 'GH', 'ZM', 'ZW', 'MW', 'RW',
            'GB', 'DE', 'FR', 'CA', 'AU', 'JP', 'KR', 'SG', 'MY', 'TH'
        ]

        statuses = ['pending', 'approved', 'rejected', 'permanently rejected']
        status_weights = [0.6, 0.2, 0.15, 0.05]  # Most should be pending

        embassy_templates = {
            'US': 'U.S. Embassy\n{city}\nSouth Africa',
            'GB': 'British High Commission\n{city}\nSouth Africa', 
            'DE': 'German Embassy\n{city}\nSouth Africa',
            'FR': 'French Embassy\n{city}\nSouth Africa',
            'CN': 'Chinese Embassy\n{city}\nSouth Africa',
            'IN': 'Indian High Commission\n{city}\nSouth Africa',
            'default': '{country} Embassy\n{city}\nSouth Africa'
        }

        cities = ['Pretoria', 'Cape Town', 'Johannesburg', 'Durban']

        rejection_reasons = [
            'Incomplete documentation provided',
            'Passport validity insufficient',
            'Conference registration not confirmed',
            'Accommodation details missing',
            'Flight itinerary not provided',
            'Insufficient financial documentation',
            'Purpose of visit unclear',
            'Previous visa violations detected'
        ]

        # Get or create users for visa letters
        users = list(User.objects.all())
        if len(users) < count:
            # Create additional users if needed
            needed_users = count - len(users)
            for i in range(needed_users):
                username = f'testuser_{len(users) + i + 1}'
                email = f'{username}@example.com'
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    password='testpass123'
                )
                users.append(user)

        created_count = 0
        for i in range(count):
            # Generate random data
            first_name = random.choice(first_names)
            last_name = random.choice(last_names)
            full_name = f'{first_name} {last_name}'
            
            # Generate passport number (2 letters + 6-8 digits)
            passport_prefix = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
            passport_number = f'{passport_prefix}{random.randint(100000, 99999999)}'
            
            country_code = random.choice(common_countries)
            
            # Generate embassy address
            city = random.choice(cities)
            country_name = dict(countries)[country_code]
            
            if country_code in embassy_templates:
                embassy_address = embassy_templates[country_code].format(
                    city=city, country=country_name
                )
            else:
                embassy_address = embassy_templates['default'].format(
                    city=city, country=country_name
                )
            
            # Select user (ensure no duplicates)
            available_users = [u for u in users if not hasattr(u, 'visa_letter')]
            if not available_users:
                # If all users have visa letters, skip creating more
                self.stdout.write(
                    self.style.WARNING(
                        f'Only created {created_count} visa letters - '
                        f'all available users already have visa letters'
                    )
                )
                break
            
            user = random.choice(available_users)
            
            # Select status
            status = random.choices(statuses, weights=status_weights)[0]
            
            # Create visa letter
            visa_letter = VisaInvitationLetter.objects.create(
                user=user,
                full_name=full_name,
                passport_number=passport_number,
                country_of_origin=country_code,
                embassy_address=embassy_address,
                status=status
            )
            
            # Add rejection reason if rejected
            if status in ['rejected', 'permanently rejected']:
                visa_letter.rejection_reason = random.choice(rejection_reasons)
                visa_letter.save(update_fields=['rejection_reason'])
            
            created_count += 1

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully created {created_count} mock visa letters'
            )
        )
        
        # Show status distribution
        status_counts = {}
        for status, _ in VisaInvitationLetter.STATUS_CHOICES:
            count = VisaInvitationLetter.objects.filter(status=status).count()
            if count > 0:
                status_counts[status] = count
        
        self.stdout.write('\nStatus distribution:')
        for status, count in status_counts.items():
            self.stdout.write(f'  {status}: {count}')