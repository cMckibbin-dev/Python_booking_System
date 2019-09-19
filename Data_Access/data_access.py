import sqlite3 as sql
from os import path as os
from classes import *
from datetime import datetime


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
    if not os.isfile('Data_Access/database'):
        db = sql.connect('Data_Access/database')
        create_database(db)
        return db
    else:
        return sql.connect('Data_Access/database')


def convert_pound(value):
    """converts pence store as int into pound and pence as a float"""
    return float(value / 100)


def convert_pence(value):
    """converts money store as pounds and pence into pence to be stored as int in database"""
    return int(value * 100)


def _create_wedding(row):
    """function will construct a instance of wedding class from a row selected from the database"""
    w = Wedding(ID=row[0], noGuests=row[1], nameofContact=row[2],
                address=row[3],
                contactNo=row[4], eventRoomNo=row[5],
                dateOfEvent=datetime.strptime(row[6], '%Y-%m-%d').date(),
                dateOfBooking=datetime.strptime(row[7], '%Y-%m-%d').date(),
                costPerhead=convert_pound(row[8]),
                bandName=row[9], bandPrice=convert_pound(row[10]), noBedroomsReserved=row[11])
    return w


def _create_party(row):
    """function will construct a instance of party class from a row selected from the database"""
    p = Party(ID=row[0], noGuests=row[1], nameofContact=row[2], address=row[3],
              contactNo=row[4], eventRoomNo=row[5],
              dateOfEvent=datetime.strptime(row[6], '%Y-%m-%d').date()
              , dateofBooking=datetime.strptime(row[7], '%Y-%m-%d').date(), costPerhead=convert_pound(row[8]),
              bandName=(row[9]), bandPrice=convert_pound(row[10]))
    return p


def _create_conference(row):
    """function will construct a instance of conference class from a row selected from the database"""
    c = Conference(ID=row[0], noGuests=int(row[1]), nameofContact=row[2],
                   address=row[3], contactNo=row[4], eventRoomNo=row[5],
                   dateOfEvent=datetime.strptime(row[6], '%Y-%m-%d').date(),
                   dateofBooking=datetime.strptime(row[7], '%Y-%m-%d').date(),
                   costPerhead=convert_pound(row[8]), companyName=row[9], noOfDays=row[10],
                   projectorRequired=bool(row[11]))
    return c


class DBAccess:

    def __init__(self):
        self.dbCon = _connect_to_database()
        self.cursor = self.dbCon.cursor()

    def all_weddings(self, future=False):
        """gets all weddings from database"""
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
        """returns all conferences from connected database"""
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
        """returns all parties from connected database"""
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
        """returns all events from connected database in one list"""
        weddings = self.all_weddings() if not future else self.all_weddings(future)
        parties = self.all_party() if not future else self.all_party(future)
        conferences = self.all_conferences() if not future else self.all_conferences(future)
        results = weddings + conferences + parties
        return results

    def insert_wedding(self, wedding):
        """inserts a wedding object to the database"""
        self.cursor.execute("""insert into wedding(numberGuests, name_of_contact, address,
                          contactNumber, eventRoom, dateOfEvent, dateOfBooking,
                          costPerHead, bandName, bandPrice, numberOfRooms) values(?,?,?,?,?,?,?,?,?,?,?)""",
                            (wedding.noGuests, wedding.nameofContact, wedding.address, wedding.contactNo,
                             wedding.eventRoomNo, wedding.dateOfEvent, wedding.dateOfBooking,convert_pence(wedding.costPerhead),
                             convert_pence(wedding.bandPrice), wedding.bandName, convert_pence(wedding.bandPrice),
                             wedding.noBedroomsReserved))
        self.dbCon.commit()

    def insert_conference(self, conference):
        """inserts a conference object to the database"""

        self.cursor.execute("""Insert into conference(numberGuests, name_of_contact, address,
                          contactNumber, eventRoom, dateOfEvent, dateOfBooking,
                          costPerHead, companyName, numberDays, projectorRequired) values(?,?,?,?,?,?,?,?,?,?,?)""",
                            (conference.noGuests, conference.nameofContact, conference.address, conference.contactNo,
                             conference.eventRoomNo, conference.dateOfEvent.date(), conference.dateOfBooking.date(),
                             convert_pence(conference.costPerhead), conference.companyName, conference.noOfDays,
                             conference.projectorRequired))
        self.dbCon.commit()

    def insert_party(self, party):
        """inserts a party object to the database"""
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
        """method to delete a booking from the database"""
        sqlString = """Delete from {} WHERE ID = ?""".format(tableName)
        print(sqlString)
        self.cursor.execute(sqlString, (event.id,))
        self.dbCon.commit()

    def bookings_between_dates(self, eventTypes, dateFrom, dateTo):
        """method will return the total income of events of a certain type between two dates. takes in a list of event
        types that will be selected from"""
        results = []
        for event in eventTypes:
            self.cursor.execute("select * from {} Where date(dateOfEvent) between date('{}') and date('{}')"
                                .format(event, dateFrom, dateTo))
            all_rows = self.cursor.fetchall()
            if event == 'Conference':
                for row in all_rows:
                    results.append(_create_conference(row))
            elif event == 'Wedding':
                for row in all_rows:
                    results.append(_create_wedding(row))
            elif event == 'party':
                for row in all_rows:
                    results.append(_create_party(row))

        return results

    def disconnect_db(self):
        """Disconnect the database and the cursor"""
        self.dbCon.close()

    def __del__(self):
        self.dbCon.close()
        print('closed connection')
