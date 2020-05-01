import sqlite3
import os
files = os.listdir();
class Saver:
    def __init__(self,kind="Load"):
        self.con = sqlite3.connect("mydb")
        self.cur = self.con.cursor()
        self.dataexists = False
        self.createtablecommand="create table player(" \
                                "id int primary key,"\
                                "posx integer," \
                                "posy integer," \
                                "velx integer," \
                                "vely integer," \
                                "angle integer," \
                                "accx integer," \
                                "accy integer" \
                                ");"

        self.insertnewvalue="insert into player (id, posx, posy, velx, vely, angle, accx, accy) values (?,?,?,?,?,?,?,?)"
        self.fetchcountins="select count(*) from player"
        if kind == "create":
            self.dataexists = False
            self.cur.execute(self.createtablecommand)
        else:
            self.dataexists = True

    def createnew(self):
        self.cur.execute(self.createtablecommand)

    def show(self):
        self.cur.execute("select * from player")
        print(self.cur.fetchall())

    def save(self,player):
        self.cur.execute(self.fetchcountins)
        id = self.cur.fetchall()[0][0] +1
        self.cur.execute(self.insertnewvalue,(id,player.pos[0],player.pos[1],player.vel[0],player.vel[1],player.angle,player.accel[0],player.accel[1]))

    def deleteall(self):
        self.cur.execute("delete from player")

    def commit(self):
        self.con.commit()
    def dataexist(self):
        return self.dataexists
    def loadrecent(self):
        self.cur.execute("select * from player")
        k = self.cur.fetchall()[-1]
        return k;

if __name__ == '__main__':
    from ship import *
    p = Player([1000,2000])
    s = Saver()
    #s.save(p)
    s.show()
    #s.deleteall()
    #s.commit()