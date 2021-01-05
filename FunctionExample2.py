# keyword arguments/ named arguments
def karan(name, section, roll):
    print("Name=", name.upper(), ", Section=", section.upper(), ", roll=", roll)


# arbitrary keyword argument
def raju(**data): # ** represents arbitrary keyword arguments
    # in arbitrary keyword argument , argument comes in dictionary form
   keylist = data.keys()
   if "Name" in keylist:
        print("Name=", data["Name"])

   if "Section" in keylist:
       print("Section=",  data["Section"])


# function with default argument
def manohar(name="Manohar", section="A"):
    print("Name=", name, "Section=", section)


def ankit():
    pass


karan("Karan", "A", 89)
karan("45", "B", "Ankit Kumar")
karan(roll=45, name="ankit Kumar", section="B")
raju(Name="Raju Kumar")
raju (Name="Manohar singh", Section="C")
manohar()
manohar("Ankit Kumar")
manohar("Raju Kumar", "B")
manohar(section="D")
manohar(section="B", name="Karan")
ankit()




