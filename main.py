from modules import difmapper
from modules.flags import PROCESS_FLAGS


def main():
    difmapper.DiffMapper(r"E:\Apijay@Projects\ProjectOpenTools\data\images\sample.png", r"E:\Apijay@Projects\ProjectOpenTools\data\images\sample.png", r"E:\Apijay@Projects\ProjectOpenTools\data\exports")
    print(PROCESS_FLAGS.meta)

if __name__ == "__main__":
    main()
