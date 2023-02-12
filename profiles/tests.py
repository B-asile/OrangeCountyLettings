from django.test import TestCase

from faker import Faker
from django.urls import reverse
from django.contrib.auth.models import User

from .models import Profile


class ProfilesTest(TestCase):

    faker = Faker()

    def setUp(self):
        self.user = User.objects.create_user(
            username=self.faker.user_name(),
            first_name=self.faker.first_name(),
            last_name=self.faker.last_name(),
            email=self.faker.email(),
            password=self.faker.password(),
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city=self.faker.city(),
        )

    def test_index(self):
        response = self.client.get(reverse('profiles:index'))
        assert response.status_code == 200
        assert b"<title>Profiles</title>" in response.content

    def test_profile(self):
        response = self.client.get(
            reverse('profiles:profile', args=[self.profile.user.username])
        )
        assert response.status_code == 200
