"""Create Order Table

Revision ID: 10439a8b788d
Revises: 719fb2c52f69
Create Date: 2021-03-16 19:40:35.327631

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '10439a8b788d'
down_revision = '719fb2c52f69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'order',
        sa.Column('id', mysql.INTEGER(unsigned=True), autoincrement=True,
                  nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('vehicle_manufacturer', sa.String(length=16), nullable=False),
        sa.Column('model', sa.String(length=16), nullable=False),
        sa.Column('price', sa.Integer(), nullable=False),
        sa.Column('currency', sa.String(length=3), nullable=False),
        sa.Column('created', sa.TIMESTAMP(),
                  server_default=sa.text('CURRENT_TIMESTAMP'),
                  nullable=False),
        sa.Column('updated', sa.TIMESTAMP(),
                  server_default=sa.text(
                      'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP')),
        sa.ForeignKeyConstraint(['user_id'], ['user.id'],
                                onupdate='CASCADE', ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    # ### end Alembic commands ###
