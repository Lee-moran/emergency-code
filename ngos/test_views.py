from django.test import TestCase
from . models import Category, NonGovernmentOrg


class TestViews(TestCase):
    """ Test for ngos app views """

    def test_can_get_ngos_page(self):
        response = self.client.get('/ngos/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ngos/ngos.html')

    def test_can_get_all_products_from_search(self):
        """ test to get all ngos page from search """
        response = self.client.get('/ngos/', {'search_term': 'anti-poverty',
                                   'current_categories': 'anti-poverty'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ngos/ngos.html')

    def test_sort(self):
        """ test categories sorting with parameters """
        response = self.client.get('/ngos/', {'sort': 'name',
                                   'direction': 'desc'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ngos/ngos.html')
