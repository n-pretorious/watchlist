"""fixing logic

Revision ID: 288032b0a8cf
Revises: f22ffb2d578a
Create Date: 2020-09-23 10:11:39.419772

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '288032b0a8cf'
down_revision = 'f22ffb2d578a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
