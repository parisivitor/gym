"""empty message

Revision ID: 42dd7afac79f
Revises: fe956582d578
Create Date: 2023-03-11 22:56:39.870357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42dd7afac79f'
down_revision = 'fe956582d578'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('category_type', sa.Column('name', sa.String(length=50), nullable=False))
    op.alter_column('category_type', 'description',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    op.drop_constraint('category_type_nome_key', 'category_type', type_='unique')
    op.create_unique_constraint(None, 'category_type', ['uuid'])
    op.create_unique_constraint(None, 'category_type', ['name'])
    op.drop_column('category_type', 'nome')
    op.add_column('execution_type', sa.Column('name', sa.String(length=50), nullable=False))
    op.alter_column('execution_type', 'description',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    op.drop_constraint('execution_type_nome_key', 'execution_type', type_='unique')
    op.create_unique_constraint(None, 'execution_type', ['uuid'])
    op.create_unique_constraint(None, 'execution_type', ['name'])
    op.drop_column('execution_type', 'nome')
    op.create_unique_constraint(None, 'exercise', ['uuid'])
    op.add_column('exercise_type', sa.Column('name', sa.String(length=50), nullable=False))
    op.alter_column('exercise_type', 'description',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    op.drop_constraint('exercise_type_nome_key', 'exercise_type', type_='unique')
    op.create_unique_constraint(None, 'exercise_type', ['name'])
    op.create_unique_constraint(None, 'exercise_type', ['uuid'])
    op.drop_column('exercise_type', 'nome')
    op.add_column('measure_type', sa.Column('name', sa.String(length=50), nullable=False))
    op.alter_column('measure_type', 'description',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
    op.drop_constraint('measure_type_nome_key', 'measure_type', type_='unique')
    op.create_unique_constraint(None, 'measure_type', ['uuid'])
    op.create_unique_constraint(None, 'measure_type', ['name'])
    op.drop_column('measure_type', 'nome')
    op.create_unique_constraint(None, 'planned', ['uuid'])
    op.create_unique_constraint(None, 'train', ['uuid'])
    op.create_unique_constraint(None, 'workout', ['uuid'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'workout', type_='unique')
    op.drop_constraint(None, 'train', type_='unique')
    op.drop_constraint(None, 'planned', type_='unique')
    op.add_column('measure_type', sa.Column('nome', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'measure_type', type_='unique')
    op.drop_constraint(None, 'measure_type', type_='unique')
    op.create_unique_constraint('measure_type_nome_key', 'measure_type', ['nome'])
    op.alter_column('measure_type', 'description',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.drop_column('measure_type', 'name')
    op.add_column('exercise_type', sa.Column('nome', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'exercise_type', type_='unique')
    op.drop_constraint(None, 'exercise_type', type_='unique')
    op.create_unique_constraint('exercise_type_nome_key', 'exercise_type', ['nome'])
    op.alter_column('exercise_type', 'description',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.drop_column('exercise_type', 'name')
    op.drop_constraint(None, 'exercise', type_='unique')
    op.add_column('execution_type', sa.Column('nome', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'execution_type', type_='unique')
    op.drop_constraint(None, 'execution_type', type_='unique')
    op.create_unique_constraint('execution_type_nome_key', 'execution_type', ['nome'])
    op.alter_column('execution_type', 'description',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.drop_column('execution_type', 'name')
    op.add_column('category_type', sa.Column('nome', sa.VARCHAR(length=50), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'category_type', type_='unique')
    op.drop_constraint(None, 'category_type', type_='unique')
    op.create_unique_constraint('category_type_nome_key', 'category_type', ['nome'])
    op.alter_column('category_type', 'description',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
    op.drop_column('category_type', 'name')
    # ### end Alembic commands ###
