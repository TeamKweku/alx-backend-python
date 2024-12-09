#!/usr/bin/env python3
"""Module for concurrent database operations"""

import asyncio
import aiosqlite


async def async_fetch_users():
    """Fetch all users from the database"""
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users") as cursor:
            return await cursor.fetchall()


async def async_fetch_older_users():
    """Fetch users older than 40 from the database"""
    async with aiosqlite.connect("users.db") as db:
        async with db.execute("SELECT * FROM users WHERE age > 40") as cursor:
            return await cursor.fetchall()


async def fetch_concurrently():
    """Execute both queries concurrently"""
    users, older_users = await asyncio.gather(
        async_fetch_users(), async_fetch_older_users()
    )
    return users, older_users


if __name__ == "__main__":
    result = asyncio.run(fetch_concurrently())
    print("All users:", result[0])
    print("Users older than 40:", result[1])
