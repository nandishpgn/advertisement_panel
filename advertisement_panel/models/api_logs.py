import sqlalchemy


metadata = sqlalchemy.MetaData()
posts = sqlalchemy.Table(
    "advertisement_panel",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("title", sqlalchemy.String(length=100), nullable=True),
    sqlalchemy.Column("description", sqlalchemy.String(length=500), nullable=True),
    sqlalchemy.Column("photo", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("start_date",sqlalchemy.Date()),
    sqlalchemy.Column("end_date",sqlalchemy.Date()),
    sqlalchemy.Column("campaign_start_date",sqlalchemy.Date()),
    sqlalchemy.Column("campaign_end_date",sqlalchemy.Date()),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime()),
    sqlalchemy.Column("updated_date", sqlalchemy.DateTime())
)
