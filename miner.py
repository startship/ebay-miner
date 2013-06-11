# -*- coding: utf-8 -*-
'''
© 2012-2013 j$ startship enterprise
Authored by: Justin $
Licensed under CDDL 1.0
'''

import os
import sys
import json
from optparse import OptionParser
from xml.dom.minidom import parseString
import datetime

sys.path.insert(0, '%s/../' % os.path.dirname(__file__))

import ebaysdk
from ebaysdk import trading

class miner:
    def removeNonAscii(self, s): return "".join(i for i in s if ord(i)<128)

    def __init__(self):
        usage = "usage: %prog [options]"
        self.parser = OptionParser(usage=usage)

        self.parser.add_option("-d", "--debug",
                          action="store_true", dest="debug", default=False,
                          help="Enabled debugging [default: %default]")
        self.parser.add_option("-y", "--yaml",
                          dest="yaml", default='ebay.yaml',
                          help="Specifies the name of the YAML defaults file. [default: %default]")
        self.parser.add_option("-a", "--appid",
                          dest="appid", default=None,
                          help="Specifies the eBay application id to use.")
        self.parser.add_option("-p", "--devid",
                          dest="devid", default=None,
                          help="Specifies the eBay developer id to use.")
        self.parser.add_option("-c", "--certid",
                          dest="certid", default=None,
                          help="Specifies the eBay cert id to use.")

        (self.opts, self.args) = self.parser.parse_args()


    def getItemDetail(self, item_id = None):
        print "retrieving results for item",
        print item_id
        print "Using ebay trading SDK version %s" % ebaysdk.get_version()
        print "===================="
        # build and execute ebay API call GetItemTransactions
        api = trading(debug=self.opts.debug, config_file=self.opts.yaml, appid=self.opts.appid,
                      certid=self.opts.certid, devid=self.opts.devid)
        token = api.api_config.get('token')
        
        api.execute('GetItem', {'ItemID': item_id, 'DetailLevel': 'ReturnAll'})
        
        if api.error():
            print api.error()
            raise Exception(api.error())

        if api.response_content():
            print "Call Success: %s in length" % len(api.response_content())

        print "Response code: %s" % api.response_code()
        print "Response DOM: %s" % api.response_dom()
        debug_results = parseString(self.removeNonAscii(api.response_content()))
        print debug_results.toprettyxml()
    


    def getItemTrans(self, item_id = None):
        print "retrieving results for item",
        print item_id
        print "Using ebay trading SDK version %s" % ebaysdk.get_version()
        print "===================="


        # build and execute ebay API call GetItemTransactions
        api = trading(debug=self.opts.debug, config_file=self.opts.yaml, appid=self.opts.appid,
                      certid=self.opts.certid, devid=self.opts.devid)
        token = api.api_config.get('token')
        
        api.execute('GetItemTransactions', {'ItemID': item_id})

     

        if api.error():
            print api.error()
            raise Exception(api.error())

        if api.response_content():
            print "Call Success: %s in length" % len(api.response_content())

        print "Response code: %s" % api.response_code()
        print "Response DOM: %s" % api.response_dom()

        seller = api.response_dict().Item.Seller.UserID
        title = self.removeNonAscii(api.response_dict().Item.Title)
        sold = api.response_dict().Item.SellingStatus.QuantitySold

        if self.opts.debug:
            debug_results = parseString(self.removeNonAscii(api.response_content()))
            with open(item_id + "_full_results.xml", "w") as f:
                f.write( debug_results.toprettyxml() )

        print "Listing" + title 
        print "Seller: " + seller 
        print "Quanitiy Sold: " + sold 
        print "==========================================================================="
        print "========================= Sales History (30 days)=========================="
        print "==========================================================================="
        # output all transactions
        if api.response_dict().TransactionArray != None:
            if type(api.response_dict().TransactionArray.Transaction) is list:
                for trans in api.response_dict().TransactionArray.Transaction:
                    date = trans.CreatedDate
                    user = trans.Buyer.UserID
                    paid = trans.ConvertedTransactionPrice.value 
                    shipping = trans.ShippingDetails.ShippingServiceOptions.ShippingService
                    
                    print "Date: %(date)s \t Price: %(price)s \t User: %(user)s \t Shipping: %(ship)s" % \
                                 {'date': date, 'price' : paid, 'user' : user, 'ship' : shipping}
            else:
                # if only one transaction, we have to deal with a list instead of dict
                trans = api.response_dict().TransactionArray.Transaction
                date = trans.CreatedDate
                user = trans.Buyer.UserID
                paid = trans.ConvertedTransactionPrice.value 
                shipping = trans.ShippingDetails.ShippingServiceOptions.ShippingService
                
                print "Date: %(date)s \t Price: %(price)s \t User: %(user)s \t Shipping: %(ship)s" % \
                             {'date': date, 'price' : paid, 'user' : user, 'ship' : shipping}

    def getSellerItems(self, seller_id = None, cat_id = None, days = None):
        print "retrieving items for seller/category id: ",
        print seller_id + " / ",
        print cat_id
        print "Using ebay trading SDK version %s" % ebaysdk.get_version()
        print "===================="
        if days > 0:
            earliest = datetime.datetime.now()
            latest = earliest + (datetime.timedelta(days))
            earliest_s = 'EndTimeFrom'
            latest_s = 'EndTimeTo'
            
        else:
            latest = datetime.datetime.now()
            earliest = latest + (datetime.timedelta(days))
            earliest_s = 'StartTimeFrom'
            latest_s = 'StartTimeTo'
        print earliest
        print latest

        # build and execute ebay API call GetItemTransactions
        api = trading(debug=self.opts.debug, config_file=self.opts.yaml, appid=self.opts.appid,
                      certid=self.opts.certid, devid=self.opts.devid)
        token = api.api_config.get('token')
        
        page = 1
        api.execute('GetSellerList', {'DetailLevel': 'ItemReturnDescription', \
                                        'Pagination':{'EntriesPerPage': 50, 'PageNumber': page},\
                                        'CategoryID': cat_id,'UserID': seller_id, \
                                        earliest_s: earliest, latest_s: latest})
        if api.error():
            print api.error()
            raise Exception(api.error())

        if api.response_content():
            print "Call Success: %s in length" % len(api.response_content())
            print "Response code: %s" % api.response_code()
            print "Response DOM: %s" % api.response_dom()
            
        num_pages = api.response_dict().PaginationResult.TotalNumberOfPages

        while 1:
            if self.opts.debug:
                debug_results = parseString(self.removeNonAscii(api.response_content()))
                print debug_results.toprettyxml()
            # output all seller items
            if api.response_dict().ItemArray != None:
                for item in api.response_dict().ItemArray.Item:
                    id = item.ItemID
                    list_date, time = item.ListingDetails.StartTime.split('T')
                    cat = item.PrimaryCategory.CategoryID
                    quantity = item.Quantity
                    sold = item.SellingStatus.QuantitySold
                    cprice = item.SellingStatus.ConvertedCurrentPrice.value
                    sprice = item.ShippingDetails.ShippingServiceOptions.ShippingServiceCost.value
                    title = item.Title
                    SKU = item.SKU
                    hits = item.HitCount
                    print "ItemID> %(item)s >Category> %(cat)s >SKU> %(SKU)s  >Title> %(title)s >Quantity> %(quantity)s >Price> %(price)s >ShipCost> %(ship)s >Sold> %(sold)s >Listed> %(list_date)s >PageHits> %(hits)s" % \
                    {'item': id, 'cat' : cat, 'SKU' : SKU, 'title': title, 'quantity' : quantity, 'price': cprice, 'ship': sprice, 'sold': sold, 'list_date': list_date, 'hits': hits }
            #determine if we need another pass
            page+=1
            sys.stdout.flush()
            if page <= num_pages:
                api.execute('GetSellerList', {'DetailLevel': 'ItemReturnDescription', \
                        'Pagination':{'EntriesPerPage': 50, 'PageNumber': page},\
                        'CategoryID': cat_id,'UserID': seller_id, \
                        earliest_s: earliest, latest_s: latest})
            else:break


    def getCategories(self):
        # build and execute ebay API call GetItemTransactions
        api = trading(debug=self.opts.debug, config_file=self.opts.yaml, appid=self.opts.appid,
                      certid=self.opts.certid, devid=self.opts.devid)
        token = api.api_config.get('token')
        api.execute('GetCategories', {'DetailLevel': 'ReturnAll', 'ViewAllNodes': 'true'})
        if api.error():
            print api.error()
            raise Exception(api.error())

        if api.response_content():
            print "Call Success: %s in length" % len(api.response_content())

        print "Response code: %s" % api.response_code()
        print "Response DOM: %s" % api.response_dom()
        debug_results = parseString(self.removeNonAscii(api.response_content()))
        print debug_results.toprettyxml()

if __name__ == "__main__":
    m = miner()
    item_id  = sys.argv[1]
    miner.getItemTrans(item_id)
