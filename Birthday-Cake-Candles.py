candles = [3, 2, 1, 3]

def birthdayCakeCandles(candles):
    maxi_height = 0
    count = 0
    for candle in candles:
        if candle > maxi_height:
            maxi_height = candle
    
    for candle in candles:
        if candle == maxi_height:
            count += 1
    
    #print(count)
            
    return count

birthdayCakeCandles(candles)