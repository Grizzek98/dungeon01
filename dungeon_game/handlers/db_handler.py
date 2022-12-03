import sqlite3
import csv
import dungeon_game.constants as c

class DBHandler:

    q_dict = {
        'fetch_item': '''SELECT * FROM item WHERE name=?''',
        'fetch_mob': '''SELECT * FROM mob WHERE name=?''',
        'fetch_command': '''SELECT * FROM command WHERE ? in 
                            (command_name, a1, a2, a3, a4, a5, a6)''',
    }
    
    @staticmethod
    def initialize_db():
        con = sqlite3.connect(c.DATABASE_PATH)
        cur = con.cursor()
        DBHandler.populate_db(cur)
        con.commit()
        con.close()

    @staticmethod
    def populate_db(cur):
        DBHandler.populate_items(cur)
        DBHandler.populate_mobs(cur)
        DBHandler.populate_commands(cur)
    
    @staticmethod
    def populate_items(cur):
        cur.execute('''DROP TABLE IF EXISTS item''')
        cur.execute('''CREATE TABLE item 
                    (item_type text, 
                    name text, 
                    weight real,
                    damage int, 
                    use_range int, 
                    hp_gain int, 
                    armor int)''')
        with open(c.ITEM_INFO_PATH) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # print(row)
                cur.execute('''INSERT INTO item VALUES
                    (?, ?, ?, ?, ?, ?, ?)''', 
                    (row['item_type'], 
                    row['name'],
                    row['weight'],
                    row['damage'], 
                    row['use_range'],
                    row['hp_gain'],
                    row['armor'],
                    ))

    @staticmethod
    def populate_mobs(cur):
        cur.execute('''DROP TABLE IF EXISTS mob''')
        cur.execute('''CREATE TABLE mob 
                    (mob_type text,
                    name text,
                    max_health int,
                    str int,
                    dex int,
                    vit int,
                    cha int,
                    mag int)''')
        with open(c.MOB_INFO_PATH) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # print(row)
                cur.execute('''INSERT INTO mob VALUES
                    (?, ?, ?, ?, ?, ?, ?, ?)''', 
                    (row['mob_type'], 
                    row['name'], 
                    row['max_health'], 
                    row['str'],
                    row['dex'],
                    row['vit'],
                    row['cha'],
                    row['mag'],
                    ))

    @staticmethod
    def populate_commands(cur):
        cur.execute('''DROP TABLE IF EXISTS command''')
        cur.execute('''CREATE TABLE command
                    (command_name text,
                    a1 text,
                    a2 text,
                    a3 text,
                    a4 text,
                    a5 text,
                    a6 text)''')
        with open(c.COMMAND_INFO_PATH) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                cur.execute('''INSERT INTO command VALUES
                (?, ?, ?, ?, ?, ?, ?)''',
                (row['command_name'],
                row['a1'],
                row['a2'],
                row['a3'],
                row['a4'],
                row['a5'],
                row['a6'],
                ))

    @staticmethod
    def fetch_item(name):
        con = sqlite3.connect(c.DATABASE_PATH)
        # con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(DBHandler.q_dict['fetch_item'], [name])
        return cur

    @staticmethod
    def fetch_mob(name):
        con = sqlite3.connect(c.DATABASE_PATH)
        # con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(DBHandler.q_dict['fetch_mob'], [name])
        return cur

    @staticmethod
    def fetch_command(name):
        con = sqlite3.connect(c.DATABASE_PATH)
        # con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(DBHandler.q_dict['fetch_command'], [name])
        return cur