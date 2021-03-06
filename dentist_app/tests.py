from __future__ import absolute_import
from django.test import TestCase, override_settings
from dentist_app.views import get_index, get_ourteam, get_contact, get_contact_thanks
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from accounts.models import User

@override_settings(STATICFILES_STORAGE=None)
class PagesTest(TestCase):

    def setUp(self):
        super(PagesTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('letmein')
        self.user.save()
        self.login = self.client.login(username='testuser',
                                       password='letmein')
        self.assertEqual(self.login, True)

    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)

    def test_home_page_status_code_is_ok(self):
        home_page = self.client.get('/')
        self.assertEqual(home_page.status_code, 200)

    def test_check_content_is_correct(self):
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "index.html")
        home_page_template_output = render_to_response("index.html", {'user': self.user}).content
        self.assertEqual(home_page.content, home_page_template_output)

    def test_ourteam_page_resolves(self):
        page = resolve('/ourteam/')
        self.assertEqual(page.func, get_ourteam)

    def test_ourteam_page_status_code_is_ok(self):
        page = self.client.get('/ourteam/')
        self.assertEqual(page.status_code, 200)

    def test_check_ourteam_content_is_correct(self):
        page = self.client.get('/ourteam/')
        self.assertTemplateUsed(page, "ourteam.html")
        page_template_output = render_to_response("ourteam.html", {'user': self.user}).content
        self.assertEqual(page.content, page_template_output)

    def test_contact_page_resolves(self):
        page = resolve('/contact/')
        self.assertEqual(page.func, get_contact)

    def test_contact_page_status_code_is_ok(self):
        page = self.client.get('/contact/')
        self.assertEqual(page.status_code, 200)

    def test_check_contact_content_is_correct(self):
        page = self.client.get('/contact/')
        self.assertTemplateUsed(page, "contacts/contact.html")
        page_template_output = render_to_response("contacts/contact.html", {'user': self.user}).content
        self.assertEqual(page.content, page_template_output)

    def test_contact_thanks_page_resolves(self):
        page = resolve('/contact_thanks/')
        self.assertEqual(page.func, get_contact_thanks)

    def test_contact_thanks_page_status_code_is_ok(self):
        page = self.client.get('/contact_thanks/')
        self.assertEqual(page.status_code, 200)

    def test_check_contact_thanks_content_is_correct(self):
        page = self.client.get('/contact_thanks/')
        self.assertTemplateUsed(page, "contacts/contact_thanks.html")
        page_template_output = render_to_response("contacts/contact_thanks.html", {'user': self.user}).content
        self.assertEqual(page.content, page_template_output)
