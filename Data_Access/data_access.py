import sqlite3 as sql
from os import path as os
from classes import *
from datetime import datetime


def create_database(db):
    createTablesCommands = ["""Create Table wedding(numberGuests integer, name_of_contact text, address text,
                            contactNumber text, eventRoom text, dateOfEvent text, dateOfBooking text, costPerHead 
                            integer, bandName text, bandPrice integer, numberOfRooms integer );""",
                            """Create Table conference(numberGuests integer, name_of_contact text, address text,
                          contactNumber text, eventRoom text, dateOfEvent text, dateOfBooking text,
                          costPerHead integer, companyName text, numberDays integer, projectorRequired integer);""",
                            """create table party(numberGuests integer, name_of_contact text, address text,
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
    result = float(value / 100)
    return result


class DBAccess:

    def __init__(self):
        self.dbCon = _connect_to_database()
        self.cursor = self.dbCon.cursor()
        self.dbCon.row_factory = sql.Row

    def all_weddings(self, future=False):
        """gets all weddings from database"""
        if not future:
            self.cursor.execute("select * from wedding")
        else:
            self.cursor.execute("select * from wedding where date(dateOfEvent) > date('now')")

        all_rows = self.cursor.fetchall()
        listWeddings = []
        for row in all_rows:
            w = Wedding(noGuests=row[0], nameofContact=row[1],
                        address=row[2],
                        contactNo=row[3], eventRoomNo=row[4]
                        , dateOfEvent=datetime.strptime(row[5], '%Y-%m-%d'),
                        dateOfBooking=datetime.strptime(row[6], '%Y-%m-%d'),
                        costPerhead=convert_pound(row[7]),
                        bandName=row[8]
                        , bandPrice=convert_pound(row[9]), noBedroomsReserved=row[10])
            listWeddings.append(w)
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
            c = Conference(noGuests=int(row[0]), nameofContact=row[1],
                           address=row[2], contactNo=row[3], eventRoomNo=row[4],
                           dateOfEvent=datetime.strptime(row[5], '%Y-%m-%d')
                           , dateofBooking=datetime.strptime(row[6], '%Y-%m-%d'), costPerhead=convert_pound(row[7]),
                           companyName=row[8],
                           noOfDays=row[9],
                           projectorRequired=convert_pound(row[10]))
            listConferences.append(c)
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
            p = Party(noGuests=row[0], nameofContact=row[1], address=row[2],
                      contactNo=row[3], eventRoomNo=row[4],
                      dateOfEvent=datetime.strptime(row[5], '%Y-%m-%d')
                      , dateofBooking=datetime.strptime(row[6], '%Y-%m-%d'), costPerhead=convert_pound(row[7]),
                      bandName=(row[8]),
                      bandPrice=convert_pound(row[9]))
            listParties.append(p)
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
                          contactNumber, eventRoom, dateOfEvent, dateOfBooking
                          costPerHead, bandName, bandPrice, numberOfRooms) values(?,?,?,?,?,?,?,?,?,?,?)""",
                            (wedding.noGuests, wedding.nameofContact, wedding.address, wedding.contactNo,
                             wedding.eventRoomNo, wedding.dateOfEvent, wedding.dateOfBooking, wedding.costPerhead,
                             wedding.bandPrice, wedding.bandName, wedding.bandPrice, wedding.noBedroomsReserved))
        self.dbCon.commit()

    def insert_conference(self, conference):
        """inserts a conference object to the database"""
        self.cursor.execute("""Insert into conference(numberGuests, name_of_contact, address,
                          contactNumber, eventRoom, dateOfEvent, dateOfBooking
                          costPerHead, companyName, numberDays, projectorRequired) values(?,?,?,?,?,?,?,?,?,?,?)""",
                            (conference.noGuests, conference.nameofContact, conference.address, conference.contactNo,
                             conference.eventRoomNo, conference.dateOfEvent, conference.dateOfBooking,
                             conference.costPerhead, conference.companyName, conference.noOfDays,
                             conference.projectorRequired))
        self.dbCon.commit()

    def insert_party(self, party):
        """inserts a party object to the database"""
        self.cursor.execute("""Insert into party(numberGuests, name_of_contact, address,
                          contactNumber, eventRoom, dateOfEvent, dateOfBooking
                          costPerHead, bandName, bandPrice) values(?,?,?,?,?,?,?,?,?,?)""",
                            (party.noGuests, party.nameofContact, party.address, party.contactNo, party.eventRoomNo,
                             party.dateOfEvent, party.dateOfBooking, party.costPerhead, party.bandName,
                             party.bandPrice))
        self.dbCon.commit()

    def disconnect_db(self):
        """Disconnect the database and the cursor"""
        self.dbCon.close()
        self.dbCon.close()

    # def __del__(self):
    #     self.dbCon.close()
    #     self.cursor.close()
