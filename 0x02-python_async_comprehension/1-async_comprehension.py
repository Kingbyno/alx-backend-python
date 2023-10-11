#!/usr/bin/env python3
"""10 random numbers using an async comprehensing over"""
from typing import List
async_generator = __import__('0-async_generator').async_generator

async def comprehension() -> List[float]:
    """
    async_comprehension - function that takes no arguments
    Return: 10 random numbers
    """
     random_numbers = [i async for i in async_generator()]
     return random_numbers
