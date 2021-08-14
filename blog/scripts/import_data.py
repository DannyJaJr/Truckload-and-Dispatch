from blog.models import Load

def run():
    for i in range(5, 8):
        load = Load()
        load.image = "http://default"
        #  formating numbers %s placeholder
        load.tilte = "Load No #%s" % i
        #  formating numbers %d placeholder
        load.price = "Price No #%d" % i
        load.desc = "Description load No #%s" % i
        load.save()
print("test passed")