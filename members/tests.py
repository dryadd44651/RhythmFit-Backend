from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from members.models import Exercise, Workout


class UserTests(APITestCase):
    def test_register_user(self):
        """
        Test user registration API
        """
        url = reverse('register')
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "password123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("username", response.data)


class ExerciseTests(APITestCase):
    def setUp(self):
        # 創建測試用戶並獲取 JWT Token
        self.user = User.objects.create_user(username="testuser", password="password123")
        token_url = reverse('token_obtain_pair')
        response = self.client.post(token_url, {
            "username": "testuser",
            "password": "password123"
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_exercise(self):
        """
        Test creating a new exercise
        """
        url = reverse('exercise-list')  # DRF router 自動生成 URL
        data = {
            "name": "Squat",
            "max1RM": 200,
            "group": "Legs"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], "Squat")

    def test_get_exercise_list(self):
        """
        Test retrieving a list of exercises
        """
        Exercise.objects.create(name="Bench Press", max1RM=150, group="Chest", user=self.user)
        url = reverse('exercise-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_exercise(self):
        """
        Test updating an exercise
        """
        exercise = Exercise.objects.create(name="Deadlift", max1RM=250, group="Back", user=self.user)
        url = reverse('exercise-detail', args=[exercise.id])
        data = {
            "name": "Deadlift",
            "max1RM": 260,
            "group": "Back"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["max1RM"], 260)

    def test_delete_exercise(self):
        """
        Test deleting an exercise
        """
        exercise = Exercise.objects.create(name="Pull-up", max1RM=0, group="Back", user=self.user)
        url = reverse('exercise-detail', args=[exercise.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class WorkoutTests(APITestCase):
    def setUp(self):
        # 創建測試用戶並獲取 JWT Token
        self.user = User.objects.create_user(username="testuser", password="password123")
        token_url = reverse('token_obtain_pair')
        response = self.client.post(token_url, {
            "username": "testuser",
            "password": "password123"
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_workout(self):
        """
        Test creating a new workout
        """
        url = reverse('workout-list')
        data = {
            "currentCycle": "medium",
            "trainedGroups": ["Legs", "Back"],
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["currentCycle"], "medium")

    def test_get_current_workout(self):
        """
        Test retrieving the current workout
        """
        Workout.objects.create(user=self.user, currentCycle="heavy", trainedGroups=["Chest"])
        url = reverse('workout-current-workout')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["currentCycle"], "heavy")

    def test_update_workout(self):
        """
        Test updating a workout
        """
        workout = Workout.objects.create(user=self.user, currentCycle="light", trainedGroups=[])
        url = reverse('workout-detail', args=[workout.id])
        data = {
            "currentCycle": "medium",
            "trainedGroups": ["Arms"]
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["currentCycle"], "medium")
        self.assertIn("Arms", response.data["trainedGroups"])

    def test_delete_workout(self):
        """
        Test deleting a workout
        """
        workout = Workout.objects.create(user=self.user, currentCycle="light", trainedGroups=[])
        url = reverse('workout-detail', args=[workout.id])
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
