class Movies(ORM.Model):

    def __init__(self, db:SQLite):
        self.db = db

        self.id_movie = ORM.Field(
         name='id_movie',
         type=ORM.BIGINT,
         not_null=True,
         auto_increment=True,
         primary_key=True)

        self.title = ORM.Field(
         name='title',
         type=ORM.TEXT,
         not_null=True,
         auto_increment=False,
         primary_key=False)

        self.duration = ORM.Field(
         name='duration',
         type=ORM.INTEGER,
         not_null=True,
         auto_increment=False,
         primary_key=False)

    # Create-s
    def create_movies(self, title: str, duration: int):
        self.db.push(f"""
        INSERT INTO Movies (title, duration)
        VALUES ({title}, {duration})""")

    # Read-s
    def get_all(self):
        self.db.push(f"""
                    SELECT * FROM Movies""")

        return self.db.fetchall()

    def get_by_id_movie(self, id_movie: int):
        self.db.push(f"""
                    SELECT * FROM Movies WHERE id_movie = {id_movie};""")

        return self.db.fetchall()

    def get_by_title(self, title: str):
        self.db.push(f"""
                    SELECT * FROM Movies WHERE title = {title};""")

        return self.db.fetchall()

    def det_by_duration(self, duration: int):
        self.db.push(f"""
                    SELECT * FROM Movies WHERE duration = {duration};""")

        return self.db.fetchall()
