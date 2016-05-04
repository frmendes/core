from geopy.geocoders import Nominatim
from geopy.distance import vincenty
import math
import threading

class GPS():
    @classmethod
    def distance_between(cls, p1, p2):
    """Returns distance between to points, in meters, rounded up to 2 decimal points"""
        return round((vincenty(p1, p2).meters),2)

    @classmethod
    def bearing_to_north(cls, lat1, lon1, lat2, lon2):
        dLon = lon2 - lon1
        y = math.sin(dLon) * math.cos(lat2)
        x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(dLon)
        return math.atan2(y, x)

    @classmethod
    def turn_between(cls, d1, d2):
        """Calculates tuple (turn angle [degrees], turn dir [+1 == right, -1 == left])."""
        diff = d1 - d2
        neg = diff < 0
        big = abs(diff) > math.pi

        if not neg and not big: theta = diff; lr = +1
        if not neg and big: theta = 2*math.pi - diff; lr = -1
        if neg and not big: theta = abs(diff); lr = -1
        if neg and big: theta = 2*math.pi - abs(diff); lr = +1

        return (theta*57.2957795, lr)

