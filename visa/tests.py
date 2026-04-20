from django.test import TestCase, Client, override_settings
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.messages import get_messages

from visa.models import VisaInvitationLetter
from django.contrib.messages.test import MessagesTestMixin


@override_settings(VISA_LETTER_REQUESTS_OPEN=True)
class VisaLetterUserFlowTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        self.client.login(username="testuser", password="testpass123")

    def test_create_form_displays_correctly(self):
        """Test that the create form displays with all expected elements"""
        url = reverse("visa:visa_letter_form")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        # Check that it's a form page (more basic check)
        self.assertContains(response, "<form")

        # Check form fields are present
        self.assertContains(response, "full_name")
        self.assertContains(response, "passport_number")
        self.assertContains(response, "country_of_origin")
        self.assertContains(response, "embassy_address")

        # Check submit button
        self.assertContains(response, "Request Visa Letter")

    def test_create_form_submission_success(self):
        """Test successful visa letter creation through form"""
        url = reverse("visa:visa_letter_form")
        form_data = {
            "full_name": "John Doe",
            "passport_number": "AB1234567",
            "country_of_origin": "US",
            "embassy_address": "123 Embassy Street\nPretoria, South Africa",
        }

        response = self.client.post(url, data=form_data)

        # Should redirect to detail view
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("visa:visa_letter_detail"))

        # Check visa letter was created with correct data
        visa_letter = VisaInvitationLetter.objects.get(user=self.user)
        self.assertEqual(visa_letter.full_name, "John Doe")
        self.assertEqual(visa_letter.passport_number, "AB1234567")
        self.assertEqual(visa_letter.country_of_origin, "US")
        self.assertEqual(visa_letter.status, "pending")

    def test_create_form_validation_errors(self):
        """Test that form shows validation errors for missing fields"""
        url = reverse("visa:visa_letter_form")
        form_data = {
            "full_name": "",  # Required field left empty
            "passport_number": "AB1234567",
            "country_of_origin": "",  # Required field left empty
            "embassy_address": "123 Embassy Street",
        }

        response = self.client.post(url, data=form_data)

        # Should stay on form page with errors
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This field is required")

        # No visa letter should be created
        self.assertFalse(VisaInvitationLetter.objects.filter(user=self.user).exists())

    def test_detail_view_displays_visa_letter_info(self):
        """Test that detail view shows visa letter information correctly"""
        # Create visa letter
        visa_letter = VisaInvitationLetter.objects.create(
            user=self.user,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street\nPretoria, South Africa",
            status="pending",
        )

        url = reverse("visa:visa_letter_detail")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        # Check page title
        self.assertContains(response, "Visa Letter Request Details")

        # Check visa letter information is displayed
        self.assertContains(response, "John Doe")
        self.assertContains(response, "AB1234567")
        self.assertContains(response, "United States")  # Country name, not code
        self.assertContains(response, "123 Embassy Street")
        self.assertContains(response, "Pretoria, South Africa")

        # Check status display
        self.assertContains(response, "Pending")

        # Check edit button is present when requests are open
        self.assertContains(response, "Edit Visa Letter Request")

    def test_detail_view_shows_different_status_colors(self):
        """Test that different visa letter statuses show appropriate styling"""
        # Test pending status
        visa_letter = VisaInvitationLetter.objects.create(
            user=self.user,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street",
            status="pending",
        )

        url = reverse("visa:visa_letter_detail")
        response = self.client.get(url)

        # Should have yellow styling for pending
        self.assertContains(response, "bg-yellow-100 text-yellow-800")
        self.assertContains(response, "being reviewed by our team")

        # Test approved status
        visa_letter.status = "approved"
        visa_letter.save()

        response = self.client.get(url)
        self.assertContains(response, "bg-green-100 text-green-800")
        self.assertContains(response, "has been approved")

        # Test rejected status
        visa_letter.status = "rejected"
        visa_letter.rejection_reason = "Incomplete documentation"
        visa_letter.save()

        response = self.client.get(url)
        self.assertContains(response, "bg-red-100 text-red-800")
        self.assertContains(response, "Rejection Reason")
        self.assertContains(response, "Incomplete documentation")

    def test_update_form_displays_existing_data(self):
        """Test that update form is pre-populated with existing visa letter data"""
        # Create visa letter
        VisaInvitationLetter.objects.create(
            user=self.user,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street\nPretoria, South Africa",
        )

        url = reverse("visa:visa_letter_edit")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        # Check that form is pre-populated with existing data
        self.assertContains(response, 'value="John Doe"')
        self.assertContains(response, 'value="AB1234567"')
        self.assertContains(response, "123 Embassy Street")
        self.assertContains(response, "Pretoria, South Africa")

    def test_update_form_submission_success(self):
        """Test successful visa letter update through form"""
        # Create visa letter
        visa_letter = VisaInvitationLetter.objects.create(
            user=self.user,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street",
        )

        url = reverse("visa:visa_letter_edit")
        form_data = {
            "full_name": "Jane Smith",
            "passport_number": "CD7890123",
            "country_of_origin": "CA",
            "embassy_address": "456 Embassy Avenue\nCape Town, South Africa",
        }

        response = self.client.post(url, data=form_data)

        # Should redirect to detail view
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("visa:visa_letter_detail"))

        # Check visa letter was updated
        visa_letter.refresh_from_db()
        self.assertEqual(visa_letter.full_name, "Jane Smith")
        self.assertEqual(visa_letter.passport_number, "CD7890123")
        self.assertEqual(visa_letter.country_of_origin, "CA")

    def test_update_form_resets_status_to_pending(self):
        """Test that editing a visa letter resets status to pending"""
        # Create visa letter with approved status
        visa_letter = VisaInvitationLetter.objects.create(
            user=self.user,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street",
            status="approved",  # Start with approved status
        )

        # Verify initial status
        self.assertEqual(visa_letter.status, "approved")

        # Update the visa letter
        url = reverse("visa:visa_letter_edit")
        form_data = {
            "full_name": "John Doe",  # Same name
            "passport_number": "AB1234567",  # Same passport
            "country_of_origin": "US",  # Same country
            "embassy_address": "456 Different Embassy Street",  # Only change address
        }

        response = self.client.post(url, data=form_data)

        # Should redirect to detail view
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("visa:visa_letter_detail"))

        # Check that status was reset to pending
        visa_letter.refresh_from_db()
        self.assertEqual(visa_letter.status, "pending")
        self.assertEqual(visa_letter.embassy_address, "456 Different Embassy Street")

    def test_update_form_resets_status_from_rejected_to_pending(self):
        """Test that editing a rejected visa letter resets status to pending"""
        # Create visa letter with rejected status
        visa_letter = VisaInvitationLetter.objects.create(
            user=self.user,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street",
            status="rejected",
            rejection_reason="Incomplete documentation",
        )

        # Verify initial status
        self.assertEqual(visa_letter.status, "rejected")
        self.assertIsNotNone(visa_letter.rejection_reason)

        # Update the visa letter
        url = reverse("visa:visa_letter_edit")
        form_data = {
            "full_name": "John Updated Doe",
            "passport_number": "AB1234567",
            "country_of_origin": "US",
            "embassy_address": "123 Embassy Street",
        }

        response = self.client.post(url, data=form_data)

        # Should redirect to detail view
        self.assertEqual(response.status_code, 302)

        # Check that status was reset to pending and rejection reason cleared
        visa_letter.refresh_from_db()
        self.assertEqual(visa_letter.status, "pending")
        self.assertEqual(visa_letter.full_name, "John Updated Doe")
        # Note: rejection_reason should remain as it's useful historical data

    def test_navigation_flow_new_user(self):
        """Test complete navigation flow for user without visa letter"""
        # User starts by going to detail view (shouldn't exist)
        detail_url = reverse("visa:visa_letter_detail")
        response = self.client.get(detail_url)

        # Should redirect to create form
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("visa:visa_letter_form"))

        # Follow redirect to create form
        response = self.client.get(reverse("visa:visa_letter_form"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Request Visa Letter")

    def test_navigation_flow_existing_user(self):
        """Test navigation flow for user with existing visa letter"""
        # Create visa letter
        VisaInvitationLetter.objects.create(
            user=self.user,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street",
        )

        # User tries to access create form (should redirect to detail)
        create_url = reverse("visa:visa_letter_form")
        response = self.client.get(create_url)

        # Should redirect to detail view with message
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("visa:visa_letter_detail"))

    def test_success_messages_display(self):
        """Test that success messages are shown to users"""
        # Test create success message
        url = reverse("visa:visa_letter_form")
        form_data = {
            "full_name": "John Doe",
            "passport_number": "AB1234567",
            "country_of_origin": "US",
            "embassy_address": "123 Embassy Street",
        }

        response = self.client.post(url, data=form_data, follow=True)
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(len(messages), 1)
        self.assertIn("submitted successfully", str(messages[0]))
        self.assertIn("email once it has been reviewed", str(messages[0]))

    def test_update_success_message_includes_review_notice(self):
        """Test that update success message mentions it will be reviewed again"""
        # Create visa letter first
        VisaInvitationLetter.objects.create(
            user=self.user,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street",
        )

        url = reverse("visa:visa_letter_edit")
        form_data = {
            "full_name": "Jane Smith",
            "passport_number": "CD7890123",
            "country_of_origin": "CA",
            "embassy_address": "456 Embassy Avenue",
        }

        response = self.client.post(url, data=form_data, follow=True)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertIn("updated successfully", str(messages[0]))
        self.assertIn("reviewed again by our team", str(messages[0]))

    def test_buttons_lead_to_correct_views(self):
        """Test that buttons in templates lead to correct URLs"""
        # Create visa letter
        VisaInvitationLetter.objects.create(
            user=self.user,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street",
        )

        # Check detail view has edit button that links correctly
        detail_url = reverse("visa:visa_letter_detail")
        response = self.client.get(detail_url)

        edit_url = reverse("visa:visa_letter_edit")
        self.assertContains(response, f'href="{edit_url}"')
        self.assertContains(response, "Edit Visa Letter Request")


@override_settings(VISA_LETTER_REQUESTS_OPEN=False)
class VisaLetterClosedTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        self.client.login(username="testuser", password="testpass123")

    def test_create_view_redirects_when_closed(self):
        """Test that create view redirects with message when requests are closed"""
        url = reverse("visa:visa_letter_form")
        response = self.client.get(url)

        # Should redirect (exact URL doesn't matter for this test)
        self.assertEqual(response.status_code, 302)

    def test_update_view_redirects_when_closed(self):
        """Test that update view redirects when requests are closed"""
        # Create visa letter first
        VisaInvitationLetter.objects.create(
            user=self.user,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street",
        )

        url = reverse("visa:visa_letter_edit")
        response = self.client.get(url)

        # Should redirect (exact URL doesn't matter for this test)
        self.assertEqual(response.status_code, 302)

    def test_detail_view_hides_edit_button_when_closed(self):
        """Test that edit button is hidden in detail view when requests are closed"""
        # Create visa letter
        VisaInvitationLetter.objects.create(
            user=self.user,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street",
        )

        url = reverse("visa:visa_letter_detail")
        response = self.client.get(url)

        # Should show visa letter details but no edit button
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "John Doe")
        self.assertNotContains(response, "Edit Visa Letter Request")


class VisaLetterAuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_unauthenticated_user_redirected_to_login(self):
        """Test that unauthenticated users are redirected to login"""
        urls_to_test = [
            reverse("visa:visa_letter_form"),
            reverse("visa:visa_letter_detail"),
            reverse("visa:visa_letter_edit"),
        ]

        for url in urls_to_test:
            response = self.client.get(url)
            self.assertEqual(response.status_code, 302)
            self.assertIn("/accounts/login/", response.url)


# Profile menu button tests are integration tests that depend on wafer infrastructure
# They should be tested manually or in integration test suite


@override_settings(VISA_LETTER_REQUESTS_OPEN=True)
class VisaLetterDownloadTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpass123"
        )
        self.client.login(username="testuser", password="testpass123")

    def test_download_button_shows_for_approved_letters(self):
        """Test that download button appears for approved visa letters"""
        # Create approved visa letter
        VisaInvitationLetter.objects.create(
            user=self.user,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street",
            status="approved",
        )

        url = reverse("visa:visa_letter_detail")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Download PDF Letter")
        self.assertContains(response, 'href="/visa_letters/letter/download/"')

    def test_download_button_hidden_for_pending_letters(self):
        """Test that download button is hidden for pending visa letters"""
        # Create pending visa letter
        VisaInvitationLetter.objects.create(
            user=self.user,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street",
            status="pending",
        )

        url = reverse("visa:visa_letter_detail")
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Download PDF Letter")

    def test_download_view_requires_approved_status(self):
        """Test that download view only works for approved letters"""
        # Create pending visa letter
        VisaInvitationLetter.objects.create(
            user=self.user,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street",
            status="pending",
        )

        url = reverse("visa:visa_letter_download")
        response = self.client.get(url)

        # Should redirect back to detail view
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("visa:visa_letter_detail"))

    def test_download_view_requires_existing_letter(self):
        """Test that download view requires user to have a visa letter"""
        url = reverse("visa:visa_letter_download")
        response = self.client.get(url)

        # Should return 404 when no visa letter exists
        self.assertEqual(response.status_code, 404)


