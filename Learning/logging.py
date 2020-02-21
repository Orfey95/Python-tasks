import logging
name = 'sasha'
logging.basicConfig(filename="sample.log", level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')
c = 0
while c < 10:
    print("Input number:")
    x = int(input())
    if x < 5:
        logging.error("your number < 5!")
    if x > 5:
        logging.critical("your number > 5!")
    if x == 5:
        logging.info("your number = 5!")
    c = c + 1
