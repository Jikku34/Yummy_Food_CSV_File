from django.db import models


class ShopDetails(models.Model):
    shop_id = models.IntegerField()
    name = models.CharField(max_length=50, null=True)
    location = models.CharField(max_length=150, null=True)
    lat_long = models.CharField(max_length=150, null=True)
    cuisines = models.CharField(max_length=150, null=True)
    currency = models.CharField(max_length=150, null=True)
    price_range = models.IntegerField(null=True)
    mezzo_provider = models.CharField(max_length=150, null=True)
    order_deeplink = models.CharField(max_length=150, null=True)
    has_table_booking = models.IntegerField(null=True)
    is_delivering_now = models.IntegerField(null=True)
    opentable_support = models.IntegerField(null=True)
    has_online_delivery = models.IntegerField(null=True)
    include_bogo_offers = models.CharField(max_length=150, null=True)
    average_cost_for_two = models.IntegerField(null=True)
    switch_to_order_menu = models.IntegerField(null=True)
    is_book_form_web_view = models.IntegerField(null=True)
    book_form_web_view_url = models.CharField(max_length=150, null=True)
    is_table_reservation_supported = models.IntegerField(null=True)

    class Meta:
        db_table = "shop_details"

    def __int__(self):
        return self.shop_id


class ShopLocation(models.Model):
    shop_id = models.IntegerField()
    city = models.CharField(max_length=150, null=True)
    address = models.CharField(max_length=150, null=True)
    city_id = models.IntegerField(null=True)
    zipcode = models.CharField(max_length=150, null=True)
    latitude = models.CharField(max_length=150, null=True)
    locality = models.CharField(max_length=150, null=True)
    longitude = models.CharField(max_length=150, null=True)
    country_id = models.IntegerField(null=True)
    locality_verbose = models.CharField(max_length=150, null=True)

    class Meta:
        db_table = "shop_location"

    def __int__(self):
        return self.shop_id


class ShopRate(models.Model):
    shop_id = models.IntegerField()
    votes = models.IntegerField()
    rating_text = models.CharField(max_length=150, null=True)
    rating_color = models.CharField(max_length=150, null=True)
    aggregate_rating = models.FloatField()

    class Meta:
        db_table = "shop_rate"

    def __int__(self):
        return self.shop_id


class ShopDish(models.Model):
    shop_id = models.IntegerField()
    food = models.CharField(max_length=150, null=True)
    price = models.FloatField(null=True)

    class Meta:
        db_table = "shop_dishes"

    def __int__(self):
        return self.shop_id
