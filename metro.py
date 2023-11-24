import random
starting_station = input("Which station are you starting from? ")
color_line = input("Which color is your station on? ")

colors = ['blue', 'red', 'green', 'orange', 'yellow', 'brown']

brown = {1: 'taipei zoo', 2: 'muhza', 3: 'wanfang community', 4: 'wanfang hospital', 5: 'xinhai', 6: 'linguang', 7: 'liuzangli', 
         8: 'technology building', 9: 'daan', 10: 'zhongxiao fuxing', 11: 'nanjing fuxing', 12: 'zhongshan junior high', 
         13: 'songshan airport', 14: 'dahzi', 15: 'jiannan road', 16: 'xihu', 17: 'gangqian', 18: 'wende', 19: 'neihu', 20: 'dahu park', 
         21: 'huzhou', 22: 'donghu', 23: 'nangang software park', 24: 'nangang exhibtion center'}

green = {1: 'xindian', 2: 'xindian district office', 3: 'qizhang', 4: 'dapinglin', 5: 'jingmei', 6: 'wanlong', 7: 'gongguan', 8: 'taipower building',
         9: 'guting', 10: 'chiang kai shek memorial hall', 11: 'xiaonamen', 12: 'ximen', 13: 'beimen', 14: 'zhongshan', 15: 'songjiang nanjing',
         16: 'nanjing fuxing', 17: 'taipei arena', 18: 'nanjing sanmin', 19: 'songshan'}

heads = 'north/east'
tails= 'south/west'

# randomize coin flip
coin_flip = ['heads','tails'] 
coin_flip_result = random.choice(coin_flip)

# convert string to dict 
color_dict = eval(color_line)

dice = [1, 2, 3, 4, 5, 6]
randomize_number = random.choice(dice)

for station in color_dict: 
    if starting_station == color_dict.get(station):
        # station is the key aka number
        if coin_flip_result == 'heads':
        # increase station number 
            destination = station + randomize_number
            print(f"🪙 Your coin flip turned out to be {coin_flip_result}")
            print(f"🎲 You are going {randomize_number} stops in {heads} direction on the {color_line} line")
        elif coin_flip_result == 'tails':
        # decrease station number 
            destination = station - randomize_number
            print(f"🪙 Your coin flip turned out to be {coin_flip_result}")
            print(f"🎲 You are going {randomize_number} stops in {tails} direction on the {color_line} line")
            
try: 
    print(f"🥁 Your destination is {color_dict[destination]}!")
except:
    print("☹️ Try again, index out of bound")