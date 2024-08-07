from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.pydantic import pydantic_model_creator


def default_scope():
    return ["authenticated"]


class Users(Model):
    """
    The User model
    """

    id = fields.IntField(primary_key=True)
    username = fields.CharField(max_length=20, unique=True)
    first_name = fields.CharField(max_length=50, null=True)
    last_name = fields.CharField(max_length=50, null=True)
    p_hash = fields.BinaryField(max_length=128, null=True)
    p_salt = fields.BinaryField(max_length=128, null=True)
    scope = fields.JSONField(default=default_scope)
    info = fields.JSONField(default=dict)

    class PydanticMeta:
        exclude = ["p_hash", "p_salt"]


User_Pydantic = pydantic_model_creator(Users, name="User")
UserIn_Pydantic = pydantic_model_creator(Users, name="UserIn", exclude_readonly=True)


class Session(Model):

    id = fields.IntField(primary_key=True)
    token = fields.CharField(max_length=128, unique=True, db_index=True)
    user = fields.IntField(default=0)
    created_at = fields.DatetimeField(auto_now_add=True)
    expires_at = fields.DatetimeField(auto_now_add=True)


Session_Pydantic = pydantic_model_creator(Session, name="Session")

