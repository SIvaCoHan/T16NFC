import wrapper


def main():
    device = wrapper.lc_init(100, 115200)
    print(f'Device Handler: {device}')
    # wrapper.lc_beep(device, 10)

    d = wrapper.lc_getver(device)
    print(f'Device Hardware Version: {d}')

    d = wrapper.lc_getFlashUserMemSize(device)
    print(f'Max User Memory Size: {d} Byte')
    #
    #
    d = wrapper.lc_GetDevSN(device)
    print(d)
    #
    # d = wrapper.lc_getAddress(device)
    # print(d)

    d = wrapper.lc_card(device, 0)
    print(d)

    d = wrapper.lc_write_convenient(device, 4, 0x60, b'\xff\xff\xff\xff\xff\xff', b'XXX00000000MN')
    print(d)

    d = wrapper.lc_read_convenient(device, 4, 0x60, b'\xff\xff\xff\xff\xff\xff')
    # c = wrapper.hex_asc(d[:16], 16)
    print(d[: 16])



    # d = wrapper.asc_hex('616263', 3)
    # print(d)
    # d = wrapper.hex_asc('abc', 3)
    # print(d)


if __name__ == '__main__':
    main()
