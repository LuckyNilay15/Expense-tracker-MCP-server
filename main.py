import random
from fastmcp import FastMCP

mcp=FastMCP(name="Demo-server")

@mcp.tool
def roll_dice(num_dice: int) -> list[int]:
    return [random.randint(1, 6) for _ in range(num_dice)]

@mcp.tool
def add(a: int, b: int) -> int:
    return int(a) + int(b)

if __name__ == "__main__":
    mcp.run()

