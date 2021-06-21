"""empty message

Revision ID: 948bc03ffe21
Revises: 
Create Date: 2021-06-21 18:18:22.773869

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '948bc03ffe21'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('video',
    sa.Column('id', sa.String(length=48), nullable=False),
    sa.Column('video_id', sa.String(length=64), nullable=False),
    sa.Column('title', sa.String(length=250), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('thumbnail', sa.Text(length=2048), nullable=False),
    sa.Column('published_at', sa.DateTime(timezone=True), nullable=False),
    sa.PrimaryKeyConstraint('id', 'video_id')
    )
    op.create_index(op.f('ix_video_published_at'), 'video', ['published_at'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_video_published_at'), table_name='video')
    op.drop_table('video')
    # ### end Alembic commands ###