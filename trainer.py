from classifier import *
from time import time, strftime


print("Training tweet classification model...")

start = time()
model(DEFAULT_CATEGORIES, True)

print("Finished in %.2f seconds." %(time() - start))