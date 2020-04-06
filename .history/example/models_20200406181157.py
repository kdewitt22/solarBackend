from django.db import models

class Client (models.Model):
    clientCode = models.CharField(max_length=8)
    clientName = models.CharField(max_length=10)
    clientType = models.CharField(max_length=10)

class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    officePhone = models.CharField(max_length=15)
    cellPhone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    client = models.ForeignKey(Client, on_delete=CASCADE)
    
#######################
########SETTERS########
#######################
    def setUsername(self, username):
        self.username = username
    def setPassword(self, password):
        self.password = password
    def setFirstName(self, first_name):
        self.first_name = first_name
    def setMiddleName(self, middle_name):
        self.middle_name = middle_name 
    def setLastName(self, last_name):
        self.last_name = last_name
    def setAddress(self, address):
        self.address = address
    def setOfficePhone(self, officePhone):
        self.officePhone = officePhone
    def setCellPhone(self, cellPhone):
        self.cellPhone = cellPhone
    def setEmail(self, email):
        self.email = email
    

#######################
########GETTERS########
#######################
    def getUsername(self):
        return self.username
    def getPassword(self):
        return self.password
    def getFirstName(self):
        return self.first_name
    def getMiddleName(self):
        return self.midde_name
    def getLastName(self):
        return self.last_name
    def getAddress(self):
        return self.address
    def getOfficePhone(self):
        return self.officePhone
    def getCellPhone(self):
        return self.cellPhone
    def getEmail(self):
        return self.email

class Location(models.Model):
    address1 = models.CharField(max_length=10)
    address2= models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    postalCode = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    phoneNum = models.CharField(max_length=15)
    faxNum = models.CharField(max_length=15)
    client = models.ForeignKey(Client)

class TestStandard(models.Model):
    testStandard = models.CharField(max_length=20)
    description = models.CharField(max_length=255)
    publishDate = models.CharField(max_length=10)

class Certificate(models.Model):
    certID = models.CharField(max_length=8)
    user = models.ForeignKey(User)
    reportNum = models.CharField(max_length=8)
    issueDate = models.CharField(max_length=10)
    testStandard = models.ForeignKey(TestStandard)
    location = models.ForeignKey(Location)
    modelNum = models.ForeignKey(Product)

class Product(models.Model):
    productName = models.CharField(max_length=20)
    cellTechnology = models.CharField(max_length=20)
    cellManufacturer = models.CharField(max_length=20)
    numCells = models.CharField(max_length=20)
    numCellsSeries = models.CharField(max_length=20)
    numSeriesStrings = models.CharField(max_length=20)
    numDiodes = models.CharField(max_length=20)
    prodLengh = models.CharField(max_length=20)
    prodWidth = models.CharField(max_length=20)
    superstrateType = models.CharField(max_length=20)
    superstrateManufacturer = models.CharField(max_length=20)
    substrateType = models.CharField(max_length=20)
    substrateManufacturer = models.CharField(max_length=20)
    frameType = models.CharField(max_length=20)
    frameAdhesive = models.CharField(max_length=20)
    encapsulantType = models.CharField(max_length=20)
    encapsulatManufacturer = models.CharField(max_length=20)
    junctionBoxType = models.CharField(max_length=20)
    junctionBoxManufacturer = models.CharField(max_length=20)

#######################
########GETTERS########
#######################
    def getProductName(self):
        return self.productName 
    def getCellTechnology(self):
        return self.cellTechnology
    def getCellManufacturer(self):
        return self.cellManufacturer
    def getNumCells(self):
        return self.numCells 
    def getNumCellsSeries(self):
        return self.numCellsSeries
    def getSumSeriesStrings(self):
        return self.numSeriesStrings
    def getNumDiodes(self):
        return self.numDiodes 
    def getProdLength(self):
        return self.prodLengh 
    def getProdWidth(self):
        return self.prodWidth 
    def getSuperstrateType(self):
        return self.superstrateType
    def getSuperstrateManufacturer(self):
        return self.superstrateManufacturer
    def getSubstrateType(self):
        return self.substrateType 
    def getSubstrateManufacturer(self):
        return self.substrateManufacturer
    def getFrameType(self):
        return self.frameType 
    def getFrameAdhesive(self):
        return self.frameAdhesive
    def getEncapsulantType(self):
        return self.encapsulantType
    def getEncapsulantManufacturer(self):
        return self.encapsulatManufacturer
    def getJuntionBoxType(self):
        return self.junctionBoxType 
    def getJunctionBoxManufacturer(self):
        return self.junctionBoxManufacturer

#######################
########SETTERS########
#######################
    def setProductName(self, productName):
        self.productName = productName
    def setCellTechnology(self, cellTechnology):
        self.cellTechnology = cellTechnology
    def setCellManufacturer(self, cellManufacturer):
        self.cellManufacturer = cellManufacturer
    def setNumCells(self, numCells):
        self.numCells = numCells
    def setNumCellsSeries(self, numCellsSeries):
        self.numCellsSeries = numCellsSeries
    def setNumSeriesStrings(self, numSeriesStrings):
        self.numSeriesStrings = numSeriesStrings
    def setNumDiodes(self, numDiodes):
        self.numDiodes = numDiodes
    def setProdLength(self, prodLength):
        self.prodLengh = prodLength
    def setProdWidth(self, prodWidth):
        self.prodWidth = prodWidth
    def setSuperstrateType(self, superstrateType):
        self.superstrateType = superstrateType
    def setSuperstrateManufacturer(self, superstrateManufacturer):
        self.superstrateManufacturer = superstrateManufacturer
    def setSubstrateType(self, substrateType):
        self.substrateType = substrateType
    def setSubstrateManufacturer(self, substrateManufacturer):
        self.substrateManufacturer = substrateManufacturer
    def setFrameType(self, frameType):
        self.frameType = frameType
    def setFrameAdhesive(self, frameAdhesive):
        self.frameAdhesive = frameAdhesive
    def setEncapsulantType(self, encapsulantType):
        self.encapsulantType = encapsulantType
    def setEncapsulantManufacturer(self, encapsulantManufacturer):
        self.encapsulatManufacturer = encapsulantManufacturer
    def setJunctionBoxType(self, junctionBoxType):
        self.junctionBoxType = junctionBoxType
    def setJunctionBoxManufacturer(self, junctionBoxManufacturer):
        self.junctionBoxManufacturer = juctionBoxManufacturer

class TestSequence(models.Model):
    sequenceName = models.CharField(max_length = 20)

class PerformanceData(models.Model):
    product = models.ForeignKey(Product)
    sequence = models.ForeignKey(TestSequence)
    maxSystemVolts = models.CharField(max_length=10)
    voc = models.CharField(max_length=10)
    isc = models.CharField(max_length=10)
    vmp = models.CharField(max_length=10)
    imp = models.CharField(max_length=10)
    pmp = models.CharField(max_length=10)
    ff = models.CharField(max_length=10)

class Service(models.Model):
    serviceID = models.CharField(max_length=8)
    description = models.CharField(max_length=255)
    isFiRequired = models.CharField(max_length=3)
    fiFrequency = models.CharField(max_length=10)
    standard = models.ForeignKey(TestStandard)    