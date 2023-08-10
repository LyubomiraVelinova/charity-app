# Arrange, Act, Assert

from django.core.exceptions import ValidationError
from django.test import TestCase

from charityapp.user_profiles.forms import TestimonialForm


class TestimonialFormTests(TestCase):

    def test_form_valid__when_valid_data__expect_valid(self):
        valid_data = {
            'quote': 'This is a great organization!',
            'allow_posting': True,
        }
        form = TestimonialForm(data=valid_data)
        self.assertTrue(form.is_valid())

    def test_form_valid__when_invalid_data__expect_invalid(self):
        form_data = {
            'quote': '',

        }
        form = TestimonialForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('quote', form.errors)
        self.assertNotIn('allow_posting', form.errors)

    def test_allow_posting_widget_class__when_open__expect_html_class(self):
        form = TestimonialForm()
        self.assertEqual(
            form.fields['allow_posting'].widget.attrs['class'],
            'form-check-input'
        )

    def test_allow_posting_field_label__when_open__expect_label(self):
        form = TestimonialForm()
        self.assertEqual(
            form.fields['allow_posting'].label, 'I allow "Club for Future" to publish my testimonial on this website.'
        )
