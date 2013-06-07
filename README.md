ebay-miner
==========

Data miner for ebay sales data. Currently uses ebay's trading api to perform a GetItemTransactions, GetSellerList, 
and GetCategories request. Results are then parsed and display into the the textbox display.

Useage:
-----------

Item Transactions - enter an ebay item# (eg 140729321245)
  - returns 30-day transaction history

Get Seller Items - enter seller user id and a category ID# (eg. 80053 (monitors))
  - returns all seller items ending within 30-days (ebay max) w/ detailed results for each item
  - note category IDs are ebay defined assets and will change over time

Get Ebay Category#'s - no input, just push the button
  - returns an xml list of all ebay categories #'s level 1-4


  

Requirements:
------------
###*Requires ebay-sdk-python*

https://github.com/timotheus/ebaysdk-python


TODO:
==========
- [x] Implemented Calls to GetItemTransaction using ebay-sdk-python api
- [x] Parse seller_id, title, items_sold, and transaction history datat (30 day)
- [x] Output results to a txt and xml file
- [x] Created crappygui with Tkinter need something better...
- [x] Updated GUI which accepts item id , seller, and category
- [x] Add table to GUI for simplified viewing of results data (or export to excel)
- [ ] Add seller category miner, retrieving sales data for all items at once
