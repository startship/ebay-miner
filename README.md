ebay-miner
==========

Data miner for ebay sales data. Currently uses ebay's trading api to perform a GetItemTransactions 
request. Results are then parsed into a Results.txt and Results.xml file.

Useage:
-----------
Pass in an Item ID (required) as an arguments

Results are output into *_results.txt & *full_results.xml
  

Requirements:
------------
###*Requires ebay-sdk-python*

https://github.com/timotheus/ebaysdk-python


TODO:
==========
[x] Implemented Calls to GetItemTransaction using ebay-sdk-python api
[x] Parse seller_id, title, items_sold, and transaction history datat (30 day)
[x] Output results to a txt and xml file
[ ] Create GUI which accepts item id, or multple item ids
[ ] Add table to GUI for simplified viewing of results data (or export to excel)
[ ] Create more advanced features, including mining all sales data from a seller
