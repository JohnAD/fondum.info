import random
import mongoengine as db
import msg

import account__models as models

#######################################
#
#    ACCOUNT
#
#######################################

def create_account(user, person_name):
    account = models.Account()
    account.ref_user = user
    account.s_name = person_name
    account.save()
    return account


def read_account_byUser(user):
    try:
        account = models.Account.objects.get(ref_user=user.id)
    except db.DoesNotExist:
        return msg.err("Cannot find account {}".format(user.id))
    return account
