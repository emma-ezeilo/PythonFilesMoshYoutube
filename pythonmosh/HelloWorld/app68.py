from pathlib import Path

path = Path()
# ecommerce_path = Path('ecommerce')
#
# email_path = Path('emails')
# ecommerce_path.mkdir() # This makes a directory in the root folder
# ecommerce_path.rmdir() # This removes or deletes a directory
# email_path.exists() # This checks whether the path exists by sending a boolean value
# print(email_path.exists()) # Uncomment the above and run them
for file in path.glob('*.py'):
    print(file)

