from django.db import models


class Product(models.Model):
    class Category(models.TextChoices):
        OFFICE_SUPPLIES = 'Office Supplies'
        FURNITURE = 'Furniture'
        CLEANING = 'Cleaning'
        BREAKROOM = 'Breakroom'
        COMPUTERS_ACCESSORIES = 'Computer Accessories'
        ELECTRONICS = 'Electronics'
        PAPER = 'Paper'
        SCHOOL_SUPPLIES = 'School Supplies'
        INK_TONER = 'Ink and Toner'
        ETC = 'Etc'

    class Subcategory(models.TextChoices):
        PENS_PENCILS_MARKERS = 'Pens, Pencils and Markers'
        BASIC_SUPPLIES = 'Basic Supplies'
        MAILING_SHIPPING = 'Mailing and Shipping'
        FILING_FOLDERS = 'Filing and Folders'
        BINDERS_ACCESSORIES = 'Binders and Accessories'
        LABELS = 'Labels and Label Makers'
        DESK_ACCESSORIES = 'Desk Accessories'
        STORAGE = 'Storage'
        CHAIRS_SEATING = 'Chairs and Seating'
        STORAGE_SOLUTIONS = 'Storage Solutions'
        DESKS = 'Desks'
        TABLES = 'Tables'
        OFFICE_DECOR = 'Office Decor'
        LAMPS_LIGHTING = 'Lamps and Lighting'
        CLEANING_SUPPLIES = 'Cleaning Supplies'
        TRASH_CANS_BAGS = 'Trash Cans and Bags'
        MEDICAL_SUPPLIES = 'Medical Supplies'
        PAPER_PRODUCTS = 'Paper Products'
        SOAPS_SANITIZERS = 'Soaps and Sanitizers'
        SAFETY_SECURITY = 'Safety and Security'
        CLEANING_TOOLS = 'Cleaning Tools'
        AIR_FRESHENERS = 'Air Fresheners'
        COFFEE_SUPPLIES = 'Coffee Supplies'
        CUPS_PLATES_CUTLERY = 'Cups, Plates and Cutlery'
        FRESH_FROZEN_FOOD = 'Fresh and Frozen Food'
        BEVERAGES = 'Beverages'
        CANDY_SNACKS = 'Candy and Snacks'
        APPLIANCES = 'Appliances'
        COMPUTERS = 'Computers'
        SOFTWARE = 'Software'
        DATA_STORAGE_MEDIA = 'Data Storage and Media'
        COMPUTER_ACCESSORIES = 'Computer Accessories'
        PRINTERS_ACCESSORIES = 'Printers and Accessories'
        COMPUTER_COMPONENTS = 'Computer Components'
        OFFICE_EQUIPMENT = 'Office Equipment'
        PHONES_ACCESSORIES = 'Phones and Accessories'
        TVS_HOME_THEATER = 'TVs and Home Theater'
        NETWORKING_CABLES = 'Networking and Cables'
        BATTIES_POWER_PROTECTION = 'Batteries and Power Protection'
        AUDIO = 'Audio'
        COPY_PRINTER_PAPER = 'Copy and Printer Paper'
        PHOTO_PRESENTATION = 'Photo and Presentation'
        NOTEBOOKS_PADS = 'Notebooks and Pads'
        POST_IT_STICKY_PAPER = 'Post-It and Sticky Paper'
        ART_CRAFT_PAPER = 'Art and Craft Paper'
        FILLER_GRAPH_PAPER = 'Filler and Graph Paper'
        ARTS_CRAFTS = 'Arts and Crafts'
        SCHOOL_ELECTRONICS = 'School Electronics'
        WRITING = 'Writing'
        BACKPACKS_LUNCH_BAGS = 'Backpacks and Lunch Bags'
        FOLDERS_BINDERS = 'Folders and Binders'
        BASIC_SCHOOL_SUPPLIES = 'Basic School Supplies'
        NOTEBOOKS_PAPER = 'Notebooks and Paper'
        ETC = 'Etc'

    name = models.CharField(max_length=128)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.FloatField()
    img_url = models.URLField()
    category = models.CharField(
        max_length=128, choices=Category.choices)
    subcategory = models.CharField(
        max_length=128, choices=Subcategory.choices, blank=True)
    inventory = models.IntegerField()

    def __str__(self):
        return self.name
