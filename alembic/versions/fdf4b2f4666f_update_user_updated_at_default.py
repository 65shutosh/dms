"""update_user_updated_at_default

Revision ID: fdf4b2f4666f
Revises: 001
Create Date: 2024-03-19 10:30:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = 'fdf4b2f4666f'
down_revision: Union[str, None] = '001'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Update existing rows to have updated_at set to created_at
    op.execute("UPDATE users SET updated_at = created_at WHERE updated_at IS NULL")
    
    # Alter the column to have a default value
    op.alter_column('users', 'updated_at',
        existing_type=sa.DateTime(timezone=True),
        server_default=func.now(),
        existing_nullable=False)


def downgrade() -> None:
    """Downgrade schema."""
    # Remove the default value
    op.alter_column('users', 'updated_at',
        existing_type=sa.DateTime(timezone=True),
        server_default=None,
        existing_nullable=False)
