"""initial migration

Revision ID: 2f5e11ea7f1c
Revises: 
Create Date: 2017-03-12 20:56:28.655129

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f5e11ea7f1c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('articles')
    op.drop_table('authors')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('articles',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.TEXT(), nullable=True),
    sa.Column('content', sa.TEXT(), nullable=True),
    sa.Column('author_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], [u'authors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
