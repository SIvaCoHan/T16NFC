import wrapper


def main():
    device = wrapper.lc_init(100, 115200)
    print(device)
    wrapper.lc_beep(device, 10)
    err = wrapper.lc_exit(device)
    print(err)
    # d = wrapper.asc_hex('616263', 3)
    # print(d)
    # d = wrapper.hex_asc('abc', 3)
    # print(d)


if __name__ == '__main__':
    main()
