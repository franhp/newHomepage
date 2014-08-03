from django.db import models


class Flag(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.name

    def findFlag(self, country):
        try:
            return Flag.objects.filter(name=country)[0]
        except IndexError:
            raise Exception('Flag for [%s] not found, please add it' % country)


class Place(models.Model):
    country = models.CharField(max_length=200)
    latlong = models.CharField(max_length=200)
    flag = models.ForeignKey(Flag)
    flag_url = ''
    city = models.CharField(max_length=4000)
    date = models.IntegerField()
    cities = []

    def __unicode__(self):
        return self.city + ', ' + self.country + ' (' + str(self.date) + ')'

    def getPlaces(self):
        return Place.objects.all().order_by('-date', '-country')

    def getCitiesArray(self):
        places = Place.objects.all().order_by('-date')
        finalList = []
        countryList = []

        for place in places:
            p = Place()
            p.setPlace(place.country, place.latlong, place.date)
            p.flag = place.flag
            p.flag_url = place.flag.url
            cities = Place.objects.filter(country=place.country)
            citiesArray = []
            years = []
            for city in cities:
                newCity = City()
                citiesArray.append(newCity.setCity(city.city, city.date, city.latlong))
                years.append(str(city.date))
            p.cities = citiesArray
            p.date = ', '.join(list(set(years)))

            if p.country not in countryList:
                finalList.append(p)
                countryList.append(p.country)

        return finalList

    def setPlace(self, country, latlong, date):
        self.country = country
        self.latlong = latlong
        self.date = date
        return self

    def savePlace(self, country, city, latlong, date):
        f = Flag()
        flag = f.findFlag(country)
        p = Place(country=country, latlong=latlong[1:-1], flag=flag, city=city, date=date)
        p.save()


class City():
    name = ''
    date = ''
    latlong = ''

    def setCity(self, name, date, latlong):
        self.name = name
        self.date = date
        self.latlong = latlong
        return self