@override_settings(VISA_LETTER_REQUESTS_OPEN=True)
class VisaLetterBulkAdminTests(MessagesTestMixin, TestCase):
    def setUp(self):
        self.client = Client()
        self.admin_user = User.objects.create_superuser(
            username="admin", email="admin@example.com", password="adminpass123"
        )
        self.regular_user1 = User.objects.create_user(
            username="user1", email="user1@example.com", password="userpass123"
        )
        self.regular_user2 = User.objects.create_user(
            username="user2", email="user2@example.com", password="userpass123"
        )
        self.client.login(username="admin", password="adminpass123")

    def test_bulk_reject_redirects_to_form_view(self):
        """Test that bulk reject action redirects to form view"""
        visa_letter1 = VisaInvitationLetter.objects.create(
            user=self.regular_user1,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street",
            status="pending",
        )

        visa_letter2 = VisaInvitationLetter.objects.create(
            user=self.regular_user2,
            full_name="Jane Smith",
            passport_number="CD7890123",
            country_of_origin="CA",
            embassy_address="456 Embassy Avenue",
            status="pending",
        )

        from visa.admin import VisaInvitationLetterAdmin
        from django.contrib.admin.sites import AdminSite

        admin_instance = VisaInvitationLetterAdmin(VisaInvitationLetter, AdminSite())
        queryset = VisaInvitationLetter.objects.filter(
            id__in=[visa_letter1.id, visa_letter2.id]
        )

        # Create mock request
        from django.test import RequestFactory

        request = RequestFactory().get("/admin/")
        request.user = self.admin_user

        response = admin_instance.bulk_action_reject_visa_letters(request, queryset)

        # Should redirect to bulk reject view with IDs
        self.assertEqual(response.status_code, 302)
        self.assertIn("bulk-reject", response.url)
        self.assertIn("ids=", response.url)
        # Check that both IDs are present (order might vary)
        self.assertIn(str(visa_letter1.id), response.url)
        self.assertIn(str(visa_letter2.id), response.url)

    def test_bulk_reject_form_view_processes_submission(self):
        """Test that bulk reject form view processes valid form submission"""
        visa_letter1 = VisaInvitationLetter.objects.create(
            user=self.regular_user1,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street",
            status="pending",
        )

        visa_letter2 = VisaInvitationLetter.objects.create(
            user=self.regular_user2,
            full_name="Jane Smith",
            passport_number="CD7890123",
            country_of_origin="CA",
            embassy_address="456 Embassy Avenue",
            status="pending",
        )

        # Use the test client instead of RequestFactory for proper message support
        url = f"/admin/visa/visainvitationletter/bulk-reject/?ids={visa_letter1.id},{visa_letter2.id}"
        response = self.client.post(url, {
            "rejection_reason": "Missing required documents",
            "permanently_reject": False,
        })

        # Should redirect to admin changelist
        self.assertEqual(response.status_code, 302)
        self.assertIn("visa/visainvitationletter/", response.url)

        # Check that both letters were rejected
        visa_letter1.refresh_from_db()
        visa_letter2.refresh_from_db()

        self.assertEqual(visa_letter1.status, "rejected")
        self.assertEqual(visa_letter1.rejection_reason, "Missing required documents")
        self.assertEqual(visa_letter2.status, "rejected")
        self.assertEqual(visa_letter2.rejection_reason, "Missing required documents")

    def test_bulk_reject_permanent_rejection(self):
        """Test that bulk reject form view handles permanent rejection"""
        visa_letter = VisaInvitationLetter.objects.create(
            user=self.regular_user1,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street",
            status="pending",
        )

        # Use the test client for proper message support
        url = f"/admin/visa/visainvitationletter/bulk-reject/?ids={visa_letter.id}"
        response = self.client.post(url, {
            "rejection_reason": "Fraudulent application", 
            "permanently_reject": True
        })

        # Should redirect to admin changelist
        self.assertEqual(response.status_code, 302)

        # Check that letter was permanently rejected
        visa_letter.refresh_from_db()
        self.assertEqual(visa_letter.status, "permanently rejected")
        self.assertEqual(visa_letter.rejection_reason, "Fraudulent application")

    def test_bulk_reject_form_view_displays_form(self):
        """Test that bulk reject form view displays form on GET"""
        visa_letter = VisaInvitationLetter.objects.create(
            user=self.regular_user1,
            full_name="John Doe",
            passport_number="AB1234567",
            country_of_origin="US",
            embassy_address="123 Embassy Street",
            status="pending",
        )

        # Use the test client for proper message support
        url = f"/admin/visa/visainvitationletter/bulk-reject/?ids={visa_letter.id}"
        response = self.client.get(url)

        # Should render form template
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "rejection_reason")
        self.assertContains(response, "permanently_reject")

        # Check that letter status was not changed
        visa_letter.refresh_from_db()
        self.assertEqual(visa_letter.status, "pending")
