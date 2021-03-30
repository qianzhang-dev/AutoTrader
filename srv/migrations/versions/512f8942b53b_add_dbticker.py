"""add DbTicker

Revision ID: 512f8942b53b
Revises: f32451caf180
Create Date: 2021-03-14 08:34:20.199944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '512f8942b53b'
down_revision = 'f32451caf180'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('db_ticker',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ticker', sa.NCHAR(length=10), nullable=False),
    sa.Column('currency', sa.NCHAR(length=10), nullable=False),
    sa.Column('market_code', sa.Enum('XNAS', 'OOTC', 'XNYS', 'BATS', 'ARCX', 'XASE', 'IEXG', name='dbmarketcode'), nullable=False),
    sa.Column('name', sa.NCHAR(length=255), nullable=False),
    sa.Column('description', sa.Text, nullable=True),
    sa.Column('sector', sa.Enum('BASIC_MATERIALS', 'INDUSTRIALS', 'FINANCIAL_SERVICES', 'ENERGY', 'CONSUMER_CYCLICAL', 'TECHNOLOGY', 'COMMUNICATION_SERVICES', 'REAL_ESTATE', 'HEALTHCARE', 'CONSUMER_DEFENSIVE', 'UTILITIES', 'ETF', name='dbstocksector'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('db_ticker')
    # ### end Alembic commands ###
