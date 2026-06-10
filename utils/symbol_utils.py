def to_jquants_code(symbol: str) -> str:
    return symbol.replace(".T", "")
