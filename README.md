# Poultry Management API
- [Poultry Management API](#-Poultry-management-api)
  - [Services](#services)
    - [Inventory](#inventory)
    - [Manure sales](#manure-sales)
    - [Expense type](#expense-type)
    - [Egg Sales type](#egg-sales-type)

---
A poultry management api which contains farm, logistics and sales management services.

## Services
    
### Inventory  
    
| Field | Data Type | Description |
|-------|-----------|-------------|
|category | Character   | inventory category |
|Item name| Character | inventory item name|
|Quantity | Integer | quantity |
|Unit | Integer | Patients sex or gender i.e Male or Female |
|Unit price | Float | Patients date of birth |
|Expiry date | Date| Expiry date|
|Supplier| Character | supplier name|
|Source supplier| Character | source supplier|

    
### Manure Sales 

| Field | Data Type | Description |
|-------|-----------|-------------|
|Quantity bags | Character   | inventory category |
|Date| Date | Date|
|Price per bag | Float | price per bag of manure |
|Total amount | Float | Total amount |
|Buyer name | Character | Name of the buyer |
|Payment Method | Character| payment method|
|Manure type| Character | manure type|
|Manure quality| Character | manure quality|


### Expense Type
                     
| Field | Data Type | Description |
|-------|-----------|-------------|
|Expense type | Character   | Type of expense |
|Flock| Character| flock|
|Amount | Float | amount |
|Date | Date | Date |
|Description | Character | Description|
|Paid by| Character | paid by|
|Payment method| Character | Payment method|

### Egg Sales Type 

| Field | Data Type | Description |
|-------|-----------|-------------|
|Flock | Character   | flock |
|Date| Date| Date eggs were sold|
|Trays sold | Integer | Number of trays sold |
|Total amount| Float | Total amount |
|Buyer name| Character | Name of the buyer|
|Payment method| Character | Method of payment i.e cash or Mobile money|
|Sale type| Character| Type of sale i.e retail or wholesale|
|Egg type| Character| Type of egg |
|Payment status| Character | Status of payment i.e paid or unpaid |


### Expense Type 

| Field | Data Type | Description |
|-------|-----------|-------------|
|Expense type | Character   | Type of expense i.e feed or treatment or  |
|Flock| Character| type of flock i.e batch 1 or batch 2 |
|Amount| Float | Amount |
|Date| Date | Date |
|Paid by| Character | Who made the payment|
|Description| Character | Description|
|Payment method| Character | Method of payment i.e cash or Mobile money|
