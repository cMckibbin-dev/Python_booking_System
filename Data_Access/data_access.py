"""module contains functions and the DBAccess class to allow the program to interact with the sqlite 3 database"""
import sqlite3 as sql
from os import path as os
from classes import *
from datetime import datetime
import datetime


def create_database(db):
    """Function to create database tables if the database is being created"""
    createTablesCommands = ["""Create Table wedding(ID integer primary key autoincrement not null, numberGuests integer,
                            name_of_contact text, address text,
                            contactNumber text, eventRoom text, dateOfEvent text, dateOfBooking text, costPerHead 
                            integer, bandName text, bandPrice integer, numberOfRooms integer );""",

                            """Create Table conference(ID integer primary key autoincrement not null, 
                            numberGuests integer, name_of_contact text, address text,
                          contactNumber text, eventRoom text, dateOfEvent text, dateOfBooking text,
                          costPerHead integer, companyName text, numberDays integer, projectorRequired integer);""",

                            """create table party(ID integer primary key autoincrement not null, numberGuests integer,
                             name_of_contact text, address text,
                          contactNumber text, eventRoom text, dateOfEvent text, dateOfBooking text,
                          costPerHead integer, bandName text, bandPrice integer);"""]
    cursor = db.cursor()

    for command in createTablesCommands:
        cursor.execute(command)
    db.commit()


def _connect_to_database():
    """Will create connection to database or create database if it does not exist"""
    try:
        if not os.isfile('Data_Access/database.db'):
            db = sql.connect('Data_Access/database.db')
            create_database(db)
            return db
        else:
            return sql.connect('Data_Access/database.db')
    except OSError as e:
        print(e)
    except sql.Error as e:
        print(e)


def convert_pound(value):
    """converts pence store as int into pound and pence as a float. All currency values stored as pence in database"""
    return float(value / 100)


def convert_pence(value):
    """converts money store as pounds and pence into pence to be stored as int in database.
     All currency values stored as pence in database"""
    return int(value * 100)


def _create_wedding(row):
    """function will construct a instance of wedding class from a row selected from the database"""
    w = Wedding(ID=row[0], noGuests=row[1], nameofContact=row[2],
                address=row[3],
                contactNo=row[4], eventRoomNo=row[5],
                dateOfEvent=datetime.datetime.strptime(row[6], '%Y-%m-%d').date(),
                dateOfBooking=datetime.datetime.strptime(row[7], '%Y-%m-%d').date(),
                costPerhead=convert_pound(row[8]),
                bandName=row[9], bandPrice=convert_pound(row[10]), noBedroomsReserved=row[11])
    return w


def _create_party(row):
    """function will construct a instance of party class from a row selected from the database"""
    p = Party(ID=row[0], noGuests=row[1], nameofContact=row[2], address=row[3],
              contactNo=row[4], eventRoomNo=row[5],
              dateOfEvent=datetime.datetime.strptime(row[6], '%Y-%m-%d').date()
              , dateofBooking=datetime.datetime.strptime(row[7], '%Y-%m-%d').date(), costPerhead=convert_pound(row[8]),
              bandName=(row[9]), bandPrice=convert_pound(row[10]))
    return p


def _create_conference(row):
    """function will construct a instance of conference class from a row selected from the database"""
    c = Conference(ID=row[0], noGuests=int(row[1]), nameofContact=row[2],
                   address=row[3], contactNo=row[4], eventRoomNo=row[5],
                   dateOfEvent=datetime.datetime.strptime(row[6], '%Y-%m-%d').date(),
                   dateofBooking=datetime.datetime.strptime(row[7], '%Y-%m-%d').date(),
                   costPerhead=convert_pound(row[8]), companyName=row[9], noOfDays=row[10],
                   projectorRequired=bool(row[11]))
    return c


