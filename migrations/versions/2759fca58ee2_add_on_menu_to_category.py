"""Add on_menu to Category

Revision ID: 2759fca58ee2
Revises: 
Create Date: 2020-07-18 15:29:49.279631

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2759fca58ee2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category', sa.Column('on_menu', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('category', 'on_menu')
    # ### end Alembic commands ###