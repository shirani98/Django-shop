from django.db import transaction
from django.db import models
from accounts.models import User
from django.db.models import Sum, Q, Count
from django.db.models.functions import Coalesce

# Create your models here.

class Transaction(models.Model):
    status_transaction = ((1, 'Charge'), (2, 'Purchase'), (3, 'Transfer_sent'),(4, 'Transfer_received'))

    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='user_transaction')
    amount = models.BigIntegerField()
    status = models.SmallIntegerField(default=1, choices=status_transaction)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.get_status_display()} : {self.amount}"

    def calculate_amount(email):
        postive_amount = Sum("user_transaction__amount",
                             filter=Q(user_transaction__status__in=[1,4]))
        negative_amount = Sum("user_transaction__amount", filter=Q(
            user_transaction__status__in=[2, 3]))
        final = User.objects.filter(email=email).aggregate(
            total=Coalesce(postive_amount, 0)-Coalesce(negative_amount, 0))
        return final['total']


class TransactionsArchive(models.Model):
    status_transaction = ((1, 'Charge'), (2, 'Purchase'), (3, 'Transfer_sent'),(4, 'Transfer_received'))

    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='user_archive')
    amount = models.BigIntegerField()
    status = models.SmallIntegerField(default=1, choices=status_transaction)
    created = models.DateTimeField(auto_now_add=True)

    def calculate_amount(email):
        postive_amount = Sum("user_archive__amount",
                             filter=Q(user_archive__status__in=[1,4]))
        negative_amount = Sum("user_archive__amount", filter=Q(
            user_archive__status__in=[2, 3]))
        return User.objects.filter(email=email).aggregate(total=Coalesce(postive_amount, 0)-Coalesce(negative_amount, 0))

    @classmethod
    def archive(cls):
        dataset = Transaction.objects.all().values('user', 'amount', 'status')
        for data in dataset:
            cls.objects.create(
                user_id=data['user'], amount=data['amount'], status=data['status'])
        Transaction.objects.all().delete()
        UserBalance.create_amount()

    def __str__(self):
        return f"{self.user} - {self.get_status_display()} : {self.amount}"


class UserBalance(models.Model):
    status_transaction = ((1, 'Charge'), (2, 'Purchase'), (3, 'Transfer'))

    user = models.ForeignKey(
        User, on_delete=models.PROTECT, related_name='user_transaction_archive')
    amount = models.BigIntegerField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.amount} - {self.created}"

    @classmethod
    def create_amount(cls):
        for user in User.objects.all():
            tr = TransactionsArchive.calculate_amount(user.email)

            if cls.objects.filter(user=user).exists():
                instance = cls.objects.get(user=user)
                if instance.amount != tr['total']:
                    instance.amount = 0
                    instance.amount += tr['total']
                    instance.save()
            else:
                cls.objects.create(user=user, amount=tr['total'])

    @classmethod
    def calculate_amount(cls, email):
        final = cls.objects.filter(user__email=email).values('amount')
        if len(final) > 0:
            final = final[0]
            return int(final['amount'])
        return 0

    @classmethod
    def final_amount(cls, email):
        return cls.calculate_amount(email) + Transaction.calculate_amount(email)

class Transfer(models.Model):
    sender = models.ForeignKey(User, related_name="sent", on_delete=models.PROTECT)
    receiver = models.ForeignKey(User, related_name="receiver" , on_delete=models.PROTECT)
    amount = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.sender} >> {self.receiver} : {self.amount}"
    
    @classmethod
    def transfer_amount(cls, email_sender, email_receiver , amount):
        if UserBalance.final_amount(email_sender)<amount:
            return "Transaction Not Allowed"
        
        user_sender = User.objects.get(email = email_sender)
        user_reciver = User.objects.get(email = email_receiver)
        with transaction.atomic():
            Transaction.objects.create(user = user_sender, amount = amount, status =3 )
            Transaction.objects.create(user = user_reciver, amount = amount, status = 4)
            cls.objects.create(sender = user_sender, receiver = user_reciver, amount = amount)
    
    