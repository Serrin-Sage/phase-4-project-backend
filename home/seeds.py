from apps import apps
from models import User, Drink, Lists, Analytics, Achievement

def run_seeds():
    print('Seeding database ... :seedling:')
# Add your seed data
    with app.app_context():
      print('Done! :deciduous_tree:')

run_seeds()