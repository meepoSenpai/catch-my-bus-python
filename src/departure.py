'''
This only contains the Departure class.
No further explanation needed.
'''
import notify2

class Departure:
    '''
    The Departure class which has the functionality to notify the user
    of an upcoming departure. The constructor is passed a line_number
    as int, a direction as str and an arrival_time as timestamp
    '''
    def __init__(self, line_number, direction, arrival_time):
        self.line_number = line_number
        self.direction = direction
        if arrival_time == '':
            self.arrival_time = 0
        else:
            self.arrival_time = int(arrival_time)
        self.selected = False
        self.notification = {}

    def update_arrival_time(self, new_arrival_time):
        '''
        Updates the arrival_time of the Departure Object to the new
        arrival time that is passed to this function
        '''
        self.arrival_time = new_arrival_time

    def set_to_notify(self, icon_path, time=0):
        '''
        Creates a notify2 Notification and sets the departure object
        as selected
        '''
        self.selected = True
        notify2.init("StationNotification")
        self.notification = {"notification" : notify2.
                                              Notification("Bus arriving soon!",
                                                           "The bus will arrive in {0} minutes".
                                                           format(self.arrival_time),
                                                           icon_path),
                             "time" : time}

    def notify_user(self):
        '''
        Shows the notification and unselects the departure object
        '''
        self.notification['notification'].show()
        self.selected = False

    def __str__(self):
        output_str = "{0}\t{1}\t{2}"
        time_str = "{0}:{1}"
        time_h = int(self.arrival_time / 60)
        time_m = self.arrival_time % 60
        if time_m < 10:
            time_m = "0{0}".format(time_m)
        time_str = time_str.format(time_h, time_m)
        return output_str.format(self.line_number,
                                 self.direction,
                                 time_str)
