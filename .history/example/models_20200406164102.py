from django.db import models

class Client (models.Model):

    clientCode = models.CharField(max_length=8)
    clientName = models.CharField(max_length=10)
    clientType = models.CharField(max_length=10)

class Location(address1, address2, city, state, postalCode, country, phoneNum, faxNum, client):
    self.address1 = address1
    self.address2 = address2
    self.city = city
    self.postalCode = postalCode
    self.country = country
    self.phoneNum = phoneNum
    self.faxNum = faxNum
    self.client = client

TestStandard
    Name
    Desc
    PubDate
Certificate
    id
    userID>
    reportNum
    issueDate
    StandardID
    locationID
    modelNum





class Product:
    def __init__(self, productName, cellTechnology, cellManufacturer, numCells, numCellsSeries, numSeriesStrings, numDiodes, prodLength, prodWidth, superstrateType, superstrateManufacturer, substrateType, substrateManufacturer, frameType, frameAdhesive, encapsulantType, encapsulantManufacturer, junctionBoxType, junctionBoxManufacturer):
        self.productName = productName
        self.cellTechnology = cellTechnology
        self.cellManufacturer = cellManufacturer
        self.numCells = numCells
        self.numCellsSeries = numCellsSeries
        self.numSeriesStrings = numSeriesStrings
        self.numDiodes = numDiodes
        self.prodLengh = prodLength
        self.prodWidth = prodWidth
        self.superstrateType = superstrateType
        self.superstrateManufacturer = superstrateManufacturer
        self.substrateType = substrateType
        self.substrateManufacturer = substrateManufacturer
        self.frameType = frameType
        self.frameAdhesive = frameAdhesive
        self.encapsulantType = encapsulantType
        self.encapsulatManufacturer = encapsulantManufacturer
        self.junctionBoxType = junctionBoxType
        self.junctionBoxManufacturer = junctionBoxManufacturer

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

class User:
    def __init__(self, username, password, first_name, middle_name, last_name, address, officePhone, cellPhone, email):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.address = address
        self.officePhone = officePhone
        self.cellPhone = cellPhone
        self.email = email
    
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
