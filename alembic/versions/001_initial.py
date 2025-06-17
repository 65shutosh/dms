"""initial

Revision ID: 001
Revises: 
Create Date: 2024-03-19 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '001'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    # Check if enum exists before creating it
    conn = op.get_bind()
    inspector = sa.inspect(conn)
    enums = inspector.get_enums()
    enum_names = [enum['name'] for enum in enums]
    
    if 'deliverystatus' not in enum_names:
        deliverystatus = postgresql.ENUM('pending', 'assigned', 'picked_up', 'in_transit', 'delivered', 'cancelled', name='deliverystatus')
        deliverystatus.create(op.get_bind())
    # Use the already created enum type for the status column
    deliverystatus_type = postgresql.ENUM('pending', 'assigned', 'picked_up', 'in_transit', 'delivered', 'cancelled', name='deliverystatus', create_type=False)

    # Create users table
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('email', sa.String(), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('full_name', sa.String(), nullable=False),
        sa.Column('is_active', sa.Boolean(), nullable=False, default=True),
        sa.Column('is_superuser', sa.Boolean(), nullable=False, default=False),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('email')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)

    # Create deliveries table
    op.create_table(
        'deliveries',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('tracking_number', sa.String(), nullable=False),
        sa.Column('sender_name', sa.String(), nullable=False),
        sa.Column('sender_phone', sa.String(), nullable=False),
        sa.Column('sender_address', sa.String(), nullable=False),
        sa.Column('recipient_name', sa.String(), nullable=False),
        sa.Column('recipient_phone', sa.String(), nullable=False),
        sa.Column('recipient_address', sa.String(), nullable=False),
        sa.Column('package_description', sa.String(), nullable=False),
        sa.Column('weight', sa.Float(), nullable=False),
        sa.Column('status', deliverystatus_type, nullable=False),
        sa.Column('assigned_to', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
        sa.Column('updated_at', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
        sa.ForeignKeyConstraint(['assigned_to'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_deliveries_tracking_number'), 'deliveries', ['tracking_number'], unique=True)

def downgrade():
    op.drop_index(op.f('ix_deliveries_tracking_number'), table_name='deliveries')
    op.drop_table('deliveries')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    
    # Drop the enum type
    deliverystatus = postgresql.ENUM(name='deliverystatus')
    deliverystatus.drop(op.get_bind()) 