#GIVEN DATA FROM QUESTION
transactionLog = [{'orderId':1001, 'customerId':'cust_Ahmed','productId':'prod_10'},
{'orderId':1001, 'customerId':'cust_Ahmed','productId':'prod_12'},
{'orderId':1002, 'customerId':'cust_Bisma','productId':'prod_10'},
{'orderId':1002, 'customerId':'cust_Bisma','productId':'prod_15'},
{'orderId':1003, 'customerId':'cust_Ahmed','productId':'prod_15'},
{'orderId':1004, 'customerId':'cust_Faisal','productId':'prod_12'},
{'orderId':1004, 'customerId':'cust_Faisal','productId':'prod_18'},
]#product 18 is missing in the catalog let us assume its a laptop other an error is occured preventing the program run.

productCatalog = { 
    'prod_10' : 'Wireless Mouse',
    'prod_12' :'Keyboard',
    'prod_15':'USB-C HUB',
    'prod_18' : 'laptop'
}
#HERE ENDS GIVEN DATA
def process(transList):
    cust_data = {}
    for entry in transList:
        cid = entry['customerId']
        pid = entry['productId']
        if cid not in cust_data:
            cust_data[cid] = set()
        cust_data[cid].add(pid)
    return cust_data

def findReq(cust_data):
    pairCounter = {}
    for products in cust_data.values():
        pList = list(products)

        for i in range(len(pList)):
            for j in range(i+1,len(pList)):
                pair = tuple(sorted([pList[i],pList[j]]))
                pairCounter[pair] = pairCounter.get(pair,0) + 1
    return pairCounter

def getRecommended(targetPId,freqPairs):
    recs = {    }
    for (a,b),count in  freqPairs.items():
        if a == targetPId:
            recs[b] = count + recs.get(b,0)
        elif b == targetPId :
            recs[a] = count + recs.get(a,0)
    sortedRecs = sorted(recs.items(),key = lambda x: x[1], reverse=True)
    return sortedRecs[:3]

def generateReportFunction(targetPId, rec, cat):
    print(f"Recommended products for: {cat[targetPId]}")
    for i, (pid,score) in enumerate(rec, start=1):
        print(f"{i}. {cat[pid]} co-purchase count: {score}")

cust_data = process(transactionLog)
pairs = findReq(cust_data)
recs = getRecommended('prod_10',pairs)
generateReportFunction('prod_10',recs,productCatalog)
recs = getRecommended('prod_12',pairs)
generateReportFunction('prod_12',recs,productCatalog)

