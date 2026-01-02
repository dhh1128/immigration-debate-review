import os

for fname in os.listdir('.'):
    if fnamesuffix := fname.split('.')[-1] != 'md':
        continue
    if fname in ['process.md', 'facebook-post.md', 'README.md']:
        continue
    friendly = fname.replace('-', ' ').replace('_', ' ').rsplit('.', 1)[0].title()
    url = fname[:-3]
    print(f"- [{friendly}]({url})")
