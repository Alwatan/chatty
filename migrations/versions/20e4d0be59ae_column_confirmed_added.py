"""column confirmed added

Revision ID: 20e4d0be59ae
Revises: 6a98a11e56d9
Create Date: 2018-01-28 10:28:46.718031

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '20e4d0be59ae'
down_revision = '6a98a11e56d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
