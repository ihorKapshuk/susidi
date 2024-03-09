from django.test import TestCase
from home_manager.models import Anon, Comment
from accounts.models import PhoneNumbers
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import datetime

class PhoneNumbersTestCase(TestCase):

    def setUp(self) -> None:
        PhoneNumbers.objects.create(
            owner_id="Vasil_T",
            phone_number="0977654321",
            is_account_created=False
        )
        PhoneNumbers.objects.create(
            owner_id="Maria_S",
            phone_number="0637654321",
            is_account_created=False
        )
    
    def test_creation(self):
        num1 = PhoneNumbers.objects.get(owner_id="Vasil_T")
        num2 = PhoneNumbers.objects.get(owner_id="Maria_S")
        self.assertEqual(num1.phone_number, "0977654321")
        self.assertEqual(num2.phone_number, "0637654321")
        self.assertEqual(num1.is_account_created, False)
        self.assertEqual(num2.is_account_created, False)

class AnonTestCase(TestCase):

    def setUp(self) -> None:
        global cur_time
        cur_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        samp_image = SimpleUploadedFile('test_image.jpg', b"file_content", content_type='image/jpeg')
        Anon.objects.create(
            post_author="Vasil_T",
            post_name="11",
            post_text="22",
            post_date=cur_time,
            post_category=1,
            post_image=samp_image
        )
        Anon.objects.create(
            post_author="Maria_S",
            post_name="33",
            post_text="44",
            post_date=cur_time,
            post_category=2
        )
    
    def test_creation(self):
        post1 = Anon.objects.get(post_author="Vasil_T")
        post2 = Anon.objects.get(post_author="Maria_S")
        self.assertEqual(post1.post_name, "11")
        self.assertEqual(post2.post_name, "33")
        self.assertEqual(post1.post_text, "22")
        self.assertEqual(post2.post_text, "44")
        self.assertEqual(post1.post_date, cur_time)
        self.assertEqual(post2.post_date, cur_time)
        self.assertEqual(post1.post_category, 1)
        self.assertEqual(post2.post_category, 2)
        self.assertEqual(post1.post_image, "images/test_image.jpg")
        self.assertEqual(post2.post_image, "")
        Anon.objects.get(post_author="Vasil_T").post_image.delete(save=False)

class CommentTestCase(TestCase):

    def setUp(self) -> None:
        global cur_time2
        cur_time2 = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        samp_image = SimpleUploadedFile('test_image.jpg', b"file_content", content_type='image/jpeg')
        Comment.objects.create(
            com_post_id=25,
            com_author="Vasil_T",
            com_text="22",
            com_date=cur_time2,
            com_category=1,
            com_image=samp_image
        )
        Comment.objects.create(
            com_post_id=26,
            com_author="Maria_S",
            com_text="44",
            com_date=cur_time2,
            com_category=2
        )
    
    def test_creation(self):
        com1 = Comment.objects.get(com_post_id=25)
        com2 = Comment.objects.get(com_post_id=26)
        self.assertEqual(com1.com_author, "Vasil_T")
        self.assertEqual(com2.com_author, "Maria_S")
        self.assertEqual(com1.com_text, "22")
        self.assertEqual(com2.com_text, "44")
        self.assertEqual(com1.com_date, cur_time2)
        self.assertEqual(com2.com_date, cur_time2)
        self.assertEqual(com1.com_category, 1)
        self.assertEqual(com2.com_category, 2)
        self.assertEqual(com1.com_image, "images/test_image.jpg")
        self.assertEqual(com2.com_image, "")
        Comment.objects.get(com_post_id=25).com_image.delete(save=False)