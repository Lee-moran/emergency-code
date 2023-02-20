from django.test import TestCase
from . models import Category, NonGovernmentOrg


class TestNonGovernmentOrgModels(TestCase):
    """ Test for NGOs models """

    def setUp(self):
        """ Creates test NGOs objects (Category, NonGovernmentOrg) """

        self.category1 = Category.objects.create(
            name='anti-slavery',
            friendly_name='Anti-Slavery',
            slug='anti-slavery',
        )

        self.ngo1 = NonGovernmentOrg.objects.create(
            category=self.category1,
            name='great ngo',
            friendly_name='Great NGO',
            slug='great-ngo',
            is_featured=False,
            description='They really are a great NGO!',
            website='https://greatngo.com',
            image_url='image_url',
        )

    def test_category_str_method(self):
        """ tests the string representation of the category model """
        category = Category(name='Category Name')
        self.assertEqual(str(category), category.name)

    def ngo_is_featured(self):
        """ test product is featured """
        self.assertEqual(self.ngo1.is_featured, False)
