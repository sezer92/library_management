from celery import shared_task
from django.utils import timezone
from bibliothecaire.models import Member

@shared_task
def check_overdue_members():
    for member in Member.objects.all():
        if member.borrow_count > 0 and member.unblock_date and member.unblock_date < timezone.now().date():
            member.blocked = True
            member.save()
            print(f"Member {member.name} has been blocked due to overdue borrows.")
