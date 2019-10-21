import TransactionGrammar as ledgerParser
import sys
import os

def parse_index(indexPath):
    filePaths =[]
    index = open(indexPath,'r')
    for line in index:
        result = line.strip("\n ")
        result = result.split(" ")
        if result[0] != '':
            print("Result"+ str(result)) 
            if len(result) > 1:
                if result[0] == '!include':
                    filePaths.append(result[1])
                else:
                    pass
            else:
                raise Exception("While parsing file {} \n directive '{}' requires an argument".format(indexPath, result[0]))    
  
    for filePath in filePaths:
        if not os.path.isfile(filePath):
            raise Exception("While parsing file {} \n file to include was not found '{}'".format(indexPath, filePath))
    return filePaths

def read_files(filePaths):
    all_transactions=[]
    for path in filePaths:
        file_content = ''.join(open(path,'r'))
        tree = ledgerParser.parse(file_content)
        all_transactions = all_transactions + fetch_transactions(tree) 
    return all_transactions



def fetch_transactions(tree):
    transactions=[]
    for node in tree:
        T={}
        T["Date"] = node.elements[0].text
        T["Description"] = node.elements[2].text
        postings =[]
        posting = {}

        posting["Account"] = node.elements[5].elements[0].text
        posting["Quantity"] = node.elements[5].elements[2].Quantity.text
        posting["Commodity"] = node.elements[5].elements[2].Commodity.text
        postings.append(posting)

        for ap in node.elements[6]:
            auxPosting = {}
            auxPosting["Account"] = ap.elements[1].elements[0].text
            
            if len(ap.elements[1].elements[2].elements) != 0:
                auxPosting["Quantity"] = ap.elements[1].elements[2].Quantity.text
                auxPosting["Commodity"] = ap.elements[1].elements[2].Commodity.text

            else:
                auxPosting["Quantity"] = 0
                auxPosting["Commodity"] = "$"

            postings.append(auxPosting)
            
        T["Postings"] = postings
        transactions.append(T)
    return transactions