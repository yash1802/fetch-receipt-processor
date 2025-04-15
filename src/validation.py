import re

class ValidationResult:
     def __init__(self: bool, is_valid, message = ""):
        self.is_valid = is_valid
        self.message = message

def is_pattern_valid(pattern,string):
    return bool(re.match(pattern, string))

def is_input_valid(value,type):
    return value is not None and isinstance(value, type)
    
def all_items_valid (items):
    """
    Parameters:
    - items (list of dict): A list of item dictionaries to be validated. 
    
    Returns:
    - bool: True if all items are valid according to the specified conditions, False otherwise.
    """
      
    for item in items:

        if not isinstance(item,dict):
            return False    
        
        shortDescription = item.get('shortDescription')
        price = item.get('price')

        if shortDescription is None or price is None:
            return False
            
        if not isinstance(shortDescription,str) or not is_pattern_valid(r"^[\w\s\-]+$", shortDescription):
            return False
            
        if not isinstance(price,str) or not is_pattern_valid(r"^\d+\.\d{2}$", price):
            return False
            
    return True

def validate_receipt(receipt):
    """
    Parameters:
    - receipt (dict): The receipt dictionary to be validated. It should have keys 'retailer', 'purchaseDate', 
      'purchaseTime', 'total', and 'items' with appropriate values.
    
    Returns:
    - bool: True if the receipt is valid according to the specified conditions, False otherwise.
    """

    if not is_input_valid(receipt,dict):
        return ValidationResult(False, "receipt has not correct type")

    purchase_date = receipt.get("purchaseDate")
    purchase_time =  receipt.get("purchaseTime")
    retailer_name =  receipt.get("retailer")
    receipt_total =  receipt.get("total")
    receipt_items = receipt.get("items")

    if not is_input_valid(purchase_time,str) or not is_pattern_valid(r"^(?:[01]\d|2[0-3]):[0-5]\d$",purchase_time):
        return ValidationResult(False, "purchase time is not correct")
    if not is_input_valid(receipt_total,str) or not is_pattern_valid(r"^\d+\.\d{2}$", receipt_total):
        return ValidationResult(False, "receipt total is not correct")
    if not is_input_valid(retailer_name, str) or not is_pattern_valid(r"^[\w\s&\-\'.]+$", retailer_name):
        return ValidationResult(False, "retailer name is not correct")
    if not is_input_valid(purchase_date,str) or not is_pattern_valid(r"^\d{4}-\d{2}-\d{2}$", purchase_date):
        return ValidationResult(False, "purchase date is not correct")
    if  (not is_input_valid(receipt_items,list)) or len(receipt_items) == 0 or (not all_items_valid(receipt_items)):
        return ValidationResult(False, "receipt items are not correct")
    
    return ValidationResult(True)
