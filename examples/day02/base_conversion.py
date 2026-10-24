"""Convert integer strings between bases 2..36 without int(..., base) for conversion.

The implementation deliberately uses the elementary division/remainder algorithm
so students can connect the code to the manual method taught in the lesson.
"""

DIGITS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(number: int, base: int) -> str:
    """Return the representation of an integer in a base from 2 through 36."""
    if not 2 <= base <= len(DIGITS):
        raise ValueError("Asos 2 dan 36 gacha bo'lishi kerak.")
    if number == 0:
        return "0"

    sign = "-" if number < 0 else ""
    number = abs(number)
    output_digits: list[str] = []

    while number > 0:
        number, remainder = divmod(number, base)
        output_digits.append(DIGITS[remainder])

    # Qoldiqlar eng kichik razryaddan boshlab topiladi, shuning uchun teskari yozamiz.
    return sign + "".join(reversed(output_digits))


def from_base(text: str, base: int) -> int:
    """Parse an integer written in a base from 2 through 36."""
    if not 2 <= base <= len(DIGITS):
        raise ValueError("Asos 2 dan 36 gacha bo'lishi kerak.")

    cleaned = text.strip().upper()
    if not cleaned:
        raise ValueError("Son bo'sh bo'lishi mumkin emas.")

    sign = 1
    if cleaned[0] in "+-":
        if cleaned[0] == "-":
            sign = -1
        cleaned = cleaned[1:]

    if not cleaned:
        raise ValueError("Ishora ortidan raqamlar kelishi kerak.")

    value = 0
    for character in cleaned:
        digit = DIGITS.find(character)
        if digit < 0 or digit >= base:
            raise ValueError(
                f"'{character}' belgisi {base} asosli sistemada ruxsat etilmagan."
            )
        value = value * base + digit

    return sign * value


def convert_base(text: str, source_base: int, target_base: int) -> str:
    """Convert an integer numeral from source_base to target_base."""
    decimal_value = from_base(text, source_base)
    return to_base(decimal_value, target_base)


def main() -> None:
    examples = [
        ("101101", 2, 10),
        ("156", 10, 7),
        ("243", 5, 3),
        ("2D7", 16, 2),
        ("-1011", 2, 10),
    ]

    for numeral, source, target in examples:
        converted = convert_base(numeral, source, target)
        print(f"({numeral}) base {source} = ({converted}) base {target}")

    print("\nInteractive example; enter 'q' to stop.")
    while True:
        numeral = input("Son: ").strip()
        if numeral.lower() == "q":
            break
        try:
            source = int(input("Manba asosi (2..36): "))
            target = int(input("Maqsad asosi (2..36): "))
            print("Natija:", convert_base(numeral, source, target))
        except ValueError as error:
            print("Kiritish xatosi:", error)


if __name__ == "__main__":
    main()
