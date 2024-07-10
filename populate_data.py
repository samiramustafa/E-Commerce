import os
import django
from product.models import Category, Subcategory

# إعداد بيئة Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

def populate_categories():
    categories = [
        'Furniture',
        'Clothes',
        'Electronics',
        'Sports Gear',
        'Toys and Games'
    ]

    for category_name in categories:
        category, created = Category.objects.get_or_create(name=category_name)
        if created:
            print(f'Category "{category_name}" created.')
        else:
            print(f'Category "{category_name}" already exists.')

def populate_subcategories():
    categories_data = {
        'Furniture': ['Chairs', 'Tables', 'Sofas', 'Beds'],
        'Clothes': ['Accessories', 'Shoes', 'Tops','Bottoms','Dresses','Outerwear'],
        'Electronics': ['Phones', 'Laptops','Tablets,' 'Watches', 'Headphones','Accessories'],
        'Sports Gear': ['Fitness Equipment', 'Outdoor Sports', 'Indoor Sports', 'Accessories'],
        'Toys and Games': ['Board Games', 'Dolls', 'Puzzles', 'Action Figures','Educational Toys']
    }

    for category_name, subcategories_list in categories_data.items():
        category = Category.objects.get(name=category_name)
        for subcategory_name in subcategories_list:
            subcategory, created = Subcategory.objects.get_or_create(
                category=category,
                name=subcategory_name
            )
            if created:
                print(f'Subcategory "{subcategory_name}" created for category "{category_name}".')
            else:
                print(f'Subcategory "{subcategory_name}" already exists for category "{category_name}".')

if __name__ == '__main__':
    populate_categories()
    populate_subcategories()
    print("Categories and Subcategories populated successfully!")
