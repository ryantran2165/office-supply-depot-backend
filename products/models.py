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
        INK_TONER = 'Ink & Toner'
        ETC = 'Etc'

    class Subcategory(models.TextChoices):
        PENS_PENCILS_MARKERS = 'Pens, Pencils & Markers'
        BASIC_SUPPLIES = 'Basic Supplies'
        MAILING_SHIPPING = 'Mailing & Shipping'
        FILING_FOLDERS = 'Filing & Folders'
        BINDERS_ACCESSORIES = 'Binders & Accessories'
        LABELS = 'Labels & Label Makers'
        DESK_ACCESSORIES = 'Desk Accessories'
        STORAGE = 'Storage'
        CHAIRS_SEATING = 'Chairs & Seating'
        STORAGE_SOLUTIONS = 'Storage Solutions'
        DESKS = 'Desks'
        TABLES = 'Tables'
        OFFICE_DECOR = 'Office Decor'
        LAMPS_LIGHTING = 'Lamps & Lighting'
        CLEANING_SUPPLIES = 'Cleaning Supplies'
        TRASH_CANS_BAGS = 'Trash Cans & Bags'
        MEDICAL_SUPPLIES = 'Medical Supplies'
        PAPER_PRODUCTS = 'Paper Products'
        SOAPS_SANITIZERS = 'Soaps & Sanitizers'
        SAFETY_SECURITY = 'Safety & Security'
        CLEANING_TOOLS = 'Cleaning Tools'
        AIR_FRESHENERS = 'Air Fresheners'
        COFFEE_SUPPLIES = 'Coffee Supplies'
        CUPS_PLATES_CUTLERY = 'Cups, Plates & Cutlery'
        FRESH_FROZEN_FOOD = 'Fresh & Frozen Food'
        BEVERAGES = 'Beverages'
        CANDY_SNACKS = 'Candy & Snacks'
        APPLIANCES = 'Appliances'
        COMPUTERS = 'Computers'
        SOFTWARE = 'Software'
        DATA_STORAGE_MEDIA = 'Data Storage & Media'
        COMPUTER_ACCESSORIES = 'Computer Accessories'
        PRINTERS_ACCESSORIES = 'Printers & Accessories'
        COMPUTER_COMPONENTS = 'Computer Components'
        OFFICE_EQUIPMENT = 'Office Equipment'
        PHONES_ACCESSORIES = 'Phones & Accessories'
        TVS_HOME_THEATER = 'TVs & Home Theater'
        NETWORKING_CABLES = 'Networking & Cables'
        BATTIES_POWER_PROTECTION = 'Batteries & Power Protection'
        AUDIO = 'Audio'
        COPY_PRINTER_PAPER = 'Copy & Printer Paper'
        PHOTO_PRESENTATION = 'Photo & Presentation'
        NOTEBOOKS_PADS = 'Notebooks & Pads'
        POST_IT_STICKY_PAPER = 'Post-It & Sticky Paper'
        ART_CRAFT_PAPER = 'Art & Craft Paper'
        FILLER_GRAPH_PAPER = 'Filler & Graph Paper'
        ARTS_CRAFTS = 'Arts & Crafts'
        SCHOOL_ELECTRONICS = 'School Electronics'
        WRITING = 'Writing'
        BACKPACKS_LUNCH_BAGS = 'Backpacks & Lunch Bags'
        FOLDERS_BINDERS = 'Folders & Binders'
        BASIC_SCHOOL_SUPPLIES = 'Basic School Supplies'
        NOTEBOOKS_PAPER = 'Notebooks & Paper'
        ETC = 'Etc'

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

    def __str__(self):
        return self.name
