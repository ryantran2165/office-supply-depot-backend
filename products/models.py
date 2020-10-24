from django.db import models


class Product(models.Model):
    class Category(models.TextChoices):
        OFFICE_SUPPLIES = 'OFFICE_SUPPLIES', 'OFFICE_SUPPLIES'
        FURNITURE = 'FURNITURE', 'FURNITURE'
        CLEANING = 'CLEANING', 'CLEANING'
        BREAKROOM = 'BREAKROOM', 'BREAKROOM'
        COMPUTERS_ACCESSORIES = 'COMPUTERS_ACCESSORIES', 'COMPUTERS_ACCESSORIES'
        ELECTRONICS = 'ELECTRONICS', 'ELECTRONICS'
        PAPERS = 'PAPERS', 'PAPERS'
        SCHOOL_SUPPLIES = 'SCHOOL_SUPPLIES', 'SCHOOL_SUPPLIES'
        INK_TONER = 'INK_TONER', 'INK_TONER'
        ETC = 'ETC', 'ETC'

    class Subcategory(models.TextChoices):
        PENS_PENCILS_MARKERS = 'PENS_PENCILS_MARKERS', 'PENS_PENCILS_MARKERS'
        BASIC_SUPPLIES = 'BASIC_SUPPLIES', 'BASIC_SUPPLIES'
        MAILING_SHIPPING = 'MAILING_SHIPPING', 'MAILING_SHIPPING'
        FILING_FOLDERS = 'FILING_FOLDERS', 'FILING_FOLDERS'
        BINDERS_ACCESSORIES = 'BINDERS_ACCESSORIES', 'BINDERS_ACCESSORIES'
        LABELS = 'LABELS', 'LABELS'
        DESK_ACCESSORIES = 'DESK_ACCESSORIES', 'DESK_ACCESSORIES'
        STORAGE = 'STORAGE', 'STORAGE'
        CHAIRS_SEATING = 'CHAIRS_SEATING', 'CHAIRS_SEATING'
        STORAGE_SOLUTIONS = 'STORAGE_SOLUTIONS'
        DESKS = 'DESKS', 'DESKS'
        TABLES = 'TABLES', 'TABLES'
        OFFICE_DECOR = 'OFFICE_DECOR'
        LAMPS_LIGHTING = 'LAMPS_LIGHTING', 'LAMPS_LIGHTING'
        CLEANING_SUPPLIES = 'CLEANING_SUPPLIES', 'CLEANING_SUPPLIES'
        TRASH_CANS_BAGS = 'TRASH_CANS_BAGS', 'TRASH_CANS_BAGS'
        MEDICAL_SUPPLIES = 'MEDICAL_SUPPLIES', 'MEDICAL_SUPPLIES'
        PAPER_PRODUCTS = 'PAPER_PRODUCTS', 'PAPER_PRODUCTS'
        SOAPS_SANITIZERS = 'SOAPS_SANITIZERS', 'SOAPS_SANITIZERS'
        SAFETY_SECURITY = 'SAFETY_SECURITY', 'SAFETY_SECURITY'
        CLEANING_TOOLS = 'CLEANING_TOOLS', 'CLEANING_TOOLS'
        AIR_FRESHENERS = 'AIR_FRESHENERS', 'AIR_FRESHENERS'
        COFFEE_SUPPLIES = 'COFFEE_SUPPLIES', 'COFFEE_SUPPLIES'
        CUPS_PLATES_CUTLERY = 'CUPS_PLATES_CUTLERY', 'CUPS_PLATES_CUTLERY'
        FRESH_FROZEN_FOOD = 'FRESH_FROZEN_FOOD', 'FRESH_FROZEN_FOOD'
        BEVERAGES = 'BEVERAGES', 'BEVERAGES'
        CANDY_SNACKS = 'CANDY_SNACKS', 'CANDY_SNACKS'
        APPLIANCES = 'APPLIANCES', 'APPLIANCES'
        COMPUTERS = 'COMPUTERS', 'COMPUTERS'
        SOFTWARE = 'SOFTWARE', 'SOFTWARE'
        DATA_STORAGE_MEDIA = 'DATA_STORAGE_MEDIA', 'DATA_STORAGE_MEDIA'
        COMPUTER_ACCESSORIES = 'COMPUTER_ACCESSORIES', 'COMPUTER_ACCESSORIES'
        PRINTERS_ACCESSORIES = 'PRINTERS_ACCESSORIES', 'PRINTERS_ACCESSORIES'
        INCREASE_PRODUCTIVITY = 'INCREASE_PRODUCTIVITY', 'INCREASE_PRODUCTIVITY'
        COMPUTER_COMPONENTS = 'COMPUTER_COMPONENTS', 'COMPUTER_COMPONENTS'
        OFFICE_EQUIPMENT = 'OFFICE_EQUIPMENT', 'OFFICE_EQUIPMENT'
        PHONES_ACCESSORIES = 'PHONES_ACCESSORIES', 'PHONES_ACCESSORIES'
        TVS_HOME_THEATER = 'TVS_HOME_THEATER', 'TVS_HOME_THEATER'
        NETWORKING_CABLES = 'NETWORKING_CABLES', 'NETWORKING_CABLES'
        BATTIES_POWER_PROTECTION = 'BATTIES_POWER_PROTECTION', 'BATTIES_POWER_PROTECTION'
        AUDIO = 'AUDIO', 'AUDIO'
        COPY_PRINTER_PAPER = 'COPY_PRINTER_PAPER', 'COPY_PRINTER_PAPER'
        PHOTO_PRESENTATION = 'PHOTO_PRESENTATION', 'PHOTO_PRESENTATION'
        NOTEBOOKS_PADS = 'NOTEBOOKS_PADS', 'NOTEBOOKS_PADS'
        POST_IT_STICKY_PAPER = 'POST_IT_STICKY_PAPER', 'POST_IT_STICKY_PAPER'
        ART_CRAFT_PAPER = 'ART_CRAFT_PAPER', 'ART_CRAFT_PAPER'
        FILLER_GRAPH_PAPER = 'FILLER_GRAPH_PAPER', 'FILLER_GRAPH_PAPER'
        ARTS_CRAFTS = 'ARTS_CRAFTS', 'ARTS_CRAFTS'
        ELECTRONICS = 'ELECTRONICS', 'ELECTRONICS'
        WRITING = 'WRITING', 'WRITING'
        BACKPACKS_LUNCH_BAGS = 'BACKPACKS_LUNCH_BAGS', 'BACKPACKS_LUNCH_BAGS'
        FOLDERS_BINDERS = 'FOLDERS_BINDERS', 'FOLDERS_BINDERS'
        BASIC_SCHOOL_SUPPLIES = 'BASIC_SCHOOL_SUPPLIES', 'BASIC_SCHOOL_SUPPLIES'
        NOTEBOOKS_PAPER = 'NOTEBOOKS_PAPER', 'NOTEBOOKS_PAPER'
        ETC = 'ETC', 'ETC'

    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.FloatField()
    img_url = models.URLField()
    category = models.CharField(
        max_length=128, choices=Category.choices)
    subcategory = models.CharField(
        max_length=128, choices=Subcategory.choices)
    inventory = models.IntegerField()