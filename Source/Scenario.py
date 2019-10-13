# -*- coding: utf-8 -*-
import xml.etree.ElementTree as et
import DataStructures as ds

class Scenario():
    def __init__(self):
        self.cm = None
        self.channels = None
        self.cdisList = None
        
    def read(self, cm_xml_path, cdis_xml_path):
        xmlTree = et.parse(cm_xml_path)
        xmlRoot = xmlTree.getroot()
        
        ceList = []
        
        for ceElement in xmlRoot.findall('ceList'):
            ceClientList = []
            
            for ceClientElement in ceElement.findall('CEClientList'):
                id = ceClientElement.find('id').text
                latitude = float(ceClientElement.find('latitude').text)
                longitude = float(ceClientElement.find('longitude').text)
                signal = int(ceClientElement.find('nivelSinal').text)
                interference = float(ceClientElement.find('interferenciaCocanal').text)
                
                ceClient = ds.CEClient(id, latitude, longitude, signal, interference)
                
                ceClientList.append(ceClient)
            
            id = ceElement.find('id').text
            antenna = ceElement.find('antena').text
            channel = int(ceElement.find('device').find('canal').text)
            latitude = float(ceElement.find('latitude').text)
            longitude = float(ceElement.find('longitude').text)
            potency = int(ceElement.find('potencia').text)
            maxPotency = int(ceElement.find('potenciaMax').text)
            
            ce = ds.CE(id, antenna, channel, latitude, longitude, potency, maxPotency, ceClientList)
            
            ceList.append(ce)
        
        id = xmlRoot.find('id').text  
        self.cm = ds.CM(id, ceList)
        
        channelList = []
        
        for channelElement in xmlRoot.findall('channels'):
            name = channelElement.find('nome').text
            number = channelElement.find('numCanal').text
            frequency = channelElement.find('frequencia').text
            state = ds.ChannelState[channelElement.find('estado').text]
            
            channel = ds.Channel(name, number, frequency, state)
            channelList.append(channel)
        
        self.channels = channelList 
        
        xmlTree = et.parse(cdis_xml_path)
        xmlRoot = xmlTree.getroot()
        
        cdisList = []
        
        for cdisElement in xmlRoot.findall('cdis'):
            channelList = []
            
            for channelElement in cdisElement.findall('canaisTvdb'):
                name = channelElement.find('nome').text
                number = channelElement.find('numCanal').text
                frequency = channelElement.find('frequencia').text
                state = ds.ChannelState[channelElement.find('estado').text]
                
                channel = ds.Channel(name, number, frequency, state)                
                channelList.append(channel)
                
                cdis = ds.CDIS(channelList)
                cdisList.append(cdis)
                
        self.cdisList = cdisList































































