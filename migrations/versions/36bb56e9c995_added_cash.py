"""Added cash

Revision ID: 36bb56e9c995
Revises: c27a0ac2bcfe
Create Date: 2023-02-23 07:02:22.427032

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '36bb56e9c995'
down_revision = 'c27a0ac2bcfe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('cash', sa.Integer(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('cash')

    # ### end Alembic commands ###