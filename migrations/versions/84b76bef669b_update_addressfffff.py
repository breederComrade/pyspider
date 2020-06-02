"""update addressfffff 

Revision ID: 84b76bef669b
Revises: 4eb2252f0c11
Create Date: 2020-06-01 00:04:15.600627

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '84b76bef669b'
down_revision = '4eb2252f0c11'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('u_id', sa.String(length=320), nullable=True),
    sa.Column('name', sa.String(length=320), nullable=True),
    sa.Column('grade', sa.String(length=320), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('u_id'),
    mysql_collate='utf8_general_ci'
    )
    op.create_table('teachers_info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('u_id', sa.String(length=320), nullable=True),
    sa.Column('name', sa.String(length=320), nullable=True),
    sa.Column('office', sa.String(length=320), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('u_id'),
    mysql_collate='utf8_general_ci'
    )
    op.create_table('student_teacher',
    sa.Column('student_id', sa.Integer(), nullable=True),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['student_id'], ['students_info.id'], ),
    sa.ForeignKeyConstraint(['teacher_id'], ['teachers_info.id'], )
    )
    op.drop_index('name', table_name='course')
    op.drop_table('course')
    op.drop_table('tags')
    op.drop_table('student')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('student',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('tags',
    sa.Column('student_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.Column('course_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['course_id'], ['course.id'], name='tags_ibfk_1'),
    sa.ForeignKeyConstraint(['student_id'], ['student.id'], name='tags_ibfk_2'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_table('course',
    sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('name', 'course', ['name'], unique=True)
    op.drop_table('student_teacher')
    op.drop_table('teachers_info')
    op.drop_table('students_info')
    # ### end Alembic commands ###