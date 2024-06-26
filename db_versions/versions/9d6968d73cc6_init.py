"""init

Revision ID: 9d6968d73cc6
Revises: 
Create Date: 2023-12-22 18:44:44.435010

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9d6968d73cc6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('user_id', sa.BigInteger(), nullable=False),
    sa.Column('full_name', sa.String(length=255), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('language', sa.Enum('uz', 'ru'), nullable=True),
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    # ### end Alembic commands ###
