from bitarray import bitarray
import math
import random


def message_to_bits(message):
    """
    Konvertiert einen gegebenen string in seine Repräsentation als Reihe 
    von bits in Form eines bitarray.
    """
    bits = bitarray()
    bits.frombytes(message.encode("ascii"))
    return bits


def bits_to_message(bits):
    """
    Versucht eine Reihe von bits in Form eines bitarray in einen string zu konvertieren.
    bit-Folgen, die keinem Symbol zugeordnet werden können, werden in ein � umgewandelt.
    """
    bees = bits.tobytes()
    message = ""
    for bee in bees:
        try:
            message += bytes([bee]).decode("ascii")
        except:
            message += "�"
    return message


def empty_table(rows, columns):
    """
    Erstellt eine leere Tabelle als Array von bitarray in den
    Dimensionen rows ⨯ columns, und befüllt alle bits mit 0
    """
    table = []
    for i in range(0, rows):
        row = bitarray(columns)
        row.setall(0)
        table.append(row)
    return table


def copy_table(tible):
    """
    Erstellt eine Kopie von einer gegebenen Tabelle. Dies ist 
    beispielsweise nötig, wenn wir auf einer Tabelle Operationen
    vornehmen möchten, aber uns ein unverändertes Original be-
    halten möchten.
    """
    table = []
    for row in tible:
        table.append(bitarray([bit for bit in row]))
    return table


def print_table(table):
    """
    Ermöglicht uns, Tabellen einfach für einen Menschen
    zu lesen darzustellen
    """
    for row in table:
        for bit in row:
            print(bit, end=" ")
        print()
    print()


def get_column(table, index):
    """
    Liefert alle bits in einer Zeile einer Tabelle als bitarray zurück
    """
    column = bitarray()
    for row in table:
        column.append(row[index])
    return column


def bits_to_table(bits, columns=4):
    """
    Wandelt ein bitarray in eine Tabelle mit columns Spalten.
    Falls kein columns-Wert angegeben wird, dann wird 4 als Standart-
    Wert angenommen.
    """
    rows = math.ceil(len(bits) / columns)
    table = empty_table(rows, columns)

    for i, bit in enumerate(bits):
        row = int(i / columns)
        table[row][i % columns] = bit
    return table


def table_to_bits(table):
    """
    Wandelt eine Tabelle in ein einzelnes bitarray um,
    in dem es ein neues bitarray erstellt, und für jede Zeile
    jedes bit anhängt.
    """

    bits = bitarray()

    for row in table:
        for bit in row:
            bits.append(bit)

    return bits


def corrupt_bits(bats, victim_count):
    """
    Sucht sich zufällig victim_count-viele bits aus
    und ändert deren Werte. Damit das ursprüngliche
    bitarray unverändert bleibt, machen wir uns zunächst
    erst eine Kopie davon, auf welcher wir dann nachfolgend 
    arbeiten und welche wir zurückgeben.
    """
    bits = bitarray([bit for bit in bats])

    for i in range(0, victim_count):
        victim = random.randint(0, len(bits)-1)
        bits[victim] ^= 1
    return bits


def corrupt_table(tible, victim_count):
    """
    Sucht sich zufällig victim_count-viele bits aus
    und ändert deren Werte. Damit die ursprüngliche
    Tabelle unverändert bleibt, machen wir uns zunächst
    erst eine Kopie davon, auf welcher wir dann nachfolgend 
    arbeiten und welche wir zurückgeben.
    """

    table = copy_table(tible)

    for i in range(0, victim_count):
        victim_row = random.randint(0, len(table)-1)
        victim_column = random.randint(0, len(table[0])-1)
        table[victim_row][victim_column] ^= 1
    return table
