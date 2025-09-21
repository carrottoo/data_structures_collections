from priority_queue.removable_heap import RemovableHeapQ
from typing import List
"""
    An example of using RemovableHeapQ.

    We have implemented a movie renting system where entry in entries at index i are given as [shop_i, movie_i, price_i]. It means that 
    there is a copy of movie i at shop i with a rental price i. Each shop carries at most one copy of a movie i.

    The system supports:
    Search: Finds the cheapest 5 shops that have an unrented copy of a given movie. The shops should be sorted by price in ascending order, 
    and in case of a tie, the one with the smaller shopi should appear first. If there are less than 5 matching shops, then all of them 
    should be returned. If no shop has an unrented copy, then an empty list should be returned.
    Rent: Rents an unrented copy of a given movie from a given shop.
    Drop: Drops off a previously rented copy of a given movie at a given shop.
    Report: Returns the cheapest 5 rented movies (possibly of the same movie ID) as a 2D list res where res[j] = [shop_j, movie_j] describes that 
    the jth cheapest rented movie j was rented from the shop j. The movies in res should be sorted by price in ascending order, and in case of a 
    tie, the one with the smaller shopj should appear first, and if there is still tie, the one with the smaller moviej should appear first. If 
    there are fewer than 5 rented movies, then all of them should be returned. If no movies are currently being rented, then an empty list should 
    be returned.
"""
class MovieRentingSystem:

    def __init__(self, n: int, entries: List[List[int]]):
        self.movieToShopsWithUnrented = self.getMovieToShopsWithUnrentedMap(entries)
        self.cheapestRentedHeapQ = RemovableHeapQ()
        self.shopMovieToPrice = {}

        for entry in entries:
            self.shopMovieToPrice[(entry[0], entry[1])] = entry[2]

    def getMovieToShopsWithUnrentedMap(self, entries: List[List[int]]):
        result_map = {}
        for entry in entries:
            shop = entry[0]
            movie = entry[1]
            price = entry[2]
            if movie not in result_map:
                result_map[movie] = RemovableHeapQ()
            result_map[movie].add((price, shop))
        return result_map

    def search(self, movie: int) -> List[int]:
        if movie not in self.movieToShopsWithUnrented:
            return []

        foundPricesShops = []
        for i in range(5):
            res = self.movieToShopsWithUnrented[movie].pop()
            if not res:
                break
            foundPricesShops.append(res)
    
        for price, shop in foundPricesShops:
            self.movieToShopsWithUnrented[movie].add((price, shop))

        return [shop for _, shop in foundPricesShops]

    def rent(self, shop: int, movie: int) -> None:
        price = self.shopMovieToPrice[(shop, movie)]
        self.movieToShopsWithUnrented[movie].remove((price, shop))
        self.cheapestRentedHeapQ.add((price, shop, movie))

    def drop(self, shop: int, movie: int) -> None:
        price = self.shopMovieToPrice[(shop, movie)]
        self.movieToShopsWithUnrented[movie].add((price, shop))
        self.cheapestRentedHeapQ.remove((price, shop, movie))
        
    def report(self) -> List[List[int]]:
        foundPricesShopsMovies = []

        for i in range(5):
            res = self.cheapestRentedHeapQ.pop()
            if not res:
                break
            foundPricesShopsMovies.append(res)

        for price, shop, movie in foundPricesShopsMovies:
            self.cheapestRentedHeapQ.add((price, shop, movie))

        return [(shop, movie) for _, shop, movie in foundPricesShopsMovies]
