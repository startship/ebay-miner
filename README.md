ebay-miner
==========

Data miner for ebay sales data. Currently uses ebay's trading api to perform a GetItemTransactions 
request. Results are then parsed into a Results.txt and Results.xml file.

Input:
  Item ID (requeired)
  
Output:
  (Item ID)_results.txt
  (Item ID)_full_results.xml


*Requires ebay-sdk-python*
https://github.com/timotheus/ebaysdk-python
