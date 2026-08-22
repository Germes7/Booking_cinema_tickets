class Movies(ORM.Model):

    def __init__(self, db:SQLite):
        self.db = db

        self.id_movie = ORM.Field(
         name='id_movie',
         type=ORM.INTEGER,
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
        VALUES ('{title}', {duration})""")

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
                    SELECT * FROM Movies WHERE title = '{title}';""")

        return self.db.fetchall()

    def det_by_duration(self, duration: int):
        self.db.push(f"""
                    SELECT * FROM Movies WHERE duration = {duration};""")

        return self.db.fetchall()


class Hall(ORM.Model):

    def __init__(self, db:SQLite):
        self.db = db

        self.id_hall = ORM.Field(
            name='id_hall',
            type=ORM.INTEGER,
            not_null=True,
            auto_increment=True,
            primary_key=True)

        self.name_hall = ORM.Field(
            name='name_hall',
            type=ORM.TEXT,
            not_null=True,
            auto_increment=False,
            primary_key=False)

        self.capacity = ORM.Field(
            name='capacity',
            type=ORM.INTEGER,
            not_null=True,
            auto_increment=False,
            primary_key=False)

    def create_hall(self, name_hall: str, capacity: int):
        self.db.push(f"""
        INSERT INTO Hall (name_hall, capacity)
                        VALUES ('{name_hall}', {capacity})""")

    def get_all(self):
        self.db.push(f"""
                    SELECT * FROM Hall""")
        return self.db.fetchall()

    def get_by_id_hall(self, id_hall: int):
        self.db.push(f"""
                    SELECT * FROM Hall WHERE id_hall = {id_hall}""")
        return self.db.fetchall()

    def get_by_name_hall(self, name_hall: str):
        self.db.push(f"""
                    SELECT * FROM Hall WHERE name_hall = '{name_hall}'""")
        return self.db.fetchall()

    def get_by_capacity(self, capacity: int):
        self.db.push(f"""
                    SELECT * FROM Hall WHERE capacity = {capacity}""")
        return self.db.fetchall()


class Seat(ORM.Model):

    def __init__(self, db:SQLite):
        self.db = db

        self.id_seat = ORM.Field(
            name='id_seat',
            type=ORM.INTEGER,
            not_null=True,
            auto_increment=True,
            primary_key=True)

        self.id_hall = ORM.Field(
            name='id_hall',
            type=ORM.INTEGER,
            not_null=True,
            auto_increment=False,
            primary_key=False)

        self.row = ORM.Field(
            name='row',
            type=ORM.INTEGER,
            not_null=True,
            auto_increment=False,
            primary_key=False)

        self.seat_number = ORM.Field(
            name='seat_number',
            type=ORM.INTEGER,
            not_null=True,
            auto_increment=False,
            primary_key=False)

    def create_seat(self, id_hall: int, row: int, seat_number: int):
        self.db.push(f"""
        INSERT INTO Seat (id_hall, row, seat_number) VALUES ({id_hall}, {row}, {seat_number})""")

    def get_all(self):
        self.db.push(f"""
                    SELECT * FROM Seat""")
        return self.db.fetchall()

    def get_by_id_seat(self, id_seat: int):
        self.db.push(f"""
                    SELECT * FROM Seat WHERE id_seat = {id_seat};""")
        return self.db.fetchall()

    def get_by_id_hall(self, id_hall: int):
        self.db.push(f"""
                    SELECT * FROM Seat WHERE id_hall = {id_hall};""")
        return self.db.fetchall()

    def get_by_row(self, row: int):
        self.db.push(f"""
                    SELECT * FROM Seat WHERE row = {row};""")
        return self.db.fetchall()

    def get_by_seat_number(self, seat_number: int):
        self.db.push(f"""
                    SELECT * FROM Seat WHERE seat_number = {seat_number};""")
        return self.db.fetchall()


class Viewer(ORM.Model):

    def __init__(self, db:SQLite):
        self.db = db

        self.id_viewer = ORM.Field(
            name='id_viewer',
            type=ORM.INTEGER,
            not_null=True,
            auto_increment=True,
            primary_key=True)

        self.FirstName = ORM.Field(
            name='FirstName',
            type=ORM.TEXT,
            not_null=True,
            auto_increment=False,
            primary_key=False)

        self.LastName = ORM.Field(
            name='LastName',
            type=ORM.TEXT,
            not_null=True,
            auto_increment=False,
            primary_key=False)

    def create_viewer(self, FirstName: str, LastName: str):
        self.db.push(f"""
           INSERT INTO Viewer (FirstName, LastName) VALUES ('{FirstName}', '{LastName}')""")

    def get_all(self):
        self.db.push(f"""
                       SELECT * FROM Viewer""")
        return self.db.fetchall()

    def get_by_id_viewer(self, id_viewer: int):
        self.db.push(f"""
                       SELECT * FROM Viewer WHERE id_viewer = {id_viewer};""")
        return self.db.fetchall()

    def get_by_FirstName(self, FirstName: str):
        self.db.push(f"""
                       SELECT * FROM Viewer WHERE FirstName = '{FirstName}';""")
        return self.db.fetchall()

    def get_by_LastName(self, LastName: str):
        self.db.push(f"""
                       SELECT * FROM Viewer WHERE LastName = '{LastName}';""")
        return self.db.fetchall()


