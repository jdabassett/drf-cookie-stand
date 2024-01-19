from datetime import datetime, timezone, timedelta
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken
from django.test import TestCase
import pytz

from .models import CookieStand
# from .serializer import SnackSerializer


class CookieStandApiTests(APITestCase):

    def setUp(self):
        self.future_time = datetime.now(timezone.utc) + timedelta(minutes=2)
        self.past_time = datetime.now(timezone.utc) - timedelta(minutes=2)
        self.user = get_user_model().objects.create_user(username="username", password="password")
        self.cookie_stand = CookieStand.objects.create(
            average_cookies_per_sale= 1.0,
            description= "Pike Place",
            hourly_sales= [1, 2, 3],
            location= "Seattle",
            maximum_customers_per_hour= 3,
            minimum_customers_per_hour= 2,
            owner= self.user
        )
        self.client.login(username="username", password="password")
        self.refresh_token = RefreshToken.for_user(self.user)
        self.access_token = str(self.refresh_token.access_token)

    def test_get(self):
        url = reverse('cookie_stand_list_api')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        snacks = response.data
        self.assertEqual(len(snacks), 1)
        self.assertContains(response, self.cookie_stand)

    def test_get_detailed(self):
        url = reverse('cookie_stand_detail_api', kwargs={'pk':self.cookie_stand.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, self.cookie_stand)

    def test_get_tokens(self):
        url=reverse("token_pair")
        response = self.client.post(url, {'username':self.user.username, "password": "password"})
        access = response.data.get("access")
        refresh = response.data.get("refresh")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(access)
        self.assertIsNotNone(refresh)
        decoded_token = RefreshToken(refresh).payload
        self.assertEqual(decoded_token["username"], self.user.username)
        return decoded_token

    def test_get_refresh_tokens(self):
        url = reverse("token_refresh")
        data = {'username': self.user.username,
                   "password": "password",
                   "refresh":str(self.refresh_token)}
        response = self.client.post(url, data=data)

        access = response.data.get("access")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(access)

    def test_post(self):
        url = reverse("cookie_stand_list_api")
        data = {
                "average_cookies_per_sale": 1.0,
                "description": "Pike Place",
                "hourly_sales": [1, 2, 3],
                "location": "Seattle",
                "maximum_customers_per_hour": 3,
                "minimum_customers_per_hour": 2,
                "owner": self.user.pk
            }
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.post(url, data, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["description"], "Pike Place")

    def test_put(self):
        url = reverse("cookie_stand_detail_api", kwargs={"pk":self.cookie_stand.pk})
        data = {
                "average_cookies_per_sale": 1,
                "description": "Pike Place",
                "hourly_sales": [1],
                "location": "Mona",
                "maximum_customers_per_hour": 1,
                "minimum_customers_per_hour": 1,
                "owner": self.user.pk
            }
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.put(url, data, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["location"],"Mona")

    def test_delete(self):
        url = reverse("cookie_stand_detail_api", kwargs={"pk":self.cookie_stand.pk})
        headers = {'Authorization': f'Bearer {self.access_token}'}
        response = self.client.delete(url, format='json', headers=headers)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)




