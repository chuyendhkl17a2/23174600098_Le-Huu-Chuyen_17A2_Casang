inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
if 'dagger' in inventory['backpack']:
    inventory['backpack'].remove('dagger')
inventory['gold'] += 50
print("Từ điển sau khi thực hiện các yêu cầu:")
print(inventory)

