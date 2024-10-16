import asyncio
import math
import sys
import time
from functools import reduce
from pickle import FALSE

import aiohttp
import ssl

semaphore = asyncio.Semaphore(2)


async def fetch_url(single_url):
    async with semaphore:
        async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False)
        ) as session:
            async with session.get(single_url) as response:
                print(f"{single_url}: status_code: {response.status}")


async def fetch_all_urls():
    urls = [
        "https://google.com",
        "https://microsoft.com",
        "https://oracle.com",
        "https://reddit.com",
        "https://dou.ua",
        "https://stackoverflow.com",
    ]

    start_time = time.time()

    await asyncio.gather(*(fetch_url(single_url) for single_url in urls))

    end_time = time.time()

    print(f"Elapsed time {end_time - start_time: .2f} seconds")


async def is_prime(value: int) -> bool:
    for factor in range(2, int(math.sqrt(value) + 1)):
        if value % factor == 0:
            return False

    return True


def sieve_primes(value):
    values = [True for _ in range(0, value + 1)]
    values[0] = False
    values[1] = False

    for i in range(2, len(values)):
        if values[i]:
            composite = i + i

            while composite < len(values):
                values[composite] = False
                composite += i

    return [i for i, val in enumerate(values) if val is True]


async def prime_factors(value: int) -> list[int]:

    primes = sieve_primes(value + 1)

    left_to_factor = value

    factors = []

    while left_to_factor != 1:
        for single_prime in primes:
            if left_to_factor % single_prime == 0:
                factors.append(single_prime)
                left_to_factor //= single_prime
                break

    return factors


"""
Main function
"""


async def main():

    value = 123456

    start_time = time.time()
    results = await prime_factors(value)
    end_time = time.time()

    if value != reduce(lambda x, y: x * y, results):
        print("Incorrect result calculated")
    else:
        print(f"Factors for '{value}' are {results}")

    print(f"Elapsed time: {end_time - start_time:.2f} second")

    print(f"Python: {sys.version}, {ssl.OPENSSL_VERSION}")


"""
Run event loop using 'main' coroutine
"""
asyncio.run(main())
