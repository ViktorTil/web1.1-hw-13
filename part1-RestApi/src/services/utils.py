from datetime import datetime

def calc_birthday(data):
        today = datetime.now().date()
        birth_date = data
        if birth_date.month == 2 and birth_date.day == 29:
            future_birthday = datetime(year = today.year, month = 2, day = birth_date.day - int(bool(today.year%4))).date()    
            if future_birthday < today: 
                future_birthday = datetime(year = today.year + 1, month = 2, day = birth_date.day - int(bool((today.year+1)%4))).date()    
        else:
            future_birthday = datetime(year = today.year, month = birth_date.month, day = birth_date.day).date()
            if future_birthday < today:
                future_birthday = future_birthday.replace(year = today.year + 1)
        return (future_birthday - today).days
    
def next_seven_days(contacts):
    list_contacts = []
    for contact in contacts:
        if calc_birthday(contact.birthday) <= 7:
            list_contacts.append(contact)
    return list_contacts
