"""updatefuck2 

Revision ID: c5307b0bb9ab
Revises: b2ac04c3a913
Create Date: 2020-05-31 22:05:11.146733

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5307b0bb9ab'
down_revision = 'b2ac04c3a913'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('address_table_ibfk_1', 'address_table', type_='foreignkey')
    op.create_foreign_key(None, 'address_table', 'address_table', ['users_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'address_table', type_='foreignkey')
    op.create_foreign_key('address_table_ibfk_1', 'address_table', 'user_table', ['users_id'], ['id'])
    # ### end Alembic commands ###
