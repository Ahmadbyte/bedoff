

class Guest:
    def __init__(self , name):
        selfname = name

class Booking:
    def __init__(self , guest):
        self.guest = guest

class BookingGroup:
    def __init__(self , bookings , checkInDate , checkOutDate):
        self.bookings = bookings
        self.checkInDate = checkInDate
        self.checkoutDate = checkOutDate

class Result:
    def __init__(self , bookingGroupList):
        self.bookingGroupList = bookingGroupList


class BookingGroupFilter:
    def __init__(self, status , checkInDate , checkOutDate , noOfDays):
        self.statue = status
        self.checkInDate = checkInDate
        self.checkoutDate = checkOutDate
        self.noOfDays = noOfDays




