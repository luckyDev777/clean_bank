"""update tables

Revision ID: 8bc61624c0fc
Revises: 055b35dc8d2f
Create Date: 2023-07-16 18:26:38.887290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8bc61624c0fc'
down_revision = '055b35dc8d2f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('accounts', sa.Column('customer_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'accounts', 'customers', ['customer_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'accounts', type_='foreignkey')
    op.drop_column('accounts', 'customer_id')
    # ### end Alembic commands ###
