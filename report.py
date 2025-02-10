import re
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)

    args = parser.parse_args()
    filename = './rust/' + args.filename

    with open(filename, 'r') as file:
        for line in file:
            if 'The online conv2d reader communication' in line:
                print("Online phase:")
                match = re.search(r"reader communication:(\d+), writer communication:(\d+)", line)

                if match:
                    reader_comm = int(match.group(1))
                    writer_comm = int(match.group(2))
                    total = (reader_comm + writer_comm) / 1024.0 / 1024.0
                    total = round(total, 2)
                    
                    print(f"Conv2d communication cost: {total}MB")

            if 'The online other linear operators reader communication' in line:
                match = re.search(r"reader communication:(\d+), writer communication:(\d+)", line)

                if match:
                    reader_comm = int(match.group(1))
                    writer_comm = int(match.group(2))
                    total = (reader_comm + writer_comm) / 1024.0 / 1024.0
                    total = round(total, 2)
                    
                    print(f"Other linear operators communication cost: {total}MB")
            
            if 'The online relu reader communication' in line:
                match = re.search(r"reader communication:(\d+), writer communication:(\d+)", line)

                if match:
                    reader_comm = int(match.group(1))
                    writer_comm = int(match.group(2))
                    total = (reader_comm + writer_comm) / 1024.0 / 1024.0
                    total = round(total, 2)
                    
                    print(f"Non-linear operators communication cost: {total}MB")

            if 'The offline conv2d reader communication' in line:
                print("Offline phase:")
                match = re.search(r"reader communication:(\d+), writer communication:(\d+)", line)

                if match:
                    reader_comm = int(match.group(1))
                    writer_comm = int(match.group(2))
                    total = (reader_comm + writer_comm) / 1024.0 / 1024.0
                    total = round(total, 2)
                    
                    print(f"Conv2d communication cost: {total}MB")
            
            if 'The offline other linear operators reader communication' in line:
                match = re.search(r"reader communication:(\d+), writer communication:(\d+)", line)

                if match:
                    reader_comm = int(match.group(1))
                    writer_comm = int(match.group(2))
                    total = (reader_comm + writer_comm) / 1024.0 / 1024.0
                    total = round(total, 2)
                    
                    print(f"Other linear operators communication cost: {total}MB")

            if 'The offline relu reader communication' in line:
                match = re.search(r"reader communication:(\d+), writer communication:(\d+)", line)

                if match:
                    reader_comm = int(match.group(1))
                    writer_comm = int(match.group(2))
                    total = (reader_comm + writer_comm) / 1024.0 / 1024.0
                    total = round(total, 2)
                    
                    print(f"Non-linear operators communication cost: {total}MB\n")

if __name__ == '__main__':
    main()