class DBAccess:
    """The class connects to the sqlite 3 database and provides methods to retrieve stored bookings, delete bookings,
    update currently stored bookings and insert new booking for weddings, party and conference. class also contains
    methods to return booked rooms and bands on a given date. Method also exist to return events booked between tow
    given date"""

    def __init__(self):
        self.dbCon = _connect_to_database()
        self.cursor = self.dbCon.cursor()

    def all_weddings(self, future=False):
        """gets all weddings from database and returns a list of wedding objects"""
        if not future:
            self.cursor.execute("select * from wedding")
        else:
            self.cursor.execute("select * from wedding where date(dateOfEvent) > date('now')")

        all_rows = self.cursor.fetchall()
        listWeddings = []
        for row in all_rows:
            listWeddings.append(_create_wedding(row))
        return listWeddings

    def all_conferences(self, future=False):
        """returns all conferences from connected database and returns a list of conferences"""
        if not future:
            self.cursor.execute('select * from conference')
        else:
            self.cursor.execute("select * from conference where date(dateOfEvent) > date('now')")

        all_rows = self.cursor.fetchall()

        listConferences = []
        for row in all_rows:
            listConferences.append(_create_conference(row))
        return listConferences

    def all_party(self, future=False):
        """returns all parties from connected database and returns a list of parties"""
        if not future:
            self.cursor.execute('select * from party')
        else:
            self.cursor.execute("select * from party where date(dateOfEvent) > date('now')")

        all_rows = self.cursor.fetchall()
        listParties = []
        for row in all_rows:
            listParties.append(_create_party(row))
        return listParties

    def all_records(self, future=False):
        """returns all events from connected database in one list containing all event types"""
        weddings = self.all_weddings() if not future else self.all_weddings(future)
        parties = self.all_party() if not future else self.all_party(future)
        conferences = self.all_conferences() if not future else self.all_conferences(future)
        results = weddings + conferences + parties
        return results

    def insert_wedding(self, wedding):
        """inserts a wedding object into the database"""
        self.cursor.execute("""insert into wedding(numberGuests, name_of_contact, address,
                          contactNumber, eventRoom, dateOfEvent, dateOfBooking,
                          costPerHead, bandName, bandPrice, numberOfRooms) values(?,?,?,?,?,?,?,?,?,?,?)""",
                            (wedding.noGuests, wedding.nameofContact, wedding.address, wedding.contactNo,
                             wedding.eventRoomNo, wedding.dateOfEvent, wedding.dateOfBooking,
                             convert_pence(wedding.costPerhead), wedding.bandName,
                             convert_pence(wedding.bandPrice),
                             wedding.noBedroomsReserved))
        self.dbCon.commit()

    def insert_conference(self, conference):
        """inserts a conference object into the database"""

        self.cursor.execute("""Insert into conference(numberGuests, name_of_contact, address,
                          contactNumber, eventRoom, dateOfEvent, dateOfBooking,
                          costPerHead, companyName, numberDays, projectorRequired) values(?,?,?,?,?,?,?,?,?,?,?)""",
                            (conference.noGuests, conference.nameofContact, conference.address, conference.contactNo,
                             conference.eventRoomNo, conference.dateOfEvent, conference.dateOfBooking,
                             convert_pence(conference.costPerhead), conference.companyName, conference.noOfDays,
                             conference.projectorRequired))
        self.dbCon.commit()

    def insert_party(self, party):
        """inserts a party object into the database"""
        self.cursor.execute("""Insert into party(numberGuests, name_of_contact, address,
                          contactNumber, eventRoom, dateOfEvent, dateOfBooking,
                          costPerHead, bandName, bandPrice) values(?,?,?,?,?,?,?,?,?,?)""",
                            (party.noGuests, party.nameofContact, party.address, party.contactNo, party.eventRoomNo,
                             party.dateOfEvent, party.dateOfBooking, convert_pence(party.costPerhead), party.bandName,
                             convert_pence(party.bandPrice)))
        self.dbCon.commit()

    def update_conference(self, conference):
        """method update a conference booking in database"""
        values = (conference.noGuests, conference.nameofContact,
                  conference.address, conference.contactNo,
                  conference.eventRoomNo, conference.dateOfEvent,
                  conference.dateOfBooking, convert_pence(conference.costPerhead),
                  conference.companyName,
                  conference.noOfDays, int(conference.projectorRequired),
                  conference.id)
        self.cursor.execute("""update conference SET numberGuests =?, name_of_contact =?, address = ?, 
        contactNumber =?, eventRoom = ?, dateOfEvent =?, dateOfBooking = ?, costPerHead =?, companyName = ?,
        numberDays=?, projectorRequired = ? WHERE ID = ?""", (conference.noGuests, conference.nameofContact,
                                                              conference.address, conference.contactNo,
                                                              conference.eventRoomNo, conference.dateOfEvent,
                                                              conference.dateOfBooking,
                                                              convert_pence(conference.costPerhead),
                                                              conference.companyName,
                                                              conference.noOfDays, int(conference.projectorRequired),
                                                              conference.id))
        self.dbCon.commit()

    def update_party(self, party):
        """method to update party booking in database"""
        self.cursor.execute("""update party SET numberGuests =?, name_of_contact =?, address = ?, 
        contactNumber =?, eventRoom = ?, dateOfEvent =?, dateOfBooking = ?, costPerHead =?, bandName =?, bandPrice=? 
        WHERE ID = ?""", (party.noGuests, party.nameofContact, party.address, party.contactNo, party.eventRoomNo,
                          party.dateOfEvent, party.dateOfBooking, convert_pence(party.costPerhead), party.bandName,
                          convert_pence(party.bandPrice), party.id))
        self.dbCon.commit()

    def update_wedding(self, wedding):
        """method to update wedding booking in database"""
        self.cursor.execute("""update wedding set numberGuests =?, name_of_contact =?, address = ?, 
        contactNumber =?, eventRoom = ?, dateOfEvent =?, dateOfBooking = ?, costPerHead =?, bandName =?, bandPrice=?, 
        numberOfRooms=? WHERE ID = ?""", (wedding.noGuests, wedding.nameofContact, wedding.address, wedding.contactNo,
                                          wedding.eventRoomNo, wedding.dateOfEvent, wedding.dateOfBooking,
                                          convert_pence(wedding.costPerhead), wedding.bandName,
                                          convert_pence(wedding.bandPrice),
                                          wedding.noBedroomsReserved, wedding.id))
        self.dbCon.commit()

    def delete_booking(self, event, tableName):
        """method to delete a booking from the database when given table name"""
        sqlString = """Delete from {} WHERE ID = ?""".format(tableName)
        print(sqlString)
        self.cursor.execute(sqlString, (event.id,))
        self.dbCon.commit()

    def bookings_between_dates(self, eventTypes, dateFrom, dateTo):
        """method returns wedding, conference and party objects type between two dates. takes in a list of event
        types that will be selected from and to dates"""
        results = []
        for event in eventTypes:
            self.cursor.execute("select * from {} Where date(dateOfEvent) between date('{}') and date('{}')"
                                .format(event, dateFrom, dateTo))
            all_rows = self.cursor.fetchall()
            if event.lower() == 'conference':
                for row in all_rows:
                    results.append(_create_conference(row))
            elif event.lower() == 'wedding':
                for row in all_rows:
                    results.append(_create_wedding(row))
            elif event.lower() == 'party':
                for row in all_rows:
                    results.append(_create_party(row))
            else:
                raise ValueError('eventTypes must be one of the following: "conference", "wedding", "party"')

        return results

    def getBookedRooms(self, tableName, date, ID=None):
        """method returns a list of all rooms booked for a certain date for an event type.  If ID is given for the
        booking then the room booked with the provided ID will not be counted"""
        if ID is None:
            sqlQuery = "select eventRoom from {} where date(dateOfEvent) == date('{}')".format(tableName, date)
        else:
            sqlQuery = "select eventRoom from {} where date(dateOfEvent) == date('{}') and ID != {}".format(tableName,
                                                                                                            date, ID)
        self.cursor.execute(sqlQuery)
        all_rows = self.cursor.fetchall()
        results = []
        if all_rows:
            for row in all_rows:
                results.append((row[0]))
        print('booked rooms')
        print(results)
        return results

    def getBookedBands(self, date, eventType, ID=None):
        """method to return a list of all bands booked for a certain date. eventType is passed so that the correct
        tables are queried when ID is given"""
        sqlQueries = []
        if ID is None:
            sqlQueryParty = "select bandName from party where date(dateOfEvent) == date('{}')".format(date)
            sqlQueryWedding = "select bandName from wedding where date(dateOfEvent) == date('{}')".format(date)
        elif eventType.lower() == 'party':
            sqlQueryParty = "select bandName from party where date(dateOfEvent) == date('{}') and ID != {}".format(date,
                                                                                                                   ID)
            sqlQueryWedding = "select bandName from wedding where date(dateOfEvent) == date('{}')".format(date)
        elif eventType.lower() == 'wedding':
            sqlQueryParty = "select bandName from party where date(dateOfEvent) == date('{}')".format(date)
            sqlQueryWedding = "select bandName from wedding where date(dateOfEvent) == date('{}') and ID != {}".format(
                date, ID)
        else:
            raise ValueError('eventType must be party or wedding')
        sqlQueries.append(sqlQueryParty)
        sqlQueries.append(sqlQueryWedding)

        results = []
        for query in sqlQueries:
            self.cursor.execute(query)
            all_rows = self.cursor.fetchall()
            for row in all_rows:
                results.append(row[0])
        print('booked bands')
        print(list(set(results)))
        return list(set(results))

    def booked_conference_rooms(self, date, number_of_days, ID=None):
        """method to return booked rooms from the conference table given a date of event and number of days the
        conference will last. If ID is passed then the query will not included room booked for that given ID"""
        if ID is None:
            self.cursor.execute("""select eventRoom, date(dateOfEvent, '+'||(numberDays - 1)||' days') as endDate from conference where
             ((date('{startDate}') BETWEEN date(dateOfEvent) and date(endDate) or date('{bookingEndDate}') BETWEEN 
            date(dateOfEvent) and date(endDate))) or ((date(dateOfEvent) BETWEEN date('{startDate}') and date('
            {bookingEndDate}') or date(endDate) BETWEEN date('{startDate}') and date('{bookingEndDate}')))""".format(
                startDate=date, bookingEndDate=date + datetime.timedelta(days=number_of_days - 1)))
        else:
            self.cursor.execute("""select eventRoom, date(dateOfEvent, '+'||(numberDays - 1)||' days') as endDate from conference 
            where id != {ID} AND ((date('{startDate}') BETWEEN date(dateOfEvent) and date(endDate) or date('{bookingEndDate}') 
            BETWEEN date(dateOfEvent) and date(endDate)) or date(dateOfEvent) BETWEEN date('{startDate}') and date(
            '{bookingEndDate}') or date(endDate) BETWEEN date('{startDate}') and date('{bookingEndDate}')) """.
                                format(startDate=date,
                                       bookingEndDate=date + datetime.timedelta(days=number_of_days - 1), ID=ID))
        all_rows = self.cursor.fetchall()
        results = []
        for row in all_rows:
            results.append(row[0])
        return list(set(results))

    def __del__(self):
        """closes database connection when DBAccess object is deleted"""
        self.dbCon.close()
        print('closed connection')
