"""Add table

Revision ID: 5100c48aece4
Revises: 
Create Date: 2023-07-08 19:36:12.070807

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5100c48aece4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('charityproject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('full_amount', sa.Integer(), nullable=True),
    sa.Column('invested_amount', sa.Integer(), nullable=True),
    sa.Column('fully_invested', sa.Boolean(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('close_date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_charityproject_create_date'), 'charityproject', ['create_date'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=320), nullable=False),
    sa.Column('hashed_password', sa.String(length=1024), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_table('donation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('full_amount', sa.Integer(), nullable=True),
    sa.Column('invested_amount', sa.Integer(), nullable=True),
    sa.Column('fully_invested', sa.Boolean(), nullable=True),
    sa.Column('create_date', sa.DateTime(), nullable=True),
    sa.Column('close_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_donation_create_date'), 'donation', ['create_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_donation_create_date'), table_name='donation')
    op.drop_table('donation')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_charityproject_create_date'), table_name='charityproject')
    op.drop_table('charityproject')
    # ### end Alembic commands ###