class Session(ORM.Model):

    def __init__(self, db:SQLite):
        self.db = db

        self.id_session = ORM.Field(
            name='id_session',
            type=ORM.INTEGER,
            not_null=True,
            auto_increment=True,
            primary_key=True)

        self.id_movie = ORM.Field(
            name='id_movie',
            type=ORM.INTEGER,
            not_null=True,
            auto_increment=False,
            primary_key=False)

        self.id_hall = ORM.Field(
            name='id_hall',
            type=ORM.INTEGER,
            not_null=True,
            auto_increment=False,
            primary_key=False)

        self.time_session = ORM.Field(
            name='time_session',
            type=ORM.TEXT,
            not_null=True,
            auto_increment=False,
            primary_key=False)

    def create_session(self, id_movie: int, id_hall: int, time_session: str):
        self.db.push(f"""
           INSERT INTO Session (id_movie, id_hall, time_session) VALUES ({id_movie}, {id_hall}, '{time_session}')""")

    def get_all(self):
        self.db.push(f"""
                       SELECT * FROM Session""")
        return self.db.fetchall()

    def get_by_id_session(self, id_session: int):
        self.db.push(f"""
                       SELECT * FROM Session WHERE id_session = {id_session};""")
        return self.db.fetchall()

    def get_by_id_movie(self, id_movie: int):
        self.db.push(f"""
                       SELECT * FROM Session WHERE id_movie = {id_movie};""")
        return self.db.fetchall()

    def get_by_id_hall(self, id_hall: int):
        self.db.push(f"""
                       SELECT * FROM Session WHERE id_hall = {id_hall};""")
        return self.db.fetchall()

    def get_by_time_session(self, time_session: str):
        self.db.push(f"""
                       SELECT * FROM Session WHERE time_session = '{time_session}';""")
        return self.db.fetchall()


class Ticket(ORM.Model):

    def __init__(self, db:SQLite):
        self.db = db

        self.id_ticket = ORM.Field(
            name='id_ticket',
            type=ORM.INTEGER,
            not_null=True,
            auto_increment=True,
            primary_key=True)

        self.id_session = ORM.Field(
            name='id_session',
            type=ORM.INTEGER,
            not_null=True,
            auto_increment=False,
            primary_key=False)

        self.id_seat = ORM.Field(
            name='id_seat',
            type=ORM.INTEGER,
            not_null=True,
            auto_increment=False,
            primary_key=False)

        self.id_viewer = ORM.Field(
            name='id_viewer',
            type=ORM.INTEGER,
            not_null=True,
            auto_increment=False,
            primary_key=False)

        self.price = ORM.Field(
            name='price',
            type=ORM.INTEGER,
            not_null=True,
            auto_increment=False,
            primary_key=False)

    def create_ticket(self, id_session: int, id_seat: int, id_viewer: int, price: int):
        self.db.push(f"""
           INSERT INTO Ticket (id_session, id_seat, id_viewer, price) VALUES ({id_session}, {id_seat}, {id_viewer}, {price})""")

    def get_all(self):
        self.db.push(f"""
                       SELECT * FROM Ticket""")
        return self.db.fetchall()

    def get_by_id_ticket(self, id_ticket: int):
        self.db.push(f"""
                       SELECT * FROM Ticket WHERE id_ticket = {id_ticket};""")
        return self.db.fetchall()

    def get_by_id_session(self, id_session: int):
        self.db.push(f"""
                       SELECT * FROM Ticket WHERE id_session = {id_session};""")
        return self.db.fetchall()

    def get_by_id_seat(self, id_seat: int):
        self.db.push(f"""
                       SELECT * FROM Ticket WHERE id_seat = {id_seat};""")
        return self.db.fetchall()

    def get_by_id_viewer(self, id_viewer: int):
        self.db.push(f"""
                       SELECT * FROM Ticket WHERE id_viewer = {id_viewer};""")
        return self.db.fetchall()

    def get_by_price(self, price: int):
        self.db.push(f"""
                       SELECT * FROM Ticket WHERE price = {price};""")
        return self.db.fetchall()