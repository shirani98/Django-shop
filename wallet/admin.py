from django.contrib import admin

from wallet.models import Transaction, TransactionsArchive, Transfer, UserBalance

# Register your models here.

admin.site.register(Transaction)
admin.site.register(TransactionsArchive)
admin.site.register(UserBalance)
admin.site.register(Transfer)
