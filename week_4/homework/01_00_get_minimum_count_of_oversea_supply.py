import heapq

ramen_stock = 4
supply_dates = [4, 10, 15]
supply_supplies = [20, 5, 10]
supply_recover_k = 30

# 힙 - 최댓값, 최솟값 뽑아낼 때 유리!!!


def get_minimum_count_of_overseas_supply(stock, dates, supplies, k):
    count = 0
    curr_index = 0
    max_heap = []

    while stock < k:
        for date in range(curr_index, len(dates)):
            if dates[date] <= stock:
                heapq.heappush(max_heap, -supplies[date])
            else:
                curr_index = date
                break
            count += 1
            stock += -heapq.heappop(max_heap)

    return count


print(get_minimum_count_of_overseas_supply(ramen_stock, supply_dates, supply_supplies, supply_recover_k))
