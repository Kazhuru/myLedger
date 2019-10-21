from flagsComms import *
URL_PDB = "price_db";
URL_INDEX = "index.ledger"

class Model:
    def __init__(self, transactions, url_PriceDB):
        self.transactions = transactions
        self.listPriceDB = readPricesDB(url_PriceDB)
        self.accounts = []
        for itTra in transactions:
            for itPost in itTra.Postings:
                fillAccounts(self,itPost.Account);
                arrAccs = itPost.Account.split(":")
                itTra.postings["Account"] = arrAccs;
                

    def fillAccounts(self, currentAccount):
        splitAccs = currentAccount.split
        if not (splitAccs[0] in self.accounts):
            self.accounts.append(splitAccs[0])

    def sortTransactionsByDate(self, list):
        if len(list) > 1:
            mid = len(list) / 2
            L = list[:mid]
            R = list[mid:]

            sortTransactionsByDate(L)
            sortTransactionsByDate(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if (L[i].date < R[j].date):
                    list[k] = L[i]
                    i += 1
                else:
                    list[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                list[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                list[k] = R[j]
                j += 1
                k += 1