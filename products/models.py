from django.db import models


class Product(models.Model):
    class Category(models.TextChoices):
        OFFICE_SUPPLIES = 'Office Supplies', 'Office Supplies'
        FURNITURE = 'Furniture', 'Furniture'
        CLEANING = 'Cleaning', 'Cleaning'
        BREAKROOM = 'Breakroom', 'Breakroom'
        COMPUTERS_ACCESSORIES = 'Computer Accessories', 'Computer Accessories'
        ELECTRONICS = 'Electronics', 'Electronics'
        PAPER = 'Paper', 'Paper'
        SCHOOL_SUPPLIES = 'School Supplies', 'School Supplies'
        INK_TONER = 'Ink and Toner', 'Ink and Toner'
        ETC = 'Etc', 'Etc'

    class Subcategory(models.TextChoices):
        PENS_PENCILS_MARKERS = 'Pens, Pencils and Markers', 'Pens, Pencils and Markers'
        BASIC_SUPPLIES = 'Basic Supplies', 'Basic Supplies'
        MAILING_SHIPPING = 'Mailing and Shipping', 'Mailing and Shipping'
        FILING_FOLDERS = 'Filing and Folders', 'Filing and Folders'
        BINDERS_ACCESSORIES = 'Binders and Accessories', 'Binders and Accessories'
        LABELS = 'Labels and Label Makers', 'Labels and Label Makers'
        DESK_ACCESSORIES = 'Desk Accessories', 'Desk Accessories'
        STORAGE = 'Storage', 'Storage'
        CHAIRS_SEATING = 'Chairs and Seating', 'Chairs and Seating'
        STORAGE_SOLUTIONS = 'Storage Solutions', 'Storage Solutions'
        DESKS = 'Desks', 'Desks'
        TABLES = 'Tables', 'Tables'
        OFFICE_DECOR = 'Office Decor', 'Office Decor'
        LAMPS_LIGHTING = 'Lamps and Lighting', 'Lamps and Lighting'
        CLEANING_SUPPLIES = 'Cleaning Supplies', 'Cleaning Supplies'
        TRASH_CANS_BAGS = 'Trash Cans and Bags', 'Trash Cans and Bags'
        MEDICAL_SUPPLIES = 'Medical Supplies', 'Medical Supplies'
        PAPER_PRODUCTS = 'Paper Products', 'Paper Products'
        SOAPS_SANITIZERS = 'Soaps and Sanitizers', 'Soaps and Sanitizers'
        SAFETY_SECURITY = 'Safety and Security', 'Safety and Security'
        CLEANING_TOOLS = 'Cleaning Tools', 'Cleaning Tools'
        AIR_FRESHENERS = 'Air Fresheners', 'Air Fresheners'
        COFFEE_SUPPLIES = 'Coffee Supplies', 'Coffee Supplies'
        CUPS_PLATES_CUTLERY = 'Cups, Plates and Cutlery', 'Cups, Plates and Cutlery'
        FRESH_FROZEN_FOOD = 'Fresh and Frozen Food', 'Fresh and Frozen Food'
        BEVERAGES = 'Beverages', 'Beverages'
        CANDY_SNACKS = 'Candy and Snacks', 'Candy and Snacks'
        APPLIANCES = 'Appliances', 'Appliances'
        COMPUTERS = 'Computers', 'Computers'
        SOFTWARE = 'Software', 'Software'
        DATA_STORAGE_MEDIA = 'Data Storage and Media', 'Data Storage and Media'
        COMPUTER_ACCESSORIES = 'Computer Accessories', 'Computer Accessories'
        PRINTERS_ACCESSORIES = 'Printers and Accessories', 'Printers and Accessories'
        COMPUTER_COMPONENTS = 'Computer Components', 'Computer Components'
        OFFICE_EQUIPMENT = 'Office Equipment', 'Office Equipment'
        PHONES_ACCESSORIES = 'Phones and Accessories', 'Phones and Accessories'
        TVS_HOME_THEATER = 'TVs and Home Theater', 'TVs and Home Theater'
        NETWORKING_CABLES = 'Networking and Cables', 'Networking and Cables'
        BATTERIES_POWER_PROTECTION = 'Batteries and Power Protection', 'Batteries and Power Protection'
        AUDIO = 'Audio', 'Audio'
        COPY_PRINTER_PAPER = 'Copy and Printer Paper', 'Copy and Printer Paper'
        PHOTO_PRESENTATION = 'Photo and Presentation', 'Photo and Presentation'
        NOTEBOOKS_PADS = 'Notebooks and Pads', 'Notebooks and Pads'
        POST_IT_STICKY_PAPER = 'Post-It and Sticky Paper', 'Post-It and Sticky Paper'
        ART_CRAFT_PAPER = 'Art and Craft Paper', 'Art and Craft Paper'
        FILLER_GRAPH_PAPER = 'Filler and Graph Paper', 'Filler and Graph Paper'
        ARTS_CRAFTS = 'Arts and Crafts', 'Arts and Crafts'
        SCHOOL_ELECTRONICS = 'School Electronics', 'School Electronics'
        BACKPACKS_LUNCH_BAGS = 'Backpacks and Lunch Bags', 'Backpacks and Lunch Bags'
        ETC = 'Etc', 'Etc'

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
