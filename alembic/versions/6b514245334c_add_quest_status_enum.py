"""Add quest status enum

Revision ID: 6b514245334c
Revises: 7e9a746031d1
Create Date: 2024-11-24 03:15:50.429319

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b514245334c'
down_revision: Union[str, None] = '7e9a746031d1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("ALTER TYPE queststatus ADD VALUE 'accepted';")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
