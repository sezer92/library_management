from django.test import TestCase
from bibliothecaire.models import Member

class MemberTestCase(TestCase):
    def setUp(self):
        self.member = Member.objects.create(name="John Doe")

    def test_can_borrow(self):
        self.assertTrue(self.member.can_borrow())
        self.member.borrow_count = 3
        self.member.save()
        self.assertFalse(self.member.can_borrow())
        self.member.blocked = True
        self.member.save()
        self.assertFalse(self.member.can_borrow())

    def test_create_member(self):
        member = Member.objects.get(name="John Doe")
        self.assertEqual(member.name, "John Doe")

    def test_borrow_limit(self):
        member = Member.objects.create(name="Jane Doe", borrow_count=3)
        self.assertFalse(member.can_borrow())

    def test_update_member(self):
        self.member.name = "Jane Doe"
        self.member.save()
        member = Member.objects.get(id=self.member.id)
        self.assertEqual(member.name, "Jane Doe")

    def test_delete_member(self):
        self.member.delete()
        self.assertEqual(Member.objects.count(), 0)
