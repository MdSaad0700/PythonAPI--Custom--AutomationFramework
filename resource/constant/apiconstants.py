# URL Constants


def base_url():
    return "https://restful-booker.herokuapp.com"


def create_booking():
    return "https://restful-booker.herokuapp.com/booking"

def create_token():
    return "https://restful-booker.herokuapp.com/auth"

def update_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking"+booking_id