class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        max_buy_index = -1
        max_sell_index = -1

        for buy_index in range(len(prices)):
            for sell_index in range(buy_index, len(prices)):
                if prices[buy_index] < prices[sell_index]:
                    profit = prices[sell_index] - prices[buy_index]
                    if profit > max_profit:
                        max_profit = profit
                        max_buy_index = buy_index
                        max_sell_index = sell_index

        return max_profit