from faker import Faker
fake = Faker()

for x in range(10):
    print(fake.name())
# 'Lucy Cechtelar'

#fake.address()
# '426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700'