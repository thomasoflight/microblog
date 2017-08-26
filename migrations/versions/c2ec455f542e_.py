"""empty message

Revision ID: c2ec455f542e
Revises: 83e66e1441d4
Create Date: 2017-08-25 21:35:42.812599

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c2ec455f542e'
down_revision = '83e66e1441d4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('curr_pstn', sa.Integer(), nullable=True),
    sa.Column('tasks', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tasks_curr_pstn'), 'tasks', ['curr_pstn'], unique=True)
    op.create_index(op.f('ix_tasks_name'), 'tasks', ['name'], unique=True)
    op.create_index(op.f('ix_tasks_tasks'), 'tasks', ['tasks'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tasks_tasks'), table_name='tasks')
    op.drop_index(op.f('ix_tasks_name'), table_name='tasks')
    op.drop_index(op.f('ix_tasks_curr_pstn'), table_name='tasks')
    op.drop_table('tasks')
    # ### end Alembic commands ###