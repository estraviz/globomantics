from django.contrib.syndication.views import Feed
from django.urls import reverse


class NewInventoryFeed(Feed):
    title = "New Inventory"
    link = "/newitem/"

    def items(self):
        # In a real scenario, this would be a database query
        return ("iPhone 12", "Samsung Galaxy S21", "Google Pixel 5")

    def item_title(self, item):
        return "New Inventory Item"

    def item_description(self, item):
        return item

    def item_link(self, item):
        return reverse('newitem')
