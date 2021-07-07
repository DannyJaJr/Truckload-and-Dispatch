from blog.models import Load

def run():
    for i in range(5, 8):
        load = Load()
        load.image = "http://default"
        load.tilte = "Load No #%d" % i
        load.price = "Price No #%d" % i
        load.desc = "Description load No #%d" % i
        load.save()
print("test passed")