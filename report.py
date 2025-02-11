import re
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', type=str)

    args = parser.parse_args()
    filename = './rust/' + args.filename

    offlineconv = 0
    offlineconvpercent = 0
    offlineotherlinear = 0
    offlineotherlinearpercent = 0
    offlinerelu = 0
    offlinerelupercent = 0

    onlineconv = 0
    onlineotherlinear = 0
    onlinerelu = 0
    onlineconvpercent = 0
    onlineotherlinearpercent = 0
    onlinerelupercent = 0

    with open(filename, 'r') as file:
        for line in file:
            if 'The online conv2d reader communication' in line:
                match = re.search(r"reader communication:(\d+), writer communication:(\d+)", line)

                if match:
                    reader_comm = int(match.group(1))
                    writer_comm = int(match.group(2))
                    total = (reader_comm + writer_comm) / 1024.0 / 1024.0
                    total = round(total, 2)

                    offlineconv = total

            if 'The online other linear operators reader communication' in line:
                match = re.search(r"reader communication:(\d+), writer communication:(\d+)", line)

                if match:
                    reader_comm = int(match.group(1))
                    writer_comm = int(match.group(2))
                    total = (reader_comm + writer_comm) / 1024.0 / 1024.0
                    total = round(total, 2)

                    offlineotherlinear = total
            
            if 'The online relu reader communication' in line:
                match = re.search(r"reader communication:(\d+), writer communication:(\d+)", line)

                if match:
                    reader_comm = int(match.group(1))
                    writer_comm = int(match.group(2))
                    total = (reader_comm + writer_comm) / 1024.0 / 1024.0
                    total = round(total, 2)
                    
                    offlinerelu = total

            if 'The offline conv2d reader communication' in line:
                match = re.search(r"reader communication:(\d+), writer communication:(\d+)", line)

                if match:
                    reader_comm = int(match.group(1))
                    writer_comm = int(match.group(2))
                    total = (reader_comm + writer_comm) / 1024.0 / 1024.0
                    total = round(total, 2)
                    
                    onlineconv = total
            
            if 'The offline other linear operators reader communication' in line:
                match = re.search(r"reader communication:(\d+), writer communication:(\d+)", line)

                if match:
                    reader_comm = int(match.group(1))
                    writer_comm = int(match.group(2))
                    total = (reader_comm + writer_comm) / 1024.0 / 1024.0
                    total = round(total, 2)
                    
                    onlineotherlinear = total

            if 'The offline relu reader communication' in line:
                match = re.search(r"reader communication:(\d+), writer communication:(\d+)", line)

                if match:
                    reader_comm = int(match.group(1))
                    writer_comm = int(match.group(2))
                    total = (reader_comm + writer_comm) / 1024.0 / 1024.0
                    total = round(total, 2)
                    
                    onlinerelu = total
    
    offlineconvpercent = round(offlineconv*100 / (offlineconv + offlineotherlinear + offlinerelu), 2)
    offlineotherlinearpercent = round(offlineotherlinear*100 / (offlineconv + offlineotherlinear + offlinerelu), 2)
    offlinerelupercent = 100 - offlineconvpercent - offlineotherlinearpercent
    print("Offline phase:")
    print(f"Conv2d communication cost: {offlineconv:.2f}MB({offlineconvpercent:.2f}%)")
    print(f"Other linear operators communication cost: {offlineotherlinear:.2f}MB({offlineotherlinearpercent:.2f}%)")
    print(f"Non-linear operators communication cost: {offlinerelu:.2f}MB({offlinerelupercent:.2f}%)\n")

    onlineconvpercent = round(onlineconv*100 / (onlineconv + onlineotherlinear + onlinerelu), 2)
    onlineotherlinearpercent = round(onlineotherlinear*100 / (onlineconv + onlineotherlinear + onlinerelu), 2)
    onlinerelupercent = 100 - onlineconvpercent - onlineotherlinearpercent
    print("Online phase:")
    print(f"Conv2d communication cost: {onlineconv:.2f}MB({onlineconvpercent:.2f}%)")
    print(f"Other linear operators communication cost: {onlineotherlinear:.2f}MB({onlineotherlinearpercent:.2f}%)")
    print(f"Non-linear operators communication cost: {onlinerelu:.2f}MB({onlinerelupercent:.2f}%)")


if __name__ == '__main__':
    main()
