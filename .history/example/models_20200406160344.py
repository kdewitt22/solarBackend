from django.db import models

class Product:
    def __init__(self, modelNumber, manufacturer, manufacturingDate, length, width, weight, cellArea, cellTechnology, totalNumCells, seriesCells, seriesStrings, bypassDiodes, seriesFuseRating, interconnectMaterial, interconnectSupplier, superstrateType, superstrateManufacturer, substrateType, substrateManufacturer, frameMaterial, frameAdhesive, encapsulantType, encapsulantManufacturer, junctionBoxType, juctionBoxManufacturer, junctionBoxAdhesive, cableType, connectorType, maximumSystemVoltage, voc, isc, vmp, imp, pmp, ff): 
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
        self.junctionBoxManufacturer = juctionBoxManufacturer

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




    def setModelNumber(self, ):
        self.modelNumber = modelNumber
    def setManufacturer(self, manufacturer):
        self.manufacturer = manufacturer
    def setManufacturingDate(self, manufacturingDate):
        self.manufacturingDate = manufacturingDate
    def setLenth(self, length):
        self.length = length
    def setWidth(self, width):
        self.width = width
    def setWeight(self, weight):
        self.weight = weight
    def setCellArea(self, cellArea):
        self.cellArea = cellArea
    def setCellTechnology(self):
        self.cellTechnology = cellTechnology
    def setTotalNumCells(self, totalNumCells):
        self.totalNumCells = totalNumCells
    def setSeriesCells(self, seriesCells):
        self.seriesCells = seriesCells
    def setSeriesStrings(self, seriesStrings):
        self.seriesStrings = seriesStrings
    def setBypassDiodes(self, bypassDiodes):
        self.bypassDiodes = bypassDiodes
    def setSeriesFuseRating(self, seriesFuseRating):
        self.seriesFuseRating = seriesFuseRating
    def setInterconnectMaterial(self, interconnectMaterial):
        self.interconnectMaterial = interconnectMaterial
    def setInterconnectSupplier(self, interconnectSupplier):
        self.interconnectSupplier = interconnectSupplier
    def setSuperstrateType(self, superstrateType):
        self.superstrateType = superstrateType
    def setSuperstrateManufacturer(self, superstrateManufactueer):
        self.superstrateManufacturer = superstrateManufacturer
    def setSubstrateType(self, substrateType):
        self.substrateType = substrateType
    def setSubstrateManufacturer(self, substrateManufacturer):
        self.substrateManufacturer = substrateManufacturer
    def setFrameMaterial(self, frameMaterial):
        self.frameMaterial = frameMaterial
    def setFrameAdhesive(self, frameAdhesive):
        self.frameAdhesive = frameAdhesive
    def setEncapsulantType(self, encapsulantType):
        self.encapsulantType = encapsulantType
    def setEncapsulantManufacturer(self, encapsulantManufacturer):
        self.encapsulatManufacturer = encapsulantManufacturer
    def setJunctionBoxType(self, junctionBoxType):
        self.junctionBoxType = junctionBoxType
    def setJunctionBoxManufacturer(self, junctionBoxManufacturer):
        self.junctionBoxManufacturer = junctionBoxManufacturer
    def setJunctionBoxAdhesive(self, junctionBoxAdhesive):
        self.junctionBoxAdhesive = junctionBoxAdhesive
    def setCableType(self, cableType):
        self.cableType = cableType
    def setConnectorType(self, connectorType):
        self.connectorType = connectorType
    def setMaximumSystemVoltage(self, maximumSystemVoltage):
        self.maximumSystemVoltage = maximumSystemVoltage
    def setVOC(self, voc):
        self.voc = voc
    def setISC(self, isc):
        self.isc = isc
    def setVMP(self, vmp):
        self.vmp = vmp
    def setIMP(self, imp):
        self.imp = imp
    def setPMP(self, pmp):
        self.pmp = pmp
    def setFF(self, ff):
        self.ff = ff

    def getModelNumber(self):
        return self.modelNumber
    def getManufacturer(self):
        return self.manufacturer
    def getManufacturingDate(self):
        return self.manufacturingDate
    def getLength(self):
        return self.length
    def getWidth(self):
        return self.width
    def getWeight(self):
        return self.weight
    def getCellArea(self):
        return self.cellArea
    def getCellTechnology(self):
        return self.cellTechnology
    def getTotalNumCells(self):
        return self.totalNumCells
    def getSeriesCells(self):
        return self.seriesCells
    def getSeriesStrings(self):
        return self.seriesStrings
    def getBypassDiodes(self):
        return self.bypassDiodes
    def getSeriesFuseRating(self):
        return self.seriesFuseRating
    def getInterconnectMaterial(self):
        return self.interconnectMaterial
    def getInterconnectSupplier(self):
        return self.interconnectSupplier
    def getSuperstrateType(self):
        return self.superstrateType
    def getSuperstrateManufacturer(self):
        return self.superstrateManufacturer
    def getSubstrateType(self):
        return self.substrateType
    def getSubstrateManufacturer(self):
        return self.substrateManufacturer
    def getFrameMaterial(self):
        return self.frameMaterial
    def getFrameAdhesive(self):
        return self.frameAdhesive
    def getEncapsulantType(self):
        return self.encapsulantType
    def getEncapsulantManufacturer(self):
        return self.encapsulantManufacturer
    def getJunctionBoxType(self):
        return self.junctionBoxType
    def getJunctionBoxManufacturer(self):
        return self.junctionBoxManufacturer
    def getJunctionBoxAdhesive(self):
        return self.junctionBoxAdhesive
    def getCableType(self):
        return self.cableType
    def getConnectorType(self):
        return self.connectorType
    def getMaxSystemVoltage(self):
        return self.maximumSystemVoltage
    def getVOC(self):
        return self.voc
    def getISC(self):
        return self.isc
    def getVMP(self):
        return self.vmp
    def getIMP(self):
        return self.imp
    def getPMP(self):
        return self.pmp
    def getFF(self):
        return self.ff
