from django.test import TestCase
from .models import Plan
# Create your tests here.

class PlanTestCase(TestCase):
    def setUp(self):
        Plan.objects.create(
            titulo="Plan XS"
            velocidad="50 Megas"
            minutos=1000
            canales="150 Canales"
            valor=25990
        )

        Plan.objects.create(
            titulo="Plan S"
            velocidad="70 Megas"
            minutos=1500
            canales="150 Canales"
            valor=25990
        )

        Plan.objects.create(
            titulo="Plan M"
            velocidad="50 Megas"
            minutos=1000
            canales="150 Canales"
            valor=25990
        )