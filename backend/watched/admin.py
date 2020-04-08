from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import path

from watched.models import Title


class CustomTitle(admin.ModelAdmin):
    list_display = ("name", "title_type", "site_rating", "my_rating", "ranking_order")
    list_filter = ("title_type",)
    search_fields = ("name",)

    def get_urls(self):
        urls = super(CustomTitle, self).get_urls()
        new_urls = [
            path("import_imdb/", import_imdb),
            path("import_goodreads/", import_goodreads),
        ]
        return new_urls + urls


def import_imdb(self):
    Title.import_imdb()
    return HttpResponseRedirect(self.META["HTTP_REFERER"])


def import_goodreads(self):
    Title.import_goodreads()
    return HttpResponseRedirect(self.META["HTTP_REFERER"])


admin.site.register(Title, CustomTitle)
