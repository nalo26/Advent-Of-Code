file = open("input.txt")

message = file.readline()
binary = list("".join([bin(int(c, 16))[2:].zfill(4) for c in message]))

def a_int(it, base = 10):
    return int("".join(it), base)

def parse(packet):
    version = a_int(packet[:3], 2)
    packet[:] = packet[3:]
    type_id = a_int(packet[:3], 2)
    packet[:] = packet[3:]
    if type_id == 4:
        data = []

        while True:
            b = packet.pop(0)
            data += packet[:4]
            packet[:] = packet[4:]
            if b == "0": break # last group

        return version, type_id, a_int(data, 2)

    length_type_id = packet.pop(0)
    packets = []

    if length_type_id == "0": # 15 bits
        subpackets_length = a_int(packet[:15], 2)
        packet[:] = packet[15:]
        data = packet[:subpackets_length]
        packet[:] = packet[subpackets_length:]

        while data:
            packets.append(parse(data))

    else: # 11 bits
        subpackets_amount = a_int(packet[:11], 2)
        packet[:] = packet[11:]

        for _ in range(subpackets_amount):
            packets.append(parse(packet))

    return version, type_id, packets

def compute_packets(packets):
    version = packets[0]
    if packets[1] == 4: return version
    count = version
    for packet in packets[2]:
        count += compute_packets(packet)
    return count


packets = parse(binary)
print(compute_packets(packets))