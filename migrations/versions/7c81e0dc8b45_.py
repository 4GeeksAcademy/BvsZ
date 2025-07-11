"""empty message

Revision ID: 7c81e0dc8b45
Revises: 0763d677d453
Create Date: 2025-07-03 18:05:15.670542

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7c81e0dc8b45'
down_revision = '0763d677d453'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=32), nullable=False))
        batch_op.add_column(sa.Column('age', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('language', sa.String(length=32), nullable=False))
        batch_op.add_column(sa.Column('country', sa.String(length=64), nullable=False))
        batch_op.add_column(sa.Column('is_verified', sa.Boolean(), nullable=False))
        batch_op.add_column(sa.Column('verification_token', sa.String(length=128), nullable=True))
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('verification_token')
        batch_op.drop_column('is_verified')
        batch_op.drop_column('country')
        batch_op.drop_column('language')
        batch_op.drop_column('age')
        batch_op.drop_column('username')

    # ### end Alembic commands ###
