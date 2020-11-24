# Generated by Django 3.1.2 on 2020-11-21 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20201120_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Office Supplies', 'Office Supplies'), ('Furniture', 'Furniture'), ('Cleaning', 'Cleaning'), ('Breakroom', 'Breakroom'), ('Computer Accessories', 'Computer Accessories'), ('Electronics', 'Electronics'), ('Paper', 'Paper'), ('School Supplies', 'School Supplies'), ('Ink and Toner', 'Ink and Toner'), ('Etc', 'Etc')], max_length=128),
        ),
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(blank=True, choices=[('Pens, Pencils and Markers', 'Pens, Pencils and Markers'), ('Basic Supplies', 'Basic Supplies'), ('Mailing and Shipping', 'Mailing and Shipping'), ('Filing and Folders', 'Filing and Folders'), ('Binders and Accessories', 'Binders and Accessories'), ('Labels and Label Makers', 'Labels and Label Makers'), ('Desk Accessories', 'Desk Accessories'), ('Storage', 'Storage'), ('Chairs and Seating', 'Chairs and Seating'), ('Storage Solutions', 'Storage Solutions'), ('Desks', 'Desks'), ('Tables', 'Tables'), ('Office Decor', 'Office Decor'), ('Lamps and Lighting', 'Lamps and Lighting'), ('Cleaning Supplies', 'Cleaning Supplies'), ('Trash Cans and Bags', 'Trash Cans and Bags'), ('Medical Supplies', 'Medical Supplies'), ('Paper Products', 'Paper Products'), ('Soaps and Sanitizers', 'Soaps and Sanitizers'), ('Safety and Security', 'Safety and Security'), ('Cleaning Tools', 'Cleaning Tools'), ('Air Fresheners', 'Air Fresheners'), ('Coffee Supplies', 'Coffee Supplies'), ('Cups, Plates and Cutlery', 'Cups, Plates and Cutlery'), ('Fresh and Frozen Food', 'Fresh and Frozen Food'), ('Beverages', 'Beverages'), ('Candy and Snacks', 'Candy and Snacks'), ('Appliances', 'Appliances'), ('Computers', 'Computers'), ('Software', 'Software'), ('Data Storage and Media', 'Data Storage and Media'), ('Computer Accessories', 'Computer Accessories'), ('Printers and Accessories', 'Printers and Accessories'), ('Computer Components', 'Computer Components'), ('Office Equipment', 'Office Equipment'), ('Phones and Accessories', 'Phones and Accessories'), ('TVs and Home Theater', 'TVs and Home Theater'), ('Networking and Cables', 'Networking and Cables'), ('Batteries and Power Protection', 'Batteries and Power Protection'), ('Audio', 'Audio'), ('Copy and Printer Paper', 'Copy and Printer Paper'), ('Photo and Presentation', 'Photo and Presentation'), ('Notebooks and Pads', 'Notebooks and Pads'), ('Post-It and Sticky Paper', 'Post-It and Sticky Paper'), ('Art and Craft Paper', 'Art and Craft Paper'), ('Filler and Graph Paper', 'Filler and Graph Paper'), ('Arts and Crafts', 'Arts and Crafts'), ('School Electronics', 'School Electronics'), ('Backpacks and Lunch Bags', 'Backpacks and Lunch Bags'), ('Etc', 'Etc')], max_length=128),
        ),
    ]