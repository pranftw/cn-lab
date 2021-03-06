import random
import time

def get_rand():
    return random.randint(1,100)

def process_packet(packet_size, max_chunk_size, capacity, int_arr_time):
    if packet_size>capacity:
        print("Packet size exceeds capacity!")
    else:
        already_processed = 0
        orig_packet_size = packet_size
        while(packet_size>0):
            time.sleep(int_arr_time)
            if(packet_size-max_chunk_size>=0):
                already_processed+=max_chunk_size
                currently_processed = max_chunk_size
                packet_size-=max_chunk_size
            else:
                already_processed+=packet_size
                currently_processed = packet_size
                packet_size = 0
            print(f"Processed {currently_processed} {already_processed}/{orig_packet_size}")
    print()

if __name__=='__main__':
    num = int(input("Enter the number of packets: "))
    capacity = int(input("Enter the capacity of the bucket: "))
    max_chunk_size = int(input("Enter the maximum chunk size: "))
    int_arr_time = int(input("Enter the inter arrival time: "))
    random_packets = []
    for _ in range(num):
        random_packets.append(get_rand())
    print()
    for i,packet in enumerate(random_packets):
        print(f"Processing packet {i} with size {packet} ...")
        process_packet(packet, max_chunk_size, capacity, int_arr_time)