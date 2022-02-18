class Person:

    def __init__(self, name, familyname, age, occupation, nationality):

        self.name = name
        self.familyname = familyname
        self.age = age
        self.occupation = occupation
        self.nationality = nationality

    def year_born(self,cur_year):
        self.cur_year = cur_year
        year_born = self.cur_year - self.age
        return year_born

    def get_full_name(self):
        return self.name +" "+ self.familyname

    def get_full_info(self,info):
        return self.name+" "+self.familyname+" "+self.name+" "+self.occupation+" "+self.nationality
        